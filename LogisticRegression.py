
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv ("Website_VIP_User_data_10000.csv")

#Partition the data into 70-30

def main():
  predictors = ['payment_7_day','dau_days','days_between_install_first_pay','total_txns_7_day','total_page_views','total_product_liked','product_like_rate','total_free_coupon_got','total_bonus_xp_points']
  y_variable = ['IsVIP_500']
  predictors_train, predictors_test, y_variable_train, y_variable_test = train_test_split(df[predictors],df[y_variable],train_size = 0.7,random_state=7)
                                    
