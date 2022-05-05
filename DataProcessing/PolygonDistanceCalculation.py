import pandas as pd
import shapely.wkt

df = pd.read_csv('ProcessedData/UnemploymentPolygon.csv', sep=',')
neighbours_FIPS_list = []
neighbours = [float('inf')]*5
for i in range(0,len(df)):
    neighbours_FIPS = [0]*5
    for j in range(0, len(df)):
        if i != j:
            P1 = shapely.wkt.loads(df['geometry'][i])
            P2 = shapely.wkt.loads(df['geometry'][j])
            distance = P1.distance(P2)

            # Find the closest five neighbours
            if neighbours[4] > distance:
                if neighbours[3] > distance:
                    if neighbours[2] > distance:
                        if neighbours[1] > distance:
                            if neighbours[0] > distance:
                                neighbours[0] = distance
                                neighbours_FIPS[0] = df['FIPS'][j]
                            else:
                                neighbours[1] = distance
                                neighbours_FIPS[1] = df['FIPS'][j]
                        else:
                            neighbours[2] = distance
                            neighbours_FIPS[2] = df['FIPS'][j]
                    else:
                        neighbours[3] = distance
                        neighbours_FIPS[3] = df['FIPS'][j]
                else:
                    neighbours[4] = distance
                    neighbours_FIPS[4] = df['FIPS'][j]

    neighbours_FIPS_list.append(neighbours_FIPS)

new_df = pd.DataFrame()
new_df['FIPS'] = df['FIPS']
new_df['neighbours'] = neighbours_FIPS_list

new_df.to_csv('ProcessedData/PolygonDistanceByFIPS', index=False)
