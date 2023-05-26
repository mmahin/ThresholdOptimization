import sqlite3
import pickle
from scipy.stats import stats,pearsonr
import pandas as pd
import geopandas as gpd
from esda.moran import Moran_BV, Moran_Local_BV
#from splot.esda import plot_moran_bv_simulation, plot_moran_bv
from libpysal.weights.contiguity import Queen
from SubModules.ObtainVariableDataframesAndStateDictionary import getAllVariableDataframesAndSpatialIndexes
# connect to the database
data_path = 'C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/DataProcessing/InitialExtractedData/dataset_combined.csv'
df = getAllVariableDataframesAndSpatialIndexes(data_path)
gdf = gpd.GeoDataFrame(columns=['feature'], geometry='feature')
gdf['feature'] = df['geometry']
w = Queen.from_dataframe(df)
# connect to the database
conn = sqlite3.connect('hotspots_50_1.db')
# create a cursor object
c = conn.cursor()

variable_names = ['UnempRate2018',"avg_precipitation_for_county","PctEmpInformation","PctEmpFIRE","PctEmpTrans","PctEmpConstruction",
                  "PctEmpTrade","PctEmpGovt","PctEmpMining","avg_temp_for_county","PctEmpAgriculture","PctEmpServices",
                  "PctEmpManufacturing","povertyRate","bachelor_degree_density_2014_2018","medianHouseHoldIncome",
                  "covid_cases_density","covid_death_density","population_density_on_land_2010","household_density_on_land_2010"]

