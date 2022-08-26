'''
    This function is given a point and dataset as input and it returns value on that point. The dataset contains a set
    of shapely polygons and a set of values for each polygon.

    Inputs
    ____________________________________________________________________________________________________________________
    - point: a point object represented by (latitude, longitude) pair
     -  type: shapely point object
    - dataset: a pandas dataframe containing two columns
        - polygons: representing a polygon
            - type: shapely polygon object
        - values: representing values associated with each polygon
            -type: floating point

    Outputs
    ____________________________________________________________________________________________________________________
    - returns a value for the point
        -type: floating point
'''
from shapely.geometry import Point, Polygon
import shapely.wkt
import geopandas as gpd
def PolygonalValueEstimationUsingR_TreeAndDictionary(point:object, dataset:object, dict):
    path_shp = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/tl_2016_us_state/tl_2016_us_state.shp"
    my_df_shp = gpd.read_file(path_shp)
    fips = 0
    for count in range(len(my_df_shp['geometry'])):
        if point.within(my_df_shp['geometry'][count]):
            fips = int(my_df_shp['STATEFP'][count])
            break
    withinPolygons = False
    if fips != 0 and (fips in dict.keys()):
        rows = dict[int(fips)]
        for row in rows:
            if point.within(dataset['polygons'][row]):
                return dataset['values'][row]

    if withinPolygons == False:
        return 0


'''
# Create Point objects
p1 = Point(24.952242, 60.1696017)
p2 = Point(24.976567, 60.1612500)
# Create a Polygon
coords = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
poly = Polygon(coords)
PolygonalValueEstimation(p1,poly)
'''