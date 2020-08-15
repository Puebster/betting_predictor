import pandas as pd
import datetime
import json
import sys
sys.path.append('../')


def feature_tablepos_spieltag(df):
    """
    Calculates features for position in the table and for gameday
    ------------------------------------
    input:  df (pd.DataFrame):
    ------------------------------------
    output:
            df with new features
    """
    print('Start joining basic features\n')
#    df = df.drop('season', axis=1)
#    df['datetime'] = df['datetime'].apply(lambda x:
#                                          str(x).split(' ')[0])
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    new_new = None
    d_seasons = {1213: [datetime.datetime(2012, 8, 22),
                        datetime.datetime(2013, 5, 19)],
                 1314: [datetime.datetime(2013, 8, 8),
                        datetime.datetime(2014, 5, 11)],
                 1415: [datetime.datetime(2014, 8, 22),
                        datetime.datetime(2015, 5, 24)],
                 1516: [datetime.datetime(2015, 8, 13),
                        datetime.datetime(2016, 5, 15)],
                 1617: [datetime.datetime(2016, 8, 25),
                        datetime.datetime(2017, 5, 21)],
                 1718: [datetime.datetime(2017, 8, 17),
                        datetime.datetime(2018, 5, 13)],
                 1819: [datetime.datetime(2018, 8, 23),
                        datetime.datetime(2019, 5, 19)],
                 1920: [datetime.datetime(2019, 8, 15),
                        datetime.datetime(2019, 12, 2)]}

    rename_dict = {'Borussia Dortmund': 'Dortmund',
                   'FC Augsburg': 'Augsburg',
                   'Eintracht Frankfurt': 'Frankfurt',
                   'SC Freiburg': 'Freiburg',
                   'SpVgg Greuther Fürth': 'Fürth',
                   'Hamburger SV': 'HSV',
                   'Borussia Mönchengladbach': 'Gladbach',
                   'VfB Stuttgart': 'Stuttgart',
                   'Hannover 96': 'Hannover',
                   '1. FSV Mainz 05': 'Mainz',
                   'Bayern München': 'Bayern',
                   '1. FC Nürnberg': 'Nürnberg',
                   'FC Schalke 04': 'Schalke',
                   'VfL Wolfsburg': 'Wolfsburg',
                   'Fortuna Düsseldorf': 'Düsseldorf',
                   'TSG 1899 Hoffenheim': 'Hoffenheim',
                   'Bayer Leverkusen': 'Leverkusen',
                   'Werder Bremen': 'Bremen',
                   'Hertha BSC': 'Hertha',
                   '1. FC Köln': 'Köln',
                   'SC Paderborn 07': 'Paderborn',
                   'SV Darmstadt 98': 'Darmstadt',
                   'FC Ingolstadt 04': 'Ingolstadt',
                   'RB Leipzig': 'Leipzig',
                   '1. FC Union Berlin': 'Union'}

    dict_names = []
    for i in d_seasons:
        one_season = df[(df['Date'] > d_seasons[i][0]) &
                        (df['Date'] < d_seasons[i][1])]
        one_season = one_season.sort_values(by='Date')
        season_names = list(one_season['AwayTeam'].unique())
        for missing_name in list(one_season['HomeTeam'].unique()):
            if missing_name not in season_names:
                season_names.append(missing_name)
        spieltag_per_team = {}
        for team_name in season_names:
            spieltag_per_team[team_name] = 0
        dict_file = ('C:/Users/Frido/Desktop/betting/bet_algo/files/' +
                     'tabellen_files/' + str(i) + '.json')

        with open(dict_file, 'r') as f:
            table = json.load(f)
        for spieltag in table:
            for position in table[spieltag]:
                position[0] = position[0].replace(' (N)', '')
                position[0] = position[0].replace(' (M, P)', '')
                position[0] = position[0].replace(' (M)', '')
                position[0] = position[0].replace(' (P)', '')
                if position[0] not in dict_names:
                    dict_names.append(position[0])

        h_teams_game_day = []
        h_teams_points = []
        h_goal_diff = []
        h_table_pos = []
        a_teams_game_day = []
        a_teams_points = []
        a_goal_diff = []
        a_table_pos = []
        new = pd.DataFrame(data={'IDX': list(one_season['IDX'].values)})
        H_A = list(zip(one_season.HomeTeam, one_season.AwayTeam))

        for combi in H_A:
            h = combi[0]
            a = combi[1]
            spieltag_h = spieltag_per_team[h]
            spieltag_a = spieltag_per_team[a]
            h_breakin = False
            a_breakin = False
            if spieltag_h == 0:
                h_teams_game_day.append(spieltag_h)
                h_teams_points.append(0)
                h_goal_diff.append(0)
                h_table_pos.append(1)
                spieltag_per_team[h] += 1
                h_breakin = True
            if spieltag_a == 0:
                a_teams_game_day.append(spieltag_a)
                a_teams_points.append(0)
                a_goal_diff.append(0)
                a_table_pos.append(1)
                spieltag_per_team[a] += 1
                a_breakin = True

            if not h_breakin:
                for row in table[str(spieltag_h)]:
                    if row[0] == rename_dict[h]:
                        h_teams_game_day.append(spieltag_h)
                        h_teams_points.append(row[3])
                        h_goal_diff.append(row[2])
                        h_table_pos.append(table[str(spieltag_h)].index(row))
                        spieltag_per_team[h] += 1
                        break
                    if row == table[str(spieltag_h)][17]:
                        h_teams_game_day.append(spieltag_h)
                        h_teams_points.append(None)
                        h_goal_diff.append(None)
                        h_table_pos.append(None)
                        spieltag_per_team[h] += 1
            if not a_breakin:
                for row in table[str(spieltag_a)]:
                    if row[0] == rename_dict[a]:
                        a_teams_game_day.append(spieltag_a)
                        a_teams_points.append(row[3])
                        a_goal_diff.append(row[2])
                        a_table_pos.append(table[str(spieltag_a)].index(row))
                        spieltag_per_team[a] += 1
                        break
                    if row == table[str(spieltag_a)][17]:
                        a_teams_game_day.append(spieltag_a)
                        a_teams_points.append(None)
                        a_goal_diff.append(None)
                        a_table_pos.append(None)
                        spieltag_per_team[a] += 1

        new['HTGD'] = h_teams_game_day
        new['ATGD'] = a_teams_game_day
        new['HP'] = h_teams_points
        new['AP'] = a_teams_points
        new['HTTP'] = h_table_pos
        new['ATTP'] = a_table_pos
        new['HGD'] = h_goal_diff
        new['AGD'] = a_goal_diff

        if new_new is None:
            new_new = new
        else:
            new_new = pd.concat([new_new, new], ignore_index=False)

        if i == 1920:
            print('Saison ' + str(i) + ': ' + str(one_season.shape[0]) +
                  ' --- Fehlen: ' + str(9 * 11 - one_season.shape[0]) +
                  ', sind: ' +
                  str(round(((9 * 11 - one_season.shape[0]) / 306) * 100, 2)) +
                  '%')
        else:
            print('Saison ' + str(i) + ': ' + str(one_season.shape[0]) +
                  ' --- Fehlen: ' + str(306 - one_season.shape[0]) +
                  ', sind: ' +
                  str(round(((306 - one_season.shape[0]) / 306)*100, 2)) + '%')

    new_df = df.merge(new_new, how='inner', on='IDX')
    print('Gesamt: ' + str(new_df.shape[0]) +
          ' --- Fehlen: ' + str(306 * 7 + 9 * 11 - new_df.shape[0]) +
          ', sind: ' + str(round(((306 * 7 + 9 * 11 - new_df.shape[0]) /
                                  306 * 7 + 9 * 11) * 1, 2)) + '%')

    return new_df


