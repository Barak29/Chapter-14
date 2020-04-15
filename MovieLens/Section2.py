# -*- coding: utf-8 -*-
"""
Code for section 2 in Chapter 14
C:/Users/barak/OneDrive/Documents/python/Python for Data Analisys/pydata-book-2nd-edition/datasets/movielens



"""
#Importing File
import pandas as pd
import numpy as np
uname =['user_id', 'gender', 'age', 'occupation', 'zip']
main='C:/Users/barak/OneDrive/Documents/python/Python for Data Analisys/pydata-book-2nd-edition/datasets/movielens'
main+'/users.dat'
users = pd.read_table((main+'/users.dat'), sep='::',
                       header=None, names=uname)

rnames=['user_id','movie_id', 'rating','timestamp']
ratings = pd.read_table((main+'/ratings.dat'), sep='::',
                       header=None, names=rnames)

mnames=['movie_id','title', 'geners']
movies = pd.read_table((main+'/movies.dat'), sep='::',
                       header=None, names=mnames)


users.info()

#Merging Data
data=pd.merge(pd.merge(ratings,users),movies)

#Mean movie rating by gender
##Using pivot table
mean_rating=data.pivot_table('rating',index='title',
                             columns='gender',aggfunc='mean')

#using groupby
mean_rating2=data[['title','gender','rating']].groupby(['title','gender']).mean().unstack()

#number of ratings
ratings_by_title=data.groupby('title').size()

#
active_titles=ratings_by_title.index[ratings_by_title>=250]


####Checking active ratings for mean rating
mean_rating3= mean_rating.loc[active_titles]
mean_rating3


top_female = mean_rating3.sort_values(by='F',ascending=False)
top_female[:10]

#Rating disagreements
mean_rating['diff']=mean_rating['M']-mean_rating3['F']
sorted_by_diff=mean_rating.sort_values(by='diff')
#reverse the order of the rows
sorted_by_diff=sorted_by_diff[sorted_by_diff['diff'].notna()]
sorted_by_diff=sorted_by_diff[::-1]
sorted_by_diff[:10]
sorted_by_diff

#Standard Dev by title
rating_std_by_title = data.groupby('title')['rating'].std()
#filter only to active
rating_std_by_title=rating_std_by_title.loc[active_titles]
rating_std_by_title.sort_values(ascending=False)[:10]

#plot distribution of ratings and std
import matplotlib.pyplot as plt


plt.plot(data)
fig = plt.figure()
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)

ax1.hist(data.groupby('title')['rating'].std(),bins=20,color='k',alpha=0.3)
ax1.set_title('Std Distribution')

ax2.hist(mean_rating['F'])
ax2.set_title('Female Rating Dist')

ax3.hist(mean_rating['M'])
ax3.set_title('Male Rating Dist')
