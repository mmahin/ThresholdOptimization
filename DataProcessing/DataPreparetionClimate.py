import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

import io
df = pd.read_csv('RawData/unified_climate.csv',sep=',')
for item in df:
    print(item)

new_df = pd.DataFrame()
FIPS = []
avg_precipitation_for_county = []
avg_temp_for_county = []
for count in range(len(df['FIPS'])):
    if df['FIPS'][count] > 1000:
        avg_precipitation = (df['Jan Precipitation / inch'][count] + df['Feb Precipitation / inch'][count] +
                             df['Mar Precipitation / inch'][count] + df['Apr Precipitation / inch'][count] +
                             df['May Precipitation / inch'][count] + df['Jun Precipitation / inch'][count] +
                             df['Jul Precipitation / inch'][count] + df['Aug Precipitation / inch'][count] +
                             df['Sep Precipitation / inch'][count] + df['Oct Precipitation / inch'][count] +
                             df['Nov Precipitation / inch'][count] + df['Dec Precipitation / inch'][count] )/12

        avg_temp = (df['Jan Temp AVG / F'][count] + df['Feb Temp AVG / F'][count] + df['Mar Temp AVG / F'][count] +
                    df['Apr Temp AVG / F'][count] + df['May Temp AVG / F'][count] + df['Jun Temp AVG / F'][count] +
                    df['Jul Temp AVG / F'][count] + df['Aug Temp AVG / F'][count] + df['Sep Temp AVG / F'][count] +
                    df['Oct Temp AVG / F'][count] + df['Nov Temp AVG / F'][count] + df['Dec Temp AVG / F'][count]) / 12

        FIPS.append(int(df['FIPS'][count]))
        avg_precipitation_for_county.append(avg_precipitation)
        avg_temp_for_county.append(avg_temp)

new_df['FIPS'] = FIPS
new_df['avg_precipitation_for_county'] = avg_precipitation_for_county
new_df['avg_temp_for_county'] = avg_temp_for_county
new_df.to_csv('InitialExtractedData/climate.csv', index= False)

'''
new_df = pd.DataFrame()
FIPS = []
population_density_on_land_2010 = []
household_density_on_land_2010 = []
for count in range(len(df['Id'])):
    if df['Target Geo Id2'][count] > 1000:
        FIPS.append(int(df['Target Geo Id2'][count]))
        population_density_on_land_2010.append(df['Density per square mile of land area - Population'][count])
        household_density_on_land_2010.append(df['Density per square mile of land area - Housing units'][count])


new_df['FIPS'] = FIPS
new_df['population_density_on_land_2010'] = population_density_on_land_2010
new_df['household_density_on_land_2010'] = household_density_on_land_2010
new_df.to_csv('InitialExtractedData/HouseHoldDensity2010.csv', index= False)
'''
