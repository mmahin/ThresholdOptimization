import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

import io
df = pd.read_csv('RawData/income.csv',sep=',')
for item in df:
    print(item)

FIPS = []
medianHouseHoldIncome = []
povertyRate = []
for count in range(len(df['FIPS'])):
    if df['FIPS'][count] > 1000:
        FIPS.append(df['FIPS'][count])
        medianHouseHoldIncome.append(df['MedHHInc'][count])
        povertyRate.append(df['PovertyAllAgesPct'][count])
new_df = pd.DataFrame()
new_df['FIPS'] = FIPS
new_df['medianHouseHoldIncome'] = medianHouseHoldIncome
new_df['povertyRate'] = povertyRate
new_df.to_csv('InitialExtractedData/poverty.csv', index= False)
