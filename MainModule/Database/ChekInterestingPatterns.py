import sqlite3
import pickle

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
pattern = []
threhsold1_max_agreement = []
threhsold2_max_agreement = []
max_agreement = []
max_agreement_expected = []
threhsold1_max_diffrence = []
threhsold2_max_diffrence = []
max_difference = []
max_difference_agreemnt = []
max_difference_expected = []
threhsold1_min_diffrence = []
threhsold2_min_diffrence = []
min_difference = []
min_difference_agreemnt = []
min_difference_expected = []
max_lift = []
area_under_the_curve = []
expected_area_under_the_curve = []
count = 0
l = 1
threshold_area_dict = {}
for variable1_name in variable_names:

    for k in range(l,len(variable_names)):

        variable2_name = variable_names[k]
        if variable1_name not in threshold_area_dict.keys():
            c.execute(f'SELECT * FROM {variable1_name}')
            rows = c.fetchall()
            for row in rows:
                threshold_area_dict[variable1_name] = {}
                threshold_area_dict[variable1_name][str(row[1])] = row[3]

        if variable2_name not in threshold_area_dict.keys():
            c.execute(f'SELECT * FROM {variable2_name}')
            rows = c.fetchall()
            for row in rows:
                threshold_area_dict[variable2_name] = {}
                threshold_area_dict[variable2_name][str(row[1])] = row[3]

        table_name = variable1_name+"_"+variable2_name
        print(table_name)
        if variable1_name != variable2_name:# and table_name  in already_completed:


            c.execute(f'SELECT * FROM {table_name}')
            rows = c.fetchall()

            # print the rows
            threshold1_set = []
            threshold2_set = []
            agreement_set = []
            expected_set = []
            difference_set = []
            lift_set = []
            for row in rows:
                threshold1_set.append(row[1])
                threshold2_set.append(row[2])
                agreement_set.append(row[3])
                expected_set.append(row[4])
                difference_set.append(row[3]-row[4])
                lift_set.append(row[3]/row[4])
            pattern.append(table_name)
            max_agreement.append(max(agreement_set))
            max_agreement_expected.append(expected_set[agreement_set.index(max(agreement_set))])
            threhsold1_max_agreement.append(threshold1_set[agreement_set.index(max(agreement_set))])
            threhsold2_max_agreement.append(threshold2_set[agreement_set.index(max(agreement_set))])
            max_difference.append(max(difference_set))
            max_difference_agreemnt.append(agreement_set[difference_set.index(max(difference_set))])
            max_difference_expected.append(expected_set[difference_set.index(max(difference_set))])
            threhsold1_max_diffrence.append(threshold1_set[difference_set.index(max(difference_set))])
            threhsold2_max_diffrence.append(threshold2_set[difference_set.index(max(difference_set))])
            min_difference.append(min(difference_set))
            min_difference_agreemnt.append(agreement_set[difference_set.index(min(difference_set))])
            min_difference_expected.append(expected_set[difference_set.index(min(difference_set))])
            threhsold1_min_diffrence.append(threshold1_set[difference_set.index(min(difference_set))])
            threhsold2_min_diffrence.append(threshold2_set[difference_set.index(min(difference_set))])
            max_lift.append(max(lift_set))
            area_under_the_curve.append(sum(agreement_set)/len(agreement_set))
            expected_area_under_the_curve.append(sum(expected_set) / len(expected_set))
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
            count += len(agreement_set)
    l += 1
print("total pattern:",count)
import pandas as pd
df = pd.DataFrame()
df['pattern'] = pattern
df['max_agreement'] = max_agreement
df['max_agreement_expected'] = max_agreement_expected
df['threhsold1_max_agreement'] = threhsold1_max_agreement
df['threhsold2_max_agreement'] = threhsold2_max_agreement

df['max_difference'] = max_difference
df['max_difference_agreemnt'] = max_difference_agreemnt
df['max_difference_expected'] = max_difference_expected
df['threhsold1_max_diffrence'] = threhsold1_max_diffrence
df['threhsold2_max_diffrence'] = threhsold2_max_diffrence

df['min_difference'] = min_difference
df['min_difference_agreemnt'] = min_difference_agreemnt
df['min_difference_expected'] = min_difference_expected
df['threhsold1_min_diffrence'] = threhsold1_min_diffrence
df['threhsold2_min_diffrence'] = threhsold2_min_diffrence

df['max_lift'] = max_lift
df['area_under_the_curve'] = area_under_the_curve
df['expected_area_under_the_curve'] = expected_area_under_the_curve
path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/TKDE/Agreements/Files/All/data.csv"
df.to_csv(path,index=False)