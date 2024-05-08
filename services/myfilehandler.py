from datetime import date, datetime
from http.client import HTTPException
import os, shutil
from typing import List, Optional, Tuple, Type
import pandas as pd
from pydantic import BaseModel, ValidationError
import requests


class myFileHandler:
    def __init__(self,**kwargs):
        file = kwargs.get('file', None)
        folder = kwargs.get('folder', None)
        root = os.getcwd()

        if file:
            file_extension = os.path.splitext(file)[1]
            if file_extension.lower() == '.csv': 
                self.files = [os.path.join(root,file)]
        elif folder:
            filenames = os.listdir(folder)
            self.files = [os.path.join(root, folder, filename) for filename in filenames
                                        if filename.lower().endswith('.csv')]
                

#############################################################################################################
    def save_file_to_disk(self):
        # Check if the uploads directory exists, if not, create it
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
        # Write the contents of the uploaded file to a new file in the server
        try:
            with open(self.file_location, "wb") as buffer:
                shutil.copyfileobj(self.file.file, buffer)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Could not write to file: {str(e)}")
#############################################################################################################
    def read_file(self,file,**kwargs):
        fileheaders = kwargs.get('fileheaders', None)
        try:
            if fileheaders:
                return pd.read_csv(file, na_values=[], header=None, names=fileheaders,index_col=False)
            else:
                return pd.read_csv(file, na_values=[],index_col=False)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to load file into DataFrame: {str(e)}")
#############################################################################################################
    def read_data(self,**kwargs):
        column_names = kwargs.get('column_names', None)
        try:
            for file in self.files:
                return self.read_file(file,column_names=column_names)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to load file into DataFrame: {str(e)}")
#############################################################################################################
    def convert_dataframe_to_list_dto(
            self,
            df: pd.DataFrame, #pandas.DataFrame containing the data.
            dto_class: Type[BaseModel] #The DTO class to which rows will be converted.
            )  -> Tuple[List[BaseModel],List[str]]: #Return a list of DTO instances.
    
        dto_list=[]
        for index, row in df.iterrows():
            try:
                dto_instance = dto_class(**row.to_dict()) # Use dictionary unpacking to initialize the DTO from a row.
                dto_list.append(dto_instance)
            except ValidationError as e:
                print(f"Error occurred at row index {index}")
                
        print(type(dto_list))   

        return dto_list
#############################################################################################################
    def parse_date(self,date_str):
        if len(date_str.split('/')[-1]) == 4:  # Check if the year part has four digits
            return pd.to_datetime(date_str, format='%m/%d/%Y', errors='coerce')
        else:
            return pd.to_datetime(date_str, format='%m/%d/%y', errors='coerce')
#############################################################################################################
    # Convert the DataFrame to a list of dictionaries
    def format_date(self,x):
        return x.strftime('%Y-%m-%d') if not pd.isna(x) and isinstance(x, date) else None
#############################################################################################################
    def convert_columns_to_date(self, 
                        df: pd.DataFrame, 
                        column_names: List[str],
                        **kwargs) -> pd.DataFrame:
        null_value_date = kwargs.get('null_value_date', '2099-12-31')
  
        for column_name in column_names:
            if column_name in df.columns:
                try:
                    df[column_name] = df[column_name].fillna(pd.Timestamp(null_value_date))
                    df[column_name] = df[column_name].apply(self.parse_date).dt.date
                    df[column_name] = df[column_name].apply(self.format_date)  # Format the 'tdate' column
                except Exception as e:
                    print(f"Error converting {column_name}: {e}")
            else:
                print(f"Column {column_name} not found in DataFrame.")
        return df
#############################################################################################################   
    def convert_month_to_date(self, 
                            df: pd.DataFrame, 
                            column_names: List[str],
                            **kwargs) -> pd.DataFrame:
            null_value_date = kwargs.get('null_value_date', '2099-12-31')
            for column_name in column_names:
                if column_name in df.columns:
                    try:
                        df[column_name] = df[column_name].fillna(pd.Timestamp(null_value_date))
                        df[column_name] = pd.to_datetime(df[column_name]).dt.date
                        df[column_name] = pd.to_datetime(df[column_name]).dt.to_period('M').dt.to_timestamp()
                    except Exception as e:
                        print(f"Error converting {column_name}: {e}")
                else:
                    print(f"Column {column_name} not found in DataFrame.")
            return df
