import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pd.set_option('display.width', None)

file = 'C://Users//samee//Documents//Datasets//personal-well-being-borough.xlsx'

data = pd.ExcelFile(file)
#print(data.sheet_names)

meta = pd.read_excel(data, 0)
summary = pd.read_excel(data, 1, header=0)
satisfied = pd.read_excel(data, 2)
worthwhile = pd.read_excel(data, 3)
happy = pd.read_excel(data, 4, header=1)
anxiety = pd.read_excel(data, 5)

#print(df.columns)
#print(df[['Code', 'Area', '2018/19.3', '2017/18.3']].head(20))
#print(df[df['Area'] == 'Waltham Forest'])

#print(meta)
#print(summary.iloc[:,8:13].head())
satisfaction = summary.iloc[:,1:10]

print(satisfaction.head(20))

