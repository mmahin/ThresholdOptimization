#polygon division
#polygon intersection and merge
#state_to_county_tree
#Full tree
import geopandas as gpd
import pandas as pd
from PolygonalR_Tree import polygonalR_NodeGenerator
import shapely.wkt
# Get the states
path_shp = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/tl_2016_us_state/tl_2016_us_state.shp"
my_df_shp = gpd.read_file(path_shp)

df = pd.read_csv('C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv')

for count in range(len(my_df_shp['geometry'])):
    stateFIPSfromShape = int(my_df_shp["STATEFP"][count])
    state_counties = []
    for count_df in range(len(df['FIPS'])):
        stateFIPSfromDataset = int(df['FIPS'][count_df] / 1000)

        if stateFIPSfromShape == stateFIPSfromDataset:
            state_counties.append(shapely.wkt.loads(df['geometry'][count_df]))

    print(len(state_counties))
    print(polygonalR_NodeGenerator(my_df_shp['geometry'][count], state_counties))
    break