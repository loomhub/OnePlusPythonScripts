from http.client import HTTPException

import pandas as pd
from dto.tenant_dto import tenantsListDTO
from services.myfilehandler import myFileHandler


class tenantFileHandler(myFileHandler):
    def __init__(self,**kwargs):
        file = kwargs.get('file', None)
        folder = kwargs.get('folder', None)
        if file:
            super().__init__(file=file)
        elif folder:
            super().__init__(folder=folder)
        
#######################################################################################################################    
    def convert_df_to_list(self, df:pd.DataFrame,**kwargs) -> tenantsListDTO:
        column_names = kwargs.get('column_names', None)
        rename_columns = kwargs.get('rename_columns', None) #rename columns for Chase downloads

        errorsList = []
        
        if rename_columns:
            df.rename(columns=column_names, inplace=True)
        df=self.convert_columns_to_date(df, ['lease_start','lease_end'])
        df=self.convert_columns_to_numeric(df, ['rent','security_deposit'])
        df=self.convert_columns_to_string(df, ['unit_name'], na_values='NA')
        errorsList = self.validate_null(df)
        dupList = self.check_duplicates(df,columns=['customer', 'property_name','unit_name','lease_start','lease_end'])
        try:
            if errorsList:
                return {},errorsList
            elif dupList:
                return {},dupList
            else:
                tenants_data = df.to_dict(orient='records')
                return tenants_data,[]
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing data: {str(e)}")

# #################################################################################################################