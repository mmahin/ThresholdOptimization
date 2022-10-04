from scipy.stats import spearmanr
import pandas as pd
from SubModules.ObtainVariableDataframesAndStateDictionary import getAllVariableDataframesAndSpatialIndexes

data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'
df = getAllVariableDataframesAndSpatialIndexes(data_path)
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


corr1, pval1 = spearmanr(df[variable1], df[variable2])
corr2, pval2 = spearmanr(df[variable1], df[variable3])
corr3, pval3 = spearmanr(df[variable1], df[variable4])
corr4, pval4 = spearmanr(df[variable1], df[variable5])
corr5, pval5 = spearmanr(df[variable1], df[variable6])
corr6, pval6 = spearmanr(df[variable1], df[variable7])
corr7, pval7 = spearmanr(df[variable1], df[variable8])
corr8, pval8 = spearmanr(df[variable1], df[variable9])
corr9, pval9 = spearmanr(df[variable1], df[variable10])
corr10, pval10 = spearmanr(df[variable1], df[variable11])
corr11, pval11 = spearmanr(df[variable1], df[variable12])
corr12, pval12 = spearmanr(df[variable1], df[variable13])
corr13, pval13 = spearmanr(df[variable1], df[variable14])
corr14, pval14 = spearmanr(df[variable1], df[variable15])
corr15, pval15 = spearmanr(df[variable1], df[variable16])
corr16, pval16 = spearmanr(df[variable1], df[variable17])
corr17, pval17 = spearmanr(df[variable1], df[variable18])
corr18, pval18 = spearmanr(df[variable1], df[variable19])
corr19, pval19 = spearmanr(df[variable1], df[variable20])

print(round(corr1,2), round(corr2,2), round(corr3,2), round(corr4,2), round(corr5,2), round(corr6,2), round(corr7,2), round(corr8,2)
      ,round(corr9,2), round(corr10,2), round(corr11,2), round(corr12,2), round(corr13,2), round(corr14,2), round(corr15,2),
      round(corr16,2), round(corr17,2), round(corr18,2), round(corr19,2))

print(round(pval1,2), round(pval2,2), round(pval3,2), round(pval4,2), round(pval5,2), round(pval6,2), round(pval7,2), round(pval8,2)
      ,round(pval9,2), round(pval10,2), round(pval11,2), round(pval12,2), round(pval13,2), round(pval14,2), round(pval15,2),
      round(pval16,2), round(pval17,2), round(pval18,2), round(pval19,2))