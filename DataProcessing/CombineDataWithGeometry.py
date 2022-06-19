import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
path_shp = "RawData/cb_2018_us_county_500k/cb_2018_us_county_500k.shp"
my_df_shp = gpd.read_file(path_shp)
my_df_shp = my_df_shp.to_crs("epsg:4326")

continuous_us_fips = pd.read_csv("RawData/continuous_us_fips.csv")
continuous_us_fips= continuous_us_fips['FIPS'].values

#STATEFP
#COUNTYFP
#COUNTYNS
#AFFGEOID
#GEOID
#NAME
#LSAD
#ALAND
#AWATER
#geometry
county_fips = []
geometries = []
for count in range(len(my_df_shp)):
    if int(my_df_shp['STATEFP'][count]) in continuous_us_fips:
        #poly = my_df_shp['geometry'][count]
        #gdf = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[poly])
        #gdf.plot(linewidth=0.8, ax=ax, edgecolor='black', facecolor="none")
        #print(my_df_shp['STATEFP'][count], my_df_shp['COUNTYFP'][count])
        county_fips.append(int(my_df_shp['STATEFP'][count] + my_df_shp['COUNTYFP'][count]))
        geometries.append(my_df_shp['geometry'][count])

bacheor = pd.read_csv("InitialExtractedData/bachelor_degree_density_2014_2018.csv")
climate = pd.read_csv("InitialExtractedData/climate.csv")
covid = pd.read_csv("InitialExtractedData/covid.csv")
householdDensity = pd.read_csv("InitialExtractedData/HouseHoldDensity2010.csv")
jobs = pd.read_csv("InitialExtractedData/jobs2018.csv")
poverty = pd.read_csv("InitialExtractedData/poverty.csv")

df = pd.DataFrame()
df['FIPS'] = county_fips
df['geometry'] = geometries



df['bachelor_degree_density_2014_2018'] = [0]*len(county_fips)
df['avg_precipitation_for_county'] = [0]*len(county_fips)
df['avg_temp_for_county'] = [0]*len(county_fips)
df['covid_cases'] = [0]*len(county_fips)
df['covid_deaths'] = [0]*len(county_fips)

df['population_density_on_land_2010'] = [0]*len(county_fips)
df['household_density_on_land_2010'] = [0]*len(county_fips)
df['UnempRate2018'] = [0]*len(county_fips)
df['PctEmpAgriculture'] = [0]*len(county_fips)
df['PctEmpMining'] = [0]*len(county_fips)

df['PctEmpConstruction'] = [0]*len(county_fips)
df['PctEmpManufacturing'] = [0]*len(county_fips)
df['PctEmpTrade'] = [0]*len(county_fips)
df['PctEmpTrans'] = [0]*len(county_fips)
df['PctEmpInformation'] = [0]*len(county_fips)
df['PctEmpFIRE'] = [0]*len(county_fips)

df['PctEmpServices'] = [0]*len(county_fips)
df['PctEmpGovt'] = [0]*len(county_fips)
df['medianHouseHoldIncome'] = [0]*len(county_fips)
df['povertyRate'] = [0]*len(county_fips)


