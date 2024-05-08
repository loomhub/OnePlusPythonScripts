from http.client import HTTPException

import pandas as pd
from dto.transaction_dto import transactionsListDTO
from services.myfilehandler import myFileHandler


class transactionFileHandler(myFileHandler):
    def __init__(self,**kwargs):
        file = kwargs.get('file', None)
        folder = kwargs.get('folder', None)
        if file:
            super().__init__(file=file)
        elif folder:
            super().__init__(folder=folder)
        
#######################################################################################################################    
    def convert_df_to_list(self, file:str, df:pd.DataFrame,**kwargs) -> transactionsListDTO:
        column_names = kwargs.get('column_names', None)
        rename_columns = kwargs.get('rename_columns', None) #rename columns for Chase downloads

        errorsList = []
        
        if rename_columns:
            df.rename(columns=column_names, inplace=True)
        df=self.adjust_columns(df, column_names, remove_starting_with ='not_required')
        df=self.convert_columns_to_string(df, ['bank_account_key','description','classification','period_status',
                                                'transaction_group','transaction_type','comments',
                                                'vendor_no_w9','customer_no_w9'])
        df=self.convert_columns_to_string(df, ['vendor'], na_values='GeneralVendor')
        df=self.convert_columns_to_string(df, ['customer'], na_values='GeneralCustomer')
        df=self.convert_columns_to_date(df, ['tdate'])
        df=self.convert_columns_to_numeric(df, ['amount'])
        errorsList = self.validate_null(df)
        dupList = self.check_duplicates(df,columns=['bank_account_key','tdate','description','amount'])
        try:
            if errorsList:
                return {},errorsList
            elif dupList:
                return {},dupList
            else:
                transactions_data = df.to_dict(orient='records')
                return transactions_data,[]
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing data: {str(e)}")

# #################################################################################################################