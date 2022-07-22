import geopandas as gpd
path_shp = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/tl_2016_us_state/tl_2016_us_state.shp"
my_df_shp = gpd.read_file(path_shp)
for item in my_df_shp:
    print(item)

for item in my_df_shp['STATEFP']:
    print(item)

for item in my_df_shp['geometry']:
    print(item.bounds)