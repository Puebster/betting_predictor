import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import keras.callbacks
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD
from sklearn.model_selection import train_test_split, KFold, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, auc, classification_report
import json

def initialize_nn(nn_architecture):
    model = Sequential()
    for layer in nn_architecture:
        model.add(Dense(layer['output_dim'], input_dim=layer['input_dim'], kernel_initializer="uniform"))
        model.add(Activation(layer['activation']))
        # model.add(Dropout(0.5))
        # sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def first_mlp(df):

    df = df.drop(['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'IDX'], axis=1)
    # df = df.drop(['B365H', 'B365D', 'B365A', 'BWH', 'BWD', 'H_ELO', 'A_ELO', 'HTGD', 'HP', 'ATTP',
    #               'HGD', 'AGD'], axis=1)
    df = df.to_numpy()

    X = df[:, 1:]
    X = np.load('C:/Users/Frido/Desktop/PC_Data_4pcas.npy')
    Y = df[:, 0]
    new_y = np.array([[0]*3 for i in range(Y.shape[0])])
    for i in range(Y.shape[0]):
        new_y[i, int(Y[i])] = 1

    # Without PCA-reduction
    # nn_architecture = [
    # {"input_dim": 16, "output_dim": 8, "activation": "relu"},
    # {"input_dim": 8, "output_dim": 3, "activation": "softmax"}]

    # With PCA-reduction
    nn_architecture = [
    {"input_dim": 4, "output_dim": 8, "activation": "relu"},
    {"input_dim": 8, "output_dim": 3, "activation": "softmax"}]

    n_split = 10
    folds = list(StratifiedKFold(n_splits=n_split, shuffle=True, random_state=1).split(X, Y))

    epochs = 20
    verbose = 1
    y_all = None
    y_all_pred = None

    for j, (train_idx, val_idx) in enumerate(folds):
        print('\nFold ',j)
        x_train, x_test = X[train_idx], X[val_idx]
        y_train, y_test = new_y[train_idx], new_y[val_idx]

        scaler = StandardScaler()
        scaler.fit(x_train)
        x_train = scaler.transform(x_train)

        model = initialize_nn(nn_architecture)
        # print(model.summary())

        cb = [keras.callbacks.EarlyStopping(monitor='loss', min_delta=0.002, patience=4,
                                            verbose=0, mode='auto')]

        model.fit(x_train, y_train, steps_per_epoch=int(len(x_train)),
                  epochs=epochs, callbacks=cb , verbose=verbose)

        y_pred = model.predict(scaler.transform(x_test))
        if y_all is None:
            y_all = y_test
            y_all_pred = y_pred
        else:
            y_all = np.concatenate((y_all, y_test))
            y_all_pred = np.concatenate((y_all_pred, y_pred))


    tholds = [x/100 for x in range(0, 100, 3)]
    # y_all = np.argmax(y_all, axis=1)

    all_predictions = {}
    for thold in tholds:
        y_all_thold = np.copy(y_all_pred)
        for itera in range(y_all_thold.shape[0]):
            temp = np.copy(y_all_thold[itera, :])
            for ii in range(temp.shape[0]):
                if temp[ii] < thold:
                    temp[ii] = 0
                else:
                    temp[ii] = 1

            # number_of_ones = 0
            # for itera2 in range(temp.shape[0]):
            #     if temp[itera2] == 1:
            #         number_of_ones += 1
            # if number_of_ones != 1:
            #     temp = np.copy(y_all_thold[itera, :])

            y_all_thold[itera, :] = temp

        print(thold, 'finished')
        classes = {}
        # y_all_thold = np.argmax(y_all_thold, axis=1)
        # y_all_pred = np.argmax(y_all_pred, axis=1)
        for iii in range(y_all_thold.shape[1]):
            classes[iii] = classification_report(y_all[:, iii], y_all_thold[:, iii])
        # overall = classification_report(y_all_thold, y_all_pred)
        all_predictions[thold] = classes
    return all_predictions


def plot_prec_reca():
    with open("C:/Users/Frido/Desktop/results.json", 'r') as f:
        result = json.load(f)

    null = []
    eins = []
    zwei = []
    thold = []
    for i in result:
        thold.append(i)
        res = result[i]['0']
        null.append([float(res.split('    ')[13]), float(res.split('    ')[14])])

        res = result[i]['1']
        eins.append([float(res.split('    ')[13]), float(res.split('    ')[14])])

        res = result[i]['2']
        zwei.append([float(res.split('    ')[13]), float(res.split('    ')[14])])

    null, eins, zwei = np.array(null), np.array(eins), np.array(zwei)

    plt.plot(null[1:-3, 1], null[1:-3, 0], label = 'Class 0')
    plt.plot(eins[1:-3, 1], eins[1:-3, 0], label = 'Class 1')
    plt.plot(zwei[1:-3, 1], zwei[1:-3, 0], label = 'Class 2')



    plt.ylabel('Precision')
    plt.xlabel('Recall')

    plt.legend()
    plt.show()
    return thold, null, eins, zwei, result


def plot3pcas():
    from mpl_toolkits import mplot3d
    df = pd.read_csv('C:/Users/Frido/Desktop/betting/bet_algo/files/output_files/jannis_features.csv', index_col=0)

    resulti = df['FTR'].to_numpy()
    null = np.argwhere(resulti==0)
    eins = np.argwhere(resulti==1)
    zwei = np.argwhere(resulti==2)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    XX = np.load('C:/Users/Frido/Desktop/PC_Data_4pcas.npy')
    pca1_x, pca1_y, pca1_z = XX[null, 0], XX[null, 1], XX[null, 2]
    pca2_x, pca2_y, pca2_z = XX[eins, 0], XX[eins, 1], XX[eins, 2]
    pca3_x, pca3_y, pca3_z = XX[zwei, 0], XX[zwei, 1], XX[zwei, 2]

    ax.scatter3D(pca1_x, pca1_y, pca1_z, label='Class 0')
    ax.scatter3D(pca2_x, pca2_y, pca2_z, label='Class 1')
    ax.scatter3D(pca3_x, pca3_y, pca3_z, label='Class 2')
    ax.set_xlabel('PCA - component 1')
    ax.set_ylabel('PCA - component 2')
    ax.set_zlabel('PCA - component 3')
    plt.legend()
    plt.show()



if __name__ == '__main__':
	#CHANGE THIS TO YOUR PATH
    df = pd.read_csv('C:/Users/Frido/Desktop/betting/bet_algo/files/output_files/jannis_features.csv', index_col=0)
    result = first_mlp(df)
    thold, null, eins, zwei, result = plot_prec_reca()
    df = pd.DataFrame({'0_precision': null[:, 0],
                      '0_recall': null[:, 1],
                      '1_precision': eins[:, 0],
                      '1_recall': eins[:, 1],
                      '2_precision': zwei[:, 0],
                      '2_recall': zwei[:, 1],
                      'thold': thold})
    # df.to_csv('C:/Users/Frido/Desktop/prec_rec.csv')
    # plot3pcas()
