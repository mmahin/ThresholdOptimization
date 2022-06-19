import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import shapely.wkt
df = pd.read_csv("InitialExtractedData/dataset_combined.csv")
fig, axs = plt.subplots(4, 5, constrained_layout=False)

for count in range(len(df['FIPS'])):
    poly = shapely.wkt.loads(df['geometry'][count])
    gdf = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[poly])

    if not(pd.isna(df['bachelor_degree_density_2014_2018'][count])):
        gdf.plot(linewidth=0.8, ax=axs[0,0], edgecolor='red', color='r',facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[0, 0], edgecolor='black', color='k',facecolor="none")

    if not(pd.isna(df['avg_precipitation_for_county'][count])):
        gdf.plot(linewidth=0.8, ax=axs[0,1], edgecolor='red', color='r', facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[0, 1], edgecolor='black', color='k',facecolor="black")

    if not(pd.isna(df['avg_temp_for_county'][count])):
        gdf.plot(linewidth=0.8, ax=axs[0,2], edgecolor='red', color='r',facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[0, 2], edgecolor='black', color='k',facecolor="black")

    if not(pd.isna(df['covid_cases'][count])):
        gdf.plot(linewidth=0.8, ax=axs[0,3], edgecolor='red', color='r',facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[0, 3], edgecolor='black', color='k',facecolor="black")

    if not(pd.isna(df['covid_deaths'][count])):
        gdf.plot(linewidth=0.8, ax=axs[0,4], edgecolor='red', color='r',facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[0, 4], edgecolor='black', color='k',facecolor="black")

    if not(pd.isna(df['population_density_on_land_2010'][count])):
        gdf.plot(linewidth=0.8, ax=axs[1,0], edgecolor='red', color='r', facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[1, 0], edgecolor='black', color='k',facecolor="black")

    if not(pd.isna(df['household_density_on_land_2010'][count])):
        gdf.plot(linewidth=0.8, ax=axs[1,1], edgecolor='red', color='r',facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[1, 1], edgecolor='black', color='k',facecolor="black")

    if not(pd.isna(df['UnempRate2018'][count])):
        gdf.plot(linewidth=0.8, ax=axs[1,2], edgecolor='red', color='r',facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[1, 2], edgecolor='black', color='k',facecolor="black")

    if not(pd.isna(df['PctEmpAgriculture'][count])):
        gdf.plot(linewidth=0.8, ax=axs[1,3], edgecolor='red', color='r',facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[1, 3], edgecolor='black', color='k',facecolor="black")

    if not(pd.isna(df['PctEmpMining'][count])):
        gdf.plot(linewidth=0.8, ax=axs[1,4], edgecolor='red', color='r',facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[1, 4], edgecolor='black', color='k',facecolor="black")

    if not(pd.isna(df['PctEmpConstruction'][count])):
        gdf.plot(linewidth=0.8, ax=axs[2,0], edgecolor='red', color='r',facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[2, 0], edgecolor='black', color='k',facecolor="black")

    if not(pd.isna(df['PctEmpManufacturing'][count])):
        gdf.plot(linewidth=0.8, ax=axs[2,1], edgecolor='red', color='r',facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[2, 1], edgecolor='black', color='k',facecolor="black")


    if not(pd.isna(df['PctEmpTrade'][count])):
        gdf.plot(linewidth=0.8, ax=axs[2,2], edgecolor='red', color='r',facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[2, 2], edgecolor='black', color='k',facecolor="black")

    if not(pd.isna(df['PctEmpTrans'][count])):
        gdf.plot(linewidth=0.8, ax=axs[2,3], edgecolor='red', color='r',facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[2, 3], edgecolor='black', color='k',facecolor="black")

    if not(pd.isna(df['PctEmpInformation'][count])):
        gdf.plot(linewidth=0.8, ax=axs[2,4], edgecolor='red',color='r', facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[2, 4], edgecolor='black', color='k',facecolor="black")


    if not(pd.isna(df['PctEmpFIRE'][count])):
        gdf.plot(linewidth=0.8, ax=axs[3,0], edgecolor='red', color='r',facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[3, 0], edgecolor='black', color='k',facecolor="black")

    if not(pd.isna(df['PctEmpServices'][count])):
        gdf.plot(linewidth=0.8, ax=axs[3,1], edgecolor='red', color='r',facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[3, 1], edgecolor='black', color='k',facecolor="black")

    if not(pd.isna(df['PctEmpGovt'][count])):
        gdf.plot(linewidth=0.8, ax=axs[3,2], edgecolor='red', color='r',facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[3, 2], edgecolor='black',color='k', facecolor="black")

    if not(pd.isna(df['medianHouseHoldIncome'][count])):
        gdf.plot(linewidth=0.8, ax=axs[3,3], edgecolor='red',color='r', facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[3, 3], edgecolor='black', color='k',facecolor="black")

    if not(pd.isna(df['povertyRate'][count])):
        gdf.plot(linewidth=0.8, ax=axs[3,4], edgecolor='red', color='r',facecolor="red")
    else:
        gdf.plot(linewidth=0.8, ax=axs[3, 4], edgecolor='black', color='k',facecolor="black")


axs[0, 0].set_title("Bachelor Degree %")
axs[0, 1].set_title("Average Precipitation")
axs[0, 2].set_title("Average Temperature")
axs[0, 3].set_title("Covid Cases")
axs[0, 4].set_title("Covid Deaths")
axs[1, 0].set_title("Population Density")
axs[1, 1].set_title("Household Density")

axs[1, 2].set_title("Unemployment Rate")
axs[1, 3].set_title("Agriculture Employment %")

axs[1, 4].set_title("Mining Employment %")
axs[2, 0].set_title("Construction Employment %")

axs[2, 1].set_title("Manufacturing Employment %")
axs[2, 2].set_title("Trade Employment %")
axs[2, 3].set_title("Transportation Employment %")
axs[3, 4].set_title("Information Employment %")
axs[2, 4].set_title("Fire Employment %")
axs[3, 0].set_title("Services Employment %")
axs[3, 1].set_title("Govermnent Employment %")
axs[3, 2].set_title("Median Houshold Income")
axs[3, 3].set_title("Poverty Rate")


from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color='r', lw=4),
                Line2D([0], [0], color='k', lw=4),
                Line2D([0], [0], color='w', lw=4)]
#location = 0 # For the best location
#legend_drawn_flag = True
#plt.legend(["Not Flooded", "Flood Height Between 0 to 1 Feet", "Flood Height Greater than 1 Feet"], loc=0, frameon=legend_drawn_flag)
plt.legend(custom_lines, ['Have Values', 'Null Values', 'No Geometry'],bbox_to_anchor=(1.04,1), loc='upper left')


plt.show()