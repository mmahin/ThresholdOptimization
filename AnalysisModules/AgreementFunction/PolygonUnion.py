from AgreementFunction.PolygonAreaCalculation import PolygonArea
def PolygonUnion(polygon_list1: list, polygon_list2: list, Total_intersection_area: float):
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
        list of points representing union of polygon
    """
    Total_Union_area = 0
    for polygon in polygon_list1:
        area = PolygonArea(polygon)
        Total_Union_area += area

    for polygon in polygon_list2:
        area = PolygonArea(polygon)
        Total_Union_area += area

    Total_Union_area  -= Total_intersection_area

    return Total_Union_area