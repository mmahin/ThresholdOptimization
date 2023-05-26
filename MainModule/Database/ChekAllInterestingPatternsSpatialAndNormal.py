import sqlite3
import pickle
import pandas as pd
from scipy.stats import pearsonr
# connect to the database
data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'
df = pd.read_csv(data_path)
# connect to the database
conn = sqlite3.connect('hotspots_50_1.db')
# create a cursor object
c = conn.cursor()

variable_names = ['UnempRate2018',"avg_precipitation_for_county","PctEmpInformation","PctEmpFIRE","PctEmpTrans","PctEmpConstruction",
                  "PctEmpTrade","PctEmpGovt","PctEmpMining","avg_temp_for_county","PctEmpAgriculture","PctEmpServices",
                  "PctEmpManufacturing","povertyRate","bachelor_degree_density_2014_2018","medianHouseHoldIncome",
                  "covid_cases_density","covid_death_density","population_density_on_land_2010","household_density_on_land_2010"]

#already_completed = ["UnempRate2018_avg_precipitation_for_county","UnempRate2018_PctEmpInformation","UnempRate2018_PctEmpFIRE","UnempRate2018_PctEmpTrans","UnempRate2018_PctEmpConstruction","UnempRate2018_PctEmpTrade","UnempRate2018_PctEmpGovt","UnempRate2018_PctEmpMining","UnempRate2018_avg_temp_for_county","UnempRate2018_PctEmpAgriculture","UnempRate2018_PctEmpServices","UnempRate2018_PctEmpManufacturing","UnempRate2018_povertyRate","UnempRate2018_bachelor_degree_density_2014_2018","UnempRate2018_medianHouseHoldIncome","UnempRate2018_covid_cases_density","UnempRate2018_covid_death_density","UnempRate2018_population_density_on_land_2010","UnempRate2018_household_density_on_land_2010"
#                     ,'avg_precipitation_for_county_PctEmpInformation','avg_precipitation_for_county_PctEmpFIRE','avg_precipitation_for_county_PctEmpTrans','avg_precipitation_for_county_PctEmpConstruction','avg_precipitation_for_county_PctEmpTrade','avg_precipitation_for_county_PctEmpGovt','avg_precipitation_for_county_PctEmpMining','avg_precipitation_for_county_avg_temp_for_county','avg_precipitation_for_county_PctEmpAgriculture','avg_precipitation_for_county_PctEmpServices','avg_precipitation_for_county_PctEmpManufacturing','avg_precipitation_for_county_povertyRate' ,'avg_precipitation_for_county_bachelor_degree_density_2014_2018','avg_precipitation_for_county_medianHouseHoldIncome','avg_precipitation_for_county_covid_cases_density','avg_precipitation_for_county_covid_death_density','avg_precipitation_for_county_population_density_on_land_2010','avg_precipitation_for_county_household_density_on_land_2010'
#                    , 'PctEmpInformation_PctEmpFIRE','PctEmpInformation_PctEmpTrans','PctEmpInformation_PctEmpConstruction','PctEmpInformation_PctEmpTrade','PctEmpInformation_PctEmpGovt','PctEmpInformation_PctEmpMining','PctEmpInformation_avg_temp_for_county','PctEmpInformation_PctEmpAgriculture','PctEmpInformation_PctEmpServices','PctEmpInformation_PctEmpManufacturing','PctEmpInformation_povertyRate','PctEmpInformation_bachelor_degree_density_2014_2018','PctEmpInformation_medianHouseHoldIncome','PctEmpInformation_covid_cases_density','PctEmpInformation_covid_death_density','PctEmpInformation_population_density_on_land_2010','PctEmpInformation_household_density_on_land_2010','PctEmpFIRE_PctEmpTrans','PctEmpFIRE_PctEmpConstruction','PctEmpFIRE_PctEmpTrade','PctEmpFIRE_PctEmpGovt','PctEmpFIRE_PctEmpMining','PctEmpFIRE_avg_temp_for_county','PctEmpFIRE_PctEmpAgriculture','PctEmpFIRE_PctEmpServices','PctEmpFIRE_PctEmpManufacturing','PctEmpFIRE_povertyRate','PctEmpFIRE_bachelor_degree_density_2014_2018','PctEmpFIRE_medianHouseHoldIncome','PctEmpFIRE_covid_cases_density','PctEmpFIRE_covid_death_density','PctEmpFIRE_population_density_on_land_2010','PctEmpFIRE_household_density_on_land_2010','PctEmpTrans_PctEmpConstruction','PctEmpTrans_PctEmpTrade','PctEmpTrans_PctEmpGovt','PctEmpTrans_PctEmpMining','PctEmpTrans_avg_temp_for_county','PctEmpTrans_PctEmpAgriculture','PctEmpTrans_PctEmpServices','PctEmpTrans_PctEmpManufacturing','PctEmpTrans_povertyRate','PctEmpTrans_bachelor_degree_density_2014_2018','PctEmpTrans_medianHouseHoldIncome','PctEmpTrans_covid_cases_density','PctEmpTrans_covid_death_density','PctEmpTrans_population_density_on_land_2010','PctEmpTrans_household_density_on_land_2010','PctEmpConstruction_PctEmpTrade','PctEmpConstruction_PctEmpGovt','PctEmpConstruction_PctEmpMining','PctEmpConstruction_avg_temp_for_county','PctEmpConstruction_PctEmpAgriculture','PctEmpConstruction_PctEmpServices','PctEmpConstruction_PctEmpManufacturing','PctEmpConstruction_povertyRate','PctEmpConstruction_bachelor_degree_density_2014_2018','PctEmpConstruction_medianHouseHoldIncome','PctEmpConstruction_covid_cases_density','PctEmpConstruction_covid_death_density','PctEmpConstruction_population_density_on_land_2010','PctEmpConstruction_household_density_on_land_2010','PctEmpTrade_PctEmpGovt','PctEmpTrade_PctEmpMining','PctEmpTrade_avg_temp_for_county','PctEmpTrade_PctEmpAgriculture','PctEmpTrade_PctEmpServices','PctEmpTrade_PctEmpManufacturing','PctEmpTrade_povertyRate','PctEmpTrade_bachelor_degree_density_2014_2018','PctEmpTrade_medianHouseHoldIncome','PctEmpTrade_covid_cases_density','PctEmpTrade_covid_death_density','PctEmpTrade_population_density_on_land_2010','PctEmpTrade_household_density_on_land_2010','PctEmpGovt_PctEmpMining','PctEmpGovt_avg_temp_for_county','PctEmpGovt_PctEmpAgriculture','PctEmpGovt_PctEmpServices','PctEmpGovt_PctEmpManufacturing','PctEmpGovt_povertyRate','PctEmpGovt_bachelor_degree_density_2014_2018','PctEmpGovt_medianHouseHoldIncome','PctEmpGovt_covid_cases_density','PctEmpGovt_covid_death_density','PctEmpGovt_population_density_on_land_2010','PctEmpGovt_household_density_on_land_2010','PctEmpMining_avg_temp_for_county','PctEmpMining_PctEmpAgriculture','PctEmpMining_PctEmpServices','PctEmpMining_PctEmpManufacturing','PctEmpMining_povertyRate','PctEmpMining_bachelor_degree_density_2014_2018','PctEmpMining_medianHouseHoldIncome','PctEmpMining_covid_cases_density','PctEmpMining_covid_death_density','PctEmpMining_population_density_on_land_2010','PctEmpMining_household_density_on_land_2010','avg_temp_for_county_PctEmpAgriculture','avg_temp_for_county_PctEmpServices','avg_temp_for_county_PctEmpManufacturing','avg_temp_for_county_povertyRate','avg_temp_for_county_bachelor_degree_density_2014_2018','avg_temp_for_county_medianHouseHoldIncome','avg_temp_for_county_covid_cases_density','avg_temp_for_county_covid_death_density','avg_temp_for_county_population_density_on_land_2010','avg_temp_for_county_household_density_on_land_2010','PctEmpAgriculture_PctEmpServices','PctEmpAgriculture_PctEmpManufacturing','PctEmpAgriculture_povertyRate','PctEmpAgriculture_bachelor_degree_density_2014_2018','PctEmpAgriculture_medianHouseHoldIncome','PctEmpAgriculture_covid_cases_density','PctEmpAgriculture_covid_death_density','PctEmpAgriculture_population_density_on_land_2010','PctEmpAgriculture_household_density_on_land_2010','PctEmpServices_PctEmpManufacturing','PctEmpServices_povertyRate','PctEmpServices_bachelor_degree_density_2014_2018','PctEmpServices_medianHouseHoldIncome','PctEmpServices_covid_cases_density','PctEmpServices_covid_death_density','PctEmpServices_population_density_on_land_2010','PctEmpServices_household_density_on_land_2010','PctEmpManufacturing_povertyRate','PctEmpManufacturing_bachelor_degree_density_2014_2018','PctEmpManufacturing_medianHouseHoldIncome','PctEmpManufacturing_covid_cases_density','PctEmpServices_covid_death_density','PctEmpServices_population_density_on_land_2010','PctEmpServices_household_density_on_land_2010','PctEmpManufacturing_povertyRate','PctEmpManufacturing_bachelor_degree_density_2014_2018','PctEmpManufacturing_medianHouseHoldIncome','PctEmpManufacturing_covid_cases_density','PctEmpManufacturing_covid_death_density','PctEmpManufacturing_population_density_on_land_2010','PctEmpManufacturing_household_density_on_land_2010','povertyRate_bachelor_degree_density_2014_2018'
#                      ]
def find_matching_pairs(t1, t2, t3, t4):
    # Create a dictionary to store elements from t1 and their indices
    dictionary = {}
    for i, elem in enumerate(t1):
        dictionary[elem] = i

    matching_pairs = []
    for j, elem in enumerate(t3):
        if elem in dictionary:
            i = dictionary[elem]
            if t2[i] == t4[j]:
                matching_pairs.append((i, j))

    return matching_pairs
