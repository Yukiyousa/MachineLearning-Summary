from sklearn.model_selection import learning_curve
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

digits = load_digits()
x = digits.data
y = digits.target
print(x)
train_size,train_loss,test_loss = learning_curve(SVC(gamma=0.0001),x,y,cv=10,scoring='neg_mean_squared_error',train_sizes=[0.1,0.25,0.5,1])
train_loss_mean = -np.mean(train_loss,axis=1)
test_loss_mean = -np.mean(test_loss,axis=1)

plt.plot(train_size,train_loss_mean,'o-',color='r',label="Training")
plt.plot(train_size,test_loss_mean,'o-',color='g',label="Cross-Validation")

plt.xlabel("Training examples")
plt.ylabel("Loss")
plt.legend(loc="best")
plt.show()