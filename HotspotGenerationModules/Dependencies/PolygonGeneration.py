#import alphashape
from shapely.geometry import Polygon
def HotspotPointsWithCoordinatesToPolygonUsingConcaveHull(Hotspot: list, alpha: int):
    """This function takes the hotspots where everypoint has their latituate and longitude coordinates and
    generate polygon for each hotspot

    Parameters
    ----------
    Hotspots: list of list
        The list of hotspots, where each list contains points in the hotspot

    alpha: integer
        Indicates the shape of polygon. Higher values will make the polygon too edgey. For 0 we will get  convex
        hull polygones

    Returns
    -------
    list of list
        list of polygones where each list is a polygon. Every polygon is a PolygonPatch
    """
    alpha_shape = alphashape.alphashape(Hotspot, alpha)
    return alpha_shape

def HotspotPointsWithCoordinatesToPolygonUsingShapely( Hotspot: list):
    """This function takes the hotspots where everypoint has their latituate and longitude coordinates and
    generate polygon for each hotspot

    Parameters
    ----------
    Hotspots: list of list
        The list of hotspots, where each list contains points in the hotspot

    alpha: integer
        Indicates the shape of polygon. Higher values will make the polygon too edgey. For 0 we will get  convex
        hull polygones

    Returns
    -------
    list of list
        list of polygones where each list is a polygon. Every polygon is a PolygonPatch
    """
    if len(Hotspot) >= 3:
        polygon = Polygon(Hotspot)

        return polygon