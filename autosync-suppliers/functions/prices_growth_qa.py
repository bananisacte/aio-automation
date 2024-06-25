import warnings

import pandas as pd


def clean_up_qa_file(qa_df):
    columns_to_keep = [
        "ItemId",
        "category",
        "SubCategory",
        "CostPrice",
        "RegularPrice",
        "zap_url",
        "ZapLocation",
        "ZapMinimumPrice",
        "ZapDecreasingPrice"
    ]
    filtered_df = qa_df[columns_to_keep]
    filtered_df = filtered_df[filtered_df['category'] != 'לא פעילים - למחיקה או טיפול']
    filtered_df['Growth'] = ((filtered_df['ZapMinimumPrice'] - filtered_df['CostPrice']) / filtered_df['CostPrice'] * 100).round(2)
    filtered_df.loc[filtered_df['ZapMinimumPrice'].isnull(), 'Growth'] = ((filtered_df['RegularPrice'] - filtered_df['CostPrice']) / filtered_df['CostPrice'] * 100).round(2)
    filtered_df.to_csv("Files\\qa_results.csv", encoding='utf-8-sig', index=False)


def generate_qa_results(qa_file_path):
    warnings.filterwarnings('ignore', category=pd.errors.DtypeWarning)
    df = pd.read_csv(qa_file_path)
    qa_df = df.copy()
    clean_up_qa_file(qa_df)
