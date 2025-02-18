import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import MinMaxScaler
import joblib
import numpy as np

# Load the data
data = pd.read_csv(r'/home/muhammad-ahmad-nadeem/Projects/Lahore_house_price_predictor/resources/lahore_housing_prices.csv')

# Initial Data Inspection
data.head(3)
#    house_id   Type                        Location      Area  Bath(s)  Bedroom(s)     Price
# 0  46326643  House     DHA Defence, Lahore, Punjab   1 Kanal        6           5  75500000
# 1  46952582  House  Bahria Orchard, Lahore, Punjab   8 Marla        5           5  25000000
# 2  47357581  House    Paragon City, Lahore, Punjab  10 Marla        6           5  47000000

'''data.shape'''
#17169, 7

data.describe()
#            house_id       Bath(s)    Bedroom(s)         Price
# count  1.716900e+04  17169.000000  17169.000000  1.716900e+04
# mean   4.655362e+07      4.716233      4.183820  4.758766e+07
# std    1.796472e+06      1.329716      1.294566  5.467632e+07
# min    6.872350e+05      1.000000      1.000000  1.150000e+05
# 25%    4.652353e+07      4.000000      3.000000  1.800000e+07
# 50%    4.706818e+07      5.000000      4.000000  3.200000e+07
# 75%    4.731195e+07      6.000000      5.000000  6.000000e+07
# max    4.739719e+07     10.000000     11.000000  7.171000e+08

''' data.info() '''
# RangeIndex: 17169 entries, 0 to 17168
# Data columns (total 7 columns):
#  #   Column      Non-Null Count  Dtype 
# ---  ------      --------------  ----- 
#  0   house_id    17169 non-null  int64 
#  1   Type        17169 non-null  object
#  2   Location    17169 non-null  object
#  3   Area        17169 non-null  object
#  4   Bath(s)     17169 non-null  int64 
#  5   Bedroom(s)  17169 non-null  int64 
#  6   Price       17169 non-null  int64 
# dtypes: int64(4), object(3)
# memory usage: 939.1+ KB

# Check for null and duplicate values
'''no null value'''
data.isnull().sum()

'''no duplicate value'''
data.duplicated().sum()

'''unique values in each column'''
data['Location'].nunique() #324
data['Area'].nunique() #170
data['Type'].nunique() #4

# Frequency Encoding
locfre = data['Location'].value_counts()
data['Location'] = data['Location'].map(locfre)

Arfre = data['Area'].value_counts()
data['Area'] = data['Area'].map(Arfre)

tyfre = data['Type'].value_counts()
data['Type'] = data['Type'].map(tyfre)

# Data Scaling
scaler = MinMaxScaler()
data[['Price']] = scaler.fit_transform(data[['Price']])

# Visualizations
# Boxplot for Price Distribution
plt.figure(figsize=(4, 4))
plt.boxplot(x=data['Price'], vert=False, patch_artist=True)
plt.title('House Price Distribution')
plt.xlabel('Price')
# plt.show()

# Area vs. Price Scatter Plot
sorted_data = data.sort_values(by='Area')
plt.figure(figsize=(6, 6))
plt.plot(sorted_data['Area'], sorted_data['Price'], color='green', linewidth=2)
plt.title('Area vs. Price', fontsize=16)
plt.xlabel('Area (sq. ft)', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
# plt.show()

# Location vs. Price Scatter Plot
sorted_data = data.sort_values(by='Location')
plt.figure(figsize=(6, 6))
plt.plot(sorted_data['Location'], sorted_data['Price'], color='green', linewidth=2)
plt.title('Location vs. Price', fontsize=16)
plt.xlabel('Location', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
# plt.show()

# Outlier Removal
Q1 = data['Price'].quantile(0.25)
Q3 = data['Price'].quantile(0.75)
IQR = Q3 - Q1
min1 = Q1 - 1.5 * IQR
max1 = Q3 + 1.5 * IQR
data = data[(data['Price'] >= min1) & (data['Price'] <= max1)]

data.head(3)
#    house_id   Type  Location      Area  Bath(s)  Bedroom(s)     Price
# 0  46326643  16017  1.000000  0.889844        6           5  0.105142
# 1  46952582  16017  0.085467  0.085057        5           5  0.034708
# 2  47357581  16017  0.051610  0.881710        6           5  0.065392

# Boxplot After Outlier Removal
plt.figure(figsize=(4, 4))
plt.boxplot(x=data['Price'], vert=False, patch_artist=True)
plt.title('After Removing Outliers')
plt.xlabel('Price')
# plt.show()

# Drop Useless Columns
data = data.drop(['house_id'], axis=1)

# Train-Test Split
inpu = data.iloc[:, :-1]
outpu = data['Price']
x_train, x_test, y_train, y_test = train_test_split(inpu, outpu, random_state=42, test_size=0.2)

# Train the Model
sv = DecisionTreeRegressor(max_features='log2', max_depth=15, min_samples_leaf=1, min_samples_split=10)
sv.fit(x_train, y_train)

# Hyperparameter Tuning (Commented for brevity)
# param_grid = {
#     'max_depth': [5, 10, 15],
#     'max_features': ['auto', 'log2'],
#     'min_samples_split': [2, 5, 10],
#     'min_samples_leaf': [1, 2, 4]
# }
# grid_search = GridSearchCV(estimator=sv, param_grid=param_grid, cv=5)
# grid_search.fit(x_train, y_train)
# print(grid_search.best_params_)

# Save Model and Supporting Files
house_type_freq = data['Type'].value_counts().to_dict()
location_freq = data['Location'].value_counts().to_dict()

joblib.dump(sv, 'rfc_model.pkl')
joblib.dump((house_type_freq, location_freq), 'frequency_mappings.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Load Saved Components
rfc_loaded = joblib.load('rfc_model.pkl')
house_type_freq, location_freq = joblib.load('frequency_mappings.pkl')
scaler = joblib.load('scaler.pkl')

# Prediction Function
def predict_house_price(house_type, num_bedrooms, num_bathrooms, location, area):
    try:
        house_type_encoded = house_type_freq.get(house_type, 0)
        location_encoded = location_freq.get(location, 0)
        input_features = [[house_type_encoded, num_bedrooms, num_bathrooms, location_encoded, area]]
        predicted = rfc_loaded.predict(input_features)
        predictions_original_scale = scaler.inverse_transform([[predicted[0]]])
        return predictions_original_scale[0][0]
    except Exception as e:
        raise ValueError(f"An error occurred during prediction: {e}")

# Example Prediction
# house_type = 'house'
# num_bedrooms = 3
# num_bathrooms = 2
# location = 'Gulberg'
# area = 2000

# try:
#     predicted_price = predict_house_price(house_type, num_bedrooms, num_bathrooms, location, area)
#     print("Predicted Price:", predicted_price)
# except ValueError as e:
#     print(e)
