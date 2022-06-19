import pandas as pd
'''
df = pd.read_csv("RawData/covid-us-counties-recent_trimmed.csv")

fips = []
cases = []
deaths = []
for count in range(len(df['fips'])):
    if not(pd.isna(df['fips'][count])):
        #print(int(df['fips'][count]),int(df['cases'][count]), int(df['deaths'][count]))
        fips.append(int(df['fips'][count]))
        if not(pd.isna(df['cases'][count])):
            cases.append(int(df['cases'][count]))
        else:
            cases.append(float('NaN'))
        if not(pd.isna(df['deaths'][count])):
            deaths.append(int(df['deaths'][count]))
        else:
            deaths.append(float('NaN'))



new_df = pd.DataFrame()
new_df['fips'] = fips
new_df['cases'] = cases
new_df['deaths'] = deaths

new_df.to_csv('InitialExtractedData/covid.csv', index= False)
'''
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
df = pd.read_csv("RawData/PopulationEstimates.csv")
df2 = pd.read_csv("InitialExtractedData/dataset_combined.csv")
covid_cases_density = []
covid_death_density = []
for count in range(len(df2['FIPS'])):
    if df2['FIPS'][count] in df['FIPS'].values:
        index = ((df.index[df['FIPS']==df2['FIPS'][count]]).values)[0]
        if not(pd.isna(df['POP_ESTIMATE_2018'][index])):
            value = locale.atoi(df['POP_ESTIMATE_2018'][index]) #int((df['POP_ESTIMATE_2018'][index]).replace("\"",""))
            covid_cases_density.append(df2['covid_cases'][count]/value)
            covid_death_density.append(df2['covid_deaths'][count]/value)


df2['covid_cases_density'] = covid_cases_density
df2['covid_death_density'] = covid_death_density
df2.to_csv("InitialExtractedData/dataset_combined.csv", index= False)