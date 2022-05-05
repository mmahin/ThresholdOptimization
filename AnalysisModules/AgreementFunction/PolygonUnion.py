def PolygonUnion(self, polygon1: list, polygon2: list):
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
    output_polygon = polygon1.union(polygon2)
    return output_polygon