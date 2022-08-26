import shapely.wkt
import geopandas as gpd
import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 1, constrained_layout=False)
path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/InputPolygon.txt'
with open(path) as f:
    lines = f.readlines()
    polygon = shapely.wkt.loads(lines[0])
    gdf = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon])
    gdf.plot(linewidth=0.8, ax=axs[0], edgecolor='black', color='k', facecolor="none")

    new_polygon = polygon.simplify(0.01, preserve_topology=False)
    print(new_polygon)
    gdf = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[new_polygon])
    gdf.plot(linewidth=0.8, ax=axs[1], edgecolor='black', color='k', facecolor="none")
    plt.show()

