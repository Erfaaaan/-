import pandas as pd
import numpy as np
import os

#read 2d merged csv file
df = pd.read_csv('../data/merge.csv')


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
print(arr)

