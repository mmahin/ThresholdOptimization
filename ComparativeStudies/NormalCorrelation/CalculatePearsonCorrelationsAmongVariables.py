from scipy.stats import pearsonr
import pandas as pd
df = pd.read_csv('C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv')

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


corr1, _ = pearsonr(df[variable1], df[variable2])
corr2, _ = pearsonr(df[variable1], df[variable3])
corr3, _ = pearsonr(df[variable1], df[variable4])
corr4, _ = pearsonr(df[variable1], df[variable5])
corr5, _ = pearsonr(df[variable1], df[variable6])
corr6, _ = pearsonr(df[variable1], df[variable7])
corr7, _ = pearsonr(df[variable1], df[variable8])
corr8, _ = pearsonr(df[variable1], df[variable9])
corr9, _ = pearsonr(df[variable1], df[variable10])
corr10, _ = pearsonr(df[variable1], df[variable11])
corr11, _ = pearsonr(df[variable1], df[variable12])
corr12, _ = pearsonr(df[variable1], df[variable13])
corr13, _ = pearsonr(df[variable1], df[variable14])
corr14, _ = pearsonr(df[variable1], df[variable15])
corr15, _ = pearsonr(df[variable1], df[variable16])
corr16, _ = pearsonr(df[variable1], df[variable17])
corr17, _ = pearsonr(df[variable1], df[variable18])
corr18, _ = pearsonr(df[variable1], df[variable19])
corr19, _ = pearsonr(df[variable1], df[variable20])

print(round(corr1,2), round(corr2,2), round(corr3,2), round(corr4,2), round(corr5,2), round(corr6,2), round(corr7,2), round(corr8,2)
      ,round(corr9,2), round(corr10,2), round(corr11,2), round(corr12,2), round(corr13,2), round(corr14,2), round(corr15,2),
      round(corr16,2), round(corr17,2), round(corr18,2), round(corr19,2))