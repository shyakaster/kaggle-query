import os
import random
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi


api = KaggleApi()
api.authenticate()

datasets = api.dataset_list()

dataset_list = []

for dataset in datasets:
    dataset_attributes = vars(dataset)
    dataset_list.append(dataset_attributes)

dataset_df = pd.DataFrame(dataset_list)

print(dataset_df.shape)

# only 20 datasets
# it seems the API uses pagination, it only returns datasets 20 at a time
# so we'll have to work around this

dataset_df.to_csv('dataset_df.csv',index = False)

