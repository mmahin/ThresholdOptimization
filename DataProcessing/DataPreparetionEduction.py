import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

import io
df = pd.read_csv('RawData/Education.csv',sep=',', encoding='latin-1')
for item in df:
    print(item)
FIPS = []
bachelor_degree_density_2014_2018 = []
for count in range(len(df['FIPS Code'])):
    if df['FIPS Code'][count] > 1000:
        FIPS.append(df['FIPS Code'][count])
        bachelor_degree_density_2014_2018.append(df['Percent of adults with a bachelor\'s degree or higher 2014-18'][count])
new_df = pd.DataFrame()
new_df['FIPS'] = FIPS
new_df['bachelor_degree_density_2014_2018'] = bachelor_degree_density_2014_2018
new_df.to_csv('InitialExtractedData/bachelor_degree_density_2014_2018.csv', index= False)

