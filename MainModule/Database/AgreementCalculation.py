import sqlite3
import pickle
from AgreementFunction.agreementFunction import Agreement
# connect to the database
conn = sqlite3.connect('hotspots_50_1.db')
variable_names = ['UnempRate2018',"avg_precipitation_for_county","PctEmpInformation","PctEmpFIRE","PctEmpTrans","PctEmpConstruction",
                  "PctEmpTrade","PctEmpGovt","PctEmpMining","avg_temp_for_county","PctEmpAgriculture","PctEmpServices",
                  "PctEmpManufacturing","povertyRate","bachelor_degree_density_2014_2018","medianHouseHoldIncome",
                  "covid_cases_density","covid_death_density","population_density_on_land_2010","household_density_on_land_2010"]

already_completed = ["UnempRate2018_avg_precipitation_for_county","UnempRate2018_PctEmpInformation","UnempRate2018_PctEmpFIRE","UnempRate2018_PctEmpTrans","UnempRate2018_PctEmpConstruction","UnempRate2018_PctEmpTrade","UnempRate2018_PctEmpGovt","UnempRate2018_PctEmpMining","UnempRate2018_avg_temp_for_county","UnempRate2018_PctEmpAgriculture","UnempRate2018_PctEmpServices","UnempRate2018_PctEmpManufacturing","UnempRate2018_povertyRate","UnempRate2018_bachelor_degree_density_2014_2018","UnempRate2018_medianHouseHoldIncome","UnempRate2018_covid_cases_density","UnempRate2018_covid_death_density","UnempRate2018_population_density_on_land_2010","UnempRate2018_household_density_on_land_2010"
                     ,'avg_precipitation_for_county_PctEmpInformation','avg_precipitation_for_county_PctEmpFIRE','avg_precipitation_for_county_PctEmpTrans','avg_precipitation_for_county_PctEmpConstruction','avg_precipitation_for_county_PctEmpTrade','avg_precipitation_for_county_PctEmpGovt','avg_precipitation_for_county_PctEmpMining','avg_precipitation_for_county_avg_temp_for_county','avg_precipitation_for_county_PctEmpAgriculture','avg_precipitation_for_county_PctEmpServices','avg_precipitation_for_county_PctEmpManufacturing','avg_precipitation_for_county_povertyRate' ,'avg_precipitation_for_county_bachelor_degree_density_2014_2018','avg_precipitation_for_county_medianHouseHoldIncome','avg_precipitation_for_county_covid_cases_density','avg_precipitation_for_county_covid_death_density','avg_precipitation_for_county_population_density_on_land_2010','avg_precipitation_for_county_household_density_on_land_2010'
                    , 'PctEmpInformation_PctEmpFIRE','PctEmpInformation_PctEmpTrans','PctEmpInformation_PctEmpConstruction','PctEmpInformation_PctEmpTrade','PctEmpInformation_PctEmpGovt','PctEmpInformation_PctEmpMining','PctEmpInformation_avg_temp_for_county','PctEmpInformation_PctEmpAgriculture','PctEmpInformation_PctEmpServices','PctEmpInformation_PctEmpManufacturing','PctEmpInformation_povertyRate','PctEmpInformation_bachelor_degree_density_2014_2018','PctEmpInformation_medianHouseHoldIncome','PctEmpInformation_covid_cases_density','PctEmpInformation_covid_death_density','PctEmpInformation_population_density_on_land_2010','PctEmpInformation_household_density_on_land_2010','PctEmpFIRE_PctEmpTrans','PctEmpFIRE_PctEmpConstruction','PctEmpFIRE_PctEmpTrade','PctEmpFIRE_PctEmpGovt','PctEmpFIRE_PctEmpMining','PctEmpFIRE_avg_temp_for_county','PctEmpFIRE_PctEmpAgriculture','PctEmpFIRE_PctEmpServices','PctEmpFIRE_PctEmpManufacturing','PctEmpFIRE_povertyRate','PctEmpFIRE_bachelor_degree_density_2014_2018','PctEmpFIRE_medianHouseHoldIncome','PctEmpFIRE_covid_cases_density','PctEmpFIRE_covid_death_density','PctEmpFIRE_population_density_on_land_2010','PctEmpFIRE_household_density_on_land_2010','PctEmpTrans_PctEmpConstruction','PctEmpTrans_PctEmpTrade','PctEmpTrans_PctEmpGovt','PctEmpTrans_PctEmpMining','PctEmpTrans_avg_temp_for_county','PctEmpTrans_PctEmpAgriculture','PctEmpTrans_PctEmpServices','PctEmpTrans_PctEmpManufacturing','PctEmpTrans_povertyRate','PctEmpTrans_bachelor_degree_density_2014_2018','PctEmpTrans_medianHouseHoldIncome','PctEmpTrans_covid_cases_density','PctEmpTrans_covid_death_density','PctEmpTrans_population_density_on_land_2010','PctEmpTrans_household_density_on_land_2010','PctEmpConstruction_PctEmpTrade','PctEmpConstruction_PctEmpGovt','PctEmpConstruction_PctEmpMining','PctEmpConstruction_avg_temp_for_county','PctEmpConstruction_PctEmpAgriculture','PctEmpConstruction_PctEmpServices','PctEmpConstruction_PctEmpManufacturing','PctEmpConstruction_povertyRate','PctEmpConstruction_bachelor_degree_density_2014_2018','PctEmpConstruction_medianHouseHoldIncome','PctEmpConstruction_covid_cases_density','PctEmpConstruction_covid_death_density','PctEmpConstruction_population_density_on_land_2010','PctEmpConstruction_household_density_on_land_2010','PctEmpTrade_PctEmpGovt','PctEmpTrade_PctEmpMining','PctEmpTrade_avg_temp_for_county','PctEmpTrade_PctEmpAgriculture','PctEmpTrade_PctEmpServices','PctEmpTrade_PctEmpManufacturing','PctEmpTrade_povertyRate','PctEmpTrade_bachelor_degree_density_2014_2018','PctEmpTrade_medianHouseHoldIncome','PctEmpTrade_covid_cases_density','PctEmpTrade_covid_death_density','PctEmpTrade_population_density_on_land_2010','PctEmpTrade_household_density_on_land_2010','PctEmpGovt_PctEmpMining','PctEmpGovt_avg_temp_for_county','PctEmpGovt_PctEmpAgriculture','PctEmpGovt_PctEmpServices','PctEmpGovt_PctEmpManufacturing','PctEmpGovt_povertyRate','PctEmpGovt_bachelor_degree_density_2014_2018','PctEmpGovt_medianHouseHoldIncome','PctEmpGovt_covid_cases_density','PctEmpGovt_covid_death_density','PctEmpGovt_population_density_on_land_2010','PctEmpGovt_household_density_on_land_2010','PctEmpMining_avg_temp_for_county','PctEmpMining_PctEmpAgriculture','PctEmpMining_PctEmpServices','PctEmpMining_PctEmpManufacturing','PctEmpMining_povertyRate','PctEmpMining_bachelor_degree_density_2014_2018','PctEmpMining_medianHouseHoldIncome','PctEmpMining_covid_cases_density','PctEmpMining_covid_death_density','PctEmpMining_population_density_on_land_2010','PctEmpMining_household_density_on_land_2010','avg_temp_for_county_PctEmpAgriculture','avg_temp_for_county_PctEmpServices','avg_temp_for_county_PctEmpManufacturing','avg_temp_for_county_povertyRate','avg_temp_for_county_bachelor_degree_density_2014_2018','avg_temp_for_county_medianHouseHoldIncome','avg_temp_for_county_covid_cases_density','avg_temp_for_county_covid_death_density','avg_temp_for_county_population_density_on_land_2010','avg_temp_for_county_household_density_on_land_2010','PctEmpAgriculture_PctEmpServices','PctEmpAgriculture_PctEmpManufacturing','PctEmpAgriculture_povertyRate','PctEmpAgriculture_bachelor_degree_density_2014_2018','PctEmpAgriculture_medianHouseHoldIncome','PctEmpAgriculture_covid_cases_density','PctEmpAgriculture_covid_death_density','PctEmpAgriculture_population_density_on_land_2010','PctEmpAgriculture_household_density_on_land_2010','PctEmpServices_PctEmpManufacturing','PctEmpServices_povertyRate','PctEmpServices_bachelor_degree_density_2014_2018','PctEmpServices_medianHouseHoldIncome','PctEmpServices_covid_cases_density','PctEmpServices_covid_death_density','PctEmpServices_population_density_on_land_2010','PctEmpServices_household_density_on_land_2010','PctEmpManufacturing_povertyRate','PctEmpManufacturing_bachelor_degree_density_2014_2018','PctEmpManufacturing_medianHouseHoldIncome','PctEmpManufacturing_covid_cases_density','PctEmpServices_covid_death_density','PctEmpServices_population_density_on_land_2010','PctEmpServices_household_density_on_land_2010','PctEmpManufacturing_povertyRate','PctEmpManufacturing_bachelor_degree_density_2014_2018','PctEmpManufacturing_medianHouseHoldIncome','PctEmpManufacturing_covid_cases_density','PctEmpManufacturing_covid_death_density','PctEmpManufacturing_population_density_on_land_2010','PctEmpManufacturing_household_density_on_land_2010','povertyRate_bachelor_degree_density_2014_2018'
                      ]
