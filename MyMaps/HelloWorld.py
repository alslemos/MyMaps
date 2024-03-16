import geopandas as gpd
import matplotlib.pyplot as plt

mapa = "assets/RS_Municipios_2022.shp"
gdf = gpd.read_file(mapa)

print(gdf.columns) # Index(['CD_MUN', 'NM_MUN', 'SIGLA_UF', 'AREA_KM2', 'geometry'], dtype='object')

municipios_verdes = ["Gravataí", "Anta Gorda", "Uruguaiana"]
gdf['cor'] = 'white'
gdf.loc[gdf['NM_MUN'].isin(municipios_verdes), 'cor'] = 'mediumseagreen'

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
gdf.plot(ax=ax, color = gdf['cor'], edgecolor='dimgrey')
plt.title('Municipios que alguem falou')
plt.show()
gdf.savefig("../mesaBranca.png")
