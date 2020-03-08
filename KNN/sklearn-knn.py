import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split, cross_val_score

iris = datasets.load_iris()
iris_x = iris.data
iris_y = iris.target

X_train,x_test,Y_train,y_test = train_test_split(iris_x,iris_y,test_size=0.3)

# print(iris_x)
# print(iris_y)

knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, iris_x, iris_y,cv=5,scoring='accuracy')
print(scores.mean())

knn.fit(X_train,Y_train)
print(knn.predict(x_test))
print(y_test)
print(knn.score(x_test,y_test))