import boto3 
import csv
import pandas as pd
import os
import os.path
import argparse
import json


BUCKET_NAME = 'spotify-dataset'
BUCKET_FILE_NAME = 'data.csv'
LOCAL_FILE_NAME = 'data.csv'
PATH = 'data.csv'


def read_s3_file(path):
    data_df = pd.read_csv(path)
    return data_df  


def upload_file(file_name, BUCKET_NAME, object_name=None)

    if object_name is None:
        object_name = file_name
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, BUCKET_NAME, object_name)
    except ClientError as e:
        print(e)
        return False
    return True
    

def download_s3_file():
    if os.path.exists(PATH):
        return read_s3_file(PATH)
    else:
        s3 = boto3.client('s3')
        s3.download_file(BUCKET_NAME, BUCKET_FILE_NAME, LOCAL_FILE_NAME)
        return read_s3_file(LOCAL_FILE_NAME)


 if __name__ == "__main__":
        
    df = download_s3_file()

    parser = argparse.ArgumentParser()
    parser.add_argument( "column", type=str)
    args = parser.parse_args()

    df = df.sort_values(by=[args.column], inplace=False, ascending=False)

    df.head(50).to_json('spotify-dataset.json', orient='table')

    upload_file('spotify-dataset.json', 'spotify-dataset')