#already_completed = ["UnempRate2018_avg_precipitation_for_county","UnempRate2018_PctEmpInformation","UnempRate2018_PctEmpFIRE","UnempRate2018_PctEmpTrans","UnempRate2018_PctEmpConstruction","UnempRate2018_PctEmpTrade","UnempRate2018_PctEmpGovt","UnempRate2018_PctEmpMining","UnempRate2018_avg_temp_for_county","UnempRate2018_PctEmpAgriculture","UnempRate2018_PctEmpServices","UnempRate2018_PctEmpManufacturing","UnempRate2018_povertyRate","UnempRate2018_bachelor_degree_density_2014_2018","UnempRate2018_medianHouseHoldIncome","UnempRate2018_covid_cases_density","UnempRate2018_covid_death_density","UnempRate2018_population_density_on_land_2010","UnempRate2018_household_density_on_land_2010"
#                     ,'avg_precipitation_for_county_PctEmpInformation','avg_precipitation_for_county_PctEmpFIRE','avg_precipitation_for_county_PctEmpTrans','avg_precipitation_for_county_PctEmpConstruction','avg_precipitation_for_county_PctEmpTrade','avg_precipitation_for_county_PctEmpGovt','avg_precipitation_for_county_PctEmpMining','avg_precipitation_for_county_avg_temp_for_county','avg_precipitation_for_county_PctEmpAgriculture','avg_precipitation_for_county_PctEmpServices','avg_precipitation_for_county_PctEmpManufacturing','avg_precipitation_for_county_povertyRate' ,'avg_precipitation_for_county_bachelor_degree_density_2014_2018','avg_precipitation_for_county_medianHouseHoldIncome','avg_precipitation_for_county_covid_cases_density','avg_precipitation_for_county_covid_death_density','avg_precipitation_for_county_population_density_on_land_2010','avg_precipitation_for_county_household_density_on_land_2010'
#                    , 'PctEmpInformation_PctEmpFIRE','PctEmpInformation_PctEmpTrans','PctEmpInformation_PctEmpConstruction','PctEmpInformation_PctEmpTrade','PctEmpInformation_PctEmpGovt','PctEmpInformation_PctEmpMining','PctEmpInformation_avg_temp_for_county','PctEmpInformation_PctEmpAgriculture','PctEmpInformation_PctEmpServices','PctEmpInformation_PctEmpManufacturing','PctEmpInformation_povertyRate','PctEmpInformation_bachelor_degree_density_2014_2018','PctEmpInformation_medianHouseHoldIncome','PctEmpInformation_covid_cases_density','PctEmpInformation_covid_death_density','PctEmpInformation_population_density_on_land_2010','PctEmpInformation_household_density_on_land_2010','PctEmpFIRE_PctEmpTrans','PctEmpFIRE_PctEmpConstruction','PctEmpFIRE_PctEmpTrade','PctEmpFIRE_PctEmpGovt','PctEmpFIRE_PctEmpMining','PctEmpFIRE_avg_temp_for_county','PctEmpFIRE_PctEmpAgriculture','PctEmpFIRE_PctEmpServices','PctEmpFIRE_PctEmpManufacturing','PctEmpFIRE_povertyRate','PctEmpFIRE_bachelor_degree_density_2014_2018','PctEmpFIRE_medianHouseHoldIncome','PctEmpFIRE_covid_cases_density','PctEmpFIRE_covid_death_density','PctEmpFIRE_population_density_on_land_2010','PctEmpFIRE_household_density_on_land_2010','PctEmpTrans_PctEmpConstruction','PctEmpTrans_PctEmpTrade','PctEmpTrans_PctEmpGovt','PctEmpTrans_PctEmpMining','PctEmpTrans_avg_temp_for_county','PctEmpTrans_PctEmpAgriculture','PctEmpTrans_PctEmpServices','PctEmpTrans_PctEmpManufacturing','PctEmpTrans_povertyRate','PctEmpTrans_bachelor_degree_density_2014_2018','PctEmpTrans_medianHouseHoldIncome','PctEmpTrans_covid_cases_density','PctEmpTrans_covid_death_density','PctEmpTrans_population_density_on_land_2010','PctEmpTrans_household_density_on_land_2010','PctEmpConstruction_PctEmpTrade','PctEmpConstruction_PctEmpGovt','PctEmpConstruction_PctEmpMining','PctEmpConstruction_avg_temp_for_county','PctEmpConstruction_PctEmpAgriculture','PctEmpConstruction_PctEmpServices','PctEmpConstruction_PctEmpManufacturing','PctEmpConstruction_povertyRate','PctEmpConstruction_bachelor_degree_density_2014_2018','PctEmpConstruction_medianHouseHoldIncome','PctEmpConstruction_covid_cases_density','PctEmpConstruction_covid_death_density','PctEmpConstruction_population_density_on_land_2010','PctEmpConstruction_household_density_on_land_2010','PctEmpTrade_PctEmpGovt','PctEmpTrade_PctEmpMining','PctEmpTrade_avg_temp_for_county','PctEmpTrade_PctEmpAgriculture','PctEmpTrade_PctEmpServices','PctEmpTrade_PctEmpManufacturing','PctEmpTrade_povertyRate','PctEmpTrade_bachelor_degree_density_2014_2018','PctEmpTrade_medianHouseHoldIncome','PctEmpTrade_covid_cases_density','PctEmpTrade_covid_death_density','PctEmpTrade_population_density_on_land_2010','PctEmpTrade_household_density_on_land_2010','PctEmpGovt_PctEmpMining','PctEmpGovt_avg_temp_for_county','PctEmpGovt_PctEmpAgriculture','PctEmpGovt_PctEmpServices','PctEmpGovt_PctEmpManufacturing','PctEmpGovt_povertyRate','PctEmpGovt_bachelor_degree_density_2014_2018','PctEmpGovt_medianHouseHoldIncome','PctEmpGovt_covid_cases_density','PctEmpGovt_covid_death_density','PctEmpGovt_population_density_on_land_2010','PctEmpGovt_household_density_on_land_2010','PctEmpMining_avg_temp_for_county','PctEmpMining_PctEmpAgriculture','PctEmpMining_PctEmpServices','PctEmpMining_PctEmpManufacturing','PctEmpMining_povertyRate','PctEmpMining_bachelor_degree_density_2014_2018','PctEmpMining_medianHouseHoldIncome','PctEmpMining_covid_cases_density','PctEmpMining_covid_death_density','PctEmpMining_population_density_on_land_2010','PctEmpMining_household_density_on_land_2010','avg_temp_for_county_PctEmpAgriculture','avg_temp_for_county_PctEmpServices','avg_temp_for_county_PctEmpManufacturing','avg_temp_for_county_povertyRate','avg_temp_for_county_bachelor_degree_density_2014_2018','avg_temp_for_county_medianHouseHoldIncome','avg_temp_for_county_covid_cases_density','avg_temp_for_county_covid_death_density','avg_temp_for_county_population_density_on_land_2010','avg_temp_for_county_household_density_on_land_2010','PctEmpAgriculture_PctEmpServices','PctEmpAgriculture_PctEmpManufacturing','PctEmpAgriculture_povertyRate','PctEmpAgriculture_bachelor_degree_density_2014_2018','PctEmpAgriculture_medianHouseHoldIncome','PctEmpAgriculture_covid_cases_density','PctEmpAgriculture_covid_death_density','PctEmpAgriculture_population_density_on_land_2010','PctEmpAgriculture_household_density_on_land_2010','PctEmpServices_PctEmpManufacturing','PctEmpServices_povertyRate','PctEmpServices_bachelor_degree_density_2014_2018','PctEmpServices_medianHouseHoldIncome','PctEmpServices_covid_cases_density','PctEmpServices_covid_death_density','PctEmpServices_population_density_on_land_2010','PctEmpServices_household_density_on_land_2010','PctEmpManufacturing_povertyRate','PctEmpManufacturing_bachelor_degree_density_2014_2018','PctEmpManufacturing_medianHouseHoldIncome','PctEmpManufacturing_covid_cases_density','PctEmpServices_covid_death_density','PctEmpServices_population_density_on_land_2010','PctEmpServices_household_density_on_land_2010','PctEmpManufacturing_povertyRate','PctEmpManufacturing_bachelor_degree_density_2014_2018','PctEmpManufacturing_medianHouseHoldIncome','PctEmpManufacturing_covid_cases_density','PctEmpManufacturing_covid_death_density','PctEmpManufacturing_population_density_on_land_2010','PctEmpManufacturing_household_density_on_land_2010','povertyRate_bachelor_degree_density_2014_2018'
#                      ]
pattern = []
correlations = []
MoranIs = []
threhsold1_max_agreement = []
threhsold2_max_agreement = []
max_agreement = []
threhsold1_max_agreement_area_coverage = []
threhsold2_max_agreement_area_coverage = []
max_agreement_expected = []
lift_maxima = []
AUC_Agreement = []
AUC_Agreement_expected = []
threshold1_set_corr = []
threshold2_set_corr = []
CVT_correlation = []
CVT_correlation_value_coverage = []
CVT_correlation_AUC = []
def compare_with_none(x):
    return float('-inf') if x is None else x