# create a cursor object
c = conn.cursor()
l = 0
for variable1_name in variable_names:
    for k in range(l,len(variable_names)):
        variable2_name = variable_names[k]
        table_name = variable1_name + "_" + variable2_name

        if variable1_name != variable2_name and table_name not in already_completed:
            c.execute(f"DROP TABLE IF EXISTS {table_name}")
            c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         threshold1 REAL,
                         threshold2 REAL,
                         agreement REAL,
                         expected REAL);''')
            # select all rows from the table
            c.execute(f'SELECT * FROM {variable1_name}')

            # retrieve all rows as a list of tuples
            rows = c.fetchall()

            # print the rows
            threshold1_set = []
            hotspot1_set = []
            area_coverage_set1 = []
            for row in rows:
                threshold1_set.append(row[1])
                hotspot1_set.append(pickle.loads(row[2]))
                area_coverage_set1.append(row[3])


            # select all rows from the table
            c.execute(f'SELECT * FROM {variable2_name}')

            # retrieve all rows as a list of tuples
            rows = c.fetchall()
            threshold2_set = []
            hotspot2_set = []
            area_coverage_set2 = []
            for row in rows:
                threshold2_set.append(row[1])
                hotspot2_set.append(pickle.loads(row[2]))
                area_coverage_set2.append(row[3])

            for i in range(len(threshold1_set)):
                for j in range(len(threshold2_set)):
                    hotspots1 = hotspot1_set[i]
                    hotspots2 = hotspot2_set[j]
                    agreement = Agreement(hotspots1, hotspots2)
                    expected = area_coverage_set1[i]* area_coverage_set2[j]
                    # Insert the data into the table
                    conn.execute(f"INSERT INTO {table_name} (threshold1, threshold2, agreement, expected) VALUES (?, ?, ?, ?)",
                                 (threshold1_set[i], threshold2_set[j], agreement, expected))

                    # Commit the changes
                    conn.commit()

            print(table_name)

    l += 1
# close the cursor and database connection
c.close()
conn.close()
