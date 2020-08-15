import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import keras.callbacks
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
import keras.optimizers
import keras.initializers
from sklearn.model_selection import StratifiedKFold #, train_test_split, KFold
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.externals import joblib
from sklearn.metrics import classification_report
import datetime
import pickle

def initialize_nn(nn_architecture):
    model = Sequential()
    go = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, amsgrad=False)
    # go = keras.optimizers.SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
    init = keras.initializers.RandomUniform(minval=-0.01, maxval=0.01, seed=7)
    for layer in nn_architecture:
        model.add(Dense(layer['output_dim'],
                        input_dim=layer['input_dim'],
                        activation=layer['activation'],
                        kernel_initializer=init))
                        #kernel_initializer=init))
        # model.add(Dropout(0.5))

    model.compile(loss='categorical_crossentropy', optimizer=go, metrics=['accuracy'])
    return model


def encode_one_hot(df, col_to_encode):
    """
    encodes all specified columns one hot
    df = dataframe
    col_to_encode = list(columns to encode)
    -----
    returns matrix, encoder
    """
    df_to_encode = df[col_to_encode].to_numpy()
    rest_df = df.drop(col_to_encode, axis=1).to_numpy()

    enc = OneHotEncoder(handle_unknown='ignore')
    y = enc.fit_transform(df_to_encode).toarray()
    encoding_length = rest_df.shape[1]
    out_put = np.concatenate((rest_df, y), axis=1)

    return out_put, enc, encoding_length

def mlp(df, kwargs):
    """
    THE MLP
    ----------
    df : numpy.array
        Numpy array with data IMPORTANT:
            THE RESULT COLUMN NEEDS TO BE AT INDEX 0
            THE SEASON COLUMN NEEDS TO BE AT INDEX 1
    kwargs : dict
        Dictionary with all the keyparameters
    -------
    Returns result
    """
    # ----------------------------SELECTION--------------------------------
    # split your data in x and y
    X = df[:, 2:]
    seasons = df[:, 1]

    # one hot encode prediction values
    Y = df[:, 0]
    new_y = np.array([[0]*3 for i in range(Y.shape[0])])
    for i in range(Y.shape[0]):
        new_y[i, int(Y[i])] = 1

    # THIS IS FOR BINARY CLASS
    # Y = df[:, 0]
    # new_y = np.array([[0]*2 for i in range(Y.shape[0])])
    # for i in range(Y.shape[0]):
    #     if int(Y[i]) == 1:
    #         new_y[i, int(Y[i])] = 1
    #     else:
    #         new_y[i, 0] = 1

    # ----------------------------SPLITTING--------------------------------
    # split into seasons
    if kwargs['split_method'] == 'seasonal':
        d_seasons = [1213, 1314, 1415, 1516, 1617, 1718, 1819, 1920]
        folds = []
        for season in d_seasons:
            train_idx = np.where(seasons != season)
            val_idx = np.where(seasons == season)

            folds.append((train_idx, val_idx))
    elif kwargs['split_method'] == '10-fold':
        n_split = 10
        folds = list(StratifiedKFold(n_splits=n_split, shuffle=True, random_state=7).split(X, Y))

    # extract the quotes
    quote_columns = [x-2 for x in kwargs['quotecolumns']]
    quotes = X[:, quote_columns]

    # ----------------------------Scaling--------------------------------
    # min max scale the Data. THIS IS BETTER THAN STANDARD SCALING
    scaler = MinMaxScaler()
    # scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)
    # X = np.load('C:/Users/Frido/Desktop/betting/For the Presentation/PC_Data_4pcas.npy')
    # ----------------------------Scaling--------------------------------
    # initiate the prediction arrays
    y_all = None
    y_all_pred = None
    q_all = None
    # ----------------------------Training--------------------------------
    # train the model
    for j, (train_idx, val_idx) in enumerate(folds):
        # print the current fold
        print('\nFold ',j)

        # definde x and y for train and test. This comes out of the folds
        x_train, x_test = X[train_idx], X[val_idx]
        y_train, y_test = new_y[train_idx], new_y[val_idx]

        # initiate the model
        model = initialize_nn(kwargs['nn_architecture'])
        # print(model.summary())
        # stop if model loss doesnt incdeas anymore
        cb = [keras.callbacks.EarlyStopping(monitor='loss', min_delta=0.02, patience=4, verbose=0, mode='auto')]

        cw = {0: 1, 1: 1, 2:1}
        # fit the model
        steps_per_epoch = int(len(x_train)/1.3)
        epochs = kwargs['num_epochs']
        verbose = kwargs['verbose']
        model.fit(x_train,
                  y_train,
                  steps_per_epoch=steps_per_epoch,
                  # batch_size=kwargs['batchsize'],
                  # shuffle=True,
                  class_weight=cw,
                  epochs=epochs,
                  callbacks=cb,
                  verbose=verbose)

        # y_train_pred =
        # ----------------------------Prediction--------------------------------
        # Predict current test data
        y_pred = model.predict(x_test)
        if y_all is None:
            y_all = y_test
            y_all_pred = y_pred
            q_all = quotes[val_idx]
        else:
            y_all = np.concatenate((y_all, y_test))
            y_all_pred = np.concatenate((y_all_pred, y_pred))
            q_all =  np.concatenate((q_all, quotes[val_idx]))

    # ----------------------------Evaluation--------------------------------
    # Evaluate the results
    # result = classification_report(np.argmax(y_all, axis=1), np.argmax(y_all_pred, axis=1), output_dict=True)
    # result_df = pd.DataFrame(result).transpose()

            # np.argmax(y_all_pred, axis=1)
    return np.argmax(y_all, axis=1), y_all_pred, q_all, model, scaler


