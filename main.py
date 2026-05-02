import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# ---------------------------
# STEP 1: CREATE SYNTHETIC DATA
# ---------------------------
np.random.seed(42)

data = pd.DataFrame({
    "area": np.random.randint(500, 4000, 200),
    "bedrooms": np.random.randint(1, 5, 200),
    "bathrooms": np.random.randint(1, 4, 200),
    "age": np.random.randint(0, 30, 200),
    "parking": np.random.randint(0, 2, 200)
})

# Price formula (simulation)
data["price"] = (
    data["area"] * 3000 +
    data["bedrooms"] * 50000 +
    data["bathrooms"] * 30000 -
    data["age"] * 10000 +
    data["parking"] * 20000 +
    np.random.randint(-50000, 50000, 200)
)

print("\nDataset Preview:\n", data.head())

# ---------------------------
# STEP 2: SPLIT DATA
# ---------------------------
X = data.drop("price", axis=1)
y = data["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------
# STEP 3: TRAIN MODELS
# ---------------------------
lr = LinearRegression()
rf = RandomForestRegressor()

lr.fit(X_train, y_train)
rf.fit(X_train, y_train)

# ---------------------------
# STEP 4: PREDICTIONS
# ---------------------------
lr_pred = lr.predict(X_test)
rf_pred = rf.predict(X_test)

# ---------------------------
# STEP 5: EVALUATION
# ---------------------------
def evaluate(name, y_test, pred):
    print(f"\n{name} Results:")
    print("MAE:", mean_absolute_error(y_test, pred))
    print("RMSE:", np.sqrt(mean_squared_error(y_test, pred)))
    print("R2:", r2_score(y_test, pred))

evaluate("Linear Regression", y_test, lr_pred)
evaluate("Random Forest", y_test, rf_pred)

# ---------------------------
# STEP 6: SAVE MODEL
# ---------------------------
joblib.dump(rf, "models/house_model.pkl")

# ---------------------------
# STEP 7: SAMPLE PREDICTION
# ---------------------------
sample = [[2000, 3, 2, 5, 1]]  # area, bed, bath, age, parking
prediction = rf.predict(sample)

print("\nSample House Prediction:", prediction[0])

# ---------------------------
# STEP 8: VISUALIZATION
# ---------------------------
plt.scatter(y_test, rf_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted")
plt.savefig("outputs/graph.png")
plt.show()