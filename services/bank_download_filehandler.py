from http.client import HTTPException

import pandas as pd
from dto.bank_download_dto import bankdownloadsListDTO
from services.myfilehandler import myFileHandler


class bankdownloadFileHandler(myFileHandler):
    def __init__(self,**kwargs):
        file = kwargs.get('file', None)
        folder = kwargs.get('folder', None)
        if file:
            super().__init__(file=file)
        elif folder:
            super().__init__(folder=folder)
        
#######################################################################################################################
    def add_bank_account_key(self, file, df):
        bank_account_key = file.split('/')[-1].split('.')[0]
        df['bank_account_key'] = bank_account_key
        return df    
#######################################################################################################################    
    def convert_df_to_list(self, file:str, df:pd.DataFrame,**kwargs) -> bankdownloadsListDTO:
        column_names = kwargs.get('column_names', None)
        rename_columns = kwargs.get('rename_columns', None) #rename columns for Chase downloads
        #fileheaders = kwargs.get('fileheaders', None) #file headers for Wells Fargo downloads

        errorsList = []
        
        if rename_columns:
            df.rename(columns=column_names, inplace=True)
        df=self.adjust_columns(df, column_names, remove_starting_with ='not_required')
        df=self.add_bank_account_key(file,df)
        df=self.convert_columns_to_string(df, ['bank_account_key','description'])
        df=self.convert_columns_to_numeric(df, ['amount'])
        df=self.convert_columns_to_date(df, ['tdate'])
        errorsList = self.validate_null(df)
        dupList = self.check_duplicates(df)
        try:
            if errorsList:
                return {},errorsList
            elif dupList:
                return {},dupList
            else:
                bank_downloads_data = df.to_dict(orient='records')
                return bank_downloads_data,[]
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing data: {str(e)}")

# #################################################################################################################