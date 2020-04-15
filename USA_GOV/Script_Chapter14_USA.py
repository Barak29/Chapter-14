# -*- coding: utf-8 -*-
#Starting to work on file
"""
Main Goal is to find the most occuring time zones in the dataset

"""

import numpy as np
import pandas as pd
import datetime
import json
path = 'C:/Users/barak/OneDrive/Documents/python/Chapter_14/USA_Gov/bitly_usagov/example.txt'
records = [json.loads(line)for line in open(path)]
records[0]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
time_zones[:10]

#Writing  function
def get_counts(seq):
    counts={}
    for x in seq:
        if x in counts:
            counts[x] +=1
        else:
            counts[x]=1
    return counts

#check = get_counts(time_zones) ; check['America/New_York']


from collections import defaultdict

def get_counts2(seq):
    counts= defaultdict(int)# initial =0
    for x in seq:
        counts[x]+=1
    return counts


counts = get_counts2(time_zones)
counts['America/New_York']

def top_10(diction, n=10):
    valuekey = [(count, tz) for tz, count in diction.items()]
    valuekey.sort()
    return valuekey[-n:]
top_10(counts)

from collections import Counter
counts1 = Counter(time_zones)
counts1.most_common(25)


#####Using Pandas

df = pd.DataFrame(records)
tz_counts=df['tz'].value_counts() # NOt including NA's
clean_tz=df['tz'].fillna('Missing')
clean_tz[clean_tz=='']='Unkown'
tz_counts=clean_tz.value_counts()
tz_counts[:10]

#Graphics
import seaborn as sns
subset= tz_counts[:10]
subset.info()
plot1 = sns.barplot(y=subset.index, x=subset.values)
plot1.figure.savefig("Firstfig.png")

######Second Part
results2 = pd.Series([x.split()[0] for x in df.a.dropna()])
results2.value_counts()[:10]

#Top time zones & windows no windows
cdf = df[df.a.notnull()]
cdf['os']=np.where(cdf['a'].str.contains('Windows'),'Window','Not Windows')
#######GroupBy
by_tz_os = cdf.groupby(['tz','os'])

agg_counts1 = by_tz_os.size().fillna(0)# Test to see what unstack does

agg_counts = by_tz_os.size().unstack().fillna(0)

indexer = agg_counts.sum(1).argsort()
counts_subset = agg_counts.take(indexer[-10:])

#Easier Function
agg_counts.sum(1).nlargest(10)

###Rearange data for Plotting
counts_subset=counts_subset.stack()
counts_subset.name='Total'
counts_subset= counts_subset.reset_index()

figure2 = sns.barplot(x='Total',y='tz',hue='os',data=counts_subset)

#### How to normalize groups (0-1)
def norm(group):
    group['Normed Total']= group.Total/group.Total.sum()
    return group

results3 = counts_subset.groupby('tz').apply(norm)

figure3 = sns.barplot(x='Normed Total', y='tz', hue='os', data=results3)

#easier Version
g = counts_subset.groupby('tz')
results4=counts_subset.Total/g.Total.transform('sum')
