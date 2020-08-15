import tkinter as tk
import pickle
import numpy as np
from keras.models import load_model
from sklearn.externals import joblib

def start_experiment():

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
    # Load Scaler
    scaler = joblib.load("scaler.save")
    eingabe = features.reshape(1,-1)
    eingabe = scaler.transform(eingabe)
    predictions = model.predict(eingabe)

    output = (homeTeam + ': ' + str(round(predictions[0, 0]*100, 2)) + '%\n' +
              'Draw: ' + str(round(predictions[0, 1]*100, 2)) + '%\n' +
              awayTeam + ': ' + str(round(predictions[0, 2]*100, 2)) + '%')

    return output

def display():
    lbl.set('Calculating...\nPlease wait.')
    prompt4 = tk.Label(textvariable=lbl, font=('Times New Roman', 15))
    prompt4.grid(column=1, row=20)
    output = start_experiment()

    # This creates a text field with the output
    lbl.set(output)
    # prompt5.grid(column=1, row=20)

window = tk.Tk()
# TITEL
window.title('Betting Predictor')
# GEOMETRY
window.geometry("800x400")

# LABELS
prompt = tk.Label(text='Welcome to the betting predictor',
                  font=('Times New Roman', 17))
prompt1 = tk.Label(text='Home Team',
                  font=('Times New Roman', 15))
prompt2 = tk.Label(text='Away Team',
                  font=('Times New Roman', 15))
prompt3 = tk.Label(text='Draw',
                  font=('Times New Roman', 15))
prompt.grid(column=1, row=0)
prompt1.grid(column=0, row=5)
prompt2.grid(column=2, row=5)
prompt3.grid(column=1, row=5)

lbl = tk.StringVar()
lbl.set('default')


# BUTTONS
button1 = tk.Button(text='Give me a prediction',
                    command=display)
button1.grid(column=1, row=10)

# Entry field
v1 = tk.StringVar(value='1.5')
v2 = tk.StringVar(value='4.4')
v3 = tk.StringVar(value='6.0')
entry_field1 = tk.Entry(textvariable=v1)
entry_field2 = tk.Entry(textvariable=v2)
entry_field3 = tk.Entry(textvariable=v3)
entry_field1.grid(column=0, row=8)
entry_field2.grid(column=1, row=8)
entry_field3.grid(column=2, row=8)

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
popupMenu1.grid(column=0, row=6)
popupMenu2.grid(column=2, row=6)

# SPAWN
window.mainloop()