# -*- coding: utf-8 -*-

import pandas as pd
names1880=pd.read_csv('C:/Users/barak/OneDrive/Documents/python/Python for Data Analisys/pydata-book-2nd-edition/datasets/babynames/yob1880.txt',
                      names=['name','sex','births'])

#number of births

names1880.groupby('sex').births.sum()

years=range(1880,2011)
pieces=[]
columns=['name','sex','births']

for year in years:
    #https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-python-string-formatting
    path= 'C:/Users/barak/OneDrive/Documents/python/Python for Data Analisys/pydata-book-2nd-edition/datasets/babynames/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    
    frame['year']=year
    pieces.append(frame)

#Conecting all years
#https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
names=pd.concat(pieces,ignore_index=True)

#Create Pivot table
"""
first value = what is beeing calculated
second->index=rows
Third->colums
Fourth->aggfunc=sum/mean.....
"""
total_births= names.pivot_table('births',index='year',columns='sex', aggfunc=sum)
#tail()->last X values
total_births.tail(10)

#plot
total_births.plot(title='Total births by sex & date')

####Probailities
def add_group(group):
    group['prop']= group.births/group.births.sum()
    return group
#For every Year&Sex ->group.births, Divide by sum off Sex(Seconed argument for each Year)
names=names.groupby(['year','sex']).apply(add_group)
#Check the Function
names.groupby(['year','sex']).prop.sum()

#Top 1000 for each Year&Sex Combination

def top_1000(group):
    return group.sort_values(by='births',ascending=False)[:1000]

grouped=names.groupby(['year','sex'])
top1000=grouped.apply(top_1000)
#Drop group index
top1000.reset_index(inplace=True,drop=True)

#Anoter way
p=[]
for year,group in names.groupby(['year','sex']):
    p.append(group.sort_values(by='births', ascending=False)[:1000])
top1000_2=pd.concat(p,ignore_index=True)

boys=top1000[top1000.sex=='M']
girls=top1000[top1000.sex=='F']

total_births2 = top1000.pivot_table('births',index='year', columns='name', aggfunc=sum)

subset=total_births2[['John','Harry','Mary','Marlyn']]
subset.plot(subplots=True, figsize=(12,10), grid=False,
            title='NUmber of births per year')

table = top1000.pivot_table('prop',index='year', columns='sex', aggfunc=sum)
import numpy as np
table.plot(title='Sum of  top 1000 proportion by year & sex', 
           yticks=np.linspace(0,1.2,13), xticks=range(1880,2020,10))


#NUmber of distinct names
df=boys[boys.year==2010]

prop_cumsum=df.sort_values(by='prop', ascending=False).prop.cumsum()
prop_cumsum.values.searchsorted(0.5)

df1= boys[boys.year==1900]
in1900=df1.sort_values(by='prop', ascending=False).prop.cumsum().values.searchsorted(0.5)+1

#quintile  function

def get_q_count(g, q=0.5):
    g=g.sort_values(by='prop',ascending=False)
    return g.prop.cumsum().values.searchsorted(q)+1

diversity= top1000.groupby(['year','sex']).apply(get_q_count)
diversity=diversity.unstack(('sex'))

diversity.plot(title='Number of names in top 50%')


#Extract last letter
get_last_letter= lambda x: x[-1]

last_letters=names.name.map(get_last_letter)
last_letters.name='last letter'

table2= names.pivot_table('births', index=last_letters,
                          columns=['sex','year'], aggfunc=sum)

subtable= table2.reindex(columns=[1910,1960,2010],level='year')
letter_prop=subtable/subtable.sum()

import matplotlib.pyplot as plt
fig, ax = plt.subplots(2,1,figsize=(10,8))
letter_prop['M'].plot(kind='bar', rot=0, ax=ax[0], title='Male')
letter_prop['F'].plot(kind='bar', rot=0, ax=ax[1], title='Female', legend=False)

letter_prop2=table2/table2.sum()

dny_ts=letter_prop2.loc[['d', 'n', 'y'],'M'].T
dny_ts.plot()
all_names=pd.Series(top1000.name.unique())
lesley= all_names[all_names.str.lower().str.contains('lesl')]

filtered= top1000[top1000.name.isin(lesley)]
filtered.groupby('name').births.sum()
table3=filtered.pivot_table('births',index='year', columns='sex', aggfunc=sum)
table3=table3.div(table3.sum(1),axis=0)

table3.plot(style={'M':'-k','F':'--k'})
