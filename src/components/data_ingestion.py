import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_path = os.path.join('artifacts','train.csv')
    test_path = os.path.join('artifacts','test.csv')
    raw_path = os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.paths = DataIngestionConfig()

    def initialise_Ingestion(self):
        logging.info('Data ingestion started')
        try:
            df = pd.read_csv('data.csv')
            logging.info('Data Read Successfully')

            os.makedirs(os.path.dirname(self.paths.train_path), exist_ok = True)
            
            df.to_csv(self.paths.raw_path, index = False, header = True)

            train, test = train_test_split(df, test_size = 0.2, random_state = 2)
            logging.info('Train test split initiated')
            
            train.to_csv(self.paths.train_path, index = False, header = True)
            test.to_csv(self.paths.test_path, index = False, header = True)

            logging.info('Data ingestion completed')
            return (self.paths.train_path, self.paths.test_path)
        
        except Exception as e:
            logging.info('Exception occured')
            raise CustomException(e, sys)
        

if __name__ == '__main__':
    data = DataIngestion()
    train, test = data.initialise_Ingestion()

    transform = DataTransformation()
    transform.initaiise_Transformation(train, test)
        

