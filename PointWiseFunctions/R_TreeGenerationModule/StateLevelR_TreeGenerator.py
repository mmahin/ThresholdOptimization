import geopandas as gpd
from shapely.geometry import Polygon, Point
from AgreementFunction.PolygonAreaCalculation import PolygonArea
import numpy as np
import pandas as pd
path_shp = "/tl_2016_us_state/tl_2016_us_state.shp"
my_df_shp = gpd.read_file(path_shp)
#import matplotlib.pyplot as plt
#fig, axs = plt.subplots(2, 1, constrained_layout=False)
sorted_state_fps_lists = []
min_long_list = []
min_lat_list = []
max_long_list = []
max_lat_list = []
for count in range(len(my_df_shp['geometry'])):
    min_long, min_lat, max_long, max_lat = my_df_shp['geometry'][count].bounds
    bottom_left_of_rectangle = [min_long, min_lat]
    upper_left_of_rectangle = [min_long, max_lat]
    bottom_right_of_rectangle = [max_long, min_lat]
    upper_right_of_rectangle = [max_long, max_lat]

    state_rectangle = Polygon([bottom_left_of_rectangle, upper_left_of_rectangle, upper_right_of_rectangle, bottom_right_of_rectangle])
    states_with_intersection_area = []
    states_with_intersection_fp = []
    for count2 in range(len(my_df_shp['geometry'])):
        state_intersection = state_rectangle.intersection(my_df_shp['geometry'][count2])
        if state_intersection:
            area = PolygonArea(state_intersection)
            states_with_intersection_area.append(area)
            states_with_intersection_fp.append(my_df_shp['STATEFP'][count2])

    sorted_area_indics = np.argsort(states_with_intersection_area)
    size = len(np.argsort(sorted_area_indics))
    sorted_fps = []
    count3 = size - 1
    while count3 >= 0:
        sorted_fps.append(int(states_with_intersection_fp[count3]))
        count3 -= 1
    sorted_state_fps_lists.append(sorted_fps)
    min_long_list.append(min_long)
    min_lat_list.append(min_lat)
    max_long_list.append(max_long)
    max_lat_list.append(max_lat)
    #gdf = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[state_rectangle])
    #gdf.plot(linewidth=0.8, ax=axs[0], edgecolor='red', color='r', facecolor="none")
    #plt.show()

df = pd.DataFrame()
df['min_long'] = min_long_list
df['min_lat'] = min_lat_list
df['max_long'] = max_long_list
df['max_lat'] = max_lat_list
df['StateFBsInBoundary'] = sorted_state_fps_lists

df.to_csv("StateLevelRtree.csv")