def load_dataset(key='all', dataset='jannis'):
    """
    Loads the dataset

    Parameters
    ----------
    key : string
        - what mlp we want to load
        - 'jan' = what jan wanted
        - 'all' = all columns

    dataset : string
        - 'jannis' = jannis_features_updated
        - 'mats' = enhanced dataset

    Returns
    -------
    the df
    """
    d_seasons = {1213: [datetime.datetime(2012, 8, 22), datetime.datetime(2013, 5, 19)],
                 1314: [datetime.datetime(2013, 8, 8), datetime.datetime(2014, 5, 11)],
                 1415: [datetime.datetime(2014, 8, 22), datetime.datetime(2015, 5, 24)],
                 1516: [datetime.datetime(2015, 8, 13), datetime.datetime(2016, 5, 15)],
                 1617: [datetime.datetime(2016, 8, 25), datetime.datetime(2017, 5, 21)],
                 1718: [datetime.datetime(2017, 8, 17), datetime.datetime(2018, 5, 13)],
                 1819: [datetime.datetime(2018, 8, 23), datetime.datetime(2019, 5, 19)],
                 1920: [datetime.datetime(2019, 8, 15), datetime.datetime(2019, 12, 2)]}
    # if dataset jannis load jannis dataset
    if dataset=='jannis' or dataset=='jan':
        df = pd.read_csv('jannis_features_updated.csv', index_col=0)

    # Join season to the Dataset
    seas = []
    for i in df['Date'].values.tolist():
        date = datetime.datetime(int(i.split('-')[0]), int(i.split('-')[1]),
                                 int(i.split('-')[2].replace(' 00:00:00', '')))
        a = len(seas)
        for j in d_seasons:
            if date >= d_seasons[j][0] and date <= d_seasons[j][1]:
                seas.append(j)
                break
        if a == len(seas):
            print('THIS DOESNT FIT INTO A SEASON', i, 'Put 0 into dataset')
            seas.append(0)

    # df['season'] = seas
    df.insert(1, 'season', seas)
    # return all the data for Jans approach
    if key == 'jan':
        return df[['FTR', 'season', 'HomeTeam', 'AwayTeam', 'B365H', 'B365D', 'B365A']]
    if key == 'all':
        a = df['FTR']
        df.drop(labels=['FTR'], axis=1,inplace = True)
        df.insert(0, 'FTR', a)
        return df


