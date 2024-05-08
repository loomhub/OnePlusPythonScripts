# class myFile:
#     def __init__(self,**kwargs): #path,pathType,dType
       
#         self.path = kwargs.get('path', None) # Optional input
#         self.pathType = kwargs.get('pathType', None) # Optional input
#         self.dType = kwargs.get('dType', None) # Optional input
#         self.debug = kwargs.get('debug', None) # Optional input
#         self.debugCount=0
        
#         if self.path!=None:
#             self.path=self.setPath(self.path,self.pathType)
#             self.files=self.getFiles(self.dType)
        
#     def setPath(self,*args,**kwargs):#path,pathType
#         path,pathType=args[0],args[1]
#         if pathType==C.REL.value:
#             root = os.getcwd().split(os.sep)[:-1]
#             fileName=os.sep.join(root)+path
#         elif pathType==C.ABS.value:
#             fileName=path
#         return fileName

#     def getFiles(self,*args,**kwargs):#dType
#         dType=args[0]
#         if dType==C.FOLDER.value:
#             files=os.listdir(self.path)
#         elif dType==C.FILE.value:
#             files=[self.path]
#         else:
#             files=[]
#         return files
    
#     def move(self,*args,**kwargs):#toPath,dType,fileNames
#         toPath,pathType,dType=args[0],args[1],args[2]
#         toPath=self.setPath(toPath,pathType)

#         self.selectFiles=kwargs.get('selectFiles', None) # Optional input
#         self.keyword=kwargs.get('keyword',None) # Optional input

#         if self.selectFiles!=None:
#             set1 = set(self.files)
#             intersection = set1.intersection(self.selectFiles)
#             self.moveFiles = list(intersection)
#             print(self.moveFiles)
        
#         if self.keyword!=None:
#             set1=set(self.files)
#             self.moveFiles = [s for s in self.files if self.keyword in s]
#             print(self.moveFiles)
                
#         if dType==C.FOLDER.value:
#             if (self.selectFiles==None)&(self.keyword==None): #User wants to move all files
#                 self.moveFiles=self.files
#             for file in self.moveFiles:
#                 fromFile=self.path+file
#                 toFile=toPath+file
#                 os.replace(fromFile,toFile)
#         elif dType==C.FILE.value:
#             fromFile=self.path
#             toFile=toPath
#             os.replace(fromFile,toFile)
    
#     def readData(self,*args,**kwargs):#fType,cols,skip,sheet
#         fType,cols,skip,sheet=args[0],args[1],args[2],args[3]
#         property = kwargs.get('property', None) # Optional input
#         total=0
#         resultDF=pd.DataFrame(columns=cols)
#         for file in self.files:
#             f=''
#             if self.dType==C.FOLDER.value:
#                 if os.path.isfile(os.path.join(self.path,file)):
#                     f=os.path.join(self.path,file)
#             elif self.dType==C.FILE.value:
#                 if os.path.isfile(file):
#                     f=file

#             if f != '': 
#                 if property!=None:
#                     propertyName=f.split('\\')[-1].split(' ')[0]
#                     print('Reading file for property {p}'.format(p=propertyName))
#                 if fType == C.CSV.value:
#                     temp=pd.read_csv(f,skiprows=skip,
#                     header=None,names=cols,keep_default_na=False,encoding=C.ISO.value)
#                 elif fType == C.EXCEL.value:
#                     if sheet==None:
#                         temp=pd.read_excel(f,skiprows=skip,header=None,names=cols,keep_default_na=False)
#                     else:
#                         temp=pd.read_excel(f,skiprows=skip,header=None,names=cols,sheet_name=sheet,keep_default_na=False)
#                 print('File Read Rows =', temp.shape[0])
#                 if property!=None:
#                     temp['Property']=propertyName
#                 total=total+temp.shape[0]
#                 resultDF=pd.concat([resultDF, temp],ignore_index=True)
        
#         print('Total Rows =', total)
#         return resultDF

#     def getFileCount(self,**kwargs):#path,pathType
#         folderName=self.setPath(self.path,self.pathType)
#         files=os.listdir(folderName)
#         return len(files)
    
#     @staticmethod
#     def checkErrorFile(**kwargs):
#         root = os.getcwd().split(os.sep)[:-1]
#         file=os.sep.join(root)+C.OUTPUT.value+C.ERROR.value+'.csv'
#         if os.path.isfile(file):
#             return True
#         else:
#             return False

#     @staticmethod
#     def buildDF(*args,**kwargs):#inputDF,tgt
#         inputDF,tgt=args[0],args[1]
#         outputDF=pd.DataFrame(columns=tgt)
#         if inputDF.shape[0]>0:
#             outputDF=inputDF[tgt]
#         return outputDF
    
#     def writeFile(self,*args,**kwargs):#df,file,pathType,fType
#         df,file,pathType,fType=args[0],args[1],args[2],args[3]

#         sheet = kwargs.get('sheet', None) # Optional input
#         id = kwargs.get('id', None) # Optional input
        
#         fileName=self.setPath(file,pathType)

#         if id==None:
#             id=False
        
#         if sheet==None:
#             sheet='Sheet1'

#         if fType==C.CSV.value:
#             df.to_csv(fileName, index=id)
#         elif fType==C.EXCEL.value:
#             df.to_excel(fileName, sheet_name=sheet,engine='xlsxwriter',index=id)
#         print('Total rows downloaded to file =',df.shape[0])


