import sqlite3
import pandas as pd
from scipy.stats import pearsonr
# connect to the database
data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'
df = pd.read_csv(data_path)

conn = sqlite3.connect('hotspots_50_1.db')
variable_names = ['UnempRate2018',"avg_precipitation_for_county","PctEmpInformation","PctEmpFIRE","PctEmpTrans","PctEmpConstruction",
                  "PctEmpTrade","PctEmpGovt","PctEmpMining","avg_temp_for_county","PctEmpAgriculture","PctEmpServices",
                  "PctEmpManufacturing","povertyRate","bachelor_degree_density_2014_2018","medianHouseHoldIncome",
                  "covid_cases_density","covid_death_density","population_density_on_land_2010","household_density_on_land_2010"]

already_completed = []
# create a cursor object
c = conn.cursor()
l = 0
alpha = 0.5
beta = 0.01
for variable1_name in variable_names:
    for k in range(l,len(variable_names)):

        variable2_name = variable_names[k]
        table_name = "Correlation_"+variable1_name + "_" + variable2_name

        if variable1_name != variable2_name and table_name not in already_completed:
            c.execute(f"DROP TABLE IF EXISTS {table_name}")
            c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         threshold1 REAL,
                         threshold2 REAL,
                         coverage REAL,
                         correlation REAL,
                         pval REAL);''')

            df[variable1_name].fillna(int(df[variable1_name].mean()), inplace=True)
            variable1_values = df[variable1_name]
            temp_unique_values_var1 = pd.unique(df[variable1_name])
            threshold1_set = []
            if len(temp_unique_values_var1) >= 200:
                cutpoint = int(len(temp_unique_values_var1)/200)
                start = 0
                while start <= len(temp_unique_values_var1):
                    threshold1_set.append(temp_unique_values_var1[start])
                    start += cutpoint
            else:
                threshold1_set = temp_unique_values_var1

            df[variable2_name].fillna(int(df[variable2_name].mean()), inplace=True)
            variable2_values = df[variable2_name]
            temp_unique_values_var2 = pd.unique(df[variable2_name])
            threshold2_set = []
            if len(temp_unique_values_var2) >= 200:
                cutpoint = int(len(temp_unique_values_var2) / 200)
                start = 0
                while start <= len(temp_unique_values_var2):
                    threshold2_set.append(temp_unique_values_var2[start])
                    start += cutpoint
            else:
                threshold2_set = temp_unique_values_var2


            for i in range(len(threshold1_set)):
                for j in range(len(threshold2_set)):
                    threshold1 = variable1_values[i]
                    threshold2 = variable2_values[j]
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
                            conn.execute(f"INSERT INTO {table_name} (threshold1, threshold2, coverage, correlation, pval) VALUES (?, ?, ?, ?, ?)",
                                 (float(threshold1), float(threshold2), float(coverage), float(corr), float(pval)))

                            # Commit the changes
                            conn.commit()



            print(table_name)

    l += 1
# close the cursor and database connection
c.close()
conn.close()
