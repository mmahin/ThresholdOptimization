import sqlite3
import pickle
import pandas as pd
from scipy.stats import pearsonr
# connect to the database
conn = sqlite3.connect('hotspots_50_1.db')
# create a cursor object
c = conn.cursor()
data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'
df = pd.read_csv(data_path)
variable_names = ['UnempRate2018',"avg_precipitation_for_county","PctEmpInformation","PctEmpFIRE","PctEmpTrans","PctEmpConstruction",
                  "PctEmpTrade","PctEmpGovt","PctEmpMining","avg_temp_for_county","PctEmpAgriculture","PctEmpServices",
                  "PctEmpManufacturing","povertyRate","bachelor_degree_density_2014_2018","medianHouseHoldIncome",
                  "covid_cases_density","covid_death_density","population_density_on_land_2010","household_density_on_land_2010"]

#already_completed = ["UnempRate2018_avg_precipitation_for_county","UnempRate2018_PctEmpInformation","UnempRate2018_PctEmpFIRE","UnempRate2018_PctEmpTrans","UnempRate2018_PctEmpConstruction","UnempRate2018_PctEmpTrade","UnempRate2018_PctEmpGovt","UnempRate2018_PctEmpMining","UnempRate2018_avg_temp_for_county","UnempRate2018_PctEmpAgriculture","UnempRate2018_PctEmpServices","UnempRate2018_PctEmpManufacturing","UnempRate2018_povertyRate","UnempRate2018_bachelor_degree_density_2014_2018","UnempRate2018_medianHouseHoldIncome","UnempRate2018_covid_cases_density","UnempRate2018_covid_death_density","UnempRate2018_population_density_on_land_2010","UnempRate2018_household_density_on_land_2010"
#                     ,'avg_precipitation_for_county_PctEmpInformation','avg_precipitation_for_county_PctEmpFIRE','avg_precipitation_for_county_PctEmpTrans','avg_precipitation_for_county_PctEmpConstruction','avg_precipitation_for_county_PctEmpTrade','avg_precipitation_for_county_PctEmpGovt','avg_precipitation_for_county_PctEmpMining','avg_precipitation_for_county_avg_temp_for_county','avg_precipitation_for_county_PctEmpAgriculture','avg_precipitation_for_county_PctEmpServices','avg_precipitation_for_county_PctEmpManufacturing','avg_precipitation_for_county_povertyRate' ,'avg_precipitation_for_county_bachelor_degree_density_2014_2018','avg_precipitation_for_county_medianHouseHoldIncome','avg_precipitation_for_county_covid_cases_density','avg_precipitation_for_county_covid_death_density','avg_precipitation_for_county_population_density_on_land_2010','avg_precipitation_for_county_household_density_on_land_2010'
#                    , 'PctEmpInformation_PctEmpFIRE','PctEmpInformation_PctEmpTrans','PctEmpInformation_PctEmpConstruction','PctEmpInformation_PctEmpTrade','PctEmpInformation_PctEmpGovt','PctEmpInformation_PctEmpMining','PctEmpInformation_avg_temp_for_county','PctEmpInformation_PctEmpAgriculture','PctEmpInformation_PctEmpServices','PctEmpInformation_PctEmpManufacturing','PctEmpInformation_povertyRate','PctEmpInformation_bachelor_degree_density_2014_2018','PctEmpInformation_medianHouseHoldIncome','PctEmpInformation_covid_cases_density','PctEmpInformation_covid_death_density','PctEmpInformation_population_density_on_land_2010','PctEmpInformation_household_density_on_land_2010','PctEmpFIRE_PctEmpTrans','PctEmpFIRE_PctEmpConstruction','PctEmpFIRE_PctEmpTrade','PctEmpFIRE_PctEmpGovt','PctEmpFIRE_PctEmpMining','PctEmpFIRE_avg_temp_for_county','PctEmpFIRE_PctEmpAgriculture','PctEmpFIRE_PctEmpServices','PctEmpFIRE_PctEmpManufacturing','PctEmpFIRE_povertyRate','PctEmpFIRE_bachelor_degree_density_2014_2018','PctEmpFIRE_medianHouseHoldIncome','PctEmpFIRE_covid_cases_density','PctEmpFIRE_covid_death_density','PctEmpFIRE_population_density_on_land_2010','PctEmpFIRE_household_density_on_land_2010','PctEmpTrans_PctEmpConstruction','PctEmpTrans_PctEmpTrade','PctEmpTrans_PctEmpGovt','PctEmpTrans_PctEmpMining','PctEmpTrans_avg_temp_for_county','PctEmpTrans_PctEmpAgriculture','PctEmpTrans_PctEmpServices','PctEmpTrans_PctEmpManufacturing','PctEmpTrans_povertyRate','PctEmpTrans_bachelor_degree_density_2014_2018','PctEmpTrans_medianHouseHoldIncome','PctEmpTrans_covid_cases_density','PctEmpTrans_covid_death_density','PctEmpTrans_population_density_on_land_2010','PctEmpTrans_household_density_on_land_2010','PctEmpConstruction_PctEmpTrade','PctEmpConstruction_PctEmpGovt','PctEmpConstruction_PctEmpMining','PctEmpConstruction_avg_temp_for_county','PctEmpConstruction_PctEmpAgriculture','PctEmpConstruction_PctEmpServices','PctEmpConstruction_PctEmpManufacturing','PctEmpConstruction_povertyRate','PctEmpConstruction_bachelor_degree_density_2014_2018','PctEmpConstruction_medianHouseHoldIncome','PctEmpConstruction_covid_cases_density','PctEmpConstruction_covid_death_density','PctEmpConstruction_population_density_on_land_2010','PctEmpConstruction_household_density_on_land_2010','PctEmpTrade_PctEmpGovt','PctEmpTrade_PctEmpMining','PctEmpTrade_avg_temp_for_county','PctEmpTrade_PctEmpAgriculture','PctEmpTrade_PctEmpServices','PctEmpTrade_PctEmpManufacturing','PctEmpTrade_povertyRate','PctEmpTrade_bachelor_degree_density_2014_2018','PctEmpTrade_medianHouseHoldIncome','PctEmpTrade_covid_cases_density','PctEmpTrade_covid_death_density','PctEmpTrade_population_density_on_land_2010','PctEmpTrade_household_density_on_land_2010','PctEmpGovt_PctEmpMining','PctEmpGovt_avg_temp_for_county','PctEmpGovt_PctEmpAgriculture','PctEmpGovt_PctEmpServices','PctEmpGovt_PctEmpManufacturing','PctEmpGovt_povertyRate','PctEmpGovt_bachelor_degree_density_2014_2018','PctEmpGovt_medianHouseHoldIncome','PctEmpGovt_covid_cases_density','PctEmpGovt_covid_death_density','PctEmpGovt_population_density_on_land_2010','PctEmpGovt_household_density_on_land_2010','PctEmpMining_avg_temp_for_county','PctEmpMining_PctEmpAgriculture','PctEmpMining_PctEmpServices','PctEmpMining_PctEmpManufacturing','PctEmpMining_povertyRate','PctEmpMining_bachelor_degree_density_2014_2018','PctEmpMining_medianHouseHoldIncome','PctEmpMining_covid_cases_density','PctEmpMining_covid_death_density','PctEmpMining_population_density_on_land_2010','PctEmpMining_household_density_on_land_2010','avg_temp_for_county_PctEmpAgriculture','avg_temp_for_county_PctEmpServices','avg_temp_for_county_PctEmpManufacturing','avg_temp_for_county_povertyRate','avg_temp_for_county_bachelor_degree_density_2014_2018','avg_temp_for_county_medianHouseHoldIncome','avg_temp_for_county_covid_cases_density','avg_temp_for_county_covid_death_density','avg_temp_for_county_population_density_on_land_2010','avg_temp_for_county_household_density_on_land_2010','PctEmpAgriculture_PctEmpServices','PctEmpAgriculture_PctEmpManufacturing','PctEmpAgriculture_povertyRate','PctEmpAgriculture_bachelor_degree_density_2014_2018','PctEmpAgriculture_medianHouseHoldIncome','PctEmpAgriculture_covid_cases_density','PctEmpAgriculture_covid_death_density','PctEmpAgriculture_population_density_on_land_2010','PctEmpAgriculture_household_density_on_land_2010','PctEmpServices_PctEmpManufacturing','PctEmpServices_povertyRate','PctEmpServices_bachelor_degree_density_2014_2018','PctEmpServices_medianHouseHoldIncome','PctEmpServices_covid_cases_density','PctEmpServices_covid_death_density','PctEmpServices_population_density_on_land_2010','PctEmpServices_household_density_on_land_2010','PctEmpManufacturing_povertyRate','PctEmpManufacturing_bachelor_degree_density_2014_2018','PctEmpManufacturing_medianHouseHoldIncome','PctEmpManufacturing_covid_cases_density','PctEmpServices_covid_death_density','PctEmpServices_population_density_on_land_2010','PctEmpServices_household_density_on_land_2010','PctEmpManufacturing_povertyRate','PctEmpManufacturing_bachelor_degree_density_2014_2018','PctEmpManufacturing_medianHouseHoldIncome','PctEmpManufacturing_covid_cases_density','PctEmpManufacturing_covid_death_density','PctEmpManufacturing_population_density_on_land_2010','PctEmpManufacturing_household_density_on_land_2010','povertyRate_bachelor_degree_density_2014_2018'
#                      ]
CorrelationPatterns = []
threhsold1_imp_agreement = []
threhsold2_imp_agreement = []
coverages = []
correlations = []
pvlues = []
correlation_full = []
pval_full = []
AUC = []
count = 0
l = 1
for variable1_name in variable_names:

    for k in range(l,len(variable_names)):
        variable2_name = variable_names[k]
        table_name = "Correlation_"+variable1_name + "_" + variable2_name

        if variable1_name != variable2_name:# and table_name  in already_completed:


            c.execute(f'SELECT * FROM {table_name}')
            rows = c.fetchall()

            # print the rows
            threshold1_set = []
            threshold2_set = []
            coverage_set = []
            correlation_set = []
            pval_set = []
            for row in rows:
                threshold1_set.append(row[1])
                threshold2_set.append(row[2])
                coverage_set.append(row[3])
                correlation_set.append(row[3])
                pval_set.append(row[3])
            df[variable1_name].fillna(int(df[variable1_name].mean()), inplace=True)
            df[variable2_name].fillna(int(df[variable2_name].mean()), inplace=True)
            corr, pval = pearsonr(df[variable1_name], df[variable2_name])
            #pattern.append(table_name)

            a_count = correlation_set.index(max(correlation_set))
            CorrelationPatterns.append(
                "{(" + variable1_name + " " + str(round(threshold1_set[a_count],4)) + "),(" + variable2_name + " " + str(
                    round(threshold2_set[a_count],4)) + ")}")
            correlations.append(max(correlation_set))
            threhsold1_imp_agreement.append(threshold1_set[a_count])
            threhsold2_imp_agreement.append(threshold2_set[a_count])
            coverages.append(coverage_set[a_count])
            pvlues.append(pval_set[a_count])
            
            AUC.append(sum(correlation_set)/len(correlation_set))
            correlation_full.append(corr)
            pval_full.append(pval)
            '''
            a_count = 0
            for correlation in correlation_set:
                if correlation > .4 and pval_set[a_count] < 1:
                    CorrelationPatterns.append("{(" + variable1_name + " " + str(round(threshold1_set[a_count],4)) + "),(" + variable2_name + " " + str(
                    round(threshold2_set[a_count],4)) + ")}")
                    correlations.append(correlation)
                    threhsold1_imp_agreement.append(threshold1_set[a_count])
                    threhsold2_imp_agreement.append(threshold2_set[a_count])
                    coverages.append(coverage_set[a_count])
                    pvlues.append(pval_set[a_count])
                    correlation_full.append(corr)
                    pval_full.append(pval)
                a_count+= 1
            '''
            '''
            c.execute(f'SELECT * FROM {variable1_name}')
            rows = c.fetchall()
            threshold1all = []

            for row in rows:
                threshold1all.append(row[1])
            c.execute(f'SELECT * FROM {variable2_name}')
            rows = c.fetchall()

            threshold2all = []
            for row in rows:
                threshold2all.append(row[1])

            import matplotlib.pyplot as plt
            from mpl_toolkits.mplot3d import Axes3D
            import numpy as np

            # Generate some data
            x = threshold1all
            y = threshold2all

            z = []
            count = 0
            for i in range(len(y)):
                temp = []
                for j in range(len(x)):
                    temp.append(agreement_set[count])

                    count += 1
                z.append(temp)
            Z= np.array(z)
            X, Y = np.meshgrid(x, y)

            # Create a 3D plot
            fig = plt.figure(figsize=(8, 6))
            ax = fig.add_subplot(111, projection='3d')
            surf = ax.plot_surface(X, Y, Z, cmap='coolwarm')

            # Hide grid lines
            ax.grid(False)

            # Add axis labels and title
            ax.set_xlabel(variable1_name)
            ax.set_ylabel(variable2_name)
            ax.set_zlabel("I")
            cbar = fig.colorbar(surf)
            cbar.ax.set_position([0.85, 0.25, 0.03, 0.5])
            # Show the plot
            #plt.show()
            path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/TKDE/Agreements/Visualizations/Ageements_50_1/"+table_name
            plt.savefig(path)
            z = []
            count = 0
            for i in range(len(y)):
                temp = []
                for j in range(len(x)):
                    temp.append(agreement_set[count]-expected_set[count])

                    count += 1
                z.append(temp)
            Z= np.array(z)
            fig = plt.figure(figsize=(8, 6))
            ax = fig.add_subplot(111, projection='3d')
            surf = ax.plot_surface(X, Y, Z, cmap='coolwarm')

            # Hide grid lines
            ax.grid(False)

            # Add axis labels and title
            ax.set_xlabel(variable1_name)
            ax.set_ylabel(variable2_name)
            ax.set_zlabel("I-EA")
            cbar=fig.colorbar(surf)
            cbar.ax.set_position([0.85, 0.25, 0.03, 0.5])
            # Show the plot
            path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/TKDE/Agreements/Visualizations/Difference_50_1/" + table_name
            plt.savefig(path)
            '''
            count += len(correlation_set)
    l += 1

print("total pattern:",count, "rank correlation:", pearsonr(correlations, AUC))
'''
import pandas as pd
df = pd.DataFrame()
df['pattern'] = CorrelationPatterns
df['imp_correlation'] = correlations
df['pval'] = pvlues
df['full_correlation'] = correlation_full
df['full_pval'] = pval_full
df['threhsold1_imp_correlation'] = threhsold1_imp_agreement
df['threhsold2_imp_correlation'] = threhsold2_imp_agreement
df['value_coveresge'] = coverages
df['AUC'] = AUC
path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/TKDE/Agreements/Files/All/data_correlation_max.csv"
df.to_csv(path,index=False)
'''