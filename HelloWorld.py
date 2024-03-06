import geopandas as gpd
import matplotlib.pyplot as plt

mapa = "BR_Municipios_2022.shp"
gdf = gpd.read_file(mapa)

print(gdf)