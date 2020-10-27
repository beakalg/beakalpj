# -*- coding: utf-8 -*-
import pandas as pd
import os
from collections import Counter
import matplotlib.pyplot as plt

os.getcwd()
os.chdir('C:\\Users\\beaka\\OneDrive\\Desktop')
os.getcwd()

seattledata = pd.read_csv("Seattle.csv")
seattledata.info()
seattledata.price
seattledata.zipcode


pop = seattledata.query('bedrooms >=4')
round(pop,2)
pop
pop.bedrooms.describe()

newer = seattledata.query('yr_built > 1999')
newer

first200 = seattledata.head(200)

#Summary stat

# Nominal data

seattledata.zipcode.count()
Counter(seattledata['id'])

#Ordinal
seattledata.grade.min()
seattledata.condition.describe()

#Ratio
round(seattledata.bedrooms.mean(),0)
round(seattledata.price.std(),2)

#Interval

seattledata.yr_built.describe()
seattledata['yr_renovated'].value_counts()


#Visualizations
#Nominal 

seattledata['zipcode'].hist(bins = 30, range = [98001,98200])
plt.title('Zipcode frequency')
plt.xlabel('zipcode', color='blue')
plt.ylabel('frequency', color='red')




plt.bar(first200['zipcode'],first200['grade'], color='purple')
plt.title('zipcode and grade for 200 properties', color='red')
plt.xlabel('zipcode', color='blue')
plt.ylabel('grade', color='orange')
plt.xlim(98001,98999)
plt.ylim(1,13)


#Ordinal
plt.bar(seattledata['yr_built'],seattledata['condition'], color='blue')
plt.title('Year built and condition relation', color='red')
plt.xlabel('year built', color='blue')
plt.ylabel('yr_bult', color='orange')
plt.xlim(1900,2050)
plt.ylim(1,5)



plt.bar(seattledata['yr_built'],seattledata['grade'], color='blue')
plt.title('Year built and grade relation', color='red')
plt.xlabel('year built', color='blue')
plt.ylabel('grade', color='orange')
plt.xlim(1900,2050)
plt.ylim(1,13)

#Ratio

plt.scatter(seattledata['price'],seattledata['bedrooms'], color='blue')
plt.title('Bedroom count and price relation', color='red')
plt.xlabel('price', color='blue')
plt.ylabel('bedrooms', color='orange')
plt.xlim(75000,200000)
plt.ylim(1,7)


plt.scatter(seattledata['price'],seattledata['bathrooms'], color='blue')
plt.title('Bathroom count and price relation', color='red')
plt.xlabel('price', color='blue')
plt.ylabel('bathroom', color='orange')
plt.xlim(75000,400000)
plt.ylim(1,7)

#Interval


seattledata['price'].hist(bins = 50, range = [75000,800000])
plt.title('Price frequency or range frequency')
plt.xlabel('price', color='black')
plt.ylabel('frequency', color='red')

plt.scatter(seattledata['sqft_lot'],seattledata['price'], color='purple')
plt.title('Lot size  and price relation', color='red')
plt.xlabel('sq lot', color='blue')
plt.ylabel('Price', color='orange')
plt.ylim(75000,600000)
plt.xlim(520,20000)

