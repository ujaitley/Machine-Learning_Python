import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv ("Website_VIP_User_data_10000.csv")
predictors = ['payment_7_day','dau_days','days_between_install_first_pay','total_txns_7_day','total_page_views','total_product_liked','product_like_rate','total_free_coupon_got','total_bonus_xp_points']
y_variable = ['IsVIP_500']
x_train, x_test, y_train, y_test = train_test_split(df[predictors],df[y_variable],train_size = 0.7,random_state=7)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train) 
