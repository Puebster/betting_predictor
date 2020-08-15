import os
from os.path import isfile, join
import datetime
import pandas as pd
import json
import numpy


def get_files_in_dir(path, file_ending='folder'):
    """
    gets all sub-folders of a directory
    ------------------------------------
    input:  path(str): string from path of directory to search for
            file_ending(str): format to look for. if 'folder' only look
                              for folders
    ------------------------------------
    output: list of strings to subfiles or folders
    """
    if file_ending == 'folder':
        return [x[0].replace('\\', '/') for x in os.walk(path)][1:]
    else:
        files = [x[2] for x in os.walk(path)][0]
        return [path + '/' + y for y in files
                if y.split('.')[-1] == file_ending]


def convert_elo_files_to_csv():
    path = 'C:/Users/Frido/Desktop/betting/bet_algo/ratingFiles/'
    folders = get_files_in_dir(path)
    for folder in folders:

        onlyfiles = [f for f in os.listdir(folder) if isfile(join(folder, f))]
        full_df = None
        for file in onlyfiles:
            print(file)
            sub_df = pd.read_csv(folder + '/' + file, error_bad_lines=False)
            sub_df = sub_df.drop(['Rank'], axis = 1)
            try:
                sub_df['From'] = pd.to_datetime(sub_df['From'], format='%d-%m-%Y')
            except Exception:
                try:
                    sub_df['From'] = pd.to_datetime(sub_df['From'],
                                                    format='%d-%m-%y')
                except Exception:
                    try:
                        sub_df['From'] = pd.to_datetime(sub_df['From'],
                                                        format='%Y-%m-%d')
                    except Exception as date_error:
                        print('Couldnt convert date column appropriatly')
                        print(date_error)
            try:
                #
                sub_df['To'] = pd.to_datetime(sub_df['To'], format='%d-%m-%Y')
            except Exception:
                try:
                    sub_df['To'] = pd.to_datetime(sub_df['To'],
                                                    format='%d-%m-%y')
                except Exception:
                    try:
                        sub_df['To'] = pd.to_datetime(sub_df['To'],
                                                        format='%Y-%m-%d')
                    except Exception as date_error:
                        print('Couldnt convert date column appropriatly')
                        print(date_error)
            sub_df = sub_df[sub_df.From > datetime.datetime(2004, 1, 1, 00, 00)]
            if full_df is None:
                full_df = sub_df
            else:
                full_df = pd.concat([full_df, sub_df], ignore_index=True,
                                    sort=False)
        full_df.to_csv(folder + '/' +  folder.split('/')[-1] +
                       '_rating_2004.csv', index=False)

    print("fertig")

def create_full_dataset(path, save=True):
    """
    creates a full dataframe from preprocessed football.uk datasets
    ------------------------------------
    input:  path(str): string from path of directory with datasets
    ------------------------------------
    output: full_dataset(pd.DataFrame):list of strings to subfiles or folders
    """
    files = get_files_in_dir(path, 'csv')
    full_df = pd.DataFrame()
    rename_dict = {}
    team_id = 0

    for file in files:
        sub_df = pd.read_csv(file, error_bad_lines=False)
        # drop unnessecary columns
        sub_df = sub_df.drop('Div', axis=1)
        sub_df = sub_df[sub_df.columns[:27]]
        # convert dates and times into appropriate format
        print(file)
        sub_df['Date'] = sub_df['Date'].apply(lambda x:
                                              str(x).replace('/', '-'))

        try:
            sub_df['Date'] = pd.to_datetime(sub_df['Date'], format='%d-%m-%Y')
        except Exception:
            try:
                sub_df['Date'] = pd.to_datetime(sub_df['Date'],
                                                format='%d-%m-%y')
            except Exception:
                try:
                    sub_df['Date'] = pd.to_datetime(sub_df['Date'],
                                                    format='%Y-%m-%d')
                except Exception as date_error:
                    print('Couldnt convert date column appropriatly')
                    print(date_error)

        seas = (str(sub_df['Date'].min()).split('-')[0][2:] +
                '/' + str(sub_df['Date'].max()).split('-')[0][2:])
        if 'Time' in sub_df.columns:
            sub_df['Time'] = pd.to_datetime(sub_df['Time'],
                                            infer_datetime_format=True)
        # convert data in Result colums into an integers
        rd = {'H': 0, 'D': 1, 'A': 2}
        sub_df = sub_df.replace({"FTR": rd, "HTR": rd})
        sub_df['Season'] = seas
        # convert Date into dateTime-format
        full_df = pd.concat([full_df, sub_df], ignore_index=True, sort=False)

    # do some cleaning:
    # update the Team dictionary
    unnamed = [x for x in full_df.columns if 'Unnamed' in x]
    full_df = full_df.drop(unnamed, axis=1)
    needed_list_d2 = ['Date', 'HomeTeam', 'AwayTeam',
                      'FTHG', 'FTAG', 'FTR', 'HTAG',
                      'HTR', 'HS', 'AS', 'HST', 'AST',
                      'HF', 'AF', 'HC', 'AC', 'HY',
                      'AY', 'HR', 'AR', 'B365H', 'B365D',
                      'B365A', 'BWH', 'BWD', 'BWA', 'Season']

    for col in full_df.columns:
        if col not in needed_list_d2:
            full_df = full_df.drop(col, axis=1)
    for team_name in full_df.HomeTeam.unique():
        if team_name not in rename_dict:
            rename_dict[team_name] = team_id
            team_id += 1
        else:
            continue
    full_df = full_df.replace({'HomeTeam': rename_dict,
                               'AwayTeam': rename_dict})
    if save:
        #only for DE
