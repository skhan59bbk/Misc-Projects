import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pd.set_option('display.width', None)

file = 'C://Users//samee//Documents//Datasets//personal-well-being-borough.xlsx'

data = pd.ExcelFile(file)
#print(data.sheet_names)

meta = pd.read_excel(data, 0)
summary = pd.read_excel(data, 1, header=1)
satisfied = pd.read_excel(data, 2)
worthwhile = pd.read_excel(data, 3)
happy = pd.read_excel(data, 4, header=1)
anxiety = pd.read_excel(data, 5)

#print(meta)

satisfaction = summary.iloc[:,1:10]
boroughs = [b for b in satisfaction['Area'] if str(b) != 'nan']

satisfaction = satisfaction.set_index('Area')

years = [year for year in range(2012, 2020)]
isling = [score for score in satisfaction.loc['Islington']]
walth = [score for score in satisfaction.loc['Waltham Forest']]


df = pd.DataFrame({'Year': years}) 
df = df.set_index('Year')

for borough in boroughs:
    df[borough] = [score for score in satisfaction.loc[borough]]

print(boroughs[1:33])
print('')
finished = False

while not finished:
    
    choice = input('Choose a borough (or hit Enter to quit): ')
    if choice == '':
        finished = True
        break

    fig, ax = plt.subplots()
    ax.plot(df[choice], label=choice, color='green')
    ax.plot(df['London'], label='London', linestyle='--', color='red')
    ax.plot(df['UK'], label='UK', linestyle='--', color='blue')
    ax.set_title(str(meta['Personal well-being scores by Borough'][23])+' Average Score Per Year. Scored 0-10 (10 most satisfied)', loc='center', wrap=True)
    plt.legend()
    plt.show()

