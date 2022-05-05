import matplotlib.pyplot as plt
import geopandas as gpd

def HotspotsVisualiztion(Hotspots):
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    for polygon in Hotspots:

        gdf = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon])
        gdf.plot(linewidth=0.8, ax=ax, edgecolor='black', facecolor="none")
    plt.show()