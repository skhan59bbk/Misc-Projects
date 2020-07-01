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

### Satisfaction ###

satisfaction = summary.iloc[:,1:10]

boroughs = [b for b in satisfaction['Area'] if str(b) != 'nan']
years = [year for year in range(2012, 2020)]

satisfaction = satisfaction.set_index('Area')
df = pd.DataFrame({'Year': years}) 
df = df.set_index('Year')

for borough in boroughs:
    df[borough] = [score for score in satisfaction.loc[borough]]


def satisfaction_chart():

    print('')
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


def most_satisfied_borough(year):
    max_borough = ''
    highest = 0
    for borough in boroughs[1:33]:
        if str(df[borough].loc[year]) != 'nan':
            if df[borough].loc[year] > highest:
                highest = df[borough].loc[year]
                max_borough = borough

    print(max_borough, highest)


def least_satisfied_borough(year):
    min_borough = ''
    lowest = 10
    for borough in boroughs[1:33]:
        if str(df[borough].loc[year]) != 'nan':
            if df[borough].loc[year] < lowest:
                lowest = df[borough].loc[year]
                min_borough = borough

    print(min_borough, lowest)


def scatter(borough_one, borough_two):

    print(df[[borough_one, borough_two]])
    fig, ax = plt.subplots()
    plt.scatter(df[borough_one], df[borough_two], c=('red','blue','green','black','orange','purple','yellow','pink'))
    plt.xlabel(borough_one)
    plt.ylabel(borough_two)
    plt.show()
    


def satisfaction_main():
    print('Most satisfied')
    for year in years:
        print(year, end=' ')
        most_satisfied_borough(year)

    print('')
    print('Least satisfied')
    for year in years:
        print(year, end=' ')
        least_satisfied_borough(year)

    satisfaction_chart()


def main():
    satisfaction_main()
    #scatter('Bromley', 'Hounslow')
 


if __name__ == '__main__':
    main()

