import pandas as pd
from shapely.ops import cascaded_union
import shapely.wkt
import geopandas as gpd
import matplotlib.pyplot as plt
from GridHandler import GridGenerator
from VisualizationModules.HotspotsVisualization import HotspotsVisualiztion
df = pd.read_csv('C:/Users/mdmah/PycharmProjects/ProfessorEick/ThresholdOptimization/DataProcessing/ProcessedData/UnemploymentPolygon.csv')

unemployment_rate_2018_df = pd.DataFrame()
median_income_2018_df = pd.DataFrame()

continuous_us_counties_polygon = []
continuous_us_unemployments = []
continuous_us_median_income = []


for i in range(0,len(df['FIPS'])):
    val = int(df['FIPS'][i]/1000)
    if val == 2 or val == 15 or val == 60 or val == 66 or val == 69 or val == 72 or val == 78:
        pass
    else:
        continuous_us_counties_polygon.append(shapely.wkt.loads(df['geometry'][i]))
        continuous_us_unemployments.append(df['Unemployment_rate_2018'][i])
        float_value = 0
        if df['Median_Household_Income_2018'][i]:
            float_value = (float((((((df['Median_Household_Income_2018'][i]).split('$'))[1]).split(' '))[0]).replace(',','')))
        continuous_us_median_income.append(float_value)

unemployment_rate_2018_df['values'] = continuous_us_unemployments
unemployment_rate_2018_df['polygons'] = continuous_us_counties_polygon

median_income_2018_df['values'] = continuous_us_median_income
median_income_2018_df['polygons'] = continuous_us_counties_polygon

boundary = gpd.GeoSeries(cascaded_union(continuous_us_counties_polygon))
#fig, ax = plt.subplots(1, 1, figsize=(10, 8))
#boundary.plot(linewidth=0.8, ax=ax, edgecolor='black', facecolor="none")
#plt.show()
bounds = boundary.bounds
minx = (bounds['minx']).values
miny = (bounds['miny']).values
maxx = (bounds['maxx']).values
maxy = (bounds['maxy']).values

print(minx, maxx, miny, maxy)
grid, grid_matrix = GridGenerator(minx, maxx, miny, maxy, 20, 20)

from PolygonalFunction import PolygonalValueEstimation
unemployment_value_matrix = []
median_income_value_matrix = []
for row in grid_matrix:
    unemployment_row_values = []
    median_income_row_values = []
    for point in row:
        value_unemployment = PolygonalValueEstimation(point, unemployment_rate_2018_df)
        value_median_income = PolygonalValueEstimation(point, median_income_2018_df)
        unemployment_row_values.append(value_unemployment)
        median_income_row_values.append(value_median_income)

    unemployment_value_matrix.append(unemployment_row_values)
    median_income_value_matrix.append(median_income_row_values)
print(median_income_value_matrix)
from HotspotsUsingBFS import hotspotOfCellsUsingBFS
hotspots = hotspotOfCellsUsingBFS(4,20, 20, unemployment_value_matrix, grid)
HotspotsVisualiztion(hotspots)
from ContourVisualization import contourPlot
#contourPlot(unemployment_value_matrix,grid[0],grid[1])
#contourPlot(median_income_value_matrix,grid[0],grid[1])
#print("HI")
