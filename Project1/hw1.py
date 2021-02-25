
#%% import packages

# impot packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp
import time
import winsound
import gc
from sklearn.feature_selection import mutual_info_classif
from sklearn.preprocessing import LabelEncoder
from pandas.api.types import is_string_dtype, is_numeric_dtype
from sklearn.preprocessing import OneHotEncoder

# coding alarm
def alarm():
    for i in range(2):
        # winsound.Beep(500, 990)
        # time.sleep(0.88)
        winsound.PlaySound('C:/Users/10331/OneDrive/Desktop/Project/Project Data/mario_coin.wav', winsound.SND_FILENAME)
        time.sleep(0.66)
        
def alarm1():
    winsound.PlaySound('C:/Users/10331/OneDrive/Desktop/Project/Project Data/super-mario-bros.wav', winsound.SND_FILENAME)
    winsound.PlaySound('C:/Users/10331/OneDrive/Desktop/Project/Project Data/mario_coin.wav', winsound.SND_FILENAME)

def alarm2():
    winsound.PlaySound('C:/Users/10331/OneDrive/Desktop/Project/Project Data/Alarm.wav', winsound.SND_FILENAME)
    
#%% import data

product = pd.read_csv("C:/Users/10331/OneDrive/Desktop/product_table.csv")
transaction = pd.read_csv("C:/Users/10331/OneDrive/Desktop/transaction_table.csv")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

product.isnull().sum()
transaction.isnull().sum()

transaction.dtypes
transaction.describe()
transaction["tran_prod_paid_amt"].value_counts().head(100)
transaction["tran_prod_paid_amt"].value_counts().reset_index().sort_values("index", ascending = False)
transaction.iloc[:,5:].sort_values("tran_prod_paid_amt", ascending = False)

product.dtypes
product.describe()
product["category_desc_eng"].value_counts().head(100)
product["category_desc_eng"].value_counts()

#%% Who are the best customers in terms of revenues, profits, transactions/store visits, number of products, etc.?

tmp = transaction.groupby("cust_id").sum().reset_index()
tmp.head()
tmp = tmp.idxmax()
tmp = product.iloc[tmp.values[[4,8]],0]

# 7671    999374982
# 7671    999374982

tmp2 = transaction.groupby("cust_id").nunique().reset_index()
tmp2.head()
tmp2 = tmp2.idxmax()
tmp2 = product.iloc[tmp2.values[[1,3,4]],0]

# 3388    999223297
# 7390    999357044
# 7242    999346275

#%% What are the products and product groups with the best volumes, revenues, profits, transactions, customers, etc.?

tmp3 = transaction.groupby("prod_id").sum().reset_index()
tmp3.head()
tmp3 = tmp3.idxmax()
tmp3 = product.iloc[tmp3.values[[5,4,8]],0]

# 3943    999232215
# 9896    999749499
# 9896    999749499

tmp4 = transaction.groupby("prod_id").nunique().reset_index()
tmp4.head()
tmp4 = tmp4.idxmax()
tmp4 = product.iloc[tmp4.values[[2,1]],0]

# 132     231387003
# 3943    999232215

#%% Which stores rank the highest in volumes, revenues, profits, transactions, customers, etc.?

tmp5 = transaction.groupby("store_id").sum().reset_index()
tmp5.head()
tmp5 = tmp5.idxmax()
tmp5 = product.iloc[tmp5.values[[5,4,8]],0]

# 163    234416010
# 163    234416010
# 163    234416010

tmp6 = transaction.groupby("store_id").nunique().reset_index()
tmp6.head()
tmp6 = tmp6.idxmax()
tmp6 = product.iloc[tmp6.values[[2,1]],0]

# 3      145519011
# 165    234416012

#%% Are there interesting groupings of customers, e.g., most valuable (buy everything at any price) or cherry-pickers 
# (buy mostly on promotions), defined by certain categories (buy baby products or never buy milk), etc.?




