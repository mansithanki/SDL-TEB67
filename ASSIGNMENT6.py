# -*- coding: utf-8 -*-
#TE B 67
import pandas as pd
ds=pd.read_csv('Game_medal.csv',encoding="ISO-8859-1")
#encoding="ISO-8859-1"
ds.head()#default first five row
ds.tail()#default last five row
ds.describe()#BEsic Summary dataset
ds.shape#Nuber of row and Colums
ds.shift#Default shift as it is database otherwise leftshif or right shift
ds.info()#Database Information
ds.NOC#Colum name NOC displayed
ds.plot()#default INteger value accept x no of record y year
import matplotlib.pyplot as plt
plt.plot(ds.Edition)#graph for edition
plt.plot(ds.Edition, label="Year of Event")#label shown
plt.legend(loc='upper left')#default first five row
plt.plot(ds.Edition, color="blue",label="Year of Event")
plt.plot(ds.Edition,linewidth=2.5, color="red",label="Year of Event")
fig = plt.gcf() # get current figure
ds.plot()
fig.savefig('my_figure.png')


