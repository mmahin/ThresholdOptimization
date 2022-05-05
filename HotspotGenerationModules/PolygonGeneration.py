import alphashape
from shapely.geometry import Polygon
def HotspotPointsWithCoordinatesToPolygonUsingConcaveHull(Hotspots: list, alpha: int):
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
    hotspotPolygones = []
    for hotspot in Hotspots:
        alpha_shape = alphashape.alphashape(hotspot, alpha)
        hotspotPolygones.append(alpha_shape)
    return hotspotPolygones

def HotspotPointsWithCoordinatesToPolygonUsingShapely( Hotspots: list):
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
    hotspotPolygones = []
    for hotspot in Hotspots:
        if len(hotspot) >= 3:
            polygon = Polygon(hotspot)
            hotspotPolygones.append(polygon)
    return hotspotPolygones