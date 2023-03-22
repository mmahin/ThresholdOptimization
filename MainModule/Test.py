import geopandas as gpd
from AgreementFunction.PolygonAreaCalculation import PolygonArea
from shapely.ops import unary_union
from SubModules.ObtainVariableDataframesAndStateDictionary import getVariableDataframesAndSpatialIndexes
import matplotlib.pyplot as plt

data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'

#Set Inputs
#data access inputs
variable1_name = 'bachelor_degree_density_2014_2018'
variable2_name = 'medianHouseHoldIncome'

variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)
polygones = []
for polygon in variable1_df['polygons']:
    polygones.append(polygon)

combined_observation_area_polygon = gpd.GeoSeries(unary_union(polygones))

total_area = 0
for polygon in combined_observation_area_polygon:
    area = PolygonArea(polygon)
    total_area += area

# Create the observation grid
bounds = combined_observation_area_polygon.bounds
minx = (bounds['minx']).values
miny = (bounds['miny']).values
maxx = (bounds['maxx']).values
maxy = (bounds['maxy']).values

from shapely import geometry
p1 = geometry.Point(minx,miny)
p2 = geometry.Point(minx,maxy)
p3 = geometry.Point(maxx,miny)
p4 = geometry.Point(maxx,maxy)

pointList = [p1, p2, p4, p3, p1]

poly = geometry.Polygon(pointList)
'''
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
gdf = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[poly])
gdf.plot(linewidth=0.8, ax=ax, edgecolor='red', color='r', facecolor="none")
plt.show()
'''
area2 = PolygonArea(poly)
print((area2-area),(area2-area)/area )