if __name__ == '__main__':
    a = pd.read_csv('C:/Users/Frido/Desktop/betting/bet_algo/files/output_files/jannis_features.csv', index_col=0)
    a = a.drop(['IDX'], axis=1)
    b = a.drop(['Date', 'HomeTeam','AwayTeam', 'FTR', 'FTAG', 'FTHG'], axis=1)
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from matplotlib import pyplot as plt
    # Separating out the features
    x = a.iloc[:, 6:].values
    # Separating out the target
    y = a.loc[:,['FTR']].values
    # Standardizing the features
    x = StandardScaler().fit_transform(x)
    pca = PCA(n_components=6)
    principalComponents = pca.fit_transform(x)

    principalDf = pd.DataFrame(data = principalComponents
                 , columns = ['PC 1', 'PC 2', 'PC 3', 'PC 4', 'PC 5', 'PC 6'])
    finalDf = pd.concat([principalDf, a[['FTR']]], axis = 1)
    what = pd.DataFrame(pca.components_,columns=b.columns,index = ['PC 1', 'PC 2', 'PC 3', 'PC 4', 'PC 5', 'PC 6'])
    what = what.transpose()
    what['PC 1'] = what['PC 1']
#    fig = plt.figure(figsize = (8,8))
#    ax = fig.add_subplot(1,1,1)
#    ax.set_xlabel('PC 1', fontsize = 15)
#    ax.set_ylabel('PC 2', fontsize = 15)
#    ax.set_xlabel('PC 3', fontsize = 15)
#    ax.set_ylabel('PC 4', fontsize = 15)
#    ax.set_title('2 component PCA', fontsize = 20)
#    targets = [0, 1, 2]
#    colors = ['r', 'g', 'b']
#    for target, color in zip(targets,colors):
#        indicesToKeep = finalDf['FTR'] == target
#        ax.scatter(finalDf.loc[indicesToKeep, 'PC 1']
#                   , finalDf.loc[indicesToKeep, 'PC 2']
#                   , finalDf.loc[indicesToKeep, 'PC 3']
#                   , finalDf.loc[indicesToKeep, 'PC 4']
#                   , c = color
#                   , s = 50)
#    ax.legend(targets)
#    ax.grid()

    print(pca.explained_variance_ratio_)
    print(sum(pca.explained_variance_ratio_))
