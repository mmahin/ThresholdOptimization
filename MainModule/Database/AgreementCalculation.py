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
