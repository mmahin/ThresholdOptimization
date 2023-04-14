import geopandas as gpd
import pandas as pd
from SamplePointGenerationModule.GridHandler import GridGenerator
from AgreementFunction.PolygonAreaCalculation import PolygonArea
from VisualizationModules.HotspotsVisualization import HotspotsVisualiztion
from shapely.ops import unary_union
from SubModules.ObtainVariableDataframesAndStateDictionary import getVariableDataframesAndSpatialIndexes
from SubModules.AssignValuesToGridUsingPointWiseFunctions import AssignValuesToGridUsingPointWiseFunctions
from HotspotsUsingBFS import hotspotOfCellsUsingBFS
import pandas as pd
import shapely.wkt
from AgreementFunction.PolygonIntersectionVisualization import PolygonIntersectionVisualization
from AgreementFunction.agreementFunction import Agreement
import numpy as np
from SubModules.SearchThresholds.FindAlphaThreshold import FindAlphaThreshold
from SubModules.SearchThresholds.FindBetaThreshold import FindBetaThreshold
from SubModules.SearchThresholds.FindCloseThreshold import FindTargetThreshold
def FindHotspotsData(variable1_name ):
    data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'
    thresholds_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/VariableThresholds_.5_.01.csv'

    # Set Inputs
    # data access inputs
    df = pd.read_csv(data_path)
    geometries = []
    variable1_valuesList = []
    stateFIPSList = []
    StateFIPSDict = {}
    for count in range(len(df['FIPS'])):
        stateFIPS = int(df['FIPS'][count] / 1000)
        if stateFIPS in range(0, 57):
            # if stateFIPS == 4 or stateFIPS == 35 or stateFIPS == 40  or stateFIPS == 48:
            # if stateFIPS in range(0, 57):
            stateFIPSList.append(stateFIPS)
            new_polygon = shapely.wkt.loads(df['geometry'][count])
            new_polygon.simplify(0.01, preserve_topology=False)
            geometries.append(new_polygon.simplify(0.01, preserve_topology=False))
            variable1_valuesList.append(df[variable1_name][count])
            if stateFIPS not in StateFIPSDict.keys():
                StateFIPSDict[stateFIPS] = [count]
            else:
                StateFIPSDict[stateFIPS].append(count)
    variable1_df = pd.DataFrame()
    variable1_df['stateFIPS'] = stateFIPSList
    variable1_df['values'] = variable1_valuesList
    variable1_df['polygons'] = geometries


    thresholds_df = pd.read_csv(thresholds_path)
    variable1_thresholds = thresholds_df['Thresholds'][thresholds_df['Name'] == variable1_name].values[0]
    variable1_thresholds_strings = variable1_thresholds.split(",")
    threshold1_set = []
    for item in variable1_thresholds_strings:
        threshold1_set.append(float(item))

    # Grid generation Inputs
    grid_row_size = 100
    grid_column_size = 100


    # calculate total observation area
    polygones = []
    for polygon in variable1_df['polygons']:
        polygones.append(polygon)

    combined_observation_area_polygon = gpd.GeoSeries(unary_union(polygones))

    total_area = 0
    for polygon in combined_observation_area_polygon:
        area = PolygonArea(polygon)
        total_area += area

    # Create the observation grid
    bounds = combined_observation_area_polygon.bounds
    minx = (bounds['minx']).values
    miny = (bounds['miny']).values
    maxx = (bounds['maxx']).values
    maxy = (bounds['maxy']).values
    grid, grid_matrix = GridGenerator(minx, maxx, miny, maxy, grid_row_size, grid_column_size)

    variable1_path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/PointWiseGridValueForAllVariables/" + variable1_name + ".csv"
    # Assign values to grid points using polygonal function
    variable1_values = pd.read_csv(variable1_path)
    variable1_value_matrix = []
    for i in range(len(variable1_values['List'])):
        strings = ((variable1_values['List'][i].replace("[", "")).replace("]", "")).split(",")
        values = []
        j = 0
        for item in strings:
            values.append(float(item))
            j += 1
        variable1_value_matrix.append(values)

    threshold1s = []
    threshold1_areas = []
    threshold1Hotspots = []
    for threshold1 in threshold1_set:
        hotspots1 = hotspotOfCellsUsingBFS(threshold1, grid_row_size, grid_column_size, variable1_value_matrix, grid)
        Total_hotspot1_area = 0
        for polygon in hotspots1:
            area = PolygonArea(polygon)
            Total_hotspot1_area += area
        threshold1s.append(threshold1)
        threshold1_areas.append(Total_hotspot1_area/total_area)
        threshold1Hotspots.append(hotspots1)


    return threshold1s, threshold1Hotspots, threshold1_areas