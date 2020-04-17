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
