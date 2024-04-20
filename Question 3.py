import pandas as pd
import numpy as np

with open("C:/Users/User/Downloads/Ace/Q3.txt") as file:
    lines = file.readlines()

columns = [line.strip().split(' ') for line in lines]
dt = pd.DataFrame(columns)
dt = dt.T
dt = dt.applymap(lambda x: str(x).replace(',', '').replace('.', '').replace('(', '').replace(')', '').replace(':', '').replace('-', ''))
dt.replace(to_replace='None', value=np.nan, inplace=True)


#Question 3a
data_by_line = {}
for x in dt.columns:
    data_by_line[x] = dt[x].str.contains('data', na=False).sum()/len(dt)*100

Q3a = pd.DataFrame(list(data_by_line.items()), columns=['line', 'Probability of data'])

print(data_by_line)
print(Q3a)



#Question 3b
from collections import Counter
data = dt.values.flatten()
data = [word for word in data if pd.notna(word)]
frequency = Counter(data)
word_frequency = pd.DataFrame(list(frequency.items()), columns=['Word', 'Frequency'])
Q3b = word_frequency.sort_values(by='Frequency', ascending=False)
print(Q3b)



#Question Q3c
combine = dt.melt(var_name='line')
print(combine)
P_data = combine['value'].str.contains('data').sum()/len(combine)*100

P_datananalytics = (combine['value'].str.contains('data', case=False)
                    & combine['value'].shift(-1).str.contains('analytics')).sum() / len(combine) * 100

Q3c = (P_datananalytics/P_data*100)
print(Q3c)






