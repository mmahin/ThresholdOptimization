from Dependencies.BFSofCellsSearchSpace import BFSofCells

from shapely.geometry import Polygon

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
    hotspotsPolygons = obj.getHotspots()


    return hotspotsPolygons


from SamplePointGenerationModule.GridHandler import GridGenerator
from shapely.geometry import Polygon, LineString, Point
import numpy as np

def max_rect(polygon):
    max_area = -1
    max_perimeter = -1
    max_rect_coords = None

    for i, coord1 in enumerate(polygon.exterior.coords[:-1]):
        for j, coord2 in enumerate(polygon.exterior.coords[i + 1:-1]):
            rect = LineString([coord1, coord2])
            if rect.length < max_perimeter:
                continue
            rect_width = 0
            rect_height = 0
            rect_area = 0
            for k, point in enumerate(polygon.exterior.coords):
                proj = rect.project(Point(point))
                proj_point = rect.interpolate(proj)
                dist = proj_point.distance(Point(point))
                if dist > rect_width:
                    rect_width = dist
                    if k > j:
                        rect_height = rect.length
                    else:
                        rect_height = LineString([coord2, point]).length
                if dist * rect.length > rect_area:
                    rect_area = dist * rect.length
                    max_perimeter = rect.length
                    max_rect_coords = [(coord1[0], coord1[1]), (coord2[0], coord2[1]),
                                       (coord2[0] + rect_height * (coord2[1] - coord1[1]) / rect.length,
                                        coord2[1] + rect_height * (coord1[0] - coord2[0]) / rect.length),
                                       (coord1[0] + rect_height * (coord2[1] - coord1[1]) / rect.length,
                                        coord1[1] + rect_height * (coord1[0] - coord2[0]) / rect.length)]
            if rect_area > max_area:
                max_area = rect_area

    return Polygon(max_rect_coords)

