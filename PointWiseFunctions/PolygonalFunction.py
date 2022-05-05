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

def PolygonalValueEstimation(point:object, dataset:object):
    row = 0
    withinPolygons = False
    for polygon in dataset['polygons']:
        if point.within(polygon):
            return dataset['values'][row]

        row += 1

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