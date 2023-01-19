import geopandas as gpd
from SamplePointGenerationModule.GridHandler import GridGenerator
from shapely.ops import unary_union
from SubModules.ObtainVariableDataframesAndStateDictionary import getVariableDataframesAndSpatialIndexes
from SubModules.AssignValuesToGridUsingPointWiseFunctions import AssignValuesToGridUsingPointWiseFunctions
from SubModules.VisualizeOneVariableInterestingnessSearchSpace import VisualizeOneVariableInterestingnessSearchSpace
from SubModules.AgreementValueGeneratorForOneThreshold import AgreementValueGeneratorForOneThreshold

data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'

#Set Inputs
#data access inputs
variable1_name = 'covid_cases_density'
variable2_name = 'population_density_on_land_2010'

names = ["bachelor_degree_density_2014_2018", "avg_precipitation_for_county", "avg_temp_for_county", "population_density_on_land_2010",\
          "household_density_on_land_2010", "UnempRate2018", "PctEmpAgriculture", "PctEmpMining", "PctEmpConstruction", "PctEmpManufacturing",\
          "PctEmpTrade", "PctEmpTrans", "PctEmpInformation", "PctEmpFIRE", "PctEmpServices", "PctEmpGovt", "medianHouseHoldIncome",\
           "povertyRate", "covid_death_density"]
for variable2_name in names:
    covid_case_rates_df, medianIncome_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(data_path, variable1_name, variable2_name)

    # Grid generation Inputs
    grid_row_size = 100
    grid_column_size = 100


    # Agreement Generation Inputs
    steps = 150

    # Create thresholds min and gradient
    max_MedianIncome2018 = max(medianIncome_df['values'])
    min_MedianIncome2018 = min(medianIncome_df['values'])
    variable_cutpoint_MedianIncome2018 = (max_MedianIncome2018 - min_MedianIncome2018)/steps

    covid_case_rates_threshold = 0.3


    # Visualization Inputs
    X_label = 'Median Income(t\')'
    Y_label = '$I_{(Covid-19\ Infection\ Rate, 0.3),(Median\ Income, t\'))}$'

    # calculate total observation area
    polygones = []
    for polygon in covid_case_rates_df['polygons']:
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
    #covid_case_rates_value_matrix, medianIncome_value_matrix =  AssignValuesToGridUsingPointWiseFunctions(grid_matrix, covid_case_rates_df, medianIncome_df, StateFIPSDict)
    from PolygonalFunction import PolygonalValueEstimation
    medianIncome_value_matrix = []
    covid_case_rates_value_matrix = []
    count = 0
    for row in grid_matrix:
        median_income_row_values = []
        covid_case_rates_row_values = []
        for point in row:
            value_median_income = PolygonalValueEstimation(point, medianIncome_df)
            value_covid_case_rates = PolygonalValueEstimation(point, covid_case_rates_df)
            median_income_row_values.append(value_median_income)
            covid_case_rates_row_values.append(value_covid_case_rates)
            #print(count ,value_unemployment, value_median_income)
            count += 1
        medianIncome_value_matrix.append(median_income_row_values)
        covid_case_rates_value_matrix.append(covid_case_rates_row_values)

    # Find  valid thresholds and agreement values
    threshold2_values, agreements = AgreementValueGeneratorForOneThreshold(covid_case_rates_threshold,
                                                            min_MedianIncome2018,variable_cutpoint_MedianIncome2018,
                                                         covid_case_rates_value_matrix,medianIncome_value_matrix,grid_row_size,
                                                         grid_column_size, grid, steps)
    print(variable2_name, len(agreements), round(sum(agreements)/len(agreements),3),round(max(agreements),3),round(threshold2_values[agreements.index(max(agreements))],3) )
'''

import pandas as pd
agreement_df = pd.DataFrame()
agreement_df['thresholds'] = threshold2_values
agreement_df['agreements'] = agreements

agreement_df.to_csv("Covid-19_median_income_agreements_one_threshold.csv")
# Visualize the agreement search space
VisualizeOneVariableInterestingnessSearchSpace(threshold2_values, agreements, X_label, Y_label)
'''