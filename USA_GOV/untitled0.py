# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:09:17 2020

@author: barak
"""

import numpy as np

data=np.random.randn(2,3)
data
data2=np.zeros((4,2))
data2
data2=np.empty((2,3,2))
arr=np.arange(10)
arr
arr[5]
arr[10]
arr[0]
points= np.arange(-5,5,0.1)
xs,ys=np.meshgrid(points,points)
ys
z=np.sqrt(xs**2+ys**2)
z
import matplotlib.pyplot as plt
plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title("image plot of $\sqrt{X^2 + Y^2}$ for a grid of values")
Text(0.5,1,'Image plot of $\\sqrt{X^2 +Y^2}$ for a grid values')
import random

np.random.seed(1234)

position = 0
walk=[position]
steps=1000

for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)
    
plt.plot(walk[:1000])

import pandas as pd
import pandas_datareader.data as web

all_data = {ticker : web.get_data_yahoo(ticker)
            for ticker in ['AAPL','IBM','MSFT','GOOG']}

all_data.items()
price= pd.DataFrame({ticker: data['Adj Close']
                    for ticker, data in all_data.items()})

volume=pd.DataFrame({ticker: data['Volume']
                     for ticker , data in all_data.items()})

all_data
returns = price.pct_change()
returns.tail(10)
returns['AAPL'].plot();



#What works on CMD
type C:\Users\barak\OneDrive\Documents\python\pydata-book-2nd-edition\examples\ex1.csv

#How to write in Spyder
df = pd.read_csv('C:/Users/barak/OneDrive/Documents/python/pydata-book-2nd-edition/examples/ex1.csv')

## Main directory
pwd()

#How to write in Spyder
df1 = pd.read_csv('C:/Users/barak/OneDrive/Documents/python/pydata-book-2nd-edition/examples/ex1.csv', header=None)

df = pd.read_csv('C:/Users/barak/OneDrive/Documents/python/pydata-book-2nd-edition/examples/csv_mindex.csv', index_col=['key1','key2'])
list(open('C:/Users/barak/OneDrive/Documents/python/pydata-book-2nd-edition/examples/ex3.txt'))
result = pd.read_csv('C:/Users/barak/OneDrive/Documents/python/pydata-book-2nd-edition/examples/ex3.txt', sep='\s+')


#Handling NA
RR = pd.read_csv('C:/Users/barak/OneDrive/Documents/python/pydata-book-2nd-edition/examples/ex5.csv', 
                 na_values=['BARAK'])

RR1
RR1 = pd.read_csv('C:/Users/barak/OneDrive/Documents/python/pydata-book-2nd-edition/examples/ex5.csv')


chunker= pd.read_csv('C:/Users/barak/OneDrive/Documents/python/pydata-book-2nd-edition/examples/ex6.csv', 
                 chunksize=1000)
chunker

data= pd.read_csv('C:/Users/barak/OneDrive/Documents/python/pydata-book-2nd-edition/examples/ex5.csv')
data.to_csv('C:\\Users\\barak/out.csv')

import sys

data.to_csv(sys.stdout, na_rep='BARAK')


######HTML
tables = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
len(tables)
failures = tables[0]
failures.head()
close_time = pd.to_datetime(failures['Closing Date'])

#IMportant for counting
close_time.dt.year.value_counts()
https://www.tase.co.il/he/market_data/index/164/historical_data

tables1 = pd.read_html('https://www.bizportal.co.il/capitalmarket/indices/transactions/13.html')



import matplotlib.pyplot as plt
import numpy as np
data = np.arange(10)
plt.plot(data)
fig = plt.figure()
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
plt.plot(np.random.randn(50).cumsum(),'k--')
ax1.hist(np.random.randn(100),bins=20,color='k',alpha=0.3)
ax2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))

fig, axes = plt.subplots(2,3)
axes
plt.plot(np.random.randn(30).cumsum(),'ko--')
data=np.random.randn(30).cumsum()
plt.plot(data,color='k',linestyle='dashed',marker='o',label='Default')
plt.plot(data,'k-',drawstyle='steps-post',label='steps-post')
plt.legend(loc='best')

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum())
ticks = ax.set_xticks([0,250,500,750,1000])
labels = ax.set_xticklabels(['one','two','three','four','five'],rotation=30, fontsize='small')
ax.set_title('My first matplotlib plot')
Text(0.5,1,'My first matplotlib plot')
ax.set_xlabel('Stages')
ax.set_ylabel('Stages1')
props={'title':'My first plot',
      'xlable':'Barak'}
ax.set(**props)
ax.legend(loc='best')

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum(),'k',label='one')

ax.plot(np.random.randn(1000).cumsum(),'k--',label='two')


ax.plot(np.random.randn(1000).cumsum(),'k',label='three')
ax.legend(loc='best')
from datetime import datetime
import pandas as pd
##############
data= pd.read_csv('C:/Users/barak/OneDrive/Documents/python/pydata-book-2nd-edition/examples/spx.csv',index_col=0,parse_dates=True)
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
spx=data['SPX']
spx.plot(ax=ax, style='k--')

crisis_data= [(datetime(2007,10,11),'Peak of Bull Market')
              ,(datetime(2008,3,12),'Bear Stearns Falls'),
              (datetime(2008,9,15), 'Lehman Bankrupcy')]

for date, label in crisis_data:
    ax.annotate(label, xy=(date,spx.asof(date)+75),
                xytext=(date,spx.asof(date)+225),
                arrowprops=dict(facecolor='black', headwidth=4, width=2,headlength=4),
                horizontalalignment='left',verticalalignment='top')
    
ax.set_xlim(['1/1/2007','1/1/2011'])
ax.set_ylim([600,1800])
ax.set_title('Imoportant dates in the 2008-2009 financial crisis')


##################### Data Frames
s= pd.Series(np.random.randn(10).cumsum(), index= np.arange(0,100,10))
s.plot()
s.value_counts().plot.bar()
df= pd.DataFrame(np.random.randn(10,4).cumsum(0),
                 columns=['A','B','C','D'],
                 index=np.arange(0,100,10))

df.plot()

fig, axes = plt.subplots(2,1)
data = pd.Series(np.random.rand(16),index=list('abcdefghijklmnop'))
data.plot.bar(ax=axes[0],color='k', alpha=0.7)
data.plot.barh(ax=axes[1],color='k',alpha=0.7)

df=pd.DataFrame(np.random.rand(6,4),
                index=['one','two','three','four','five','six'],
                columns=[pd.Index(['A','B','C','D'],name='Genus')])
df.plot.bar()
df.plot.barh(stacked=True, alpha=0.5)
df

tips =pd.read_csv('C:/Users/barak/OneDrive/Documents/python/pydata-book-2nd-edition/examples/tips.csv')
######Seaborn
import seaborn as sns
tips['tip_pct']= tips['tip']/(tips['total_bill']-tips['tip'])
tips
sns.barplot(x='tip_pct',y='day',data=tips,orient='h')
sns.barplot(x='tip_pct',y='day',data=tips,orient='h', hue='time')
sns.set(style='whitegrid')

tips['tip_pct'].plot.density()


macrodata =pd.read_csv('C:/Users/barak/OneDrive/Documents/python/pydata-book-2nd-edition/examples/macrodata.csv')
######Seaborn
data=macrodata[['cpi','m1','tbilrate','unemp']]
trans_data=np.log(data).diff().dropna()
trans_data[-5:]
sns.regplot('m1','unemp',data=trans_data)
plt.title('Change in log %s Versus log %s' % ('m1','unemp'))

sns.pairplot(trans_data,diag_kind='kde',plot_kws={'alpha':0.2})

########
adding things 