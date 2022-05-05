import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

import io
df = pd.read_csv('RawData/Unemployment.csv',sep='\t')
for item in df:
    print(item)
    ...
#df = pd.read_csv('RawData/Education.csv',sep=',', encoding='unicode_escape')
# iterating the columns
#df = pd.read_csv('RawData/FIPS_lookup.csv',sep='\t')
#for col in df.columns:
#    print(col)

path_shp = "RawData/cb_2018_us_county_500k/cb_2018_us_county_500k.shp"
my_df_shp = gpd.read_file(path_shp)

state_poly_dict = {}
for i in range(0,len(my_df_shp['STATEFP'])):
    state_poly_dict[int(my_df_shp['STATEFP'][i]+my_df_shp['COUNTYFP'][i])] = my_df_shp['geometry'][i]
print(state_poly_dict)
new_df = pd.DataFrame()
FIPS = []
Unemployment_rate_2018 = []
Median_Household_Income_2018 = []
polygons = []
''''''
for item in df['FIPS']:
    if item in state_poly_dict.keys():
        FIPS.append(item)
        polygons.append(state_poly_dict[item])
        Unemployment_rate_2018.append(((df['Unemployment_rate_2018'][df['FIPS']==item]).values)[0])
        Median_Household_Income_2018.append((((df['Median_Household_Income_2018'][df['FIPS']==item]).values)[0]))
    else:
        ...
        #print(df[df['FIPS']==item])

new_df['FIPS'] = FIPS
new_df['Unemployment_rate_2018'] = Unemployment_rate_2018
new_df['Median_Household_Income_2018'] = Median_Household_Income_2018
new_df['geometry'] = polygons
new_df.to_csv('RawData/UnemploymentPolygon.csv', index= False)
for item in Median_Household_Income_2018:
    print(item)
print(len(polygons),len(my_df_shp['STATEFP']))
'''
for i in range(0,len(my_df_shp)):
    print(my_df_shp['STATEFP'][i]+my_df_shp['COUNTYFP'][i])
'''
'''
#for item in my_df_shp['STATEFP']:
#    print(item)
State_FIPS = pd.read_csv('RawData/FIPS_State.csv',sep=',')
state_fips_dict = {}
for i in range(0,len(State_FIPS['FIPS'])):
    state_fips_dict[State_FIPS['FIPS'][i]] = State_FIPS['STATE'][i]
print(state_fips_dict)
State_Name = []
count2 = 0

for item2 in my_df_shp['STATEFP']:
    if int(item2) in state_fips_dict.keys():
        State_Name.append(state_fips_dict[int(item2)])
    else:
        print(item2)
        State_Name.append("")
    
    count = 0
    for item1 in State_FIPS['FIPS']:
        if item1 == int(item2):
            State_Name.append(State_FIPS['STATE'][count])
        count += 1
    '''

#print(len(State_Name),len(my_df_shp['STATEFP']))

'''
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
my_df_shp.plot(linewidth=0.8, ax=ax, edgecolor='black', facecolor="none")
plt.show()

df = pd.read_csv('RawData/FIPS_lookup.csv',sep=',')
print(df['County'])
for item1 in my_df_shp['NAME']:
    for item2 in df['County']:
        if item1 == item2:
            print(item1)
'''