#        make_new = list(zip(full_df.HS, full_df.AS, full_df.HST, full_df.AST))
#        HST = []
#        AST = []
#        for quad in make_new:
#            if numpy.isnan(quad[2]):
#                HST.append(int(round(quad[0]/3)))
#            else:
#                HST.append(quad[2])
#            if numpy.isnan(quad[3]):
#                AST.append(int(round(quad[1]/3)))
#            else:
#                AST.append(quad[3])
#        full_df['HST'] = HST
#        full_df['AST'] = AST
#        full_df = full_df.drop(['GBH', 'GBD', 'Time'], axis=1)
#
#        quto = 0
#        qut = True
#        make_new = list(zip(full_df.BWH, full_df.BWD, full_df.BWA))
#        BWA = []
#        tot_sum = 0
#        for trip in make_new:
#            if numpy.isnan(trip[2]):
#                schlussel = tot_sum/quto
#                qut = False
#                BWA.append(round(1/(schlussel - 1/trip[0] - 1/trip[1]), 2))
#            else:
#                BWA.append(trip[2])
#            if qut:
#                quto += 1
#                tot_sum += (1/trip[0] + 1/trip[1] + 1/trip[2])
#        full_df['BWA'] = BWA

        full_df.to_csv(path + '/' + 'full_dataset_' +
                       path.split('/')[-1] + '.csv')
        json.dump(rename_dict, open(path + '/' + 'team_ids.json', 'w'))

    return full_df, rename_dict


def csv_data_clean(path, new=False):
    """
    cuts the csv files from the football.uk website into 27 columns
    ------------------------------------
    input:  path(str): path to the csv file
            new (bool): shall the file be safed in a new folder
    ------------------------------------
    output:
            nothing, writes a new file to the location
    """
    # ## cut csv to amount of lines
    folders = get_files_in_dir(path)
    for folder in folders:
        files = get_files_in_dir(folder.replace('\\', '/'), 'csv')
        for file in files:
            f = open(file, 'r')
            lines = f.readlines()
            f.close()
            for col_num, line in enumerate(lines):
                if col_num == 0:
                    df = pd.DataFrame(columns=line.split(',')[:27])
                else:
                    insert = line.split(',')[:27]
                    df.loc[col_num-1] = insert
            if new:
                new_path = file.replace(file.split('/')[-1],
                                        'new/' + file.split('/')[-1])
                df.to_csv(new_path, index=False)
                print(file.split('/')[-1] + ' fertig')
            else:
                df.to_csv(file, index=False)
                print(file.split('/')[-1] + ' fertig')

if __name__ == '__main__':
#    csv_data_clean('C:/Users/Frido/Desktop/Datasets/bet_algo/datasets')
#    path = 'C:/Users/Frido/Desktop/betting/bet_algo/datasets'
#    # ## cut csv to amount of lines
#    folders = get_files_in_dir(path)
#    for folder in folders:
#        if os.path.exists(folder + '/team_ids.json'):
#            print('\nAlready a dataset in the folder:\n' + path)
#            continue
#        print(folder)
#        a, c = create_full_dataset(folder)
#        print('done\n')



#    path = 'C:/Users/Frido/Desktop/betting/bet_algo/ratingFiles/Germany'
#    sub_df = pd.read_csv(path + '/Düsseldorf', error_bad_lines=False)
    convert_elo_files_to_csv()