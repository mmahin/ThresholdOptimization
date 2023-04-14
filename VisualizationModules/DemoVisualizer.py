from SubModules.ObtainVariableDataframesAndStateDictionary import getVariableDataframesAndSpatialIndexes
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.ops import unary_union
from AgreementFunction.PolygonAreaCalculation import PolygonArea
from AgreementFunction.agreementFunction import Agreement
variable1_name = 'covid_cases_density'
variable2_name = 'bachelor_degree_density_2014_2018'
data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'
variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)

# calculate total observation area
polygones = []
for polygon in variable1_df['polygons']:
    polygones.append(polygon)

area_polygon = gpd.GeoSeries(unary_union(polygones))
hotspots1 = []
hotspots2 = []
area = 0
area2 = 0
area3 = 0
total_area = 0
fig, ax = plt.subplots(1, 1, figsize=(4, 3))
fig2, ax2 = plt.subplots(1, 1, figsize=(4, 3))
fig3, ax3 = plt.subplots(1, 1, figsize=(4, 3))
area_polygon.plot(linewidth=0.8, ax=ax, edgecolor='black', facecolor="none")
area_polygon.plot(linewidth=0.8, ax=ax2, edgecolor='black', facecolor="none")
area_polygon.plot(linewidth=0.8, ax=ax3, edgecolor='black', facecolor="none")
for count in range(len(variable1_df['stateFIPS'])):
    total_area += PolygonArea(variable1_df['polygons'][count])
    if variable1_df['stateFIPS'][count] in [8,20,29, 19,31 ]:
        gdf = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[variable1_df['polygons'][count]])
        gdf.plot(linewidth=0.8, ax=ax, edgecolor='red', color='r', facecolor="none")
        area += PolygonArea(variable1_df['polygons'][count])
        hotspots1.append(variable1_df['polygons'][count])

    if variable1_df['stateFIPS'][count] in [8,20,29, 31,56 ]:
        gdf = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[variable1_df['polygons'][count]])
        gdf.plot(linewidth=0.8, ax=ax2, edgecolor='red', color='r', facecolor="none")
        area2 += PolygonArea(variable1_df['polygons'][count])
        hotspots2.append(variable1_df['polygons'][count])

    if variable1_df['stateFIPS'][count] in [8,20,29, 31]:
        gdf = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[variable1_df['polygons'][count]])
        gdf.plot(linewidth=0.8, ax=ax3, edgecolor='red', color='r', facecolor="none")
        area3 += PolygonArea(variable1_df['polygons'][count])
    if variable1_df['stateFIPS'][count] in [19,56]:
        gdf = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[variable1_df['polygons'][count]])
        gdf.plot(linewidth=0.8, ax=ax3, edgecolor='blue', color='blue', facecolor="none")
        area3 += PolygonArea(variable1_df['polygons'][count])

print("Hotspot1:", area/total_area )
print("Hotspot2:", area2/total_area )
print("Intersection:", area3/total_area )
agreement = Agreement(hotspots1, hotspots2)
print("Agreement:",agreement)
plt.show()

