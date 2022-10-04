from AgreementFunction.PolygonAreaCalculation import PolygonArea

def PolygonIntersectionVisualization(polygon_list1: list, polygon_list2: list):
    """This function takes two polygones and retunes their intersection polygon

    Parameters
    ----------
    polygon1: polygon
        A shapely polygon consisting list of points

    polygon2: polygon
        A shapely polygon consisting list of points


    Returns
    -------
    list
        list of points representing intersected polygon
    """
    intersection_polygones = []
    for polygon1 in polygon_list1:
        for polygon2 in polygon_list2:
            intersection_polygon = polygon1.intersection(polygon2)
            if intersection_polygon:
                intersection_polygones.append(intersection_polygon)

    return intersection_polygones