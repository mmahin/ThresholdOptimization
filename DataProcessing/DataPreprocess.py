import pandas as pd
import shapely.wkt


def unique(list1, df):
    # initialize a null list
    unique_list = []
    print(len(list1))
    # traverse for all elements
    i = 0
    j = 0
    ranges = []
    for x in list1:
        # check if exists in unique_list or not
        range_temp = []
        if x not in unique_list:
            unique_list.append(x)
            range_temp.append([j,i])
            j = i
            val = int(df['FIPS'][j]/1000)
            #print(val)
            ranges.append(range_temp)

        i += 1
    for item in ranges:
        print(item)
    directory ={}
    i = 1
    for item in unique_list:
        directory[item] = ranges[i]
        i += 1
    print(directory)
    return ranges



df = pd.read_csv('ProcessedData/UnemploymentPolygon.csv', sep=',', na_filter= False)

search_index_directory = {}
state_ids = []
print(len(df['FIPS']))
for item in df['FIPS']:
    val = int(item/1000)
    state_ids.append(val)
    '''
    for j in range(0, len(df)):
        val2 = int(df['FIPS'][j]/1000)
        if (val1==val2):
            indexes.append(j)
    '''
    #i = j
print(unique(state_ids, df))
'''
neighbours_FIPS_list = []
for i in range(0,len(df)):
    neighbours_FIPS = [0]*5
    neighbours = [float('inf')] * 5
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
    print(i)
    neighbours_FIPS_list.append(neighbours_FIPS)

new_df = pd.DataFrame()
new_df['FIPS'] = df['FIPS']
new_df['neighbours'] = neighbours_FIPS_list

new_df.to_csv('ProcessedData/PolygonDistanceByFIPS', index=False)
'''