count = 0
l = 1
threshold_area_dict = {}
for variable1_name in variable_names:

    for k in range(l,len(variable_names)):
        variable2_name = variable_names[k]
        if variable1_name not in threshold_area_dict.keys():
            c.execute(f'SELECT * FROM {variable1_name}')
            rows = c.fetchall()
            threshold_area_dict[variable1_name] = {}
            for row in rows:
                threshold_area_dict[variable1_name][str(float(row[1]))] = row[3]
        if variable2_name not in threshold_area_dict.keys():
            c.execute(f'SELECT * FROM {variable2_name}')
            rows = c.fetchall()
            threshold_area_dict[variable2_name] = {}
            for row in rows:
                threshold_area_dict[variable2_name][str(float(row[1]))] = row[3]
        table_name =  variable1_name + "_" + variable2_name
        table2_name = "Matching_Correlation_" + variable1_name + "_" + variable2_name
        print(table_name)
        if variable1_name != variable2_name:# and table_name  in already_completed:
            df[variable1_name].fillna(int(df[variable1_name].mean()), inplace=True)
            df[variable2_name].fillna(int(df[variable2_name].mean()), inplace=True)
            corr, pval = pearsonr(df[variable1_name], df[variable2_name])
            moran_bv1 = Moran_BV(df[variable1_name], df[variable2_name], w)
            correlations.append(corr)
            MoranIs.append(moran_bv1.I)

            c.execute(f'SELECT * FROM {table_name}')
            rows = c.fetchall()

            # print the rows
            threshold1_set = []
            threshold2_set = []
            threshold1_coverage_spatial_set = []
            threshold1_coverage_normal_set=[]
            threshold2_coverage_spatial_set = []
            threshold2_coverage_normal_set = []
            agreement_set = []
            expected_set = []
            lift_set = []
            threhsoldCorrelation_coverage_set = []
            threhsoldCorrelation_set=[]
            threhsoldCorrelation_pval_set = []

            for row in rows:
                threshold1_set.append(row[1])
                threshold2_set.append(row[2])
                #threshold1_coverage_spatial_set.append(row[3])
                #threshold1_coverage_normal_set.append(row[4])
                #threshold2_coverage_spatial_set.append(row[5])
                #threshold2_coverage_normal_set.append(row[6])
                agreement_set.append(row[3])
                expected_set.append(row[4])
                lift_set.append(row[3]/row[4])
                #threhsoldCorrelation_coverage_set.append(row[10])
                #threhsoldCorrelation_set.append(row[11])
                #threhsoldCorrelation_pval_set.append(row[12])

            pattern.append(table_name)
            max_agreement.append(max(agreement_set))
            max_agreement_expected.append(expected_set[agreement_set.index(max(agreement_set))])
            threhsold1_max_agreement.append(threshold1_set[agreement_set.index(max(agreement_set))])
            threhsold2_max_agreement.append(threshold2_set[agreement_set.index(max(agreement_set))])

            #threhsold1_max_agreement_area_coverage.append(threshold1_coverage_spatial_set[agreement_set.index(max(agreement_set))])
            threhsold1_max_agreement_area_coverage.append(float(threshold_area_dict[variable1_name][str(threshold1_set[agreement_set.index(max(agreement_set))])]))
            #threhsold2_max_agreement_area_coverage.append(threshold2_coverage_spatial_set[agreement_set.index(max(agreement_set))])
            threhsold2_max_agreement_area_coverage.append(float(threshold_area_dict[variable2_name][str(threshold2_set[agreement_set.index(max(agreement_set))])]))

            lift_maxima.append(lift_set[agreement_set.index(max(agreement_set))])
            AUC_Agreement.append(sum(agreement_set)/len(agreement_set))
            AUC_Agreement_expected.append(sum(expected_set)/len(expected_set))

            c.execute(f'SELECT * FROM {table2_name}')
            rows = c.fetchall()
            for row in rows:
                threhsoldCorrelation_coverage_set.append(row[10])
                threhsoldCorrelation_set.append(row[11])
                threhsoldCorrelation_pval_set.append(row[12])

            threshold1_set_corr.append(threshold1_set[threhsoldCorrelation_set.index(max(threhsoldCorrelation_set, key=compare_with_none))])
            threshold2_set_corr.append(threshold2_set[threhsoldCorrelation_set.index(max(threhsoldCorrelation_set, key=compare_with_none))])

            CVT_correlation.append(max(threhsoldCorrelation_set, key=compare_with_none))
            CVT_correlation_value_coverage.append(
                threhsoldCorrelation_coverage_set[threhsoldCorrelation_set.index(max(threhsoldCorrelation_set, key=compare_with_none))])
            filtered_list = [x for x in threhsoldCorrelation_set if x is not None]
            CVT_correlation_AUC.append(sum(filtered_list) / len(threhsoldCorrelation_set))

            count += len(agreement_set)
    l += 1
