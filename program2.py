from sklearn.neighbors import KNeighborsClassifier

X = [[1], [2], [3], [10], [11], [12]]
y = [0, 0, 0, 1, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

print("Prediction:", model.predict([[4]]))cre