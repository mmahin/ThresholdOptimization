import pyproj
import shapely.ops as ops
from functools import partial
import warnings
import geopandas as gpd
def PolygonArea(polygon: object):
    """This function calculates and returnes total area of a shapely polygon in squared meter. This function will be used
    to calculate area of each grid cell

        Parameters
        ----------
        polygon: object
            A shapely polygon object

        Returns
        -------
        area
            Total area in squared meter

        """
    warnings.filterwarnings('ignore')
    geom = polygon
    geom_area = ops.transform(
        partial(
            pyproj.transform,
            pyproj.Proj(init='EPSG:4326'),
            pyproj.Proj(
                proj='aea',
                lat_1=geom.bounds[1],
                lat_2=geom.bounds[3])),
        geom)


    return geom_area.area

def HotspotAreaInverse(Hotspot: object):
    """This function calculates and returnes total area of a shapely polygon in squared meter. This function will be used
    to calculate area of each grid cell

        Parameters
        ----------
        polygon: object
            A shapely polygon object

        Returns
        -------
        area
            Total area in squared meter

        """
    contiguousUSA_shape = gpd.read_file(
        "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/contiguousUSASHP/contiguousUSA.shp")
    contiguousUSA_shape = contiguousUSA_shape.to_crs("epsg:4326")
    target_polygon = contiguousUSA_shape['geometry'][0]
    for polygon in Hotspot:
        target_polygon = target_polygon.difference(polygon)
    warnings.filterwarnings('ignore')
    area = 0
    for polygon in target_polygon:
        geom = polygon
        geom_area = ops.transform(
            partial(
                pyproj.transform,
                pyproj.Proj(init='EPSG:4326'),
                pyproj.Proj(
                    proj='aea',
                    lat_1=geom.bounds[1],
                    lat_2=geom.bounds[3])),
            geom)
        area += geom_area.area


    return area