def money_money_money(y_truth, y_pred, quotes):
    """
    money evaluation
    Parameters
    ----------
    y_truth : truth values
    y_pred : false value
    quote : quotes
    bet_on : str on what to bet on
        DESCRIPTION. The default is 'all'.

    Returns
    -------
    profits
    """

    einsatz = 3

    only_home = []
    money_home = 100
    only_away = []
    money_away = 100
    draw = []
    money_draw = 100
    both = []
    money_both = 100

    for i in range(y_truth.shape[0]):
        if y_pred[i] == 0:
            if y_truth[i] == y_pred[i]:
                if money_home > 0:
                    money_home += einsatz*quotes[i, 0] - einsatz
                if money_both > 0:
                    money_both += einsatz*quotes[i, 0] - einsatz
            else:
                if money_home > 0:
                    money_home -= einsatz
                if money_both > 0:
                    money_both -= einsatz

        only_home.append(money_home)

        if y_pred[i] == 1:
            if y_truth[i] == y_pred[i]:
                if money_draw > 0:
                    money_draw += einsatz*quotes[i, 1] - einsatz
            else:
                if money_draw > 0:
                    money_draw -= einsatz
        draw.append(money_draw)
        if y_pred[i] == 2:
            if y_truth[i] == y_pred[i]:
                if money_away > 0:
                    money_away += einsatz*quotes[i, 2] - einsatz
                if money_both > 0:
                    money_both += einsatz*quotes[i, 2] - einsatz
            else:
                if money_away > 0:
                    money_away -= einsatz
                if money_both > 0:
                    money_both -= einsatz
        only_away.append(money_away)
        both.append(money_both)

    x = [x1 for x1 in range(y_truth.shape[0])]

    supports = pd.DataFrame(y_pred)[0].value_counts()
    fig, ax = plt.subplots(1, 1, constrained_layout=True, figsize=(16,8))
    fig.suptitle('Profit using different betting strategies\n fixed betting size', fontsize=22, fontweight='bold')
    ax.set_xlabel('Number of games', fontsize=16)
    ax.set_ylabel('Profit', fontsize=16)
    ax.plot(x, only_home, label='only on home betting - support: ' + str(supports[0]))
    ax.plot(x, only_away, label='only on away betting - support: ' + str(supports[2]))
    ax.plot(x, draw, label='only on draw betting - support: ' + str(supports[1]))
    ax.plot(x, both, label='on home and away betting')
    ax.grid()
    ax.legend()
    # plt.savefig('saves/money_fix_m4_random.png' ,dpi=300)
    plt.show()


