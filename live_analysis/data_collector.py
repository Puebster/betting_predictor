import data_scraper
from abitrage import arbitrageModel
from utils import printTableNeat


def getBundesligaDicts():

    tipicod = data_scraper.tipicogerman()
    print("Tipico Bundesliga Done")
    xbetd = data_scraper.xbetgerman()
    print("Xbet Bundesliga Done")
    bet3000d = data_scraper.bet3000german()
    print("Bet3000 Bundesliga done")
    betfaird = data_scraper.betfairgerman()
    print("BetFair Bundesliga done")

    with open("bundesliga_dicts", "w") as bundesliga:
    	bundesliga.write(tipicod)
    	bundesliga.write(xbetd)
    	bundesliga.write(bet3000d)
    	bundesliga.write(betfaird)
    bundesliga.close()

    return [tipicod, bet3000d,betfaird, xbetd]


def getPremierleagueDicts():

    tipicod = data_scraper.tipicoenglisch()
    print("Tipico Premier League Done")
    xbetd = data_scraper.xbetenglisch()
    print("Xbet Premier League Done")
    bet3000d = data_scraper.bet3000englisch()
    print("Bet3000 Premier League done")
    betfaird = data_scraper.betfairenglisch()
    print("BetFair Premier League done")

    with open("bundesliga_dicts", "w") as premier:
    	premier.write(tipicod)
    	premier.write(xbetd)
    	premier.write(bet3000d)
    	premier.write(betfaird)
    premier.close()

    return [tipicod, bet3000d,betfaird, xbetd]


def getChampionshipDicts():

    tipicod = data_scraper.tipicoenglisch2()
    print("Tipico Championship Done")
    xbetd = data_scraper.xbetenglisch2()
    print("Xbet Championship Done")
    bet3000d = data_scraper.bet3000englisch2()
    print("Bet3000 Championship done")
    betfaird = data_scraper.betfairenglisch2()
    print("BetFair Championship done")

    with open("bundesliga_dicts", "w") as champ:
    	champ.write(tipicod)
    	champ.write(xbetd)
    	champ.write(bet3000d)
    	champ.write(betfaird)
    champ.close()

    return [tipicod, bet3000d,betfaird, xbetd]


def sucheEinmalige(Dictionarylist, gesamtEinsatz  = 12.5):
    Sets = []
    Namen = []

    for Dictionary in Dictionarylist:
        Namen.append(Dictionary["name"])
        Sets.append(set(Dictionary.keys()))

    for i in range(len(Namen)):
        alreadyseen = []
        for j in range(len(Namen)):
            if len(Sets[i]) > len(Sets[j]):
                for Ereignis in Sets[i]:
                    if Ereignis not in Sets[j]:
                        if Ereignis not in alreadyseen:
                            alreadyseen.append(Ereignis)
                            print(Namen[i])
                            print(Ereignis)
                            print(Dictionarylist[i][Ereignis])
                            Arb = arbitrageModel(Dictionarylist[i][Ereignis], gesamtEinsatz)
                            printTableNeat(Arb)


def find_if_arbitrage(Dictionarylist, gesamtEinsatz  = 12.5):
    smallest_idx = 0;
    min_len = len(Dictionarylist[0])
    for i in range(1, len(Dictionarylist)):
        if len(Dictionarylist[i]) < min_len:
            min_len = len(Dictionarylist[i])
            smallest_idx = i

    for eventname in set(Dictionarylist[smallest_idx].keys()):
        if eventname != "name":
            quote_list = []
            namen = []
            for hun in [0,1,2]:
                highest_quote = 0.0
                for Wettanbieter in Dictionarylist:
                    if eventname in set(Wettanbieter.keys()):
                        if Wettanbieter[eventname][hun] > highest_quote:
                            name = Wettanbieter["name"]
                            highest_quote = Wettanbieter[eventname][hun]
                namen.append(name)
                quote_list.append(highest_quote)
            print(eventname)
            print(quote_list)
            print(namen)
            Arb = arbitrageModel(quote_list, gesamtEinsatz)
            printTableNeat(Arb)



def put_it_all_together():

	dict_list_bundesliga = getBundesligaDicts()

	dict_list_premier_league = getPremierleagueDicts()
	dict_list_championship = getChampionshipDicts()

	print("\nBundesliga:")
	find_if_arbitrage(dict_list_bundesliga)
	print("Premier League")
	find_if_arbitrage(dict_list_premier_league)
	print("Premier League")
	find_if_arbitrage(dict_list_championship)


	#data_scraper.sucheEinmalige(dict_list)

	print("Fertig")

put_it_all_together()





