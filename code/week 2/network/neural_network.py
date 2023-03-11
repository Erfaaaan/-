import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn.model_selection as ms


#read 2d merged csv file
df = pd.read_csv('edit_merge.csv', encoding="windows_1258")


arr=np.array([])

#create a 2d array for population that each rows show populations for a country
population=df.loc[:,"population"]
population=population.values.tolist()
population=np.array(population)
population=population.reshape(211,60)


#create a 2d array for yield that each rows show yields for a country
Yield=df.loc[:,"yield"]
Yield=Yield.values.tolist()
Yield=np.array(Yield)
Yield=Yield.reshape(211,60)

#create a 2d array for harvested that each rows show harvesteds for a country
harvested=df.loc[:,"harvested"]
harvested=harvested.values.tolist()
harvested=np.array(harvested)
harvested=harvested.reshape(211,60)

#create a 2d array for production that each rows show productions for a country
production=df.loc[:,"production"]
production=production.values.tolist()
production=np.array(production)
production=production.reshape(211,60)


#create a 1d array that we will make it to a 3d array
for i in range(211):
    arr=np.append(arr,population[i])
    arr=np.append(arr,Yield[i])
    arr=np.append(arr,harvested[i])
    arr=np.append(arr,production[i])

#reshape 1d array to a 3d array that each dimension is for a country , culomn for years , and rows for values
arr=arr.reshape(211,4,60)


#train and test
x = arr[ : ,0 : 2,: ]

y = arr[: , 3 , :]

x_train,x_test,y_train,y_test = ms.train_test_split(x,y,test_size=0.2,random_state=0)

from keras.models import Model
from keras.layers import  Conv2D,MaxPool2D,Input,Flatten,Dense
from keras.losses import categorical_crossentropy
#creat modle with keras


myinput = Input(shape=(211,4,60))
conv1 = Conv2D(16,(5,3),activation='relu',padding='same')(myinput)
pool1 = MaxPool2D(pool_size=2)(conv1)
conv2 = Conv2D(16,(5,3),activation='relu',padding='same')(pool1)
pool2 =MaxPool2D(pool_size=2)(conv2)
flat = Flatten()(pool2)
outlayer =Dense(211,activation='softmax')(flat)

mymodel =Model(myinput , outlayer)


mymodel.compile(optimizer='Adam',loss=categorical_crossentropy,metrics=['accuracy'])
#train our model
network_history=mymodel.fit(x_train,y_train,epochs= 15,validation_split = 0.2)
#give us loss and acc
history = network_history.history()

# chart of our model
losses = history['loss']
accu = history['acc']
plt.plot(losses)
plt.plot(accu)














