# -*- coding: utf-8 -*-

import json
import pandas as pd
db=json.load(open('C:/Users/barak/OneDrive/Documents/python/Python for Data Analisys/pydata-book-2nd-edition/datasets/usda_food/database.json'))
infokeys=['description', 'group','id', 'manufacturer']
info=pd.DataFrame(db,columns=infokeys)
#distribution of food

pd.value_counts(info.group)[:10]
nutrients=[]
for rec in db:
    fnuts=pd.DataFrame(rec['nutrients'])
    fnuts['id']=rec['id']
    nutrients.append(fnuts)
nutrients=pd.concat(nutrients, ignore_index=True) 

#Check number of duplicates
nutrients.duplicated().sum()
nutrients=nutrients.drop_duplicates()
col_mapping={'description':'food', 'group':'fgroup'}
info=info.rename(columns=col_mapping,copy=False)
col_mapping={'description':'nutrient', 'group':'nutgroup'}
nutrients=nutrients.rename(columns=col_mapping,copy=False)

#merging files
ndata=pd.merge(nutrients,info,on='id',how='outer')
#median values by fgroup&nutrien type
result = ndata.groupby(['nutrient','fgroup'])['value'].quantile(0.5)

result['Zinc, Zn'].sort_values().plot(kind='barh')

#Which food is most dense of each nutrient
by_nutrient=ndata.groupby(['nutgroup','nutrient'])
by_nutrient2=pd.DataFrame(by_nutrient)
get_max =lambda x: x.loc[x.value.idmax()]

get_min =lambda x: x.loc[x.value.idmin()]

max_foods=by_nutrient.apply(get_max)[['value','food']]

by_nutrient2=ndata.pivot_table('value',index=['nutgroup','nutrient'],columns='food',aggfunc=max).stack('food')
AAA = by_nutrient2.loc[['Amino Acids','food']]
AAA
