import pandas as pd
import numpy as np
import GetData
from datetime import datetime


#safes data as csv input: data as a hole
def save_as_csv():
	soccerdata = [
				['Bayern-Dortmund', '2019-05-05'],
				['Tipico', '3.6-3.8-2'],
				['XBet', '3.6-3.8-2'],
				['Bet3000', '3.6-3.8-2'],
				['BetFair', '3.6-3.8-2'],
				['Union-Hertha', '2019-05-05-19:20', '2019-05-05-21:20'],
				['Tipico', '3.6-3.8-2', '2.1-3.1-19'],
				['XBet', '3.6-3.8-2', '2.1-3.1-19'],
				['Bet3000', '3.6-3.8-2', '2.1-3.1-19'],
				['BetFair', '3.6-3.8-2', '2.1-3.1-19']]

	df = pd.DataFrame(soccerdata,columns=['Spiel', '1', '2'])

	print(df)

	df.to_csv('Soccerdata.csv')
	#print(df)
	return "Data safed."

#generate date and time in the appropriate colum format
def get_dt_for_col():

	now = datetime.now()
	#get time
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	dt_string = dt_string.replace("/", "-")
	dt_string = dt_string.replace(" ", "-")
	dt_string = ''.join(dt_string.split())[:-3]

	return dt_string


#takes input csv_datei that should be changed and new quotes as a dict(TODO)
def update_data(old_data, new_quotes, game):
	#get curr date and time
	new_quotes[0] = get_dt_for_col()

	#if game not in the dataset: insert it
	if old_data['Spiel'].str.match(game).eq(False).all():
	#	print(game + " not found! Insert Game into Dataframe")
		n1 = [None for i in range(len(old_data.columns))]
		n1[0] = game
		insert(old_data,n1)
		n1[0] = 'Tipico'
		insert(old_data,n1)
		n1[0] = 'XBet'
		insert(old_data,n1)
		n1[0] = 'Bet3000'
		insert(old_data,n1)
		n1[0] = 'BetFair'
		insert(old_data,n1)

	#get index of game you want to update
	i_ofGame = old_data[old_data['Spiel'].str.match(game)].index.values.astype(int)[0]

	#get rows containing the game, find the right column index and safe its name
	change_data = old_data.iloc[i_ofGame: i_ofGame+1, :]

	# insert a new column into the dataset if the last column is full
	zw_list = list(np.where(pd.isnull(change_data)))
	if len(zw_list[1]) == 0:
		new_column = int(list(old_data)[-1])+1
		old_data[str(new_column)] = None


		#get rows containing the game, find the right column index and safe its name
		change_data = old_data.iloc[i_ofGame: i_ofGame+1, :]
		zw_list = list(np.where(pd.isnull(change_data)))


	idx = zw_list[1][0]
	col_idx = list(old_data.columns)[idx]

	#change the data with the previous row index and colum index
	for i in range(len(new_quotes)):
		old_data.loc[i + i_ofGame].at[col_idx] = new_quotes[i]
	#print("Data from game: " + game + " has been updated.")

	return old_data

#inserts new game into dataframe
def insert(df, row_insert):
	#find max index
    insert_loc = df.index.max()
    #insert
    if pd.isna(insert_loc):
        df.loc[0] = row_insert
    else:
        df.loc[insert_loc + 1] = row_insert

def main():
	#save_as_csv()
	#define file and load it into pd-frame
	csv_datei = "Soccerdata2.csv"
	old_data = pd.read_csv(csv_datei,  index_col=0)
	curr_date_time = get_dt_for_col()

	tipicod = GetData.tipicogerman()

	betfaird = {'name': 'BetFair', '1899Hoffenheim-VfLWolfsburg': [100, 100, 100], 'Schalke04-FCAugsburg': [400, 400, 400]}
	bet3000d = {'name': 'Bet3000', 'BayerLeverkusen-EintrachtFrankfurt': [100, 100, 100], 'Schalke04-FCAugsburg': [400, 400, 400]}
	xbetd = {'name': 'Xbet', 'Schalke04-FCAugsburg': [100, 100, 100]}

	#create list for iteration purposes
	Dictionarylist = [tipicod, bet3000d,betfaird, xbetd]

	#TODO LOAD DICT WITH MOST ENTRIES
	games = list(Dictionarylist[0].keys())
	games.remove('name')

	for game in games:
		#get rid of umlaute
		game_new = game.replace("\\xc3\\xbc", "ue")
		game_new = game_new.replace("\\xc3\\xb6", "ue")
		game_new = game_new.replace("\\'g","G")

		#define ne quotes
		new_quotes = [curr_date_time, None, None, None, None]

		#look if game is already in the dataframe:
		# if not old_data['Spiel'].str.match(game_new).eq(False).all():
		# 	#get index of the game
		# 	i_ofGame = old_data[old_data['Spiel'].str.match(game_new)].index.values.astype(int)[0]

		# 	if old_data.iloc[i_ofGame, 1] != None:
		# 		new_quotes[0] = old_data.iloc[i_ofGame, 1]
		# 		if old_data.iloc[i_ofGame+1, 1] != None:
		# 			new_quotes[1] = old_data.iloc[i_ofGame+1, 1]
		# 		if old_data.iloc[i_ofGame+2, 1] != None:
		# 			new_quotes[2] = old_data.iloc[i_ofGame+2, 1]
		# 		if old_data.iloc[i_ofGame+3, 1] != None:
		# 			new_quotes[3] = old_data.iloc[i_ofGame+3, 1]
		# 		if old_data.iloc[i_ofGame+4, 1] != None:
		# 			new_quotes[4] = old_data.iloc[i_ofGame+4, 1]

		#go through bettingsites and see if new quotes appeared
		for Wettanbieter in Dictionarylist:
			if game in set(Wettanbieter.keys()):
				zw_quoten = str(Wettanbieter[game]).replace("[", "").replace("]","").replace(", ", "-")
				#update quotes if that has not been the case
				if Wettanbieter["name"] == 'Tipico':
					if new_quotes[1] == None:
						new_quotes[1] = zw_quoten
				elif Wettanbieter["name"] == 'Xbet':
					if new_quotes[2] == None:
						new_quotes[2] = zw_quoten
				elif Wettanbieter["name"] == 'Bet3000':
					if new_quotes[3] == None:
						new_quotes[3] = zw_quoten
				elif Wettanbieter["name"] == 'BetFair':
					if new_quotes[1] == None:
						new_quotes[4] = zw_quoten

		#update new quotes.
		new_data = update_data(old_data, new_quotes, game_new)
		old_data = new_data

	print(old_data)
	#safe new data-frame
	old_data.to_csv('Soccerdata1.csv')

if __name__== "__main__" :
	main()

###  Dicts aus arbitrage laden und damit rechnen.