def money_money_money2(y_truth, y_pred, quotes):
    """
    money evaluation
    Parameters
    ----------
    y_truth : truth values
    y_pred : false value
    quote : quotes
    bet_on : str on what to bet on
        DESCRIPTION. The default is 'all'.

    Returns
    -------
    profits
    """
    einsatz_ratio = 0.03

    only_home = []
    money_home = 100
    only_away = []
    money_away = 100
    draw = []
    money_draw = 100
    both = []
    money_both = 100

    for i in range(y_truth.shape[0]):
        if y_pred[i] == 0:
            if y_truth[i] == y_pred[i]:
                money_home += einsatz_ratio*money_home*quotes[i, 0] - einsatz_ratio*money_home
                money_both += einsatz_ratio*money_both*quotes[i, 0] - einsatz_ratio*money_both
            else:
                money_home -= einsatz_ratio*money_home
                money_both -= einsatz_ratio*money_both
        only_home.append(money_home)

        if y_pred[i] == 1:
            if y_truth[i] == y_pred[i]:
                money_draw += einsatz_ratio*money_draw*quotes[i, 1] - einsatz_ratio*money_draw
            else:
                money_draw -= einsatz_ratio*money_draw
        draw.append(money_draw)
        if y_pred[i] == 2:
            if y_truth[i] == y_pred[i]:
                money_away += einsatz_ratio*money_away*quotes[i, 2] - einsatz_ratio*money_away
                money_both += einsatz_ratio*money_both*quotes[i, 2] - einsatz_ratio*money_both
            else:
                money_away -= einsatz_ratio*money_away
                money_both -= einsatz_ratio*money_both
        only_away.append(money_away)
        both.append(money_both)

    x = [x1 for x1 in range(y_truth.shape[0])]

    supports = pd.DataFrame(y_pred)[0].value_counts()
    fig, ax = plt.subplots(1, 1, constrained_layout=True, figsize=(16,8))
    fig.suptitle('Profit using different betting strategies\n percentual bettting size', fontsize=22, fontweight='bold')
    ax.set_xlabel('Number of games', fontsize=16)
    ax.set_ylabel('Profit', fontsize=16)
    ax.plot(x, only_home, label='only on home betting- support: ' + str(supports[0]))
    ax.plot(x, only_away, label='only on away betting- support: ' +str(supports[2]))
    ax.plot(x, draw, label='only on draw betting - support: ' + str(supports[1]))
    ax.plot(x, both, label='on home and away betting')
    ax.grid()
    ax.legend()
    # plt.savefig('saves/money_variable_m4_random.png' ,dpi=300)
    plt.show()


def money_money_money_two_class(y_truth, y_pred_all, quotes, kind='fix'):
    """
    money evaluation
    Parameters
    ----------
    y_truth : truth values
    y_pred : false value
    quote : quotes
    bet_on : str on what to bet on
        DESCRIPTION. The default is 'all'.

    Returns
    -------
    profits
    """
    tholds = [0.3, 0.4, 0.5, 0.6]
    x = [x1 for x1 in range(y_truth.shape[0])]

    for thold in tholds:
        a = []
        for j in range(y_pred_all.shape[0]):
            if y_pred_all[j][1] > thold:
                a.append(1)
            else:
                a.append(0)

        y_pred = np.array(a)
        einsatz_ratio = 0.03
        einsatz = 1
        d = []
        if kind == 'variable':
            money = 100
        else:
            money = 0

        for i in range(y_truth.shape[0]):

            if y_pred[i] == 1:
                if y_truth[i] == y_pred[i]:
                    if kind == 'variable':
                        money += einsatz_ratio*money*quotes[i, 1]*0.95 - einsatz_ratio*money
                    else:
                        money += einsatz*quotes[i, 1]*0.95 - einsatz
                else:
                    if kind == 'variable':
                        money -= einsatz_ratio*money
                    else:
                        money -= einsatz

            d.append(money)

        plt.plot(x, d, label = str(thold))

    plt.legend()
    plt.show()


