import pandas as pd

df = pd.read_csv("C:/Users/mdmah/Downloads/abalone.csv")
for item in df:
    print(item)
df['Age'] = ['']*len(df['Rings'])
count = 0
for item in df['Rings']:
    if int(df['Rings'][count]) >= 0 and int(df['Rings'][count]) <= 9:
        df['Age'][count] = 'Y'
    elif int(df['Rings'][count]) >= 10 and int(df['Rings'][count]) <= 13:
        df['Age'][count] = 'M'

    else:
        df['Age'][count] = 'O'
    count += 1

df.to_csv("C:/Users/mdmah/Downloads/YAbalone.csv",index= False)