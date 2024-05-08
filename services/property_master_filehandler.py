from http.client import HTTPException

import pandas as pd
from dto.property_master_dto import propertyMastersListDTO
from services.myfilehandler import myFileHandler


class propertyMasterFileHandler(myFileHandler):
    def __init__(self,**kwargs):
        file = kwargs.get('file', None)
        folder = kwargs.get('folder', None)
        if file:
            super().__init__(file=file)
        elif folder:
            super().__init__(folder=folder)
        
#######################################################################################################################    
    def convert_df_to_list(self, df:pd.DataFrame,**kwargs) -> propertyMastersListDTO:
        column_names = kwargs.get('column_names', None)
        rename_columns = kwargs.get('rename_columns', None) #rename columns for Chase downloads

        errorsList = []
        
        if rename_columns:
            df.rename(columns=column_names, inplace=True)
        df=self.convert_columns_to_string(df, ['property_name','property_description','llc','note','county'])
        df=self.convert_columns_to_date(df, ['purchase_date','sell_date'])
        df=self.convert_columns_to_numeric(df, ['purchase_price','sell_price'])
        df=self.convert_columns_to_int(df, ['units'])
        errorsList = self.validate_null(df)
        dupList = self.check_duplicates(df,columns=['property_name'])
        try:
            if errorsList:
                return {},errorsList
            elif dupList:
                return {},dupList
            else:
                propertyMasters_data = df.to_dict(orient='records')
                return propertyMasters_data,[]
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing data: {str(e)}")

# #################################################################################################################