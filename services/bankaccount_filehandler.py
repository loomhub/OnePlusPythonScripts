from http.client import HTTPException

import pandas as pd
from dto.bankaccount_dto import bankaccountsListDTO
from services.myfilehandler import myFileHandler


class bankaccountFileHandler(myFileHandler):
    def __init__(self,**kwargs):
        file = kwargs.get('file', None)
        folder = kwargs.get('folder', None)
        if file:
            super().__init__(file=file)
        elif folder:
            super().__init__(folder=folder)
        
#######################################################################################################################    
    def convert_df_to_list(self, df:pd.DataFrame,**kwargs) -> bankaccountsListDTO:
        column_names = kwargs.get('column_names', None)
        rename_columns = kwargs.get('rename_columns', None) #rename columns for Chase downloads

        errorsList = []
        
        if rename_columns:
            df.rename(columns=column_names, inplace=True)
        df=self.convert_columns_to_string(df, ['bank_account_key','bank','account_type','account_number','llc'])
        errorsList = self.validate_null(df)
        dupList = self.check_duplicates(df,columns=['bank_account_key'])
        try:
            if errorsList:
                return {},errorsList
            elif dupList:
                return {},dupList
            else:
                bankaccounts_data = df.to_dict(orient='records')
                return bankaccounts_data,[]
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing data: {str(e)}")

# #################################################################################################################