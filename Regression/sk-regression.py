from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


load_data = datasets.load_boston()
data_x = load_data.data
data_y = load_data.target

model = LinearRegression()
model.fit(data_x,data_y)

x,y = datasets.make_regression(100,1,1,noise=10)
plt.scatter(x,y)
plt.show()

print(model.coef_)
print(model.intercept_)
print(model.get_params())
print(model.score(data_x,data_y))
print(model.predict(data_x[:4,:]))
print((data_y[:4]))

