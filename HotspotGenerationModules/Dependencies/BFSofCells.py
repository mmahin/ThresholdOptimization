from collections import deque
from AddCoordinatesToHotspots import GridCellsToPolygones
from PolygonGeneration import HotspotPointsWithCoordinatesToPolygonUsingShapely
class BFSofCells:
    """Takes two dimentional grid points and returns one or more sets of clustered grid cells as hotspots, where the
    average value from the four intersection points of each grid cell is above a certain threshold.
    Utilize Bredth First Search  to find connected components. Two points are connected if they are reachable using
    grid edge

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

    def __init__(self, threshold: float, x_axis_size: int, y_axis_size: int, grid_mattrix: list,
                 grid):
        """Initializes class variables

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
            """

        self.__threshold = threshold
        self.__x_axis_size = x_axis_size
        self.__y_axis_size = y_axis_size

        ### __grid indicates points above threshold, as 1 others as 0
        ### __visited_points memorize the points traversed

        self.__grid = [[0 for __i in range(y_axis_size-1)]
                          for __i in range(x_axis_size-1)]
        self.__visited_points = [[False for __i in range(y_axis_size-1)]
                          for __i in range(x_axis_size-1)]

        self.__setGridValues(grid_mattrix)
        self.xx = grid[0]
        self.yy = grid[1]

    def __setGridValues(self, grid):
        # This function set the grid points values and set grid cell values. Value of each cell depends on its four
        # intersection points. If the average value of four points  is above the threshold it is marked as 1 else 0.
        # Each cell is identified by point [x,y] and is compromised of four points, [[x,y],[x,y+1],[x+1,y],[x+1,y+1]]

        # Parameter: grid

        __x = 0
        while __x in range(self.__x_axis_size - 1):
            __y = 0
            while __y in range(self.__y_axis_size - 1):
                average_of_points = (grid[__x][__y] + grid[__x][__y + 1]  + grid[__x + 1][__y]  +
                                     grid[__x + 1][__y + 1]) / 4
                #if grid[__x][__y] and grid[__x][__y] >= self.__threshold:
                if average_of_points >= self.__threshold:
                    self.__grid[__x][__y] = 1
                __y = __y + 1
            __x = __x + 1

    # A function to check if a given cell
    # (u, v) can be included in DFS
    def __isSafe(self, __mat, __i, __j):

        return ((__i >= 0) and (__i < self.__x_axis_size - 1) and
                (__j >= 0) and (__j < self.__y_axis_size - 1) and
                (__mat[__i][__j] and (not self.__visited_points[__i][__j])))

    def __MargeCells(self, mat, si, sj):
        ...
    def __BFSofCells(self, mat, si, sj):

        __island_of_points = []

        # These arrays are used to get row and column
        # numbers of 4 directly connect neighbours of
        # a given cell
        #TODO it can be changed to four neighbours if needed
        row = [ -1,  0, 0,  1]
        col = [  0, -1, 1,  0]

        # Enqueue source point and mark it as visited
        __queue = deque()
        __queue.append([si, sj])
        self.__visited_points[si][sj] = True
        __island_of_points.append([si, sj])

        # Take out items one by one from queue and
        # enqueue their univisited adjacent
        while (len(__queue) > 0):
            temp = __queue.popleft()

            __x = temp[0]
            __y = temp[1]

            # Go through all 8 adjacent neighbours
            for __neighbour in range(len(row)):
                if (self.__isSafe(mat, __x + row[__neighbour], __y + col[__neighbour])):
                    self.__visited_points[__x + row[__neighbour]][__y + col[__neighbour]] = True
                    __queue.append([__x + row[__neighbour], __y + col[__neighbour]])
                    __island_of_points.append([__x + row[__neighbour], __y + col[__neighbour]])
        #print("__island_of_points",__island_of_points)
        #print("__island_of_points",len(__island_of_points))
        #Hotspot_Polygon = GridCellsToPolygones(__island_of_points, self.xx, self.yy)
        #print("Hotspots",hotspots)
        #Hotspot_Polygon = HotspotPointsWithCoordinatesToPolygonUsingShapely(hotspots)

        return __island_of_points

    def __DFSofCells(self, mat, si, sj, __island_of_points):

        # These arrays are used to get row and column
        # numbers of 4 directly connect neighbours of
        # a given cell
        #TODO it can be changed to four neighbours if needed
        row = [ -1,  0, 0,  1]
        col = [  0, -1, 1,  0]


        self.__visited_points[si][sj] = True
        if [si, sj] not in __island_of_points:
            __island_of_points.append([si, sj])
        print(__island_of_points)

        # Take out items one by one from queue and
        # enqueue their univisited adjacent

        for __neighbour in range(len(row)):
            if (self.__isSafe(mat, si + row[__neighbour], sj + col[__neighbour])):
                self.__visited_points[si + row[__neighbour]][sj + col[__neighbour]] = True
                __island_of_points = self.__DFSofCells(mat, si + row[__neighbour], sj + col[__neighbour], __island_of_points)
        #print("__island_of_points",__island_of_points)
        #print("__island_of_points",len(__island_of_points))
        #Hotspot_Polygon = GridCellsToPolygones(__island_of_points, self.xx, self.yy)
        #print("Hotspots",hotspots)
        #Hotspot_Polygon = HotspotPointsWithCoordinatesToPolygonUsingShapely(hotspots)

        return __island_of_points #Hotspot_Polygon

    def getHotspots(self):
        """This function returns number hotspots in form of (connected
            components) in a graph. It simply works as
            BFS for disconnected graph and returns count
            of BFS calls.

           Returns
           -------
           list of list
               a list containing lists of grid points, where each list represents a hotspot in form of clusters of points
               and
               Each grid point is represented by it's coordinate [x,y]
           """

        hotspots = []

        # 5all BFS for every unvisited vertex
        # Whenever we see an univisted vertex,
        # we increment res (number of islands)
        # also.
        Visited_True = 0
        Visited_False = 0
        for __x in range(self.__x_axis_size - 1):
            for __y in range(self.__y_axis_size - 1):
                if self.__visited_points[__x][__y] == True:
                    Visited_True += 1
                else:
                    Visited_False += 1
                if (self.__grid[__x][__y] and not self.__visited_points[__x][__y]):
                    #__island_of_points = []
                    #__island_of_points = self.__DFSofCells(self.__grid, __x, __y, __island_of_points)
                    __island_of_points = self.__BFSofCells(self.__grid, __x, __y)
                    Hotspot_Polygon = GridCellsToPolygones(__island_of_points, self.xx, self.yy)
                    if type(Hotspot_Polygon) != type(None):
                        hotspots.append(Hotspot_Polygon)
                #print("Visited_true", Visited_True, "Visited_fals", Visited_False)
        print(len(hotspots))


        return hotspots
'''
### Test Code
def __main__():
    mat = [[0.6, 1  , 0  , 0  , 0   , 0.6],
           [0  , 0.7, 0  , 0  , 0.55, 0  ],
           [0.8, 0  , 0  , 0.7, 0.6 , 0,9],
           [0  , 0  , 0  , 1  , 0   , 0.8],
           [0.6, 0  , 0.7, 0.9  , 0.65, 0.7],
           [0.6, 0  , 0.7, 0  , 0.65, 0.7]]

    x_axis_size = 6
    y_axis_size = 6
    threshold = 0.5

    obj = BFSofCells(threshold,x_axis_size,y_axis_size, mat)
    print(obj.getHotspots())

__main__()
'''