def __main__():
    mat = [[0.6, 1, 0, 0, 0, 0.6],
           [0, 0.7, 0, 0, 0.55, 0],
           [0.8, 0, 0, 0.7, 0.6, 0, 9],
           [0, 0, 0, 1, 0, 0.8],
           [0.6, 0, 0.7, 0.9, 0.65, 0.7],
           [0.6, 0, 0.7, 0, 0.65, 0.7]]
    import pandas as pd

    files = ["agreementNoAreaRestrictedWithTwoThresholdBachelorIncome0.75to0.1.csv",
             "agreementNoAreaRestrictedWithTwoThresholdBachelorPoverty0.75to0.1.csv",
             "agreementNoAreaRestrictedWithTwoThresholdCovidDeath0.75to0.1.csv",
             "agreementNoAreaRestrictedWithTwoThresholdCovidIncome0.75to0.1.csv",
             "agreementNoAreaRestrictedWithTwoThresholdCovidTemp0.75to0.1.csv",
             "agreementNoAreaRestrictedWithTwoThresholdIncomePoverty0.75to0.1.csv",
             "agreementNoAreaRestrictedWithTwoThresholdUnemploymentPoverty0.75to0.1.csv",
             "agreementTwoAreaRestrictedWithTwoThresholdHighLowCovidFire0.75to0.1.csv",
             "agreementTwoAreaRestrictedWithTwoThresholdHighLowCovidTech0.75to0.1.csv",
             "agreementTwoAreaRestrictedWithTwoThresholdHighLowCovidTrans0.75to0.1.csv",
             "agreementNoAreaRestrictedWithTwoThresholdCovidPoverty0.75to0.1.csv"]

    var1_mins = [0     , 0 , 0.03 , 0.03  , 0.03,22679 ,1 ,0.03,0.03,0.03, 0.03]
    var1_maxs = [78    , 78, 1.32 , 1.32  , 1.32,136191,18,1.32,1.32,1.32, 1.32]
    var2_mins = [22679 , 3 , 0    , 22679 , 34  ,3     ,3 ,0   ,0   ,0   , 3   ]
    var2_maxs = [136191, 56, 0.012, 136191, 78  ,56    ,56,21  ,17  ,24  , 56  ]

    var1_labels = ["Bachelor Degree Rate","Bachelor Degree Rate", "COVID-19 Infection Rate", "COVID-19 Infection Rate",
                   "COVID-19 Infection Rate", "Median Income", "Unemployment Rate", "COVID-19 Infection Rate",
                   "COVID-19 Infection Rate", "COVID-19 Infection Rate", "COVID-19 Infection Rate"]
    var2_labels = ["Median Income", "Poverty Rate", "COVID-19 Death Rate", "Median Income", "Average Temperature",
                   "Poverty Rate", "Poverty Rate", "Fire-Service Employee Rate", "Technology Employee Rate",
                   "Transportation Employee Rate", "Poverty Rate"]
    # files = ["agreementNoAreaRestrictedWithTwoThresholdCovidBachelor.csv",
    #            "agreementNoAreaRestrictedWithTwoThresholdCovidIncome.csv"]

    # var1_mins = [0.03, 0.03]
    # var1_maxs = [0.45, 0.5]
    # var2_mins = [0, 22679]
    # var2_maxs = [65, 100000]
    for count in range(len(files)):
        print("\n", count, files[count], "\n")
        path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/TKDE/Agreements/Files/Specific/" + \
               files[count]
        # path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/TKDE/Agreements/Files/" + \
        #       files[count]
        df = pd.read_csv(path)
        minx = var1_mins[count]
        maxx = var1_maxs[count]
        miny = var2_mins[count] #* 10 / (var2_maxs[count])
        maxy = var2_maxs[count] #* 10 / (var2_maxs[count])
        print(minx,maxx,miny,maxy)
        alpha = (maxx-minx)/(maxy-miny)
        if alpha < 0:
            alpha = 1
        matrix = []
        maxima = 0
        maxima_x = 0
        maxima_y = 0
        count_t = 0
        area_under_the_curve = 0
        for i in range(len(df['List'])):
            strings = ((df['List'][i].replace("[", "")).replace("]", "")).split(",")
            values = []
            j = 0
            for item in strings:
                if float(item) >= 0:
                    area_under_the_curve += float(item)
                    count_t += 1
                if float(item) > maxima:
                    maxima =float(item)
                    maxima_x = i
                    maxima_y = j

                values.append(float(item))
                j += 1
            matrix.append(values)
        if count_t == 0:
            count_t = 100000000000000000000
        matrix2 = []
        for item in matrix:

            count_x = 0
            for i in range(len(item), 100):
                item.insert(count_x, 0)
                count_x += 1
            matrix2.append(item)
        count_x = 0

        for i in range(len(matrix), 100):
            vec = [0] * len(matrix2[0])
            matrix2.insert(count_x, vec)
            count_x += 1

        mat = matrix2
        print(len(matrix2), len(matrix2[0]))
        x_axis_size = 100
        y_axis_size = 100
        threshold = 0.5

        grid, grid_matrix = GridGenerator(minx, maxx, miny, maxy, x_axis_size, y_axis_size)
        hotspot_polygon = hotspotOfCellsUsingBFS(threshold, x_axis_size, y_axis_size, mat, grid)

        print("maxima:", maxima, (grid_matrix[maxima_x][maxima_y]).xy, area_under_the_curve/count_t)

        # find 5 x tics
        start = minx
        cut_point = (maxx - minx) / 6
        x_points = []
        while start <= maxx:
            x_points.append(start)
            start += cut_point

        # find 5 y labels
        x_labels = []
        for point in x_points:
            point = round(point,1)
            x_labels.append(str(point))


        # find 5 y tics
        start = miny
        cut_point = (maxy-miny)/9
        y_points = []
        while start <= maxy:
            y_points.append(start)
            start += cut_point

        # find 5 y labels
        y_labels = []
        for point in y_points:
            point = round(point,1)
            y_labels.append(str(point))

        print(y_labels)
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 1, figsize=(6, 6))
        import geopandas as gpd

        for item in hotspot_polygon:
            # print(item.exterior.xy)
            ''''''
            minx, miny, maxx, maxy = item.bounds
            print(minx, miny, maxx, maxy)
            polygon = Polygon([(minx, miny), (maxx, miny), (maxx, maxy), (minx, maxy)])
            p = gpd.GeoSeries(polygon)
        

            # print(p)
            p.plot(linewidth=0.8, ax=ax, edgecolor='red', color='r', facecolor="none")


        xlabel = var1_labels[count]
        ylabel = var2_labels[count]
        import numpy as np
        #plt.setp(ax, xlabel=xlabel, xticks=x_points,
        #         xticklabels=x_labels, ylabel=ylabel, yticks=y_points,
        #         yticklabels=y_labels)

        ax.set_xlim(minx, maxx)
        ax.set_ylim(miny, maxy)
        ax.set_xticks(x_points)
        ax.set_xticklabels(x_labels)
        ax.set_yticks(y_points)
        ax.set_yticklabels(y_labels)
        ax.tick_params(axis='both', which='major', labelsize=8)
        ax.set_xlabel(xlabel=xlabel, fontsize=10)
        ax.set_ylabel(ylabel=ylabel, fontsize=10)
        ax.set_aspect(alpha)
        # plt.setp(ax, xlabel="Covid-19 Infection Rate", ylabel= "Median Income", yticks=[ 0.04, 0.05, 0.06, 0.07, 0.08, 0.09], yticklabels=['40000', '50000', '60000', '70000', '80000', '90000'])

        plt.show()

__main__()