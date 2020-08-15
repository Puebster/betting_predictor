import tkinter as tk
import pickle
import numpy as np
import pandas as pd
from keras.models import load_model
from keras.models import Sequential
import keras
from sklearn.externals import joblib
import os.path


def start_experiment(_training_requested = True):

    if not os.path.exists('additional_data.csv'):
        _training_requested = False

    try:
        q1 = float(entry_field1.get())
    except:
        q1 = 'YOU ENTERED SOMETHING I CANT USE'
    try:
        q2 = float(entry_field2.get())
    except:
        q2 = 'YOU ENTERED SOMETHING I CANT USE'
    try:
        q3 = float(entry_field3.get())
    except:
        q3 = 'YOU ENTERED SOMETHING I CANT USE'

    homeTeam = tkhome.get()
    awayTeam = tkaway.get()

    if 'YOU ENTERED SOMETHING I CANT USE' in [q1, q2, q3]:
        output = 'There is an Error\nwith the input.\nEnter Odds with . as delimiter.'
        return output

    # Load Encoder
    pickle_in = open("TeamName_encoder.p", "rb")
    enc = pickle.load(pickle_in)

    y = enc.transform(np.array([homeTeam, awayTeam]).reshape(1, -1)).toarray()
    features = np.concatenate((np.array([q1, q2, q3]), y[0]))
    # Load Model
    model = load_model('prediction_model.h5')

    scaler = joblib.load("scaler.save")

    if _training_requested:
        # Load additional data
        df1 = pd.read_csv('additional_data.csv', index_col=0)
        df2 = pd.read_csv('base_dataset.csv', index_col=0)
        df = pd.concat([df1, df2], ignore_index=True)
        df_to_encode = df[['HomeTeam', 'AwayTeam']].to_numpy()
        result = df[['FTR']].to_numpy()
        rest_df = df.drop(['HomeTeam', 'AwayTeam', 'FTR'], axis=1).to_numpy()

        x = enc.transform(df_to_encode).toarray()
        out_put = np.concatenate((rest_df, x), axis=1)

        new_y = np.array([[0] * 3 for i in range(result.shape[0])])
        for i in range(result.shape[0]):
            new_y[i, int(result[i])] = 1

        new_x = scaler.transform(out_put)

        cb = [keras.callbacks.EarlyStopping(monitor='loss', min_delta=0.02, patience=4, verbose=0, mode='auto')]

        go = keras.optimizers.Adam(lr=1e-5, beta_1=0.9, beta_2=0.999, amsgrad=False)
        model.optimizer = go
        model.fit(new_x, new_y,
                  steps_per_epoch=new_x.shape[0],
                  epochs=30,
                  verbose=1,
                  callbacks=cb)



    eingabe = features.reshape(1, -1)
    eingabe = scaler.transform(eingabe)

    predictions = model.predict(eingabe)

    return [
        round(predictions[0, 0] * 100, 2),
        round(predictions[0, 1] * 100, 2),
        round(predictions[0, 2] * 100, 2)
    ]

def display():

    lbl_0.set('Processing...')
    lbl_1.set("-")
    lbl_2.set("-")

    [home_result, draw_result, away_result] = start_experiment(_training_requested = False)

    # This creates a text field with the output
    lbl_0.set(str(home_result) + "%")
    lbl_1.set(str(draw_result) + "%")
    lbl_2.set(str(away_result) + "%")

def display_train():

    lbl_0.set("-")
    lbl_1.set("-")
    lbl_2.set('Processing...')

    [home_result, draw_result, away_result] = start_experiment(_training_requested = True)

    # This creates a text field with the output
    lbl_0.set(str(home_result) + "%")
    lbl_1.set(str(draw_result) + "%")
    lbl_2.set(str(away_result) + "%")


def save():

    try:
        q1 = float(entry_field1.get())
    except:
        q1 = 'YOU ENTERED SOMETHING I CANT USE'
    try:
        q2 = float(entry_field2.get())
    except:
        q2 = 'YOU ENTERED SOMETHING I CANT USE'
    try:
        q3 = float(entry_field3.get())
    except:
        q3 = 'YOU ENTERED SOMETHING I CANT USE'
    try:
        goal_home = int(entry_field4.get())
    except:
        lbl_0.set("Wrong goal format!")
    try:
        goal_away = int(entry_field5.get())
    except:
        lbl_0.set("Wrong goal format!")

    homeTeam = tkhome.get()
    awayTeam = tkaway.get()

    ftr = 0
    if goal_away > goal_home:
        ftr = 2
    elif goal_away == goal_home:
        ftr = 1

    add_data = pd.DataFrame({
            "HomeTeam": [homeTeam],
            "AwayTeam": [awayTeam],
            "B365H": [q1],
            "B365D": [q2],
            "B365A": [q3],
            "FTR": [ftr],
        })

    if os.path.exists('additional_data.csv'):
        # Load additional data
        df = pd.read_csv('additional_data.csv', index_col=0)
        df.append(add_data).to_csv("additional_data.csv")
    else:
        add_data.to_csv("additional_data.csv")

