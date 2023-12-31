# -*- coding: utf-8 -*-
"""Week3_2_Rupak.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pssbcIMO_w-eI2Wbex75Mjo30pF_Nf3O

#**Data cleaning and manipulation using Pandas and Numpy**
##**Dataset:**
1. chipotle.tsv (df)


 **Columns:**
-	Order Id
-	Quantity
-	Item Name
-	Choice Description
-	Item price

2. Chipotle dataset
- Importing the libraries
"""

# importing libraries
import numpy as np
import pandas as pd

"""- Reading the data"""

df = pd.read_csv("/content/drive/MyDrive/Week 3 - Data Cleaning (Pandas) - 2/chipotle.tsv",sep='\t')

"""- Printing the dataset"""

df

"""- Copying the dataset (To preserve the content of original dataset)"""

copy_df=df.copy()

"""- Printing the first 5 columns of the uncleaned dataset"""

copy_df.head()

"""- Printing the last 5 columns of the uncleaned dataset"""

copy_df.tail()

"""-Getting the shape of the dataset"""

copy_df.shape

"""- Getting more information about the dataset"""

copy_df.info()

"""- Finding the total null values in each columns

    1. isnull() - To find the null values
    2. sum() - To find the sum of all the null values

"""

copy_df.isnull().sum()

"""- Finding the duplicate values"""

duplicates = copy_df.duplicated()
copy_df[duplicates]

"""- Dropping duplicate values"""

copy_df = copy_df.drop_duplicates()

"""- Checking again for duplicate values"""

check_duplicates = copy_df.duplicated()
copy_df[check_duplicates]

"""- Printing unique 'item_name'"""

df['item_name'].unique()

"""- Formatting string"""

copy_df['item_name'] = copy_df['item_name'].str.replace('-', ' ')

""" - Printing again unique 'item_name'"""

copy_df['item_name'].unique()

"""- Formatting string"""

copy_df['choice_description'] = copy_df['choice_description'].str.strip('[]')

copy_df['choice_description'] = copy_df['choice_description'].str.replace('[', '',).str.replace(']', ',')

copy_df

"""- Formatting string"""

copy_df['item_price'] = copy_df['item_price'].str.replace('$', '')
copy_df.head()

"""- Getting more information about the dataset"""

copy_df.info()

"""- Converting to necessary datatype"""

copy_df['item_name'] = copy_df['item_name'].astype('string')

"""- Converting to necessary datatype"""

copy_df['choice_description'] = copy_df['choice_description'].astype('string')

"""- Converting to necessary datatype"""

copy_df['item_price'] = copy_df['item_price'].astype('float')

"""- Getting more information about the dataset"""

copy_df.info()

"""- Printing the cleaned dataset"""

copy_df