import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
import category_encoders as ce
from joblib import dump

# create df
trainval = pd.read_csv('final3_airbnb.csv', header=1)
drop_cols = ['description', 'price_category', 'number_of_reviews']
trainval = trainval.drop(columns=drop_cols, axis=1)
print(trainval.shape)

# drop null values
trainval.dropna(inplace=True)

# setting features and target
target = 'price'
features = ['host_since', 'zipcode', 'room_type', 'maximum_nights', 'minimum_nights',
            'extra_people', 'accommodates', 'neighbourhood','beds', 'property_type',
            'cancellation_policy', 'guests_included', 'bedrooms', 'bathrooms']


def wrangle(X):
    X = X.copy()
    return X


train_rentals, val_rentals = train_test_split(trainval, random_state=42)
train = wrangle(train_rentals)
val = wrangle(val_rentals)
X_train = train.drop(columns=target)
X_val = val.drop(columns=target)
y_train = train[target]
y_val = val[target]

# X = train[features]
# y = train[target]

# model
model = make_pipeline(
    ce.OrdinalEncoder(),
    RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
)

model.fit(X_train, y_train)
model.predict(X_val)

print(model)
dump(model, 'model.pkl')