############################################################################################################# 
    def convert_columns_to_string(self, 
                        df: pd.DataFrame, 
                        column_names: List[str],**kwargs) -> pd.DataFrame:
        na_values = kwargs.get('na_values', '')
        for column_name in column_names:
            if column_name in df.columns:
                try:
                    df[column_name] = df[column_name].fillna(na_values).astype(str)
                except Exception as e:
                    print(f"Error converting {column_name}: {e}")
            else:
                print(f"Column {column_name} not found in DataFrame.")
        return df
#############################################################################################################    
    def convert_columns_to_numeric(self, 
                        df: pd.DataFrame, 
                        column_names: List[str]) -> pd.DataFrame:
        for column_name in column_names:
            if column_name in df.columns:
                try:
                    df[column_name] = df[column_name].fillna(0).astype(str)
                    df[column_name] = df[column_name].str.replace(',', '').str.replace('$', '')
                    df[column_name] = df[column_name].str.replace('(', '-').str.replace(')', '')
                    # Handle the case where "-" should be converted to 0, but not affect numbers like "-90"
                    df[column_name] = df[column_name].apply(lambda x: '0' if x.strip() == '-' else x)
                    #df[column_name] = df[column_name].str.replace(r'\((\d+)\)', r'-\1', regex=True).astype(float)
                    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')   
                except Exception as e:
                    print(f"Error converting {column_name}: {e}")
            else:
                print(f"Column {column_name} not found in DataFrame.")
        return df
#############################################################################################################    
    def convert_columns_to_int(self, 
                        df: pd.DataFrame, 
                        column_names: List[str]) -> pd.DataFrame:
        for column_name in column_names:
            if column_name in df.columns:
                try:
                    df[column_name] = df[column_name].astype(int)
                except Exception as e:
                    print(f"Error converting {column_name}: {e}")
            else:
                print(f"Column {column_name} not found in DataFrame.")
        return df
#############################################################################################################
    def adjust_columns(self,
                        df: pd.DataFrame, 
                        columns, 
                        **kwargs) -> pd.DataFrame:
        remove_starting_with = kwargs.get('remove_starting_with', None)

        if remove_starting_with:
            columns_to_remove = [value for key, value in columns.items() if value.startswith(remove_starting_with)]
            columns = [col for col in columns if not col.startswith(remove_starting_with)]
            df.drop(columns=columns_to_remove, inplace=True)
            return df
#############################################################################################################

    def validate_null(self,df: pd.DataFrame) -> List[str]:
    # Create a mask that is True wherever there are NaNs
        mask = df.isna().any(axis=1)
    
    # Use the mask to select all rows that have any NaN values
        errorDf = df[mask]
        errorsList = errorDf.to_dict(orient='records')
        if len(errorsList)>0:
            return {'errors':errorsList}
        else:
            return {}
############################################################################################################
  
    def check_duplicates(self,df: pd.DataFrame,columns: Optional[List[str]] = None) -> List[str]:
        if columns is not None:
            duplicates = df[df.duplicated(subset=columns)]
        else:
            duplicates = df[df.duplicated()]
        
        if len(duplicates)>0:
            error_dict = {'duplicates': duplicates.to_dict(orient='records')}
            return {'duplicates':error_dict}
        else:
            return {}
############################################################################################################
    def post_data(self, url, input_data, myObjects):
        try:
            input_count = len(input_data)
            load_data = {myObjects: input_data}  # Wrap the data in a dictionary

            response = requests.post(url, json=load_data)
            response.raise_for_status()  
            
            output_data = response.json()  # Convert the response to JSON format
            output_count = len(output_data)
            print(f"Input records: {input_count}, Output records: {output_count}")
            if output_count == input_count:
                
                return True, {'Input records': {input_count}, 'Output records': {output_count}}
            else:
                return False, {'error': 'Input and output records do not match'}
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
############################################################################################################
    def process_files(self,url,myObjects,**kwargs):
        column_names = kwargs.get('column_names', None)
        rename_columns = kwargs.get('rename_columns', None)
        fileheaders = kwargs.get('fileheaders', None)

        processing_results = []
        for file in self.files:
            filename = os.path.basename(file)    
            df = self.read_file(file,fileheaders=fileheaders)
    
            input_data, errorsList = self.convert_df_to_list(file, df,
                                                             column_names = column_names,
                                                             rename_columns = rename_columns
                                                             )

            if errorsList:
                processing_results.append({file: 'error', 'details': errorsList})
            else:
            # Send a POST request with JSON data
                try:
                    success, records = self.post_data(url, input_data,myObjects)
                    if success:
                        processing_results.append({filename: records})
                    else:
                        processing_results.append({filename: 'error', 'details': 'Error posting data'})
                except Exception as e:
                    print(f"Error: {str(e)}")
        
        return processing_results

############################################################################################################