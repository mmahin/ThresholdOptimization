import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

import io
df = pd.read_csv('RawData/jobs.csv',sep=',')
for item in df:
    print(item)
FIPS = []
UnempRate2018 = []
PctEmpAgriculture = []
PctEmpMining = []
PctEmpConstruction = []
PctEmpManufacturing = []
PctEmpTrade = []
PctEmpTrans = []
PctEmpInformation = []
PctEmpFIRE = []
PctEmpServices = []
PctEmpGovt = []

for count in range(len(df['FIPS'])):
    if df['FIPS'][count] > 1000:
        FIPS.append(int(df['FIPS'][count]))
        UnempRate2018.append(df['UnempRate2018'][count])
        PctEmpAgriculture.append(df['PctEmpAgriculture'][count])
        PctEmpMining.append(df['PctEmpMining'][count])
        PctEmpConstruction.append(df['PctEmpConstruction'][count])
        PctEmpManufacturing.append(df['PctEmpManufacturing'][count])
        PctEmpTrade.append(df['PctEmpTrade'][count])
        PctEmpTrans.append(df['PctEmpTrans'][count])
        PctEmpInformation.append(df['PctEmpInformation'][count])
        PctEmpFIRE.append(df['PctEmpFIRE'][count])
        PctEmpServices.append(df['PctEmpServices'][count])
        PctEmpGovt.append(df['PctEmpGovt'][count])

new_df = pd.DataFrame()
new_df['FIPS'] = FIPS
new_df['UnempRate2018'] = UnempRate2018
new_df['PctEmpAgriculture'] = PctEmpAgriculture
new_df['PctEmpMining'] = PctEmpMining
new_df['PctEmpConstruction'] = PctEmpConstruction
new_df['PctEmpManufacturing'] = PctEmpManufacturing
new_df['PctEmpTrade'] = PctEmpTrade
new_df['PctEmpTrans'] = PctEmpTrans
new_df['PctEmpInformation'] = PctEmpInformation
new_df['PctEmpFIRE'] = PctEmpFIRE
new_df['PctEmpServices'] = PctEmpServices
new_df['PctEmpGovt'] = PctEmpGovt
new_df.to_csv('InitialExtractedData/jobs2018.csv', index= False)