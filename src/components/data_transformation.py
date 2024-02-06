import numpy as np 
import pandas as pd 
import os
import sys
from dataclasses import dataclass

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    data_transform_path = os.path.join('artifacts','preprocessing.pkl')

class DataTransformation:
    def __init__(self):
        self.preprocessing_path = DataTransformationConfig()

    def get_transformation(self):
        try:
            num_col = ["writing_score", "reading_score"]
            cat_col = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline = Pipeline(
                steps = [
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('one hot encoding', OneHotEncoder()),
                    ('scaling', StandardScaler(with_mean=False))
                ]
            )

            preprocessor = ColumnTransformer(
                [
                ("num_pipeline", num_pipeline, num_col),
                ("cat_pipeline", cat_pipeline, cat_col)
                ]
            )

            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)
        

    def initaiise_Transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Read the data')

            preprocessing_obj = self.get_transformation()

            target_col = ['math_score']
            num_col = ["writing_score", "reading_score"]

            input_train_df = train_df.drop(columns = target_col, axis = 1)
            target_train_df = train_df[target_col]

            input_test_df = test_df.drop(columns = target_col, axis =1)
            target_test_df = test_df[target_col]

            input_train_arr=preprocessing_obj.fit_transform(input_train_df)
            input_test_arr=preprocessing_obj.transform(input_test_df)

            train_arr = np.c_[
                input_train_arr, np.array(target_train_df)
            ]
            test_arr = np.c_[input_test_arr, np.array(target_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.preprocessing_path.data_transform_path,
                obj=preprocessing_obj

            )

            return (train_arr, test_arr, self.preprocessing_path.data_transform_path)

        except Exception as e:
            raise CustomException(e, sys)