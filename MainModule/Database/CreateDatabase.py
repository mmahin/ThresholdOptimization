import sqlite3
import pickle
from MainModule.Database.FindHotspotsData import FindHotspotsData
# Connect to the database
conn = sqlite3.connect('hotspots_50_1.db')
#variable_names = ['UnempRate2018',"avg_precipitation_for_county","PctEmpInformation","PctEmpFIRE","PctEmpTrans","PctEmpConstruction",
#                  "PctEmpTrade","PctEmpGovt","PctEmpMining","avg_temp_for_county","PctEmpAgriculture","PctEmpServices",
#                  "PctEmpManufacturing","povertyRate","bachelor_degree_density_2014_2018","medianHouseHoldIncome",
#                  "covid_cases_density","covid_death_density","population_density_on_land_2010","household_density_on_land_2010"]
variable_names = ['UnempRate2018',"avg_precipitation_for_county","PctEmpInformation","PctEmpFIRE","PctEmpTrans","PctEmpConstruction",
                  "PctEmpTrade","PctEmpGovt","PctEmpMining","avg_temp_for_county","PctEmpAgriculture","PctEmpServices",
                  "PctEmpManufacturing","povertyRate","bachelor_degree_density_2014_2018","medianHouseHoldIncome",
                  "covid_cases_density","covid_death_density","population_density_on_land_2010","household_density_on_land_2010"]

for variable_name in variable_names:
    # Create a table
    c = conn.cursor()

    # create the table only if it does not exist
    c.execute(f"DROP TABLE IF EXISTS {variable_name}")
    c.execute(f'''CREATE TABLE IF NOT EXISTS {variable_name}
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 threshold REAL,
                 hotspots BLOB,
                 area_cover REAL);''')

    thresholds,hotspots,area_coverages = FindHotspotsData(variable_name)
    # Sample data
    for i in range(len(thresholds)):
        threshold = thresholds[i]
        hotspot_polygons = hotspots[i] # list of polygons
        area_cover = area_coverages[i]

        # Serialize the list of polygons using pickle
        hotspots_serialized = pickle.dumps(hotspot_polygons)

        # Insert the data into the table
        conn.execute(f"INSERT INTO {variable_name} (threshold, hotspots, area_cover) VALUES (?, ?, ?)",
                     (threshold, hotspots_serialized, area_cover))

        # Commit the changes
        conn.commit()
    print(variable_name, "Is complete")

# Close the connection
conn.close()