def plot_profit_features(df, overwrite=None):

    def evaluate(y_truth, y_pred, odds):
        einsatz = 3
        money = 100
        profit = []
        lost_everything = None
        for i in range(y_truth.shape[0]):
            if y_pred[i] == y_truth[i]:
                money += einsatz*odds[i, y_pred[i]]-einsatz
            else:
                money -= einsatz
            if lost_everything is None and money <= 0:
                lost_everything = i
            profit.append(money)
        return profit, lost_everything

    fig, ax = plt.subplots(1, 1, constrained_layout=True, figsize=(16,8))
    fig.suptitle('Profit betting on Elo-Rating and Draw from model 3', fontsize=22, fontweight='bold')
    ax.set_xlabel('Number of games', fontsize=16)
    ax.set_ylabel('Profit', fontsize=16)
    x = df.index.tolist()
    y_truth = df['FTR'].values
    odds = df[['B365H', 'B365D', 'B365A']].to_numpy()
    profitB365, lost_everythingB365 = evaluate(y_truth,
                                               df[['B365H', 'B365D', 'B365A']].to_numpy().argmax(axis=1),
                                               odds)
    profitBW, lost_everythingBW = evaluate(y_truth,
                                            df[['BWH', 'BWD', 'BWA']].to_numpy().argmax(axis=1),
                                            df[['BWH', 'BWD', 'BWA']].to_numpy())
    profitELO, lost_everythingELO = evaluate(y_truth,
                                               df[['H_ELO', 'A_ELO']].to_numpy().argmin(axis=1),
                                               odds)
    profitTP, lost_everythingTP= evaluate(y_truth,
                                               df[['HTTP', 'ATTP']].to_numpy().argmin(axis=1),
                                               odds)
    profitGD, lost_everythingGD= evaluate(y_truth,
                                               df[['HGD', 'AGD']].to_numpy().argmax(axis=1),
                                               odds)
    profitHOME, lost_everythingHOME= evaluate(y_truth,
                                               np.array([0 for i in range(y_truth.shape[0])]),
                                               odds)
    profitDRAW, lost_everythingDRAW= evaluate(y_truth,
                                               np.array([1 for i in range(y_truth.shape[0])]),
                                               odds)
    profitAway, lost_everythingAway= evaluate(y_truth,
                                               np.array([2 for i in range(y_truth.shape[0])]),
                                               odds)
    if overwrite is not None:
        a = df[['H_ELO', 'A_ELO']].to_numpy().argmax(axis=1)
        for i in range(overwrite.shape[0]):
            if overwrite[i] == 1:
                a[i] = 1
        profitA, lost_everythingA = evaluate(y_truth, a, odds)

    ### Profit for B365

    zero_line_markers = [
                        # lost_everythingHOME,
    #                      lost_everythingDRAW,
    #                      lost_everythingAway,
    #                      lost_everythingB365,
    #                      lost_everythingBW,
    #                      lost_everythingELO,
    #                      lost_everythingTP,
    #                      lost_everythingGD
                        ]
    ax.grid()
    plt.rc('legend', fontsize=16)
    # ax.set_ylim(ymin=-600, ymax=460)

    ax.plot(x, profitA, label='Betting on Elo-Draw' + ' - competitor did not went broke')

    # ax.plot(x, profitHOME, label='Betting on HomeTeam' + ' - broke after ' + str(lost_everythingHOME) + ' games')
    # ax.plot(x, profitDRAW, label='Betting on Draw' + ' - broke after ' + str(lost_everythingDRAW) + ' games')
    # ax.plot(x, profitAway, label='Betting on AwayTeam' + ' - broke after ' + str(lost_everythingAway) + ' games')
    # ax.plot(x, profitB365, label='Betting on B365-odds' + ' - broke after ' + str(lost_everythingB365) + ' games')
    # ax.plot(x, profitBW, label='Betting on BWin-odds' + ' - broke after ' + str(lost_everythingBW) + ' games')
    # ax.plot(x, profitELO, label='Betting on Elo-rating' + ' not broke')
    # ax.plot(x, profitTP, label='Betting on Table position' + ' - broke after ' + str(lost_everythingTP) + ' games')
    # ax.plot(x, profitGD, label='Betting on Goal Difference' + ' - broke after ' + str(lost_everythingGD) + ' games')

    # ax.plot(zero_line_markers, [0 for j in zero_line_markers], 'o', color='k',
    #         markersize=8, linewidth=4,
    #         markerfacecolor='k',
    #         markeredgecolor='k')

    ax.legend()
    # plt.savefig('saves/money_different_features.png' ,dpi=300)
    plt.show()
    return


