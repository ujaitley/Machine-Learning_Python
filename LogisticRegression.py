import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

def train_logistic_regression(train_x, train_y):
    logistic_regression_model = LogisticRegression()
    logistic_regression_model.fit(train_x, train_y)
    return logistic_regression_model

def model_accuracy(trained_model, features, targets):
    accuracy_score = trained_model.score(features, targets)
    return accuracy_score

def main():
    df = pd.read_csv ("TEST_CAPSTONE1.csv")
    predictors = ['payment_7_day','dau_days','days_between_install_first_pay','total_txns_7_day','total_page_views','total_product_liked','product_like_rate','total_free_coupon_got','total_bonus_xp_points']
    y_variable = ['IsVIP_500']
    predictors_train, predictors_test, y_variable_train, y_variable_test = train_test_split(df[predictors],df[y_variable],train_size = 0.7,random_state=7)
    logistic_regression_model_training = train_logistic_regression(predictors_train, y_variable_train)
    train_accuracy = model_accuracy(logistic_regression_model_training, predictors_train, y_variable_train)
 
    # Testing the logistic regression model
    test_accuracy = model_accuracy(logistic_regression_model_training, predictors_test, y_variable_test)
 
    print ("Train Accuracy :: ", train_accuracy)
    print ("Test Accuracy :: ", test_accuracy)
 
if __name__ == "__main__":
    main()                                    
