import pandas as pd
import shapely.wkt
file_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'
variable1_name = 'covid_cases_density'
variable2_name = 'medianHouseHoldIncome'

def getVariableDataframesAndSpatialIndexes(file_path, variable1_name, variable2_name):
    df = pd.read_csv(file_path)
    geometries = []
    variable1_valuesList = []
    variable2_valuesList = []
    stateFIPSList = []
    StateFIPSDict = {}
    for count in range(len(df['FIPS'])):
        stateFIPS = int(df['FIPS'][count]/1000)
        #if stateFIPS in range(0,57):
        #if stateFIPS == 4 or stateFIPS == 35 or stateFIPS == 40  or stateFIPS == 48:
        if stateFIPS in range(0, 57):
            stateFIPSList.append(stateFIPS)
            new_polygon = shapely.wkt.loads(df['geometry'][count])
            new_polygon.simplify(0.01, preserve_topology=False)
            geometries.append(new_polygon.simplify(0.01, preserve_topology=False))
            variable1_valuesList.append(df[variable1_name][count])
            variable2_valuesList.append(df[variable2_name][count])
            if stateFIPS not in StateFIPSDict.keys():
                StateFIPSDict[stateFIPS] = [count]
            else:
                StateFIPSDict[stateFIPS].append(count)


    variable1_df = pd.DataFrame()
    variable2_df = pd.DataFrame()

    variable1_df['stateFIPS'] = stateFIPSList
    variable1_df['values'] = variable1_valuesList
    variable1_df['polygons'] = geometries

    variable2_df['stateFIPS'] = stateFIPSList
    variable2_df['values'] = variable2_valuesList
    variable2_df['polygons'] = geometries

    return variable1_df, variable2_df, StateFIPSDict
#covid_case_rates_df, medianIncome_df, StateFIPSDict = getVariableDataframesAndSpatialIndexes(file_path, variable1_name, variable2_name)
#print(covid_case_rates_df, medianIncome_df, StateFIPSDict)