if __name__ == '__main__':

    # ----------------------------Define Key arguments here--------------------------------
    # Evaluate the results
    kwargs = {# dataset defines which dataset to use
              'dataset': 'jannis',
              # key defines what to use from the dataset
              'key': 'jan',
              # 'key': 'all',
              # the columns that should be dropped
              'drop': [],
              # 'drop': ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'IDX'],
              # the columns that should be encoded
              'encode': ['HomeTeam', 'AwayTeam'],
              # 'encode': [],
              # split_method defines how Folds for crossvalidation are created
              # possible: - seasonal(devide by seasons), - '10fold': 10foldcrossvalidation
              'split_method': 'seasonal',
              # number of maximum epochs
              'num_epochs': 30,
              # batchsize
              'batchsize': 5,
              # verbose indicates how progress is shown in the model
              'verbose': 1,
              # outputpath to where results should be saved
              'outputpath': 'saves/result_m4_weighted.pkl',
              #quotecolumn
              'quotecolumns': [2, 3, 4],
              #save model, scaler
              'safe_scaler_etc': False}

    # ----------------------------Loading-------------------------------
    # Load appropriate dataset
    df = load_dataset(key=kwargs['key'], dataset=kwargs['dataset'])

    # ----------------------------Preparation-------------------------------
    # prepare the dataset
    # drop columns,
    if len(kwargs['drop']) > 0:
        df = df.drop(kwargs['drop'], axis=1)
    # encode columns
    if len(kwargs['encode']) > 0:
        matrix, enc, encode_len = encode_one_hot(df, kwargs['encode'])
    else:
        matrix = df.to_numpy()

    # Definition of Neural Network architecture
    kwargs['nn_architecture'] = [{"input_dim": matrix.shape[1]-2, "output_dim": 16, "activation": "relu"},
                                  #{"input_dim": 32, "output_dim": 16, "activation": "relu"},
                                  {"input_dim": 16, "output_dim": 3, "activation": "softmax"}]

    a = np.array([0 for x in range(matrix.shape[0])])
    result = classification_report(matrix[:,0], a, output_dict=True)
    # result = classification_report(y_truth, y_pred_random, output_dict=True)
    result_df = pd.DataFrame(result).transpose()

    ##### THIS IS HOW YOU TRANSFORM THE ENCODED COLUMNS BACK:
    # matrix2 = matrix[:, encode_len:]
    # a = enc.inverse_transform(matrix2)
    import time
    now = time.time()
    # train the model
    y_truth, y_pred_all, quotes, model, scaler= mlp(matrix, kwargs)
    print(time.time()-now)
    if kwargs['safe_scaler_etc']:
        import pickle
        pickle.dump(enc, open( "saves/TeamName_encoder.p", "wb" ))
        scaler_filename = "saves/scaler.save"
        joblib.dump(scaler, scaler_filename)
        model.save('saves/prediction_model.h5')


    result = classification_report(y_truth, np.argmax(y_pred_all, axis=1), output_dict=True)
    # result = classification_report(y_truth, y_pred_random, output_dict=True)
    result_df = pd.DataFrame(result).transpose()

    # y_pred_random = np.random.choice(3, 2206, p=[1007/2206, 541/2206, 658/2206])
    # money_money_money(y_truth, y_pred_random, quotes)
    # money_money_money2(y_truth, y_pred_random, quotes)
    money_money_money(y_truth, np.argmax(y_pred_all, axis=1), quotes)
    money_money_money2(y_truth, np.argmax(y_pred_all, axis=1), quotes)
    plot_profit_features(load_dataset(key='all', dataset=kwargs['dataset']), np.argmax(y_pred_all, axis=1))
    # # save the results
    # output_path = kwargs['outputpath']
    # result_df.to_pickle(output_path)

    # plt.title('Distribution of betting odds',fontsize=32)
    # b = sns.boxplot(data=df.iloc[:,0:3], showfliers=False, palette="Set2")
    # b.set_xlabel("Prediction class",fontsize=26)
    # b.set_ylabel("Betting odds",fontsize=26)
    # b.tick_params(labelsize=22)