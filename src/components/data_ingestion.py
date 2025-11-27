import os,sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifacts/data_ingestion","train.csv")
    test_data_path = os.path.join("artifacts/data_ingestion","test.csv")
    raw_data_path = os.path.join("artifacts/data_ingestion","raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion method started")  
        try:
            logging.info("Reading the dataset from source")
            data = pd.read_csv("data-source/final_employee_attrition merge.csv")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data is saved")

            train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)
            logging.info("Train test split is completed")   

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of the data is completed")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            logging.info("Exception occurred at data ingestion stage")
            raise CustomException(e, sys)

if __name__=="__main__": 
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