ranks_AUC = stats.rankdata(AUC_Agreement)
ranks_maxima = stats.rankdata(max_agreement)
ranks_AUC_corr = stats.rankdata(CVT_correlation_AUC)
ranks_maxima_corr = stats.rankdata(CVT_correlation)
ranks_corr = stats.rankdata(correlations)
ranks_moran = stats.rankdata(MoranIs)
print("total pattern:",count, "rank correlation:")
print("Rank Correlation (Correlation Vs Maxima):", stats.spearmanr(ranks_corr, ranks_maxima))
print("Rank Correlation (Correlation Vs AUC):", stats.spearmanr(ranks_corr, ranks_AUC))
print("Rank Correlation (Maxima Vs AUC):", stats.spearmanr(ranks_maxima, ranks_AUC))
print("Rank Correlation (Correlation Vs CVTMaxima):", stats.spearmanr(ranks_corr, ranks_maxima_corr))
print("Rank Correlation (Correlation Vs CVTAUC):", stats.spearmanr(ranks_corr, ranks_AUC_corr))
print("Rank Correlation (CVTMaxima Vs CVTAUC):", stats.spearmanr(ranks_maxima_corr, ranks_AUC_corr))

print("Rank Correlation (MoranI Vs Maxima):", stats.spearmanr(ranks_moran, ranks_maxima))
print("Rank Correlation (MoranI Vs AUC):", stats.spearmanr(ranks_moran, ranks_AUC))
print("Rank Correlation (MoranI Vs CVTMaxima):", stats.spearmanr(ranks_moran, ranks_maxima_corr))
print("Rank Correlation (MoranI Vs CVTAUC):", stats.spearmanr(ranks_moran, ranks_AUC_corr))

