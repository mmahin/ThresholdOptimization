from Dependencies.BFSofCells import BFSofCells
from PolygonGeneration import HotspotPointsWithCoordinatesToPolygonUsingShapely
from PolygonGeneration import HotspotPointsWithCoordinatesToPolygonUsingConcaveHull
from collections import deque
def hotspotOfCellsUsingBFS(_threshold: float, _x_axis_size: int, _y_axis_size: int, _grid: list, grid:float):
    """This function returns number hotspots in form of (connected
    components of cells) in a graph.
    Parameters
    ----------
            threshold : float
                The value above which points are considered as hot points
            x_axis_size : int
                Number of points in the x axis
            y_axis_size : int
                Number of points in the y axis
            grid_mattrix : list of list of float type
                Matrix in a form of list of list and elements are float type

   Returns
   -------
   list of list
       a list containing lists of grid points, where each list represents a hotspot in form of clusters of points
       and
       Each grid point is represented by it's coordinate [x,y]
    """

    obj = BFSofCells(_threshold, _x_axis_size, _y_axis_size, _grid,  grid)
    hotspotsPolygons = HotspotPointsWithCoordinatesToPolygonUsingConcaveHull(obj.getHotspots(),1)

    return hotspotsPolygons
