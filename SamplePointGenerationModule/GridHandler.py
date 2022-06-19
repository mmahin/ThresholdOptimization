import numpy as np
from shapely.geometry import Point

def GridGenerator(xmin: float, xmax: float, ymin: float, ymax: float, x_axis_step_size: int,
                  y_axis_step_size: int):
    """This function returns a numpy grid

        Parameters
        ----------
        xmin : float
            The value from which x axis will start
        xmax : float
            The value where x axis will end
        ymin: float
            The value from which y axis will start
        ymax: float
            The value where y axis will end
        x_axis_step_size : int
            Number of points in the x axis
        y_axis_step_size : int
            Number of points in the y axis

        Returns
        -------
        list of list
            a numpy grid. The grid contains two list of list. First list of list contains all row points list and
            second list of list contains all column point list. Each point is a shapely point object identified by a
            latitude, longitude pair

        """
    grid = np.mgrid[xmin:xmax:(x_axis_step_size * 1j), ymin:ymax:(y_axis_step_size * 1j)]
    grid_matrix = []
    xcount = 0
    for x in grid[0]:
        ycount = 0
        row = []
        for y in grid[1]:
            point = Point(x[xcount],y[ycount])
            row.append(point)
            ycount += 1
        grid_matrix.append(row)
        xcount += 1
    return grid, grid_matrix


'''
def __main__():

    hotspots = [[[0, 0]], [[2, 3], [3, 2], [3, 3], [3, 4], [4, 2], [4, 3], [4, 4]]]
    print(GridGenerator(0,10,0, 10, 6, 6))
    #print(xx)
    #print(yy)
    #print(hotspots)
    #obj = GridHandlarModule()
    #print(obj.AddCoordinatesToGridPointBasedHotspots(hotspots, xx, yy))
    #print(obj.AddCoordinatesToGridCellBasedHotspots(hotspots,xx,yy))
__main__()
'''