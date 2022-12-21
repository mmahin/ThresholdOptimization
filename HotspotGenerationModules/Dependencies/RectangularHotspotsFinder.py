from collections import deque
from AddCoordinatesToHotspots import GridCellsToPolygones
#from PolygonGeneration import HotspotPointsWithCoordinatesToPolygonUsingShapely
class RectangularHotspotsFinder:
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
                 grid, alpha):
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
        self.alpha = alpha
        self.__threshold = threshold
        self.__x_axis_size = x_axis_size
        self.__y_axis_size = y_axis_size
        self.xx = grid[0]
        self.yy = grid[1]
        self.grid= grid
        self.grid_mattrix = grid_mattrix
        ### __grid indicates points above threshold, as 1 others as 0
        ### __visited_points memorize the points traversed

        self.__grid = [[0 for __i in range(y_axis_size-1)]
                          for __i in range(x_axis_size-1)]
        self.__visited_points = [[False for __i in range(y_axis_size-1)]
                          for __i in range(x_axis_size-1)]


        self.__setGridValues(grid_mattrix)


    def __setGridValues(self, grid):
        # This function set the grid points values and set grid cell values. Value of each cell depends on its four
        # intersection points. If the average value of four points  is above the threshold it is marked as 1 else 0.
        # Each cell is identified by point [x,y] and is compromised of four points, [[x,y],[x,y+1],[x+1,y],[x+1,y+1]]

        # Parameter: grid


        __x = 0
        while __x in range(self.__x_axis_size - 1):
            __y = 0
            while __y in range(self.__y_axis_size - 1):
                #average_of_points = (grid[__x][__y] + grid[__x][__y + 1]  + grid[__x + 1][__y]  +
                #                     grid[__x + 1][__y + 1]) / 4
                #if grid[__x][__y] and grid[__x][__y] >= self.__threshold:

                if grid[__x][__y] >= self.__threshold:
                    self.__grid[__x][__y] = 1
                __y = __y + 1
            __x = __x + 1

    # A function to check if a given cell
    # (u, v) can be included in DFS
    def __isSafe(self, __mat, __i, __j):

        return ((__i >= 0) and (__i < self.__x_axis_size - 1) and
                (__j >= 0) and (__j < self.__y_axis_size - 1) and
                (__mat[__i][__j] and (not self.__visited_points[__i][__j])))
    def __isSafeAndAllowed(self, __mat, __i, __j):

        return ((__i >= 0) and (__i < self.__x_axis_size - 1) and
                (__j >= 0) and (__j < self.__y_axis_size - 1)
                and (not self.__visited_points[__i][__j]))
    def __isSafeToInclude(self, __mat, __i, __j):

        return ((__i >= 0) and (__i < self.__x_axis_size - 1) and
                (__j >= 0) and (__j < self.__y_axis_size - 1) )



    def __hotspotSideApproval(self, mat, upperLeftCorner, upperLeftCornerChanged, upperRightCorner, upperRightCornerChanged,
                              LowerRightCorner, LowerRightCornerChanged, lowerLeftCorner, lowerLeftCornerChanged, allowed_percent):
        # define four corner

        # define four side availability
        leftSideApproved = False
        upSideApproved = False
        rightSideApproved = False
        downSideApproved = False


        if upperLeftCornerChanged and upperRightCornerChanged:
            # generate points between the two corners
            upSidePointsApproved = 0
            TotalUppsidePoints = 0
            # Check number of valid points within the side

            for column in range(upperLeftCorner[1],  upperRightCorner[1] + 1):
                if self.__isSafe(mat, upperLeftCorner[0], column):
                    upSidePointsApproved += 1
                TotalUppsidePoints += 1
            # Approve or disapprove the side
            if upSidePointsApproved / TotalUppsidePoints >= allowed_percent:
                upSideApproved = True

            if upSideApproved:
                for column in range(upperLeftCorner[1],  upperRightCorner[1] + 1):
                    if self.__isSafeToInclude(mat, upperLeftCorner[0], column):
                        self.__visited_points[upperLeftCorner[0]][column] = True

        if  upperLeftCornerChanged and lowerLeftCornerChanged:
            # generate points between the two corners
            leftSidePointsApproved = 0
            TotalLeftpsidePoints = 0
            # Check number of valid points within the side
            for row in range(upperLeftCorner[0] , lowerLeftCorner[0] + 1):
                if self.__isSafe(mat, row, upperLeftCorner[1]):
                    leftSidePointsApproved += 1
                TotalLeftpsidePoints += 1
            # Approve or disapprove the side
            if leftSidePointsApproved / TotalLeftpsidePoints >= allowed_percent:
                leftSideApproved = True

            if leftSideApproved:
                for row in range(upperLeftCorner[0], lowerLeftCorner[0] + 1):

                    if self.__isSafeToInclude(mat, row, upperLeftCorner[1]):
                        self.__visited_points[row][upperLeftCorner[1]] = True

        if  LowerRightCornerChanged and lowerLeftCornerChanged:
            # generate points between the two corners
            downSidePointsApproved = 0
            TotalDownpsidePoints = 0
            # Check number of valid points within the side

            #print(lowerLeftCorner, LowerRightCorner, self.__visited_points[lowerLeftCorner[0]][lowerLeftCorner[1]],self.__visited_points[LowerRightCorner[0]][LowerRightCorner[1]])
            for column in range(lowerLeftCorner[1]  ,  LowerRightCorner[1]+ 1):
                #print(LowerRightCorner[0], column)
                if self.__isSafe(mat, LowerRightCorner[0], column):
                    downSidePointsApproved += 1
                TotalDownpsidePoints += 1

            # Approve or disapprove the side
            if downSidePointsApproved / TotalDownpsidePoints >= allowed_percent:
                downSideApproved = True
            if downSideApproved:
                for column in range(lowerLeftCorner[1]  ,  LowerRightCorner[1]+ 1):
                    if self.__isSafeToInclude(mat, LowerRightCorner[0], column):
                        self.__visited_points[LowerRightCorner[0]][column] = True

        if LowerRightCornerChanged and upperRightCornerChanged:

            # generate points between the two corners
            rightSidePointsApproved = 0
            TotalRightpsidePoints = 0
            # Check number of valid points within the side
            for row in range(upperRightCorner[0] , LowerRightCorner[0] + 1):
                if self.__isSafe(mat, row, LowerRightCorner[1]):
                    rightSidePointsApproved += 1
                TotalRightpsidePoints += 1
            # Approve or disapprove the side
            if rightSidePointsApproved / TotalRightpsidePoints >= allowed_percent:
                rightSideApproved = True
            if rightSideApproved:
                for row in range(LowerRightCorner[1], lowerLeftCorner[1] + 1):
                    if self.__isSafeToInclude(mat, row, LowerRightCorner[1]):
                        self.__visited_points[row][LowerRightCorner[1]] = True

        return leftSideApproved, upSideApproved, rightSideApproved, downSideApproved
    def __RectangularHotspotFinder(self, mat, si, sj):
        #print([si,sj])
        allowed_percent = self.alpha
        __hotspot = []
        upperLeftCorner = [si, sj ]
        upperRightCorner = [si, sj ]
        LowerRightCorner = [si, sj ]
        lowerLeftCorner = [si , sj ]
        upperLeftCornerChanged = True
        upperRightCornerChanged = True
        LowerRightCornerChanged = True
        lowerLeftCornerChanged = True
        # define four corner


        if self.__isSafeAndAllowed(mat, upperLeftCorner[0] - 1, upperLeftCorner[1] - 1):
            upperLeftCorner = [upperLeftCorner[0] - 1, upperLeftCorner[1] - 1]
        elif self.__isSafeAndAllowed(mat, upperLeftCorner[0], upperLeftCorner[1] - 1):
            upperLeftCorner = [upperLeftCorner[0], upperLeftCorner[1] - 1]
        elif self.__isSafeAndAllowed(mat, upperLeftCorner[0] - 1, upperLeftCorner[1]):
            upperLeftCorner = [upperLeftCorner[0] - 1, upperLeftCorner[1]]
        else:
            upperLeftCornerChanged = False


        if self.__isSafeAndAllowed(mat, upperRightCorner[0] - 1, upperRightCorner[1] + 1):
            upperRightCorner = [upperRightCorner[0] - 1, upperRightCorner[1] + 1]
        elif self.__isSafeAndAllowed(mat, upperRightCorner[0] - 1, upperRightCorner[1]):
            upperRightCorner = [upperRightCorner[0] - 1, upperLeftCorner[1]]
        if self.__isSafeAndAllowed(mat, upperRightCorner[0], upperRightCorner[1] + 1):
            upperRightCorner = [upperRightCorner[0], upperLeftCorner[1] + 1]
        else:
            upperRightCornerChanged = False


        if self.__isSafeAndAllowed(mat, LowerRightCorner[0] + 1, LowerRightCorner[1] + 1):
            LowerRightCorner = [LowerRightCorner[0] + 1, LowerRightCorner[1] + 1]
        elif  self.__isSafeAndAllowed(mat, LowerRightCorner[0], LowerRightCorner[1] + 1):
            LowerRightCorner = [LowerRightCorner[0], LowerRightCorner[1] + 1]
        elif self.__isSafeAndAllowed(mat, LowerRightCorner[0] + 1, LowerRightCorner[1]):
            LowerRightCorner = [LowerRightCorner[0] + 1, LowerRightCorner[1]]
        else:
            LowerRightCornerChanged = False

        if self.__isSafeAndAllowed(mat, lowerLeftCorner[0] + 1, lowerLeftCorner[1] - 1):
            lowerLeftCorner = [lowerLeftCorner[0] + 1, lowerLeftCorner[1] - 1]
        elif self.__isSafeAndAllowed(mat, lowerLeftCorner[0] + 1, lowerLeftCorner[1]):
            lowerLeftCorner = [lowerLeftCorner[0] + 1, lowerLeftCorner[1]]
        elif self.__isSafeAndAllowed(mat, lowerLeftCorner[0], lowerLeftCorner[1] - 1):
            lowerLeftCorner = [lowerLeftCorner[0], lowerLeftCorner[1] - 1]
        else:
            lowerLeftCornerChanged = False


        leftSideApproved, upSideApproved, rightSideApproved, downSideApproved = self.__hotspotSideApproval(mat,
                        upperLeftCorner, upperLeftCornerChanged, upperRightCorner, upperRightCornerChanged,
                        LowerRightCorner, LowerRightCornerChanged, lowerLeftCorner, lowerLeftCornerChanged, allowed_percent)


        while leftSideApproved or upSideApproved or rightSideApproved or downSideApproved :
            # define four corner based on approved side
            #print(upperLeftCorner, upperRightCorner, LowerRightCorner, lowerLeftCorner,
            #      leftSideApproved, upSideApproved, rightSideApproved, downSideApproved, LowerRightCornerChanged, lowerLeftCornerChanged)
            upperLeftCornerChanged = True
            upperRightCornerChanged = True
            LowerRightCornerChanged = True
            lowerLeftCornerChanged = True
            if leftSideApproved and upSideApproved:
                if self.__isSafeAndAllowed(mat, upperLeftCorner[0] - 1, upperLeftCorner[1]  - 1):
                    upperLeftCorner = [upperLeftCorner[0] - 1, upperLeftCorner[1]  - 1]
                else:
                    upperLeftCornerChanged = False
            elif  leftSideApproved and   upSideApproved == False:
                if self.__isSafeAndAllowed(mat, upperLeftCorner[0] , upperLeftCorner[1]  - 1):
                    upperLeftCorner = [upperLeftCorner[0] , upperLeftCorner[1]  - 1]
                else:
                    upperLeftCornerChanged = False

            elif  leftSideApproved == False and   upSideApproved:
                if self.__isSafeAndAllowed(mat, upperLeftCorner[0] - 1, upperLeftCorner[1]  ):
                    upperLeftCorner = [upperLeftCorner[0] - 1, upperLeftCorner[1]  ]
                else:
                    upperLeftCornerChanged = False
            else:
                upperLeftCornerChanged = False

            if upSideApproved and rightSideApproved:
                if self.__isSafeAndAllowed(mat, upperRightCorner[0] - 1, upperRightCorner[1]  + 1):
                    upperRightCorner = [upperRightCorner[0] -  1, upperRightCorner[1]  + 1]
                else:
                    upperRightCornerChanged = False

            elif  upSideApproved and   rightSideApproved == False:
                if self.__isSafeAndAllowed(mat, upperRightCorner[0] - 1, upperRightCorner[1] ):
                    upperRightCorner = [upperRightCorner[0] - 1, upperRightCorner[1]]
                else:
                    upperRightCornerChanged = False

            elif  upSideApproved == False and   rightSideApproved:
                if self.__isSafeAndAllowed(mat, upperRightCorner[0] , upperRightCorner[1] + 1 ):
                    upperRightCorner = [upperRightCorner[0] , upperRightCorner[1] + 1 ]
                else:
                    upperRightCornerChanged = False

            else:
                upperRightCornerChanged = False
            if rightSideApproved and downSideApproved:
                if self.__isSafeAndAllowed(mat, LowerRightCorner[0] + 1 , LowerRightCorner[1] + 1 ):
                    LowerRightCorner = [LowerRightCorner[0] +  1, LowerRightCorner[1]  + 1]
                else:
                    LowerRightCornerChanged = False

            elif  rightSideApproved and   downSideApproved == False:
                if self.__isSafeAndAllowed(mat, LowerRightCorner[0]  , LowerRightCorner[1] + 1 ):
                    LowerRightCorner = [LowerRightCorner[0], LowerRightCorner[1] + 1]
                else:
                    LowerRightCornerChanged = False


            elif  rightSideApproved == False and   downSideApproved:
                if self.__isSafeAndAllowed(mat, LowerRightCorner[0] + 1  , LowerRightCorner[1] ):
                    LowerRightCorner = [LowerRightCorner[0] + 1 , LowerRightCorner[1] ]
                else:
                    LowerRightCornerChanged = False

            else:
                LowerRightCornerChanged = False

            if downSideApproved and leftSideApproved:
                if self.__isSafeAndAllowed(mat, lowerLeftCorner[0] + 1  , lowerLeftCorner[1] - 1):
                    lowerLeftCorner = [lowerLeftCorner[0] +  1, lowerLeftCorner[1]  - 1]
                else:
                    lowerLeftCornerChanged = False


            elif  downSideApproved and   leftSideApproved == False:
                if self.__isSafeAndAllowed(mat, lowerLeftCorner[0] + 1  , lowerLeftCorner[1]):
                    lowerLeftCorner = [lowerLeftCorner[0] + 1, lowerLeftCorner[1]]
                else:
                    lowerLeftCornerChanged = False


            elif  downSideApproved == False and   leftSideApproved:
                if self.__isSafeAndAllowed(mat, lowerLeftCorner[0]   , lowerLeftCorner[1] - 1):
                    lowerLeftCorner = [lowerLeftCorner[0] , lowerLeftCorner[1] - 1]
                else:
                    lowerLeftCornerChanged = False


            else:
                lowerLeftCornerChanged = False
            #print(LowerRightCornerChanged)
            leftSideApproved, upSideApproved, rightSideApproved, downSideApproved = self.__hotspotSideApproval(mat,
                                                                                                               upperLeftCorner,
                                                                                                               upperLeftCornerChanged,
                                                                                                               upperRightCorner,
                                                                                                               upperRightCornerChanged,
                                                                                                               LowerRightCorner,
                                                                                                               LowerRightCornerChanged,
                                                                                                               lowerLeftCorner,
                                                                                                               lowerLeftCornerChanged,
                                                                                                               allowed_percent)
            #print(upperLeftCorner, upperRightCorner, LowerRightCorner, lowerLeftCorner,
            #      leftSideApproved, upSideApproved, rightSideApproved, downSideApproved,  LowerRightCornerChanged, lowerLeftCornerChanged)


        if self.__isSafeToInclude(mat, upperLeftCorner[0], upperLeftCorner[1]) and self.__isSafeToInclude(mat, upperRightCorner[0], upperRightCorner[1])\
                and self.__isSafeToInclude(mat, LowerRightCorner[0], LowerRightCorner[1]) and  self.__isSafeToInclude(mat, lowerLeftCorner[0], lowerLeftCorner[1]):

            __hotspot.append(self.grid[upperLeftCorner[0]][upperLeftCorner[1]])
            __hotspot.append(self.grid[upperRightCorner[0]][upperRightCorner[1]])
            __hotspot.append(self.grid[LowerRightCorner[0]][LowerRightCorner[1]])
            __hotspot.append(self.grid[lowerLeftCorner[0]][lowerLeftCorner[1]])
            values = []
            indexes= []
            for i in range(upperLeftCorner[0],lowerLeftCorner[0]+1):
                for j in  range(upperLeftCorner[1],upperRightCorner[1]+1):
                    self.__visited_points[i][j] = True
                    p = self.grid_mattrix[i][j]
                    values.append(p)
                    indexes.append([i,j])
            max_interestingness_value = round(max(values),2)
            max_interestingness_index = values.index(max(values))
            max_index = indexes[max_interestingness_index]
            max_thresholds = [round((self.grid[max_index[0]][max_index[1]]).x,2),round((self.grid[max_index[0]][max_index[1]]).y,2)]

            print(max_interestingness_value,max_thresholds)
            #print(__hotspot)
            #print(self.__visited_points)
        return __hotspot


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
                    __island_of_points = self.__RectangularHotspotFinder(self.__grid, __x, __y)
                    #print(self.__visited_points)
                    from shapely import geometry
                    points = []
                    for point in __island_of_points:
                        points.append((round(point.x,2), round(point.y,2)))
                    print(points)
                    hotspot_polygon = geometry.Polygon(__island_of_points)
                    hotspots.append(hotspot_polygon)


                    #Hotspot_Polygon = GridCellsToPolygones(__island_of_points, self.xx, self.yy)
                    #if type(Hotspot_Polygon) != type(None):
                    #    hotspots.append(Hotspot_Polygon)
                #print("Visited_true", Visited_True, "Visited_fals", Visited_False)
        #print(len(hotspots))


        return hotspots

