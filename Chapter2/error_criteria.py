import numpy as np 

def MSE(y,y_hat):
    y , y_hat = np.array(y), np.array(y_hat)
    diff = np.subtract(y ,y_hat)
    sqr_diff =np.square(diff)
    return np.mean(sqr_diff)

def RMSE(y,y_hat):
    y , y_hat = np.array(y), np.array(y_hat)
    diff = np.subtract(y ,y_hat)
    sqr_diff =np.square(diff)
    mean= np.mean(sqr_diff)
    return np.sqrt(mean)


def MAE(y,y_hat):
    y , y_hat = np.array(y), np.array(y_hat)
    diff = np.subtract(y ,y_hat)
    absolute = np.abs(diff)
    return np.mean(absolute)

def huber_loss(y,y_hat,delta=1.0):
    y , y_hat = np.array(y), np.array(y_hat)
    huber_mse = 0.5*np.square(y-y_hat)
    huber_mae = delta*(np.abs(y-y_hat)-0.5*delta)
    return np.mean(np.where((y-y_hat)<= delta, huber_mse,huber_mae))
    
    
y = [1.08, 1.2, 1.4, 2.1, 1.9, 7, 2.9]
y_hat = [0.7, 1.1, 1.5, 1.9, 2.3, 2.7, 3.1]

mse = MSE(y=y, y_hat=y_hat)
mae = MAE(y=y, y_hat=y_hat)
huber = huber_loss(y=y, y_hat=y_hat, delta=1.35)
print("MSE = {}\nMAE = {}\nHuber Loss = {}".format(mse, mae,huber))