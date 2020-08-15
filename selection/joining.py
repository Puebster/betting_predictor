import pandas as pd
import numpy as np
import json
import datetime
from datetime import timedelta

def levenshtein(s1, s2):
    """
    levenshtein algorithm calculates how close two strings are
    runtime = O(s_x*s_y)
    ------------------------------------
    input:  s1, s2 = strings to compare
    ------------------------------------
    output levenshtein distance
    """
    s_x = len(s1) + 1
    s_y = len(s2) + 1
    # create a Matrix with width and height of the two strings
    matrix = np.zeros((s_x, s_y))
    for x in range(s_x):
        matrix[x, 0] = x
    for y in range(s_y):
        matrix[0, y] = y
    # compare the strings letter by letter - row-wise, and column-wise.
    for x in range(1, s_x):
        for y in range(1, s_y):
            if s1[x-1] == s2[y-1]:
                matrix[x, y] = min(
                    matrix[x-1, y]+1,
                    matrix[x-1, y-1],
                    matrix[x, y-1]+1)
            else:
                matrix[x, y] = min(
                    matrix[x-1, y]+1,
                    matrix[x-1, y-1]+1,
                    matrix[x, y-1]+1)
    return (matrix[s_x-1, s_y-1])


def create_name_map_dict(l1, l2):
    """
    Gets the closest string match of column one to column two
    ------------------------------------
    input:  l1, l2 (list(str)) = list with strings
    ------------------------------------
    output name_map_dict: dictionary with the name mapping
    """
    name_map_dict = {}
    # compare string one to all strings from the second list
    for s1 in l1:
        s_dist = 10000
        for s2 in l2:
            dist = levenshtein(s1, s2)
            # if the distance is closer then change the remap_string
            if dist < s_dist:
                s_dist = dist
                remap_string = s2
        # insert the entry
        name_map_dict[s1] = remap_string

# some hardcoding GERMAN 1
    name_map_dict['FC Koln'] = '1. FC Köln'
    name_map_dict['Mainz'] = '1. FSV Mainz 05'
    name_map_dict['Nurnberg'] = '1. FC Nürnberg'
    name_map_dict['Dortmund'] = 'Borussia Dortmund'
    name_map_dict["M'gladbach"] = 'Borussia Mönchengladbach'
    name_map_dict['Hoffenheim'] = 'TSG 1899 Hoffenheim'
    name_map_dict['RB Leipzig'] = 'RBLeipzig'
    not_found = ['Cottbus', 'Bielefeld', 'Braunschweig', 'Aachen']

#    for i in name_map_dict:
#        print(i, name_map_dict[i])
#    print('------------------------------------')
    for i in not_found:
        if i not in name_map_dict:
            print(i + ' not in dataframe')
        else:
            del name_map_dict[i]
    return name_map_dict, not_found


def feature_elo(df, elo):
    """
    joins the dataframes to eloratings
    ------------------------------------
    input:  df (pandas.DataFrame): footballdataset
            elo (pandas.DataFrame): elo-rating of the
            idx_to_name (dict): dictionary that contains all keys
    ------------------------------------
    output df: joined data
    """
    # some preprocessing of the data
    df = df.drop(['HTHG', 'HTAG', 'HS', 'AS', 'HST', 'AST', 'HF',
                  'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR', 'Season',
                  'HTR'# ,'Date', 'Div', 'home_team_ran', 'away_team_ran'
                  ], axis=1)
#    try:
#        df['datetime'] = pd.to_datetime(df['datetime'], format='%d-%m-%Y')
#    except Exception:
#        try:
#            df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d')
#        except Exception as d8_err2:
#            print(d8_err2)
#    try:
#        elo['date'] = pd.to_datetime(elo['date'], format='%d %b %Y')
#    except Exception as elo_date_err:
#        print(elo_date_err)

    # apply idx_to_name to dataframe
#    df = df.replace({'HomeTeam': idx_to_name, 'AwayTeam': idx_to_name})

    # create a dict with the remapping names from elo to dataframe
    list_elo_names = list(elo['name'].unique())
    list_data_names = list(df['HomeTeam'].unique())
    rename_dict, list_no_elo = create_name_map_dict(list_data_names,
                                                    list_elo_names)

    df['HomeTeam'] = df['HomeTeam'].map(rename_dict)
    df['AwayTeam'] = df['AwayTeam'].map(rename_dict)
    df = df.dropna()
    elos_as_dict = {}

    # put elo into a dictionary
    for team in list(rename_dict.values()):
        if team in list_no_elo:
            continue
        if team == 'RBLeipzig':
            ins_df = elo.loc[elo['name'] == 'RB Leipzig', :].copy()
        else:
            ins_df = elo.loc[elo['name'] == team, :].copy()
        ins_df = ins_df.reset_index(drop=True)
        elos_as_dict[team] = ins_df
    # find closest elo
    H_ELO = []
    A_ELO = []
    for kk, row in enumerate(list(zip(df.HomeTeam, df.AwayTeam, df.Date))):
        new_date_diff = None
        for duo in list(zip(elos_as_dict[row[0]].date, elos_as_dict[row[0]].rating)):
            if new_date_diff is None:
                new_date_diff = datetime.datetime.strptime(duo[0], '%d %b %Y') - row[2]
                elo = duo[1]
            if datetime.datetime.strptime(duo[0], '%d %b %Y') < row[2] + timedelta(days=1):
                break
            elif datetime.datetime.strptime(duo[0], '%d %b %Y') - row[2] < new_date_diff:
                new_date_diff = datetime.datetime.strptime(duo[0], '%d %b %Y') - row[2]
                elo = duo[1]
        H_ELO.append(elo)

        new_date_diff = None
        for duo in list(zip(elos_as_dict[row[1]].date, elos_as_dict[row[1]].rating)):
            if new_date_diff is None:
                new_date_diff = datetime.datetime.strptime(duo[0], '%d %b %Y') - row[2]
                elo = duo[1]
            if datetime.datetime.strptime(duo[0], '%d %b %Y') < row[2] + timedelta(days=1):
                break
            elif datetime.datetime.strptime(duo[0], '%d %b %Y') - row[2] < new_date_diff:
                new_date_diff = datetime.datetime.strptime(duo[0], '%d %b %Y') - row[2]
                elo = duo[1]
        A_ELO.append(elo)
        if kk % 50 == 0:
            print(kk)

    df['H_ELO'] = H_ELO
    df['A_ELO'] = A_ELO
    df = df.sort_values(by='Date').reset_index(drop=True)
    df['IDX'] = [i for i in range(df.shape[0])]
    return df


if __name__ == '__main__':
    df_path = ('C:/Users/Frido/Desktop/betting/bet_algo/files/output_files/' +
               'germany_data_set.csv')
    df = pd.read_csv(df_path, index_col=0)
    df = df.drop(['A_ELO', 'H_ELO'], axis=1)
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    df = df[df['Date'] > datetime.datetime(2012, 8, 22)]

    elo_path = 'C:/Users/Frido/Desktop/betting/bet_algo/test/ratings.csv'
    elo = pd.read_csv(elo_path, index_col=0)

#    dict_file = 'C:/Users/Frido/Desktop/betting/bet_algo/test/team_ids.json'
#    with open(dict_file, 'r') as f:
#        name_to_idx = json.load(f)
#    idx_to_name = {v: k for k, v in name_to_idx.items()}

    test = feature_elo(df, elo)