### Test Code
from SamplePointGenerationModule.GridHandler import GridGenerator
def __main__():
    mat = [[0.6, 1  , 0  , 0  , 0   , 0.6],
           [0  , 0.7, 0  , 0  , 0.55, 0  ],
           [0.8, 0  , 0  , 0.7, 0.6 , 0,9],
           [0  , 0  , 0  , 1  , 0   , 0.8],
           [0.6, 0  , 0.7, 0.9  , 0.65, 0.7],
           [0.6, 0  , 0.7, 0  , 0.65, 0.7]]
    import pandas as pd
    df = pd.read_csv(
        "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/Agreements/agreementTwoAreaRestrictedCovidBachelor.csv")
    minx = 0.033258873
    maxx = 1.315789474
    miny = 0#0#22679#0#3#0#5#0#1#0#1#0#34#0##/1000000
    maxy = 78#6#78#136191#0.012143858#56#32#82#21#17#24#35#50#22#42#60#18#37106.0#69468.0#78#6#78##/1000000
    matrix = []
    for i in range(len(df['List'])):
        strings = ((df['List'][i].replace("[", "")).replace("]", "")).split(",")
        values = []
        for item in strings:
            values.append(float(item))
        matrix.append(values)

    matrix2 = []
    for item in matrix:

        count = 0
        for i in range(len(item), 100):
            item.insert(count, 0)
            count += 1
        matrix2.append(item)
    count = 0

    for i in range(len(matrix), 100):
        vec = [0]*len(matrix2[0])
        matrix2.insert(count,vec)
        count += 1

    mat = matrix2
    print(len(matrix2),len(matrix2[0]))
    x_axis_size = 100
    y_axis_size = 100
    threshold = 0.001



    grid, grid_matrix = GridGenerator(minx, maxx, miny, maxy, x_axis_size, y_axis_size)
    alpha = 0.25
    obj = RectangularHotspotsFinder(threshold,x_axis_size,y_axis_size,mat, grid_matrix, alpha)
    hotspot_polygon = obj.getHotspots()
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    import geopandas as gpd

    for item in hotspot_polygon:
        #print(item.exterior.xy)
        p = gpd.GeoSeries(item)
        #print(p)
        p.plot(linewidth=0.8, ax=ax, edgecolor='red', color='r', facecolor="none")
    import numpy as np
    #plt.setp(ax, xlabel="Covid-19 Infection Rate", ylabel= "Median Income", yticks=[ 0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06], yticklabels=['0', '10', '20', '30', '40', '50', '60'])
    #plt.setp(ax, xlabel="Covid-19 Infection Rate", ylabel= "Median Income", yticks=[ 0.04, 0.05, 0.06, 0.07, 0.08, 0.09], yticklabels=['40000', '50000', '60000', '70000', '80000', '90000'])

    plt.show()


__main__()

#print(matrix)