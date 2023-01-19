from scipy.stats import pearsonr
import pandas as pd
from SubModules.ObtainVariableDataframesAndStateDictionary import getAllVariableDataframesAndSpatialIndexes
import numpy as np
import matplotlib.pyplot as plt

data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'
df = getAllVariableDataframesAndSpatialIndexes(data_path)
variables = ['covid_cases_density', 'bachelor_degree_density_2014_2018', 'avg_precipitation_for_county', 'avg_temp_for_county',
             'population_density_on_land_2010', 'household_density_on_land_2010', 'UnempRate2018', 'PctEmpAgriculture',
             'PctEmpMining', 'PctEmpConstruction', 'PctEmpManufacturing', 'PctEmpTrade', 'PctEmpTrans', 'PctEmpInformation',
             'PctEmpFIRE', 'PctEmpServices', 'PctEmpGovt', 'medianHouseHoldIncome', 'povertyRate', 'covid_death_density']
labels = ['Covid-19 Infection Rate', 'Bachelor Degree Rate', 'Average Precipitation', 'Average Temperature',
             'Population Density', 'Household Density', 'Unemployment Rate', 'Agriculture Employee Rate',
             'Mining Employee Rate', 'Construction Employee Rate', 'Manufacturing Employee Rate', 'Trade  Employee Rate',
             'Tranportation Employee Rate', 'Information  Employee Rate', 'FIRE Service  Employee Rate',
              'Services  Employee Rate', 'Goverment  Employee Rate', 'Median HouseHold Income', 'Poverty Rate', 'Covid-19 Death Rate']
correlation_mat = np.empty([len(variables),len(variables)])
significance_mat = [[0 for _ in range(len(variables))] for _ in range(len(variables))]
for count1 in range(len(variables)):
      df[variables[count1]].fillna(int(df[variables[count1]].mean()), inplace=True)
      for count2 in range(len(variables)):
            df[variables[count2]].fillna(int(df[variables[count2]].mean()), inplace=True)
            corr, pval = pearsonr(df[variables[count1]], df[variables[count2]])
            correlation_mat[count1][count2] = corr
            significance_mat[count1][count2] = pval
            print(round(corr,2),round(pval,2))
fig, ax = plt.subplots()
ax.matshow(correlation_mat, cmap='hot')
for (i, j), z in np.ndenumerate(correlation_mat):
    ax.text(j, i, '{:0.1f}'.format(z), ha='center', va='center')
#plt.colorbar()
xaxis = np.arange(len(labels))
ax.set_xticks(xaxis,rotation=90)
ax.set_yticks(xaxis,rotation=90)
ax.set_xticklabels(labels,rotation=90)
ax.set_yticklabels(labels)
plt.show()

variable1 = 'covid_cases_density'
variable2 = 'bachelor_degree_density_2014_2018'
variable3 = 'avg_precipitation_for_county'
variable4 = 'avg_temp_for_county'
variable5 = 'population_density_on_land_2010'
variable6 = 'household_density_on_land_2010'
variable7 = 'UnempRate2018'
variable8 = 'PctEmpAgriculture'
variable9 = 'PctEmpMining'
variable10 = 'PctEmpConstruction'
variable11 = 'PctEmpManufacturing'
variable12 = 'PctEmpTrade'
variable13 = 'PctEmpTrans'
variable14 = 'PctEmpInformation'
variable15 = 'PctEmpFIRE'
variable16 = 'PctEmpServices'
variable17 = 'PctEmpGovt'
variable18 = 'medianHouseHoldIncome'
variable19 = 'povertyRate'
variable20 = 'covid_death_density'

df[variable1].fillna(int(df[variable1].mean()), inplace=True)
df[variable2].fillna(int(df[variable2].mean()), inplace=True)
df[variable3].fillna(int(df[variable2].mean()), inplace=True)
df[variable4].fillna(int(df[variable2].mean()), inplace=True)
df[variable5].fillna(int(df[variable2].mean()), inplace=True)
df[variable6].fillna(int(df[variable2].mean()), inplace=True)
df[variable7].fillna(int(df[variable2].mean()), inplace=True)
df[variable8].fillna(int(df[variable2].mean()), inplace=True)
df[variable9].fillna(int(df[variable2].mean()), inplace=True)
df[variable10].fillna(int(df[variable2].mean()), inplace=True)
df[variable11].fillna(int(df[variable2].mean()), inplace=True)
df[variable12].fillna(int(df[variable2].mean()), inplace=True)
df[variable13].fillna(int(df[variable2].mean()), inplace=True)
df[variable14].fillna(int(df[variable2].mean()), inplace=True)
df[variable15].fillna(int(df[variable2].mean()), inplace=True)
df[variable16].fillna(int(df[variable2].mean()), inplace=True)
df[variable17].fillna(int(df[variable2].mean()), inplace=True)
df[variable18].fillna(int(df[variable2].mean()), inplace=True)
df[variable19].fillna(int(df[variable2].mean()), inplace=True)
df[variable20].fillna(int(df[variable2].mean()), inplace=True)


corr1, pval1 = pearsonr(df[variable1], df[variable2])
corr2, pval2 = pearsonr(df[variable1], df[variable3])
corr3, pval3 = pearsonr(df[variable1], df[variable4])
corr4, pval4 = pearsonr(df[variable1], df[variable5])
corr5, pval5 = pearsonr(df[variable1], df[variable6])
corr6, pval6 = pearsonr(df[variable1], df[variable7])
corr7, pval7 = pearsonr(df[variable1], df[variable8])
corr8, pval8 = pearsonr(df[variable1], df[variable9])
corr9, pval9 = pearsonr(df[variable1], df[variable10])
corr10, pval10 = pearsonr(df[variable1], df[variable11])
corr11, pval11 = pearsonr(df[variable1], df[variable12])
corr12, pval12 = pearsonr(df[variable1], df[variable13])
corr13, pval13 = pearsonr(df[variable1], df[variable14])
corr14, pval14 = pearsonr(df[variable1], df[variable15])
corr15, pval15 = pearsonr(df[variable1], df[variable16])
corr16, pval16 = pearsonr(df[variable1], df[variable17])
corr17, pval17 = pearsonr(df[variable1], df[variable18])
corr18, pval18 = pearsonr(df[variable1], df[variable19])
corr19, pval19 = pearsonr(df[variable1], df[variable20])

print(round(corr1,2), round(corr2,2), round(corr3,2), round(corr4,2), round(corr5,2), round(corr6,2), round(corr7,2), round(corr8,2)
      ,round(corr9,2), round(corr10,2), round(corr11,2), round(corr12,2), round(corr13,2), round(corr14,2), round(corr15,2),
      round(corr16,2), round(corr17,2), round(corr18,2), round(corr19,2))

print(round(pval1,2), round(pval2,2), round(pval3,2), round(pval4,2), round(pval5,2), round(pval6,2), round(pval7,2), round(pval8,2)
      ,round(pval9,2), round(pval10,2), round(pval11,2), round(pval12,2), round(pval13,2), round(pval14,2), round(pval15,2),
      round(pval16,2), round(pval17,2), round(pval18,2), round(pval19,2))