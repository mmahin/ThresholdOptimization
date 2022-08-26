import geopandas as gpd
from shapely.geometry import Polygon, Point, LineString
from shapely.ops import split
from AgreementFunction.PolygonAreaCalculation import PolygonArea
import numpy as np
import pandas as pd


def polygonalR_NodeGenerator(large_polygon, innerPolygonList):
    # Split the polygon into half
    min_long, min_lat, max_long, max_lat = large_polygon.bounds

    bottom_left_corner = [min_long, min_lat]
    upper_left_corner = [min_long, max_lat]
    bottom_right_corner = [max_long, min_lat]
    upper_right_corner = [max_long, max_lat]

    bottom_middle = [(bottom_left_corner[0]+bottom_right_corner[0])/2,
                     (bottom_left_corner[1]+bottom_right_corner[1])/2]
    upper_middle = [(upper_left_corner[0] + upper_right_corner[0]) / 2,
                     (upper_left_corner[1] + upper_right_corner[1]) / 2]
    splitting_line = LineString([bottom_middle, upper_middle])

    result = split(large_polygon, splitting_line)
    #if len(result) > 0:
    nodePolygones = []
    innerPolygonesWithinNodePolygonLists = []
    for item in result:
        polygonList = []
        for polygon in innerPolygonList:
            if item.intersects(polygon):
                polygonList.append(polygon)
                innerPolygonList.remove(polygon)
        if len(polygonList) > 0:
            innerPolygonesWithinNodePolygonLists.append(polygonList)
            nodePolygones.append(item)

    return nodePolygones, innerPolygonesWithinNodePolygonLists