for count in range(len(df['FIPS'])):

    if df['FIPS'][count] in bacheor['FIPS'].values:
        item_index = ((bacheor.index[bacheor['FIPS']==df['FIPS'][count]]).values)[0]
        df['bachelor_degree_density_2014_2018'][count] = bacheor['bachelor_degree_density_2014_2018'][item_index]
    else:
        df['bachelor_degree_density_2014_2018'][count] = float('nan')

    if df['FIPS'][count] in climate['FIPS'].values:
        item_index = ((climate.index[climate['FIPS']==df['FIPS'][count]]).values)[0]
        df['avg_precipitation_for_county'][count] = climate['avg_precipitation_for_county'][item_index]
        df['avg_temp_for_county'][count] = climate['avg_temp_for_county'][item_index]
    else:
        df['avg_precipitation_for_county'][count] = float('nan')
        df['avg_temp_for_county'][count] = float('nan')

    if df['FIPS'][count] in covid['FIPS'].values:
        item_index = ((covid.index[covid['FIPS']==df['FIPS'][count]]).values)[0]
        df['covid_cases'][count] = covid['cases'][item_index]
        df['covid_deaths'][count] = covid['deaths'][item_index]
    else:
        df['covid_cases'][count] = float('nan')
        df['covid_deaths'][count] = float('nan')


    if df['FIPS'][count] in householdDensity['FIPS'].values:
        item_index = ((householdDensity.index[householdDensity['FIPS']==df['FIPS'][count]]).values)[0]
        df['population_density_on_land_2010'][count] = householdDensity['population_density_on_land_2010'][item_index]
        df['household_density_on_land_2010'][count] = householdDensity['household_density_on_land_2010'][item_index]
    else:
        df['population_density_on_land_2010'][count] = float('nan')
        df['household_density_on_land_2010'][count] = float('nan')

    if df['FIPS'][count] in jobs['FIPS'].values:
        item_index = ((jobs.index[jobs['FIPS']==df['FIPS'][count]]).values)[0]
        df['UnempRate2018'][count] = jobs['UnempRate2018'][item_index]
        df['PctEmpAgriculture'][count] = jobs['PctEmpAgriculture'][item_index]
        df['PctEmpMining'][count] = jobs['PctEmpMining'][item_index]
        df['PctEmpConstruction'][count] = jobs['PctEmpConstruction'][item_index]
        df['PctEmpManufacturing'][count] = jobs['PctEmpManufacturing'][item_index]
        df['PctEmpTrade'][count] = jobs['PctEmpTrade'][item_index]
        df['PctEmpTrans'][count] = jobs['PctEmpTrans'][item_index]
        df['PctEmpInformation'][count] = jobs['PctEmpInformation'][item_index]
        df['PctEmpFIRE'][count] = jobs['PctEmpFIRE'][item_index]
        df['PctEmpServices'][count] = jobs['PctEmpServices'][item_index]
        df['PctEmpGovt'][count] = jobs['PctEmpGovt'][item_index]
    else:
        df['UnempRate2018'][count] = float('nan')
        df['PctEmpAgriculture'][count] = float('nan')
        df['PctEmpMining'][count] = float('nan')
        df['PctEmpConstruction'][count] = float('nan')
        df['PctEmpManufacturing'][count] = float('nan')
        df['PctEmpTrade'][count] = float('nan')
        df['PctEmpTrans'][count] = float('nan')
        df['PctEmpInformation'][count] = float('nan')
        df['PctEmpFIRE'][count] = float('nan')
        df['PctEmpServices'][count] = float('nan')
        df['PctEmpGovt'][count] = float('nan')

    if df['FIPS'][count] in poverty['FIPS'].values:
        item_index = ((poverty.index[poverty['FIPS']==df['FIPS'][count]]).values)[0]
        df['medianHouseHoldIncome'][count] = poverty['medianHouseHoldIncome'][item_index]
        df['povertyRate'][count] = poverty['povertyRate'][item_index]
    else:
        df['medianHouseHoldIncome'][count] = float('nan')
        df['povertyRate'][count] = float('nan')

import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
df1 = pd.read_csv("RawData/PopulationEstimates.csv")
covid_cases_density = []
covid_death_density = []
for count in range(len(df['FIPS'])):
    if df['FIPS'][count] in df['FIPS'].values:
        index = ((df1.index[df1['FIPS']==df['FIPS'][count]]).values)[0]
        if not(pd.isna(df1['POP_ESTIMATE_2018'][index])):
            value = locale.atoi(df1['POP_ESTIMATE_2018'][index]) #int((df['POP_ESTIMATE_2018'][index]).replace("\"",""))
            covid_cases_density.append(df['covid_cases'][count]/value)
            covid_death_density.append(df['covid_deaths'][count]/value)


df['covid_cases_density'] = covid_cases_density
df['covid_death_density'] = covid_death_density
df.to_csv("InitialExtractedData/dataset_combined.csv",index=False)

#plt.show()