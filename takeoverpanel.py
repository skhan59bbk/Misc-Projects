import pandas as pd
from datetime import datetime
import os


def download_and_reformat():

    url = 'https://www.thetakeoverpanel.org.uk/new/disclosureTable/v3/disclosuretable.csv'
    os.makedirs('..//Testing//takeover//disclosure tables/', exist_ok=True)

    df = pd.read_csv(url, encoding='latin1')
    df.rename(columns={"Unnamed: 0": "F1", "Unnamed: 1": "F2", "Unnamed: 2": "F3",}, inplace=True)

    actual_datekey = datetime.today().strftime('%Y%m%d')
    file_datekey = df.iloc[2,0]
    file_datekey = file_datekey[-4:] + file_datekey[3:5] + file_datekey[:2]

    if actual_datekey != file_datekey:
        print('Warning: Check date in file')

    table_start = df[df.F1 == 'DISCLOSURE TABLE'].index[0]
    table_end = df[df.F1 == 'Notes:'].index[0]
    df = df.iloc[table_start:table_end]
    df.reset_index(inplace=True)
    df.drop('index', axis=1, inplace=True)
    df.to_csv('..//Testing//takeover//disclosure tables//disclosuretable_' + actual_datekey + '.csv', index=False)

    return df


def extract_key_data():

 
    df = download_and_reformat()
    dropnan = df.dropna(subset=['F1'])
    dropnan.reset_index(inplace=True)
    dropnan = dropnan.drop('index', axis=1)

    offerees = dropnan['F1'][dropnan['F1'].str.contains('OFFEREE')]
    offerees_list = [offeree.replace('OFFEREE: ', '') for offeree in offerees]
    offerees_index = list(dropnan.index[dropnan['F1'].str.contains('OFFEREE')])
    offerees_from = offerees_index
    offerees_to = offerees_index[1:]
    offerees_to.append(len(dropnan))

    offerors = dropnan['F1'][dropnan['F1'].str.contains('OFFEROR')]
    offerors_list = [offeror.replace('OFFEROR: ', '') for offeror in offerors]
    offerors_index = list(dropnan.index[dropnan['F1'].str.contains('OFFEROR')])
    offerors_from = offerors_index
    offerors_to = offerees_index[1:]
    offerors_to.append(len(dropnan))

    idx_offeree_to_offeree = [[offerees_from[i], offerees_to[i]] for i in range(len(offerees_index))]
    idx_offeree_details = [[offerees_from[j], offerors_from[j]] for j in range(len(offerees_index))]

    full_list = []

    for i in range(len(idx_offeree_to_offeree)):

        temp_list = []

        for col in dropnan.columns:
            details = [el for el in dropnan[col][idx_offeree_to_offeree[i][0]:idx_offeree_to_offeree[i][1]]]
            temp_list.append(details)

        index_of_offerors = [i for i in range(len(temp_list[0])) if temp_list[0][i][:7] == 'OFFEROR']
        offeree_data = []
        offeree_data.append(temp_list[0][0])
        offeree_isin = [el for el in temp_list[1][:index_of_offerors[0]] if not pd.isnull(el)]

        if len(offeree_isin) > 1:
            for i in range(len(offeree_isin)):
                offeree_data.append(offeree_isin[i])

        else:
             offeree_data.append(','.join(offeree_isin))

        offeror_data = []
        for i in range(len(index_of_offerors)):
            offeror = []
            offeror.append(temp_list[0][index_of_offerors[i]])

            ### if not the last offeror in the list...

            if i != len(index_of_offerors)-1:
                offeror_isin = [el for el in temp_list[1][index_of_offerors[i]:index_of_offerors[i+1]] if not pd.isnull(el)]
                if len(offeror_isin) > 1:
                    for i in range(len(offeror_isin)):
                        offeror.append(offeror_isin[i])
                else:
                    offeror.append(','.join(offeror_isin))                                                      
           
                    if temp_list[0][index_of_offerors[i+1]-1] != 'Disclosure of dealings and positions in this offeror is not required':
                        offeror.append('Disclose')
                    else:
                        offeror.append('Do not disclose')



            ### if the last offeror

            else:
                offeror_isin = [el for el in temp_list[1][index_of_offerors[i]:] if not pd.isnull(el)]
                if len(offeror_isin) > 1:
                    for i in range(len(offeror_isin)):
                        offeror.append(offeror_isin[i])
                else:
                    offeror.append(','.join(offeror_isin))
                        if temp_list[0][-1] != 'Disclosure of dealings and positions in this offeror is not required':
                            offeror.append('Disclose')
                        else:
                            offeror.append('Do not disclose')
            offeror_data.append(offeror)

        for i in range(len(index_of_offerors)):
            full_list.append([*offeree_data, *offeror_data[i]])


    return full_list
 

def output_dataframe():
    key_data = extract_key_data()
    datekey = datetime.today().strftime('%Y%m%d')
    desired_columns = ['Offeree Name', 'Offeree ISIN 1', 'Offeree ISIN 2', 'Offeror Name', 'Offeror ISIN 1', 'Offeror ISIN 2', 'Offeror Requirement', 'DateKey']

    for i in range(len(key_data)):
        if key_data[i][0][:7] != 'OFFEREE' and key_data[i][0] != '':
            key_data[i].insert(0, '')
        else:
            key_data[i][0] = key_data[i][0].replace('OFFEREE: ', '').replace(',', '')[:40]
                
                if key_data[i][1][:4] != 'ISIN' and key_data[i][1] != '':
                    key_data[i].insert(1, '')
                else:
                   key_data[i][1] = key_data[i][1].replace('ISIN: ', '')

                if key_data[i][2][:4] != 'ISIN' and key_data[i][2] != '':
                     key_data[i].insert(2, '')
                else:
                    key_data[i][2] = key_data[i][2].replace('ISIN: ', '')
           
                if key_data[i][3][:7] != 'OFFEROR' and key_data[i][3] != '':
                    key_data[i].insert(3, '')
                else:
                    key_data[i][3] = key_data[i][3].replace('OFFEROR: ', '').replace(',', '')[:40]
               
                if key_data[i][4][:4] != 'ISIN' and key_data[i][4] != '':
                    key_data[i].insert(4, '')
                else:
                    key_data[i][4] = key_data[i][4].replace('ISIN: ', '')

                if key_data[i][5][:4] != 'ISIN' and key_data[i][5] != '':
                    key_data[i].insert(5, '')
                else:
                    key_data[i][5] = key_data[i][5].replace('ISIN: ', '')
               
                if key_data[i][6][:1] != 'D' and key_data[i][6] != '':
                    key_data[i].insert(6, '')

                key_data[i].insert(7, datekey)


    df = pd.DataFrame(key_data)

    df.rename(columns={
                0: desired_columns[0],
                1: desired_columns[1],
                2: desired_columns[2],
                3: desired_columns[3],
                4: desired_columns[4],
                5: desired_columns[5],
                6: desired_columns[6],
                7: desired_columns[7]
                }, inplace=True)

 
    output_dir = '..//company//data//datafeeds//temp//takeoverpanel//'
    df.to_csv(output_dir + 'disclosure-table-' + datekey + '.csv', index=False)
    output_dir_ops = '..//company//operations//takeover panel list//disclosure tables//'
    df.to_csv(output_dir_ops + 'disclosure-table-' + datekey + '.csv', index=False)

 

 

if __name__ == '__main__':
    output_dataframe()