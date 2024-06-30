from http.client import HTTPException

import pandas as pd
from dto.transreport_dto import transreportsListDTO
from services.myfilehandler import myFileHandler


class transreportFileHandler(myFileHandler):
    def __init__(self,**kwargs):
        file = kwargs.get('file', None)
        folder = kwargs.get('folder', None)
        if file:
            super().__init__(file=file)
        elif folder:
            super().__init__(folder=folder)
        
#######################################################################################################################    
    def convert_df_to_list(self, df:pd.DataFrame,**kwargs) -> transreportsListDTO:
        column_names = kwargs.get('column_names', None)
        rename_columns = kwargs.get('rename_columns', None) #rename columns for Chase downloads

        errorsList = []
        
        if rename_columns:
            df.rename(columns=column_names, inplace=True)
        df=self.convert_columns_to_int(df, ['sequence_id'])    
        df=self.convert_columns_to_string(df, ['category','calc_method','fields'])
        errorsList = self.validate_null(df)
        dupList = self.check_duplicates(df,columns=['sequence_id'])
        try:
            if errorsList:
                return {},errorsList
            elif dupList:
                return {},dupList
            else:
                transreports_data = df.to_dict(orient='records')
                return transreports_data,[]
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing data: {str(e)}")

# #################################################################################################################