patterns = []
threhsold1_imp_agreement = []
threhsold2_imp_agreement = []
imp_agreement = []
threhsold1_imp_agreement_area_cover = []
threhsold2_imp_agreement_area_cover  = []
imp_agreement_expected = []
imp_agreement_lift = []

count = 0
l = 1
threshold_area_dict = {}
for variable1_name in variable_names:

    for k in range(l,len(variable_names)):

        variable2_name = variable_names[k]
        if variable1_name not in threshold_area_dict.keys():
            c.execute(f'SELECT * FROM {variable1_name}')
            rows = c.fetchall()
            threshold_area_dict[variable1_name] = {}
            for row in rows:
                threshold_area_dict[variable1_name][str(float(row[1]))] = row[3]
        if variable2_name not in threshold_area_dict.keys():
            c.execute(f'SELECT * FROM {variable2_name}')
            rows = c.fetchall()
            threshold_area_dict[variable2_name] = {}
            for row in rows:
                threshold_area_dict[variable2_name][str(float(row[1]))] = row[3]
                
        table_name = variable1_name+"_"+variable2_name
        table2_name = "Matching_Correlation_" + variable1_name + "_" + variable2_name
        print(table2_name)
        if variable1_name != variable2_name:# and table_name  in already_completed:


            c.execute(f'SELECT * FROM {table_name}')
            rows = c.fetchall()

            # print the rows
            threshold1_set = []
            threshold2_set = []
            agreement_set = []
            expected_set = []
            lift_set = []
            for row in rows:
                threshold1_set.append(row[1])
                threshold2_set.append(row[2])
                agreement_set.append(row[3])
                expected_set.append(row[4])
                lift_set.append(row[3]/row[4])
            #pattern.append(table_name)

            c.execute(f"DROP TABLE IF EXISTS {table2_name}")
            c.execute(f'''CREATE TABLE IF NOT EXISTS {table2_name}
                                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                     threshold1 REAL,
                                     threshold2 REAL,
                                     threshold1_coverage_spatial REAL,
                                     threshold1_coverage_normal REAL,
                                     threshold2_coverage_spatial REAL,
                                     threshold2_coverage_normal REAL,
                                     agreement REAL,
                                     expected_agreement REAL,
                                     lift REAL,
                                     correlation_coverage REAL,
                                     correlation REAL,
                                     pval REAL);''')

            df[variable1_name].fillna(int(df[variable1_name].mean()), inplace=True)
            variable1_values = df[variable1_name]
            df[variable2_name].fillna(int(df[variable2_name].mean()), inplace=True)
            variable2_values = df[variable2_name]

            for i in range(len(threshold1_set)):
                threshold1 = threshold1_set[i]
                threshold2 = threshold2_set[i]
                selected_variable1_values = []
                selected_variable2_values = []

                for k in range(len(variable1_values)):
                    if variable1_values[k]>= threshold1 and variable2_values[k]>= threshold2:
                        selected_variable1_values.append(variable1_values[k])
                        selected_variable2_values.append(variable2_values[k])
                coverage = len(selected_variable1_values)/len(variable1_values)
                if coverage <= 0.5 and coverage >= 0.01:
                    corr, pval = pearsonr(selected_variable1_values, selected_variable2_values)
                    if corr is not None:
                        conn.execute(f"INSERT INTO {table2_name} (threshold1, threshold2, threshold1_coverage_spatial,"
                                     f"threshold1_coverage_normal, threshold2_coverage_spatial, threshold2_coverage_normal,"
                                     f"agreement, expected_agreement, lift, correlation_coverage, correlation, pval"
                                     f") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                             (float(threshold1), float(threshold2), float(threshold_area_dict[variable1_name][str(threshold1)]),
                              float(coverage), float(threshold_area_dict[variable2_name][str(threshold2)]),
                              float(coverage), float(agreement_set[i]), float(expected_set[i]), float(lift_set[i]),float(coverage),
                              float(corr), float(pval)))

                        # Commit the changes
                        conn.commit()

            count += len(agreement_set)
    l += 1
print("total pattern:",count)
'''
import pandas as pd
df = pd.DataFrame()
df['pattern'] = patterns
df['imp_agreement'] = imp_agreement
df['imp_agreement_expected'] = imp_agreement_expected
df['threhsold1_imp_agreement'] = threhsold1_imp_agreement
df['threhsold2_imp_agreement'] = threhsold2_imp_agreement
df['threhsold1_imp_agreement_area_cover'] = threhsold1_imp_agreement_area_cover
df['threhsold2_imp_agreement_area_cover'] = threhsold2_imp_agreement_area_cover
df['pattern_lift'] = imp_agreement_lift
path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/TKDE/Agreements/Files/All/data_all_v2.csv"
df.to_csv(path,index=False)
'''