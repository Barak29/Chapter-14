# -*- coding: utf-8 -*-
import pandas as pd
fec=pd.read_csv('C:/Users/barak/OneDrive/Documents/python/Python for Data Analisys/pydata-book-2nd-edition/datasets/fec/P00000001-ALL.csv')

unique_cands= fec.cand_nm.unique()

 parties = {'Bachmann, Michelle': 'Republican',
             'Cain, Herman': 'Republican',
               'Gingrich, Newt': 'Republican',
              'Huntsman, Jon': 'Republican',
              'Johnson, Gary Earl': 'Republican',
              'McCotter, Thaddeus G': 'Republican',
              'Obama, Barack': 'Democrat',
              'Paul, Ron': 'Republican',
              'Pawlenty, Timothy': 'Republican',
              'Perry, Rick': 'Republican',
              "Roemer, Charles E. 'Buddy' III": 'Republican',
              'Romney, Mitt': 'Republican',
              'Santorum, Rick': 'Republican'}
 
 fec['party']=fec.cand_nm.map(parties)
fec['party'].value_counts()


#only positive donations
(fec.contb_receipt_amt>0).value_counts()
fec=fec[fec.contb_receipt_amt>0]

#Only Romney & Obama
fec_mrbo=fec[fec.cand_nm.isin(['Obama, Barack','Romney, Mitt'])]

fec.contbr_occupation.value_counts()[:10]
#names of columns
fec.columns


occ_mapping= {'INFORMATION REQUESTED PER BEST EFFORTS' : 'NOT PROVIDED',
       'INFORMATION REQUESTED' : 'NOT PROVIDED',
       'INFORMATION REQUESTED (BEST EFFORTS)' : 'NOT PROVIDED',
       'C.E.O.': 'CEO'
    }

#If no mapping ->returnx
f= lambda x: occ_mapping.get(x,x)
fec.contbr_occupation=fec.contbr_occupation.map(f)


emp_mapping = {
       'INFORMATION REQUESTED PER BEST EFFORTS' : 'NOT PROVIDED',
       'INFORMATION REQUESTED' : 'NOT PROVIDED',
       'SELF' : 'SELF-EMPLOYED',
      'SELF EMPLOYED' : 'SELF-EMPLOYED',
    }
f = lambda x: emp_mapping.get(x,x)
fec.contbr_employer = fec.contbr_employer.map(f)

by_occupation =fec.pivot_table('contb_receipt_amt', index='contbr_occupation',
                 columns='party', aggfunc='sum')

over2m=by_occupation[by_occupation.sum(1)>2000000]
over2m.plot(kind='barh')

def top_amount(g,key,n=5):
    totals=g.groupby(key)['contb_receipt_amt'].sum()
    return totals.nlargest(n)

grouped = fec_mrbo.groupby('cand_nm')
grouped.apply(top_amount, 'contbr_occupation',n=7)

#Creating bins
import numpy as np
bins = np.array([0,1,10,1000,10000,100000,1000000,10000000])
lables=pd.cut(fec_mrbo.contb_receipt_amt,bins)
lables

grouped2= fec_mrbo.groupby(['cand_nm',lables])
grouped2.size().unstack(0)

bucket_sums = grouped2.contb_receipt_amt.sum().unstack(0)
normed_sums=bucket_sums.div(bucket_sums.sum(axis=1),axis=0)
normed_sums[:-2].plot(kind='barh')


grouped3=fec_mrbo.groupby(['cand_nm','contbr_st'])
totals=grouped3.contb_receipt_amt.sum().unstack(0).fillna(0)
totals=totals[totals.sum(1)>100000]


"""
Divide every line (axis=0) in the value of 'totals.sum(axis=1)'
"""

percent= totals.div(totals.sum(axis=1),axis=0)