print("Rank Correlation (Maxima Vs CVTMaxima):", stats.spearmanr(ranks_maxima, ranks_maxima_corr))
print("Rank Correlation (AUC Vs CVTAUC):", stats.spearmanr(ranks_AUC, ranks_AUC_corr))

print("Rank Correlation (CVTMaxima Vs CVTAUC):", stats.spearmanr(ranks_maxima, ranks_AUC))


import pandas as pd

'''
df = pd.DataFrame()
df['pattern'] = pattern
df['Pearson correlations'] = correlations
df['Bivariate Moran I'] = MoranIs
df['max_agreement'] = max_agreement
df['max_agreement_expected'] = max_agreement_expected
df['threhsold1_max_agreement'] = threhsold1_max_agreement
df['threhsold2_max_agreement'] = threhsold2_max_agreement
df['threhsold1_max_agreement_area_coverage'] = threhsold1_max_agreement_area_coverage
df['threhsold2_max_agreement_area_coverage'] = threhsold2_max_agreement_area_coverage
df['lift_maxima'] = lift_maxima

df['AUC_Agreement'] = AUC_Agreement
df['AUC_Agreement_expected'] = AUC_Agreement_expected
df['CVT_correlation_maxima'] = CVT_correlation
df['CVT_correlation_maxima_t1'] = threshold1_set_corr
df['CVT_correlation_maxima_t2'] = threshold2_set_corr
df['CVT_correlation_value_coverage_maxima'] = CVT_correlation_value_coverage
df['CVT_correlation_AUC'] = CVT_correlation_AUC

df['ranks_corr'] = ranks_corr
df['ranks_moran'] = ranks_moran
df['ranks_maxima'] = ranks_maxima
df['ranks_AUC'] = ranks_AUC
df['ranks_maxima_corr'] = ranks_maxima_corr
df['ranks_AUC_corr'] = ranks_AUC_corr



path = "C:/Users/mdmah/PycharmProjects/ProfessorEick/ProfessorEick/ThresholdOptimization/Outputs/TKDE/Agreements/Files/All/full_summary_data.csv"
df.to_csv(path,index=False)
'''