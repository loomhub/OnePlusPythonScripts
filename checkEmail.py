import email
from email.header import decode_header
import imaplib
import re
import requests
from dto.processed_dto import processedDTO, listProcessedDTO

class mailHandler:
    def __init__(self):
        print("Mail Handler Created")
        self.hostName = 'http://localhost:8080'
        self.imapServer = 'imap.gmail.com'
        self.inbox = 'inbox'
        self.llcKeyword = '(SUBJECT "#oneplus")'
        self.llc_url = '/llcs/email?receiver='
        self.bird = '/birds'
        self.emailSentCompleted = listProcessedDTO()
############################################################################################################        
    def get_bird(self):
      #Call /birds
        url = self.hostName + self.bird
        data = requests.get(url).json()
        active_record = None
        for record in data['birds']:
            if record['active'] == 'X':
                active_record = record
                break
        return active_record
############################################################################################################    
    def select_inbox(self, bird):
        mail = imaplib.IMAP4_SSL(self.imapServer)
        mail.login(bird['sender'], bird['pwd'])
        mail.select(self.inbox)
        return mail
############################################################################################################
    def extract_email(self,address):
        match = re.search(r'<([^>]+)>', address)
        if match:
            return match.group(1)
        else:
            return address     
############################################################################################################  
    def process_send_and_trash(self,mail, data,keyword):
        for num in data[0].split():
                typ, data = mail.fetch(num, '(RFC822)')
                msg = email.message_from_bytes(data[0][1])
                receiver = msg['from']
                receiver=self.extract_email(receiver)
                if not any(done.receiver == receiver and done.report == keyword for done in self.emailSentCompleted.done):
                    url = self.hostName + self.llc_url + receiver
                    response = requests.get(url)
                    if response.status_code == 200:
                        print(f"Email sent to {receiver}")
                        new_done = processedDTO(report=keyword, receiver=receiver)
                        self.emailSentCompleted.done.append(new_done)
                        mail.store(num, '+X-GM-LABELS', '\\Trash')
                    else:
                        print(f"Email not sent to {receiver}")
                else:
                    mail.store(num, '+X-GM-LABELS', '\\Trash')
############################################################################################################ 
    def process_llc_email(self,mail):
        ttype, data = mail.search(None, self.llcKeyword)
        self.process_send_and_trash(mail, data,self.llcKeyword)
############################################################################################################    
    def check_email(self):
        bird = self.get_bird() 
        try:   
            mail = self.select_inbox(bird)
            self.process_llc_email(mail)
            mail.close()
            mail.logout()
        except Exception as e:
            print(f"Error: {e}")