import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([20, 30, 40, 50, 60])

model = LinearRegression()
model.fit(X, y)

print("Prediction:", model.predict([[6]]))