import geopandas as gpd
from SamplePointGenerationModule.GridHandler import GridGenerator
from AgreementFunction.PolygonAreaCalculation import PolygonArea
from VisualizationModules.HotspotsVisualization import HotspotsVisualiztion
from shapely.ops import unary_union
from SubModules.ObtainVariableDataframesAndStateDictionary import getVariableDataframesAndSpatialIndexes
from SubModules.AssignValuesToGridUsingPointWiseFunctions import AssignValuesToGridUsingPointWiseFunctions
from HotspotsUsingBFS import hotspotOfCellsUsingBFS
from AgreementFunction.PolygonIntersectionVisualization import PolygonIntersectionVisualization
from AgreementFunction.agreementFunction import Agreement
data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'

variable2_manes = ['avg_precipitation_for_county', 'avg_temp_for_county','population_density_on_land_2010', 'household_density_on_land_2010',
                    'UnempRate2018', 'PctEmpAgriculture', 'PctEmpMining', 'PctEmpConstruction', 'PctEmpManufacturing', 'PctEmpTrade', 'PctEmpTrans',
                    'PctEmpInformation', 'PctEmpFIRE', 'PctEmpServices','PctEmpGovt','medianHouseHoldIncome', 'povertyRate',
                   'covid_death_density']
Medians_without_covid_infection = [3, 55, 45, 21, 3, 2, 0, 6, 11, 13, 5, 1, 4, 42, 4, 48711, 14, 0.0037]
for count in range(len(variable2_manes)):
    #Set Inputs
    #data access inputs
    variable1_name = 'covid_cases_density'
    variable2_name = variable2_manes[count]

    variable1_df, variable2_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)

    # Grid generation Inputs
    grid_row_size = 100
    grid_column_size = 100



    # calculate total observation area
    polygones = []
    for polygon in variable1_df['polygons']:
        polygones.append(polygon)

    combined_observation_area_polygon = gpd.GeoSeries(unary_union(polygones))


    # Create the observation grid
    bounds = combined_observation_area_polygon.bounds
    minx = (bounds['minx']).values
    miny = (bounds['miny']).values
    maxx = (bounds['maxx']).values
    maxy = (bounds['maxy']).values


    grid, grid_matrix = GridGenerator(minx, maxx, miny, maxy, grid_row_size, grid_column_size)

    # Assign values to grid points using polygonal function
    variable1_value_matrix, variable2_value_matrix =  AssignValuesToGridUsingPointWiseFunctions(grid_matrix, variable1_df, variable2_df, StateFIPSDict)

    # Find  valid thresholds and agreement values



    Covid_median = 0.25

    threshold1 = Covid_median
    threshold2 = Medians_without_covid_infection[count]
    hotspots1 = hotspotOfCellsUsingBFS(threshold1, grid_row_size, grid_column_size, variable1_value_matrix, grid)

    hotspots2 = hotspotOfCellsUsingBFS(threshold2, grid_row_size, grid_column_size, variable2_value_matrix, grid)

    intersection_hotspots = PolygonIntersectionVisualization(hotspots1,hotspots2)

    agreement = Agreement(hotspots1, hotspots2)
    print(variable2_name, threshold1, threshold2,agreement)
    #HotspotsVisualiztion(hotspots1, combined_observation_area_polygon)
    #HotspotsVisualiztion(hotspots2, combined_observation_area_polygon)
    #HotspotsVisualiztion(intersection_hotspots, combined_observation_area_polygon)
