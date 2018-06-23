#Upload the data and print first 5 rows

import pandas as pd
df = pd.read_csv ("Website_VIP_User_data_10000.csv")
print(df.head())

#Check for null values~ No null values are present
print(df.isnull().sum())

#Check for datatypes ~ All datatypes are correct
df.info()

#Check for the outliers
df['x-Mean'] = abs(df['payment_7_day'] - df['payment_7_day'].mean())
df['1.96*std'] = 1.96*df['payment_7_day'].std()  
df['Outlier_payment_7_day'] = abs(df['payment_7_day'] - df['payment_7_day'].mean()) > 1.96*df['payment_7_day'].std()
df1= df['Outlier_payment_7_day'].value_counts()
print (df1)

#Partition the data into 70-30
from sklearn.model_selection import train_test_split
predictors = ['payment_7_day','dau_days','days_between_install_first_pay','total_txns_7_day','total_page_views','total_product_liked','product_like_rate','total_free_coupon_got','total_bonus_xp_points']
y_variable = ['IsVIP_500']
predictors_train, predictors_test, y_variable_train, y_variable_test = train_test_split(df[predictors],df[y_variable],train_size = 0.7,random_state=7)
                                    
