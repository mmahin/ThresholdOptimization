import pygeoda
from esda.moran import Moran_BV, Moran_Local_BV
#from splot.esda import plot_moran_bv_simulation, plot_moran_bv
from libpysal.weights.contiguity import Queen
import geopandas as gpd
df = pygeoda.open('C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/Covid_19_Median_Income_SHP/Covid_19_Median_Income.shp')
print(df)
w = pygeoda.queen_weights(df )
print(w )
df2 = gpd.read_file('C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/Covid_19_Median_Income_SHP/Covid_19_Median_Income.shp')

nm = pygeoda.local_bimoran(w, df['covid_case'], df['medianHous'])
data = df2[['covid_case','medianHous']]
lm = pygeoda.neighbor_match_test(df, data, 4)

guerry = pygeoda.open('C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Inputs/GeoDaSample/Guerry.shp')
data = guerry[['Crm_prs','Crm_prp']]
lm = pygeoda.neighbor_match_test(guerry, data, 6)
guerry_w = pygeoda.queen_weights(guerry )
geary_crmprp = pygeoda.local_multigeary(guerry_w, data)

print(geary_crmprp)