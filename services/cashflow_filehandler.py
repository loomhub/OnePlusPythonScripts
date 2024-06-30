from http.client import HTTPException

import pandas as pd
from dto.cashflow_dto import cashflowsListDTO
from services.myfilehandler import myFileHandler


class cashflowFileHandler(myFileHandler):
    def __init__(self,**kwargs):
        file = kwargs.get('file', None)
        folder = kwargs.get('folder', None)
        if file:
            super().__init__(file=file)
        elif folder:
            super().__init__(folder=folder)
        
#######################################################################################################################    
    def convert_df_to_list(self, df:pd.DataFrame,**kwargs) -> cashflowsListDTO:
        column_names = kwargs.get('column_names', None)
        rename_columns = kwargs.get('rename_columns', None) #rename columns for Chase downloads

        errorsList = []
        
        if rename_columns:
            df.rename(columns=column_names, inplace=True)
        df=self.convert_columns_to_string(df, ['bank_account_key','period_status'])
        df=self.convert_columns_to_date(df, ['start_date','end_date'])
        df=self.convert_columns_to_numeric(df, ['cash_change','ending_balance','calc_balance'])
        errorsList = self.validate_null(df)
        dupList = self.check_duplicates(df,columns=['bank_account_key','start_date','end_date'])
        try:
            if errorsList:
                return {},errorsList
            elif dupList:
                return {},dupList
            else:
                cashflows_data = df.to_dict(orient='records')
                return cashflows_data,[]
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing data: {str(e)}")

# #################################################################################################################