window = tk.Tk()
# TITEL
window.title('Betting Predictor')
# GEOMETRY
window.geometry("650x350")

# LABELS
prompt = tk.Label(text='Welcome to the betting predictor',
                  font=('Arial', 20, "bold"), fg="#1d5696")
prompt1 = tk.Label(text='Home Team',
                  font=('Arial', 15, "bold"))
prompt2 = tk.Label(text='Away Team',
                  font=('Arial', 15, "bold"))
prompt3 = tk.Label(text='Draw',
                  font=('Arial', 15, "bold"))

tk.Label(text='Names:', font=('Arial', 15, "bold")).grid(column=0, row=2, padx=5, sticky="E")
tk.Label(text='Odds:', font=('Arial', 15, "bold")).grid(column=0, row=3, padx=5, sticky="E")

prompt.grid(column=1, row=0, columnspan=3, pady=20)

prompt1.grid(column=1, row=1)
prompt2.grid(column=3, row=1)
prompt3.grid(column=2, row=1)

lbl_0 = tk.StringVar()
lbl_0.set('-')

lbl_1 = tk.StringVar()
lbl_1.set('-')

lbl_2 = tk.StringVar()
lbl_2.set('-')

prompt4 = tk.Label(textvariable=lbl_0, font=('Arial', 15))
prompt4.grid(column=1, row=5)

prompt5 = tk.Label(textvariable=lbl_1, font=('Arial', 15))
prompt5.grid(column=2, row=5)

prompt6 = tk.Label(textvariable=lbl_2, font=('Arial', 15))
prompt6.grid(column=3, row=5)


# BUTTONS
button1 = tk.Button(text='Predict',
                    command=display)
button1.grid(column=0, row=5, padx=5, sticky="E")

button3 = tk.Button(text='Train and predict',
                    command=display_train)
button3.grid(column=0, row=6, padx=5, sticky="E")

button2 = tk.Button(text='Save Result',
                    command=save)
button2.grid(column=0, row=10, padx=5, sticky="E")

# Entry field
v1 = tk.StringVar(value='1.5')
v2 = tk.StringVar(value='4.4')
v3 = tk.StringVar(value='6.0')
entry_field1 = tk.Entry(textvariable=v1)
entry_field2 = tk.Entry(textvariable=v2)
entry_field3 = tk.Entry(textvariable=v3)
entry_field1.grid(column=1, row=3)
entry_field2.grid(column=2, row=3)
entry_field3.grid(column=3, row=3)



# Entry field
tk.Label(text="Goals:", font=('Arial', 15, "bold")).grid(column=0, row=9)
tk.Label(text="Train the model by specifying the outcome:", font=('Arial', 15, "bold")).grid(column=1, columnspan=3, row=7)
v4 = tk.StringVar(value='2')
v5 = tk.StringVar(value='1')
entry_field4 = tk.Entry(textvariable=v4)
entry_field5 = tk.Entry(textvariable=v5)
entry_field4.grid(column=1, row=9)
entry_field5.grid(column=3, row=9)



tkhome = tk.StringVar(window)
tkaway = tk.StringVar(window)

teams = {'Borussia Dortmund',
         'VfB Stuttgart',
         'FC Augsburg',
         'Eintracht Frankfurt',
         'SC Freiburg',
         'SpVgg Greuther Fürth',
         'Hamburger SV',
         'Borussia Mönchengladbach',
         'Hannover 96',
         '1. FSV Mainz 05',
         'Fortuna Düsseldorf',
         'TSG 1899 Hoffenheim',
         'Bayer Leverkusen',
         '1. FC Nürnberg',
         'FC Schalke 04',
         'Werder Bremen',
         'Bayern München',
         'VfL Wolfsburg',
         'Hertha BSC',
         '1. FC Köln',
         'SC Paderborn 07',
         'SV Darmstadt 98',
         'FC Ingolstadt 04',
         'RB Leipzig',
         '1. FC Union Berlin'}

team_choices = sorted(teams)

tkhome.set('Borussia Dortmund')
tkaway.set('Borussia Mönchengladbach')

popupMenu1 = tk.OptionMenu(window, tkhome, *team_choices)
popupMenu2 = tk.OptionMenu(window, tkaway, *team_choices)
popupMenu1.grid(column=1, row=2)
popupMenu2.grid(column=3, row=2)




# SPAWN
window.mainloop()