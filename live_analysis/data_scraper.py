import urllib
import re


#TODO Interwetten https://www.interwetten7.com/de/sportwetten/l/1019/deutschland-bundesliga

def tipicogerman():
    # data = usock.read()
    # usock.close()


    url = 'https://www.tipico.de/de/online-sportwetten/fussball/deutschland/bundesliga/g42301/'
    page = urllib.request.urlopen(url)
    data = page.read()
    # data = open("test.txt", "r").read()

    dataAsString = str(data)
    page.close()

    # Quoten bekommen
    quotenindex = [m.start() for m in re.finditer("tresult_pk", dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+33]
        Quote = toBeExtracted[toBeExtracted.find(">") + 1:toBeExtracted.rfind("<")].replace(",", ".")
        Quotenliste.append(float(Quote))
    # print("Tipico Quoten done")

    # Spiele bekommen
    spielIndex = [m.start() for m in re.finditer("http://schema.org/SportsEvent", dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+120]
        Spiel = toBeExtracted[toBeExtracted.find("content=") + len("content=")+1:toBeExtracted.rfind('">')]
        Spieleliste.append("".join(Spiel.split()))
    # print("Tipico Spiele done")

    # Connect Spiele und Quoten
    tipicoDict = {}
    tipicoDict["name"] = "Tipico"
    a = 0
    for Spielereignis in Spieleliste:
        tipicoDict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(tipicoDict)


def tipicogerman2():

    url = 'https://www.tipico.de/de/online-sportwetten/fussball/deutschland/2-bundesliga/g41301/'
    page = urllib.request.urlopen(url)
    data = page.read()
    # data = open("test.txt", "r").read()

    dataAsString = str(data)
    page.close()

    # Quoten bekommen
    quotenindex = [m.start() for m in re.finditer("tresult_pk", dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+33]
        Quote = toBeExtracted[toBeExtracted.find(">") + 1:toBeExtracted.rfind("<")].replace(",", ".")
        Quotenliste.append(float(Quote))
    # print("Tipico Quoten done")

    # Spiele bekommen
    spielIndex = [m.start() for m in re.finditer("http://schema.org/SportsEvent", dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+120]
        Spiel = toBeExtracted[toBeExtracted.find("content=") + len("content=")+1:toBeExtracted.rfind('">')]
        Spieleliste.append("".join(Spiel.split()))
    # print("Tipico Spiele done")

    # Connect Spiele und Quoten
    tipicoDict = {}
    tipicoDict["name"] = "Tipico"
    a = 0
    for Spielereignis in Spieleliste:
        tipicoDict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(tipicoDict)


def tipicoitalien():

    url = 'https://www.tipico.de/de/online-sportwetten/fussball/italien/serie-a/g33301/'
    page = urllib.request.urlopen(url)
    data = page.read()
    # data = open("test.txt", "r").read()

    dataAsString = str(data)
    page.close()

    # Quoten bekommen
    quotenindex = [m.start() for m in re.finditer("tresult_pk", dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+33]
        Quote = toBeExtracted[toBeExtracted.find(">") + 1:toBeExtracted.rfind("<")].replace(",", ".")
        Quotenliste.append(float(Quote))
    # print("Tipico Quoten done")

    # Spiele bekommen
    spielIndex = [m.start() for m in re.finditer("http://schema.org/SportsEvent", dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+120]
        Spiel = toBeExtracted[toBeExtracted.find("content=") + len("content=")+1:toBeExtracted.rfind('">')]
        Spieleliste.append("".join(Spiel.split()))
    # print("Tipico Spiele done")

    # Connect Spiele und Quoten
    tipicoDict = {}
    tipicoDict["name"] = "Tipico"
    a = 0
    for Spielereignis in Spieleliste:
        tipicoDict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(tipicoDict)


def tipicoitalien2():

    url = 'https://www.tipico.de/de/online-sportwetten/fussball/italien/serie-b/g34301/'
    page = urllib.request.urlopen(url)
    data = page.read()
    # data = open("test.txt", "r").read()

    dataAsString = str(data)
    page.close()

    # Quoten bekommen
    quotenindex = [m.start() for m in re.finditer("tresult_pk", dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+33]
        Quote = toBeExtracted[toBeExtracted.find(">") + 1:toBeExtracted.rfind("<")].replace(",", ".")
        Quotenliste.append(float(Quote))
    # print("Tipico Quoten done")

    # Spiele bekommen
    spielIndex = [m.start() for m in re.finditer("http://schema.org/SportsEvent", dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+120]
        Spiel = toBeExtracted[toBeExtracted.find("content=") + len("content=")+1:toBeExtracted.rfind('">')]
        Spieleliste.append("".join(Spiel.split()))
    # print("Tipico Spiele done")

    # Connect Spiele und Quoten
    tipicoDict = {}
    tipicoDict["name"] = "Tipico"
    a = 0
    for Spielereignis in Spieleliste:
        tipicoDict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(tipicoDict)


def tipicospanien():

    url = 'https://www.tipico.de/de/online-sportwetten/fussball/spanien/la-liga/g36301/'
    page = urllib.request.urlopen(url)
    data = page.read()
    # data = open("test.txt", "r").read()

    dataAsString = str(data)
    page.close()

    # Quoten bekommen
    quotenindex = [m.start() for m in re.finditer("tresult_pk", dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+33]
        Quote = toBeExtracted[toBeExtracted.find(">") + 1:toBeExtracted.rfind("<")].replace(",", ".")
        Quotenliste.append(float(Quote))
    # print("Tipico Quoten done")

    # Spiele bekommen
    spielIndex = [m.start() for m in re.finditer("http://schema.org/SportsEvent", dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+120]
        Spiel = toBeExtracted[toBeExtracted.find("content=") + len("content=")+1:toBeExtracted.rfind('">')]
        Spieleliste.append("".join(Spiel.split()))
    # print("Tipico Spiele done")

    # Connect Spiele und Quoten
    tipicoDict = {}
    tipicoDict["name"] = "Tipico"
    a = 0
    for Spielereignis in Spieleliste:
        tipicoDict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(tipicoDict)


def tipicospanien2():

    url = 'https://www.tipico.de/de/online-sportwetten/fussball/spanien/la-liga-2/g37301/'
    page = urllib.request.urlopen(url)
    data = page.read()
    # data = open("test.txt", "r").read()

    dataAsString = str(data)
    page.close()


    # Quoten bekommen
    quotenindex = [m.start() for m in re.finditer("tresult_pk", dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+33]
        Quote = toBeExtracted[toBeExtracted.find(">") + 1:toBeExtracted.rfind("<")].replace(",", ".")
        Quotenliste.append(float(Quote))
    # print("Tipico Quoten done")

    # Spiele bekommen
    spielIndex = [m.start() for m in re.finditer("http://schema.org/SportsEvent", dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+120]
        Spiel = toBeExtracted[toBeExtracted.find("content=") + len("content=")+1:toBeExtracted.rfind('">')]
        Spieleliste.append("".join(Spiel.split()))
    # print("Tipico Spiele done")

    # Connect Spiele und Quoten
    tipicoDict = {}
    tipicoDict["name"] = "Tipico"
    a = 0
    for Spielereignis in Spieleliste:
        tipicoDict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(tipicoDict)


def tipicoenglisch():

    url = 'https://www.tipico.de/de/online-sportwetten/fussball/england/premier-league/g1301/'
    page = urllib.request.urlopen(url)
    data = page.read()
    # data = open("test.txt", "r").read()

    dataAsString = str(data)
    page.close()

    # Quoten bekommen
    quotenindex = [m.start() for m in re.finditer("tresult_pk", dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+33]
        Quote = toBeExtracted[toBeExtracted.find(">") + 1:toBeExtracted.rfind("<")].replace(",", ".")
        Quotenliste.append(float(Quote))
    # print("Tipico Quoten done")

    # Spiele bekommen
    spielIndex = [m.start() for m in re.finditer("http://schema.org/SportsEvent", dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+120]
        Spiel = toBeExtracted[toBeExtracted.find("content=") + len("content=")+1:toBeExtracted.rfind('">')]
        Spieleliste.append("".join(Spiel.split()))
    # print("Tipico Spiele done")

    # Connect Spiele und Quoten
    tipicoDict = {}
    tipicoDict["name"] = "Tipico"
    a = 0
    for Spielereignis in Spieleliste:
        tipicoDict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(tipicoDict)


def tipicoenglisch2():

    url = 'https://www.tipico.de/de/online-sportwetten/fussball/england/championship/g2301/'
    page = urllib.request.urlopen(url)
    data = page.read()
    # data = open("test.txt", "r").read()

    dataAsString = str(data)
    page.close()


    # Quoten bekommen
    quotenindex = [m.start() for m in re.finditer("tresult_pk", dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+33]
        Quote = toBeExtracted[toBeExtracted.find(">") + 1:toBeExtracted.rfind("<")].replace(",", ".")
        Quotenliste.append(float(Quote))
    # print("Tipico Quoten done")

    # Spiele bekommen
    spielIndex = [m.start() for m in re.finditer("http://schema.org/SportsEvent", dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+120]
        Spiel = toBeExtracted[toBeExtracted.find("content=") + len("content=")+1:toBeExtracted.rfind('">')]
        Spieleliste.append("".join(Spiel.split()))
    # print("Tipico Spiele done")

    # Connect Spiele und Quoten
    tipicoDict = {}
    tipicoDict["name"] = "Tipico"
    a = 0
    for Spielereignis in Spieleliste:
        tipicoDict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(tipicoDict)


def bet3000german():

    url = 'https://www.bet3000.com/de/events/1876-1-bundesliga'

    page = urllib.request.urlopen(url)
    data = page.read()

    # data = open("test.txt", "r").read()
    dataAsString = str(data)
    page.close()

    # Quoten bekommen
    quotenindex = [m.start() for m in re.finditer('span class="odds">', dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+len('span class="odds">')+4]
        Quote = toBeExtracted[toBeExtracted.find(">") + 1:toBeExtracted.rfind("<")].replace(",", ".")
        Quotenliste.append(round(float(Quote)*0.95, 2))
    # print("Bet3000 Quoten done")

    # Spiele bekommen
    spielIndex = [m.start() for m in re.finditer('itemType="http://schema.org/SportsEvent" data-radium="true"><meta itemProp="name" content=', dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+ len('itemType="http://schema.org/SportsEvent" data-radium="true"><meta itemProp="name" content=')+60]
        Spiel = toBeExtracted[toBeExtracted.find("content=") + len("content=")+1:toBeExtracted.rfind('"/>')]
        Spielbearb = "".join(Spiel.split())
        Spielbearb = Spielbearb.replace("1.FsvMainz05", "FSVMainz05")
        Spielbearb = Spielbearb.replace("FCSchalke04", "Schalke04")
        Spielbearb = Spielbearb.replace("BorussiaM&#x27;gladbach", "BorussiaM\\'gladbach")
        Spielbearb = Spielbearb.replace("Fort.D\\xc3\\xbcsseldorf", "FortunaD\\xc3\\xbcsseldorf")
        Spielbearb = Spielbearb.replace("SCPaderborn07", "SCPaderborn")
        Spieleliste.append(Spielbearb)
    # print("Bet3000 Spiele done")

    # Connect Spiele und Quoten
    bet3000dict = {}
    bet3000dict["name"] = "Bet3000"
    a = 0
    for Spielereignis in Spieleliste:
        bet3000dict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(bet3000dict)


def bet3000german2():

    url = 'https://www.bet3000.com/de/events/1941-2-bundesliga'

    page = urllib.request.urlopen(url)
    data = page.read()

    dataAsString = str(data)
    page.close()

    # Quoten bekommen
    quotenindex = [m.start() for m in re.finditer('span class="odds">', dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+len('span class="odds">')+4]
        Quote = toBeExtracted[toBeExtracted.find(">") + 1:toBeExtracted.rfind("<")].replace(",", ".")
        Quotenliste.append(round(float(Quote)*0.95,2))
    # print("Bet3000 Quoten done")

    # Spiele bekommen
    spielIndex = [m.start() for m in re.finditer('itemType="http://schema.org/SportsEvent" data-radium="true"><meta \
                                                 itemProp="name" content=', dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+ len('itemType="http://schema.org/SportsEvent"\
                                                                    data-radium="true"><meta itemProp="name"\
                                                                    content=')+60]
        Spiel = toBeExtracted[toBeExtracted.find("content=") + len("content=")+1:toBeExtracted.rfind('"/>')]
        Spielbearb = "".join(Spiel.split())
        Spielbearb = Spielbearb.replace("SVDarmstadt", "SVDarmstadt98")
        Spielbearb = Spielbearb.replace("FCSt.Pauli", "St.Pauli")
        Spieleliste.append(Spielbearb)
    # print("Bet3000 Spiele done")

    # Connect Spiele und Quoten
    bet3000dict = {}
    bet3000dict["name"] = "Bet3000"
    a = 0
    for Spielereignis in Spieleliste:
        bet3000dict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(bet3000dict)


def bet3000englisch():

    url = 'https://www.bet3000.com/de/events/1948-premier-league'

    page = urllib.request.urlopen(url)
    data = page.read()

    # data = open("test.txt", "r").read()
    dataAsString = str(data)
    page.close()


    # Quoten bekommen
    quotenindex = [m.start() for m in re.finditer('span class="odds">', dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+len('span class="odds">')+4]
        Quote = toBeExtracted[toBeExtracted.find(">") + 1:toBeExtracted.rfind("<")].replace(",", ".")
        Quotenliste.append(round(float(Quote)*0.95,2))


    #Spiele bekommen
    spielIndex = [m.start() for m in re.finditer('itemType="http://schema.org/SportsEvent" data-radium="true"><meta itemProp="name" content=', dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+ len('itemType="http://schema.org/SportsEvent" data-radium="true"><meta itemProp="name" content=')+60]
        Spiel = toBeExtracted[toBeExtracted.find("content=") + len("content=")+1:toBeExtracted.rfind('"/>')]
        Spielbearb = "".join(Spiel.split())
        Spielbearb = Spielbearb.replace("ArsenalFC", "FCArsenal")
        Spielbearb = Spielbearb.replace("Brighton&amp;Hove", "Brighton&Hove")
        Spielbearb = Spielbearb.replace("SheffieldUnited", "SheffieldUtd")
        Spieleliste.append(Spielbearb)


    #Connect Spiele und Quoten
    bet3000dict = {}
    bet3000dict["name"] = "Bet3000"
    a = 0
    for Spielereignis in Spieleliste:
        bet3000dict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(bet3000dict)

def bet3000englisch2():

    url = 'https://www.bet3000.com/de/events/1949-championship'

    page = urllib.request.urlopen(url)
    data = page.read()

    #data = open("test.txt", "r").read()
    dataAsString = str(data)
    page.close()


    #Quoten bekommen
    quotenindex = [m.start() for m in re.finditer('span class="odds">', dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+len('span class="odds">')+4]
        Quote = toBeExtracted[toBeExtracted.find(">") + 1:toBeExtracted.rfind("<")].replace(",", ".")
        Quotenliste.append(round(float(Quote)*0.95,2))


    #Spiele bekommen
    spielIndex = [m.start() for m in re.finditer('itemType="http://schema.org/SportsEvent" data-radium="true"><meta itemProp="name" content=', dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+ len('itemType="http://schema.org/SportsEvent" data-radium="true"><meta itemProp="name" content=')+60]
        Spiel = toBeExtracted[toBeExtracted.find("content=") + len("content=")+1:toBeExtracted.rfind('"/>')]
        Spielbearb = "".join(Spiel.split())
        Spielbearb = Spielbearb.replace("SheffieldUnited", "SheffieldUtd")
        Spielbearb = Spielbearb.replace("QPRangers","QueensParkRangers")
        Spielbearb = Spielbearb.replace("WestBrom", "WestBromwich")
        Spielbearb = Spielbearb.replace("RotherhamUnited", "RotherhamUtd")
        Spielbearb = Spielbearb.replace("BirminghamCity", "Birmingham")
        Spielbearb = Spielbearb.replace("BlackburnRovers", "BlackburnRov.")
        Spielbearb = Spielbearb.replace("AstonVilla", "AstonVillaFC")
        Spielbearb = Spielbearb.replace("CharltonAthletic", "CharltonAth.")
        Spieleliste.append(Spielbearb)


    #Connect Spiele und Quoten
    bet3000dict = {}
    bet3000dict["name"] = "Bet3000"
    a = 0
    for Spielereignis in Spieleliste:
        bet3000dict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(bet3000dict)

def bet3000spanien():

    url = 'https://www.bet3000.com/de/events/1945-la-liga'

    page = urllib.request.urlopen(url)
    data = page.read()

    #data = open("test.txt", "r").read()
    dataAsString = str(data)
    page.close()
    # with open("test.txt", "w", encoding='utf-8') as yoho:
    #     yoho.write(dataAsString)


    #Quoten bekommen
    quotenindex = [m.start() for m in re.finditer('span class="odds">', dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+len('span class="odds">')+4]
        Quote = toBeExtracted[toBeExtracted.find(">") + 1:toBeExtracted.rfind("<")].replace(",", ".")
        Quotenliste.append(round(float(Quote)*0.95,2))
    #print("Bet3000 Quoten done")

    #Spiele bekommen
    spielIndex = [m.start() for m in re.finditer('itemType="http://schema.org/SportsEvent" data-radium="true"><meta itemProp="name" content=', dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+ len('itemType="http://schema.org/SportsEvent" data-radium="true"><meta itemProp="name" content=')+60]
        Spiel = toBeExtracted[toBeExtracted.find("content=") + len("content=")+1:toBeExtracted.rfind('"/>')]
        Spielbearb = "".join(Spiel.split())
        Spielbearb = Spielbearb.replace("FCValencia", "ValenciaC.F.")
        Spielbearb = Spielbearb.replace("DeportivoAlaves", "Alaves")
        Spielbearb = Spielbearb.replace("RealBetis", "BetisSevilla")
        Spieleliste.append(Spielbearb)
    #print("Bet3000 Spiele done")

    #Connect Spiele und Quoten
    bet3000dict = {}
    bet3000dict["name"] = "Bet3000"
    a = 0
    for Spielereignis in Spieleliste:
        bet3000dict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(bet3000dict)

def bet3000spanien2():

    url = 'https://www.bet3000.com/de/events/5603-la-liga-2'

    page = urllib.request.urlopen(url)
    data = page.read()

    #data = open("test.txt", "r").read()
    dataAsString = str(data)
    page.close()
    # with open("test.txt", "w", encoding='utf-8') as yoho:
    #     yoho.write(dataAsString)


    #Quoten bekommen
    quotenindex = [m.start() for m in re.finditer('span class="odds">', dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+len('span class="odds">')+4]
        Quote = toBeExtracted[toBeExtracted.find(">") + 1:toBeExtracted.rfind("<")].replace(",", ".")
        Quotenliste.append(round(float(Quote)*0.95,2))
    #print("Bet3000 Quoten done")

    #Spiele bekommen
    spielIndex = [m.start() for m in re.finditer('itemType="http://schema.org/SportsEvent" data-radium="true"><meta itemProp="name" content=', dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+ len('itemType="http://schema.org/SportsEvent" data-radium="true"><meta itemProp="name" content=')+60]
        Spiel = toBeExtracted[toBeExtracted.find("content=") + len("content=")+1:toBeExtracted.rfind('"/>')]
        Spielbearb = "".join(Spiel.split())
        Spielbearb = Spielbearb.replace("Ponferradina", "SDPonferradina")
        Spielbearb = Spielbearb.replace("Albacete", "AlbaceteBalompie")
        Spielbearb = Spielbearb.replace("LaCoruna", "DeportivoLaCoruna")
        Spielbearb = Spielbearb.replace("FCMalaga", "CFMalaga")

        Spielbearb = Spielbearb.replace("ElcheCF", "CFElche")
        Spielbearb = Spielbearb.replace("LasPalmas", "UDLasPalmas")
        Spieleliste.append(Spielbearb)
    #print("Bet3000 Spiele done")

    #Connect Spiele und Quoten
    bet3000dict = {}
    bet3000dict["name"] = "Bet3000"
    a = 0
    for Spielereignis in Spieleliste:
        bet3000dict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(bet3000dict)

def bet3000italien():

    url = 'https://www.bet3000.com/de/events/1946-serie-a'

    page = urllib.request.urlopen(url)
    data = page.read()

    #data = open("test.txt", "r").read()
    dataAsString = str(data)
    page.close()
    # with open("test.txt", "w", encoding='utf-8') as yoho:
    #     yoho.write(dataAsString)


    #Quoten bekommen
    quotenindex = [m.start() for m in re.finditer('span class="odds">', dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+len('span class="odds">')+4]
        Quote = toBeExtracted[toBeExtracted.find(">") + 1:toBeExtracted.rfind("<")].replace(",", ".")
        Quotenliste.append(round(float(Quote)*0.95,2))
    #print("Bet3000 Quoten done")

    #Spiele bekommen
    spielIndex = [m.start() for m in re.finditer('itemType="http://schema.org/SportsEvent" data-radium="true"><meta itemProp="name" content=', dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+ len('itemType="http://schema.org/SportsEvent" data-radium="true"><meta itemProp="name" content=')+60]
        Spiel = toBeExtracted[toBeExtracted.find("content=") + len("content=")+1:toBeExtracted.rfind('"/>')]
        Spielbearb = "".join(Spiel.split())
        Spielbearb = Spielbearb.replace("USSassuoloCalcio", "USSassuolo")
        Spielbearb = Spielbearb.replace("UCSampdoria", "SampdoriaGenua")
        Spielbearb = Spielbearb.replace("BolognaFC", "FCBologna")
        Spielbearb = Spielbearb.replace("GenuaCfc", "GenuaFC")
        Spielbearb = Spielbearb.replace("ParmaCalcio", "FCParma")
        Spielbearb = Spielbearb.replace("SSLazioRom", "LazioRom")
        Spieleliste.append(Spielbearb)
    #print("Bet3000 Spiele done")

    #Connect Spiele und Quoten
    bet3000dict = {}
    bet3000dict["name"] = "Bet3000"
    a = 0
    for Spielereignis in Spieleliste:
        bet3000dict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(bet3000dict)

def bet3000italien2():

    url = 'https://www.bet3000.com/de/events/1947-serie-b'

    page = urllib.request.urlopen(url)
    data = page.read()

    #data = open("test.txt", "r").read()
    dataAsString = str(data)
    page.close()
    # with open("test.txt", "w", encoding='utf-8') as yoho:
    #     yoho.write(dataAsString)


    #Quoten bekommen
    quotenindex = [m.start() for m in re.finditer('span class="odds">', dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+len('span class="odds">')+4]
        Quote = toBeExtracted[toBeExtracted.find(">") + 1:toBeExtracted.rfind("<")].replace(",", ".")
        Quotenliste.append(round(float(Quote)*0.95,2))
    #print("Bet3000 Quoten done")

    #Spiele bekommen
    spielIndex = [m.start() for m in re.finditer('itemType="http://schema.org/SportsEvent" data-radium="true"><meta itemProp="name" content=', dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+ len('itemType="http://schema.org/SportsEvent" data-radium="true"><meta itemProp="name" content=')+60]
        Spiel = toBeExtracted[toBeExtracted.find("content=") + len("content=")+1:toBeExtracted.rfind('"/>')]
        Spielbearb = "".join(Spiel.split())
        Spielbearb = Spielbearb.replace("ACPisa", "SCPisa")
        Spielbearb = Spielbearb.replace("Pordenone", "PordenoneCalcio")
        Spielbearb = Spielbearb.replace("AscoliCalcio1898FC", "Ascoli")
        Spielbearb = Spielbearb.replace("ChievoVerona", "ACChievoVerona")
        Spielbearb = Spielbearb.replace("PescaraCalcio", "USPescara")
        Spielbearb = Spielbearb.replace("Benevento", "BeneventoCalcio")
        Spieleliste.append(Spielbearb)
    #print("Bet3000 Spiele done")

    #Connect Spiele und Quoten
    bet3000dict = {}
    bet3000dict["name"] = "Bet3000"
    a = 0
    for Spielereignis in Spieleliste:
        bet3000dict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(bet3000dict)






def betfairgerman():

    url = 'https://www.betfair.com/sport/football?id=59&otherAction=selectOtherCompetition&competitionEventId=605621&action=loadCompetition&competitionId=59&selectedTabType=COMPETITION&modules=multipickavbId'

    page = urllib.request.urlopen(url)
    data = page.read()

    #data = open("test.txt", "r").read()
    dataAsString = str(data)
    page.close()


    #Quoten bekommen
    quotenindex = [m.start() for m in re.finditer('<span class="ui-runner-price ui-', dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+len('<span class="ui-runner-price ui-')+40]
        Quote = toBeExtracted[toBeExtracted.find('"> ')+3:toBeExtracted.rfind(" </sp")].replace(",", ".")
        Quotenliste.append(round(float(Quote),2))
    del Quotenliste[::5]
    del Quotenliste[::4]
    #print("Betfair Quoten done")

    #Spiele bekommen
    spielIndex = [m.start() for m in re.finditer('class="team-name" title="', dataAsString)]
    Spieleliste = []
    Team1 = True
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+ len('class="team-name" title="')+30]
        Team = toBeExtracted[toBeExtracted.find("title=") + len("title=")+1:toBeExtracted.rfind('">')]
        if Team1:
            Spiel = Team
            Team1 = False
        else:
            Spiel = Spiel + "-" + Team
            Team1 = True
            Spielbearb = "".join(Spiel.split())
            Spielbearb = Spielbearb.replace("Augsburg", "FCAugsburg")
            Spielbearb = Spielbearb.replace("Hoffenheim", "1899Hoffenheim")
            Spielbearb = Spielbearb.replace("M\\'gladbach", "BorussiaM\\'gladbach")
            Spielbearb = Spielbearb.replace("Mainz", "FSVMainz05")
            Spielbearb = Spielbearb.replace("Freiburg", "SCFreiburg")
            Spielbearb = Spielbearb.replace("Stuttgart", "VFBStuttgart")
            Spielbearb = Spielbearb.replace("Hannover", "Hannover96")
            Spielbearb = Spielbearb.replace("Wolfsburg", "VfLWolfsburg")
            Spielbearb = Spielbearb.replace("VFBStuttgart", "VfBStuttgart")
            Spielbearb = Spielbearb.replace("N\\xc3\\xbcrnberg", "1.FCN\\xc3\\xbcrnberg")
            Spielbearb = Spielbearb.replace("Leverkusen", "BayerLeverkusen")
            Spielbearb = Spielbearb.replace("Dortmund", "BorussiaDortmund")
            Spielbearb = Spielbearb.replace("HerthaBerlin", "HerthaBSC")
            Spieleliste.append(Spielbearb)
    #print("Betfair Spiele done")

    #Connect Spiele und Quoten
    betfairdict = {}
    betfairdict["name"] = "BetFair"
    a = 0
    for Spielereignis in Spieleliste:
        betfairdict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(betfairdict)

def betfairenglisch():

    url = 'https://www.betfair.com/sport/football?id=10932509&otherAction=selectOtherCompetition&competitionEventId=2022802&action=loadCompetition&competitionId=10932509&selectedTabType=COMPETITION&modules=multipickavbId'

    page = urllib.request.urlopen(url)
    data = page.read()

    #data = open("test.txt", "r").read()
    dataAsString = str(data)
    page.close()



    #Quoten bekommen
    quotenindex = [m.start() for m in re.finditer('<span class="ui-runner-price ui-', dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+len('<span class="ui-runner-price ui-')+40]
        Quote = toBeExtracted[toBeExtracted.find('"> ')+3:toBeExtracted.rfind(" </sp")].replace(",", ".")
        Quotenliste.append(round(float(Quote),2))
    del Quotenliste[::5]
    del Quotenliste[::4]
    #print("Betfair Quoten done")

    #Spiele bekommen
    spielIndex = [m.start() for m in re.finditer('class="team-name" title="', dataAsString)]
    Spieleliste = []
    Team1 = True
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+ len('class="team-name" title="')+30]
        Team = toBeExtracted[toBeExtracted.find("title=") + len("title=")+1:toBeExtracted.rfind('">')]
        if Team1:
            Spiel = Team
            Team1 = False
        else:
            Spiel = Spiel + "-" + Team
            Team1 = True
            Spielbearb = "".join(Spiel.split())
            Spielbearb = Spielbearb.replace("Chelsea", "FCChelsea")
            Spielbearb = Spielbearb.replace("Burnley", "FCBurnley")
            Spielbearb = Spielbearb.replace("Fulham", "FCFulham")
            Spielbearb = Spielbearb.replace("Cardiff", "CardiffCity")
            Spielbearb = Spielbearb.replace("Leicester", "LeicesterCity")
            Spielbearb = Spielbearb.replace("Arsenal", "FCArsenal")
            Spielbearb = Spielbearb.replace("Watford", "FCWatford")
            Spielbearb = Spielbearb.replace("Southampton", "SouthamptonFC")
            Spielbearb = Spielbearb.replace("ManUtd", "ManchesterUnited")
            Spielbearb = Spielbearb.replace("Tottenham", "TottenhamHotspur")
            Spielbearb = Spielbearb.replace("Liverpool", "FCLiverpool")
            Spielbearb = Spielbearb.replace("Bournemouth", "AFCBournemouth")
            Spielbearb = Spielbearb.replace("ManCity", "ManchesterCity")
            Spielbearb = Spielbearb.replace("Wolves", "Wolverhampton")
            Spielbearb = Spielbearb.replace("Brighton", "Brighton&Hove")
            Spielbearb = Spielbearb.replace("Huddersfield", "HuddersfieldTown")
            Spielbearb = Spielbearb.replace("WestHam", "WestHamUnited")
            Spielbearb = Spielbearb.replace("Everton", "FCEverton")
            Spielbearb = Spielbearb.replace("Newcastle", "NewcastleUnited")


            Spieleliste.append(Spielbearb)
    #print("Betfair Spiele done")

    #Connect Spiele und Quoten
    betfairdict = {}
    betfairdict["name"] = "BetFair"
    a = 0
    for Spielereignis in Spieleliste:
        betfairdict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(betfairdict)

def betfairenglisch2():

    url = 'https://www.betfair.com/sport/football?id=7129730&otherAction=selectOtherCompetition&competitionEventId=1908053&action=loadCompetition&competitionId=7129730&selectedTabType=COMPETITION&modules=multipickavbId'

    page = urllib.request.urlopen(url)
    data = page.read()

    #data = open("test.txt", "r").read()
    dataAsString = str(data)
    page.close()



    #Quoten bekommen
    quotenindex = [m.start() for m in re.finditer('<span class="ui-runner-price ui-', dataAsString)]
    Quotenliste = []
    for extractQuote in quotenindex:
        toBeExtracted = dataAsString[extractQuote:extractQuote+len('<span class="ui-runner-price ui-')+40]
        Quote = toBeExtracted[toBeExtracted.find('"> ')+3:toBeExtracted.rfind(" </sp")].replace(",", ".")
        Quotenliste.append(round(float(Quote),2))
    del Quotenliste[::5]
    del Quotenliste[::4]
    #print("Betfair Quoten done")

    #Spiele bekommen
    spielIndex = [m.start() for m in re.finditer('class="team-name" title="', dataAsString)]
    Spieleliste = []
    Team1 = True
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+ len('class="team-name" title="')+30]
        Team = toBeExtracted[toBeExtracted.find("title=") + len("title=")+1:toBeExtracted.rfind('">')]
        if Team1:
            Spiel = Team
            Team1 = False
        else:
            Spiel = Spiel + "-" + Team
            Team1 = True
            Spielbearb = "".join(Spiel.split())
            Spielbearb = Spielbearb.replace("SheffUtd", "SheffieldUtd")
            Spielbearb = Spielbearb.replace("Ipswich", "IpswichTown")
            Spielbearb = Spielbearb.replace("Reading", "FCReading")
            Spielbearb = Spielbearb.replace("Derby", "DerbyCounty")
            Spielbearb = Spielbearb.replace("WestBrom", "WestBromwich")
            Spielbearb = Spielbearb.replace("Rotherham", "RotherhamUtd")
            Spielbearb = Spielbearb.replace("Wigan", "WiganAthletic")
            Spielbearb = Spielbearb.replace("Preston", "PrestonNorthEnd")
            Spielbearb = Spielbearb.replace("SheffWed", "SheffieldWed.")
            Spielbearb = Spielbearb.replace("Swansea", "SwanseaCity")
            Spielbearb = Spielbearb.replace("Hull", "HullCity")
            Spielbearb = Spielbearb.replace("QPR", "QueensParkRangers")
            Spielbearb = Spielbearb.replace("NottmForest", "NottinghamF.")
            Spielbearb = Spielbearb.replace("Millwall", "MillwallFC")
            Spielbearb = Spielbearb.replace("Stoke", "StokeCity")
            Spielbearb = Spielbearb.replace("Norwich", "NorwichCity")
            Spielbearb = Spielbearb.replace("Blackburn", "BlackburnRov.")
            Spielbearb = Spielbearb.replace("Leeds", "LeedsUnited")
            Spielbearb = Spielbearb.replace("AstonVilla", "AstonVillaFC")
            Spielbearb = Spielbearb.replace("Bolton", "BoltonWanderers")
            Spielbearb = Spielbearb.replace("Brentford", "BrentfordFC")
            Spieleliste.append(Spielbearb)
    #print("Betfair Spiele done")

    #Connect Spiele und Quoten
    betfairdict = {}
    betfairdict["name"] = "BetFair"
    a = 0
    for Spielereignis in Spieleliste:
        betfairdict[Spielereignis] = Quotenliste[a:a+3]
        a += 3
    return(betfairdict)

def xbetgerman():
    #data = usock.read()
    #usock.close()


    url = 'https://de.1xbet.com/de/betsonyour/line/Football/96463-Germany-Bundesliga/'
    page = urllib.request.urlopen(url)
    data = page.read()
    #data = open("test.txt", "r").read()

    dataAsString = str(data)
    page.close()

    #Quoten bekommen
    quotenindex1 = [m.start() for m in re.finditer('"name":"S1","price":"', dataAsString)]
    quotenindex2 = [m.start() for m in re.finditer('"name":"S2","price":"', dataAsString)]
    Quotenliste = []

    for ccc in range(len(quotenindex1)):
        if dataAsString[quotenindex1[ccc]-8:quotenindex1[ccc]-3] != "Goals":
            toBeExtracted = dataAsString[quotenindex1[ccc] + len('"name":"S1","pric'):quotenindex1[ccc]+len('"name":"S1","price":"')+10]
            Quote_H = toBeExtracted[toBeExtracted.find('e":"')+len('e":"'):toBeExtracted.rfind('"},{')].replace(",", ".")
            Quotenliste.append(round(float(Quote_H),2))
            toBeExtracted = dataAsString[quotenindex2[ccc] + len('"name":"S1","pric'):quotenindex2[ccc]+len('"name":"S1","price":"')+10]
            Quote_A = toBeExtracted[toBeExtracted.find('e":"')+len('e":"'):toBeExtracted.rfind('"}]}')].replace(",", ".")
            u_zwischen = dataAsString[dataAsString.find('{"C":' + str(Quote_H) + ',"G":1,"T":1},{"C":') + len(('{"C":' + str(Quote_H) + ',"G":1,"T":1},{"C":')):dataAsString.find('{"C":' + str(Quote_H) + ',"G":1,"T":1},{"C":') + len(('{"C":' + str(Quote_H) + ',"G":1,"T":1},{"C":')) + 6 + len(',"G":1,"T":2},{"C":' + str(Quote_A) + ',"G":1,"T":3}')]
            Quote_U = u_zwischen[:u_zwischen.rfind(',"G":1,"T":2},{"C":' + str(Quote_A) + ',"G":1,"T":3}')]

            quoteHplatz = "x" * len(Quote_H)
            quoteUplatz = "x" * len(Quote_U)
            quoteAplatz = "x" * len(Quote_A)

            dataAsString = dataAsString.replace('{"C":' + str(Quote_H) + ',"G":1,"T":1},{"C":' + str(Quote_U) + ',"G":1,"T":2},{"C":' + str(Quote_A) + ',"G":1,"T":3}', '{"C":' + str(quoteHplatz) + ',"G":1,"T":1},{"C":' + str(quoteUplatz) + ',"G":1,"T":2},{"C":' + str(quoteAplatz) + ',"G":1,"T":3}')

            Quotenliste.append(round(float(Quote_U),2))
            Quotenliste.append(round(float(Quote_A),2))

    #print("xbet Quoten done")

    #Spiele bekommen
    spielIndex = [m.start() for m in re.finditer('<span class="gname">', dataAsString)]
    Spieleliste = []
    for extractSpiel in spielIndex:
        toBeExtracted = dataAsString[extractSpiel:extractSpiel+150]
        Spiel = toBeExtracted[toBeExtracted.find('"gname">') + len('"gname">'):toBeExtracted.rfind('span class="star"')-18]
        if "(" not in Spiel and "{" not in Spiel:
            strinSpiel = "".join(Spiel.split())
            strinSpiel = strinSpiel.replace("BorussiaM\\xc3\\xb6nchengladbach", "BorussiaM\\'gladbach")
            strinSpiel = strinSpiel.replace("FCSchalke04", "Schalke04")
            strinSpiel = strinSpiel.replace("TSG1899Hoffenheim", "1899Hoffenheim")
            strinSpiel = strinSpiel.replace("FCBayernM\\xc3\\xbcnchen", "BayernM\\xc3\\xbcnchen")
            strinSpiel = strinSpiel.replace("1.FSVMainz05", "FSVMainz05")
            strinSpiel = strinSpiel.replace("Bayer04Leverkusen", "BayerLeverkusen")
            strinSpiel = strinSpiel.replace("Werder\\xd0\\x92remen", "WerderBremen")
            Spieleliste.append(strinSpiel)

    #print("xbet Spiele done")
    #Connect Spiele und Quoten
    xbetDict = {}
    xbetDict["name"] = "Xbet"
    a = 0
    for Spielereignis in Spieleliste:
        if a < len(Quotenliste):
            xbetDict[Spielereignis] = Quotenliste[a:a+3]
            a += 3
    return(xbetDict)

def xbetenglisch():
    #data = usock.read()
    #usock.close()


    url = 'https://de.1xbet.com/de/line/Football/88637-England-Premier-League/'
    page = urllib.request.urlopen(url)
    data = page.read()
    #data = open("test.txt", "r").read()

    dataAsString = str(data)
    page.close()

    #Quoten bekommen
    quotenindex1 = [m.start() for m in re.finditer('"name":"S1","price":"', dataAsString)]
    quotenindex2 = [m.start() for m in re.finditer('"name":"S2","price":"', dataAsString)]
    Quotenliste = []

    for ccc in range(len(quotenindex1)):
        if dataAsString[quotenindex1[ccc]-8:quotenindex1[ccc]-3] != "Goals":
            toBeExtracted = dataAsString[quotenindex1[ccc] + len('"name":"S1","pric'):quotenindex1[ccc]+len('"name":"S1","price":"')+10]
            Quote_H = toBeExtracted[toBeExtracted.find('e":"')+len('e":"'):toBeExtracted.rfind('"},{')].replace(",", ".")
            Quotenliste.append(round(float(Quote_H),2))
            toBeExtracted = dataAsString[quotenindex2[ccc] + len('"name":"S1","pric'):quotenindex2[ccc]+len('"name":"S1","price":"')+10]
            Quote_A = toBeExtracted[toBeExtracted.find('e":"')+len('e":"'):toBeExtracted.rfind('"}]}')].replace(",", ".")
            u_zwischen = dataAsString[dataAsString.find('{"C":' + str(Quote_H) + ',"G":1,"T":1},{"C":') + len(('{"C":' + str(Quote_H) + ',"G":1,"T":1},{"C":')):dataAsString.find('{"C":' + str(Quote_H) + ',"G":1,"T":1},{"C":') + len(('{"C":' + str(Quote_H) + ',"G":1,"T":1},{"C":')) + 6 + len(',"G":1,"T":2},{"C":' + str(Quote_A) + ',"G":1,"T":3}')]
            Quote_U = u_zwischen[:u_zwischen.rfind(',"G":1,"T":2},{"C":' + str(Quote_A) + ',"G":1,"T":3}')]

            quoteHplatz = "x" * len(Quote_H)
            quoteUplatz = "x" * len(Quote_U)
            quoteAplatz = "x" * len(Quote_A)

            dataAsString = dataAsString.replace('{"C":' + str(Quote_H) + ',"G":1,"T":1},{"C":' + str(Quote_U) + ',"G":1,"T":2},{"C":' + str(Quote_A) + ',"G":1,"T":3}', '{"C":' + str(quoteHplatz) + ',"G":1,"T":1},{"C":' + str(quoteUplatz) + ',"G":1,"T":2},{"C":' + str(quoteAplatz) + ',"G":1,"T":3}')

            Quotenliste.append(round(float(Quote_U),2))
            Quotenliste.append(round(float(Quote_A),2))


    #print("xbet Quoten done")

    #Spiele bekommen
    spielIndex1 = [m.start() for m in re.finditer('"homeTeam":{"@type":"SportsTeam","name":"', dataAsString)]
    spielIndex2 = [m.start() for m in re.finditer('"awayTeam":{"@type":"SportsTeam","name":"', dataAsString)]
    Spieleliste = []
    for extractSpiel in range(len(spielIndex1)):

        toBeExtracted1 = dataAsString[spielIndex1[extractSpiel]+len('"awayTeam":{"@type":"SportsTeam","name":"'):spielIndex1[extractSpiel]+len('"awayTeam":{"@type":"SportsTeam","name":"')+40]
        toBeExtracted2 = dataAsString[spielIndex2[extractSpiel]+len('"awayTeam":{"@type":"SportsTeam","name":"'):spielIndex2[extractSpiel]+len('"awayTeam":{"@type":"SportsTeam","name":"')+40]

        if "Heimmannschaft" not in toBeExtracted1:

            Heim = toBeExtracted1[0:toBeExtracted1.rfind('","sport":"')]
            Gast = toBeExtracted2[:toBeExtracted2.rfind('","sport":"')]
            Spiel = Heim + "-" + Gast

            if "(" not in Spiel and "{" not in Spiel:
                strinSpiel = "".join(Spiel.split())
                strinSpiel = strinSpiel.replace("Southampton", "SouthamptonFC")
                strinSpiel = strinSpiel.replace("Brighton&amp;HoveAlbion", "Brighton&Hove")
                strinSpiel = strinSpiel.replace("WolverhamptonWanderers", "Wolverhampton")
                strinSpiel = strinSpiel.replace("FKArsenal", "FCArsenal")
                Spieleliste.append(strinSpiel)
    #print("xbet Spiele done")
    #Connect Spiele und Quoten
    xbetDict = {}
    xbetDict["name"] = "Xbet"
    a = 0
    for Spielereignis in Spieleliste:
        if a < len(Quotenliste):
            xbetDict[Spielereignis] = Quotenliste[a:a+3]
            a += 3
    return(xbetDict)

def xbetenglisch2():
    #data = usock.read()
    #usock.close()


    url = 'https://de.1xbet.com/de/line/Football/105759-England-Championship/'
    page = urllib.request.urlopen(url)
    data = page.read()
    #data = open("test.txt", "r").read()

    dataAsString = str(data)
    page.close()

    #Quoten bekommen
    quotenindex1 = [m.start() for m in re.finditer('"name":"S1","price":"', dataAsString)]
    quotenindex2 = [m.start() for m in re.finditer('"name":"S2","price":"', dataAsString)]
    Quotenliste = []

    for ccc in range(len(quotenindex1)):
        if dataAsString[quotenindex1[ccc]-8:quotenindex1[ccc]-3] != "Goals":
            toBeExtracted = dataAsString[quotenindex1[ccc] + len('"name":"S1","pric'):quotenindex1[ccc]+len('"name":"S1","price":"')+10]
            Quote_H = toBeExtracted[toBeExtracted.find('e":"')+len('e":"'):toBeExtracted.rfind('"},{')].replace(",", ".")
            Quotenliste.append(round(float(Quote_H),2))
            toBeExtracted = dataAsString[quotenindex2[ccc] + len('"name":"S1","pric'):quotenindex2[ccc]+len('"name":"S1","price":"')+10]
            Quote_A = toBeExtracted[toBeExtracted.find('e":"')+len('e":"'):toBeExtracted.rfind('"}]}')].replace(",", ".")
            u_zwischen = dataAsString[dataAsString.find('{"C":' + str(Quote_H) + ',"G":1,"T":1},{"C":') + len(('{"C":' + str(Quote_H) + ',"G":1,"T":1},{"C":')):dataAsString.find('{"C":' + str(Quote_H) + ',"G":1,"T":1},{"C":') + len(('{"C":' + str(Quote_H) + ',"G":1,"T":1},{"C":')) + 6 + len(',"G":1,"T":2},{"C":' + str(Quote_A) + ',"G":1,"T":3}')]
            Quote_U = u_zwischen[:u_zwischen.rfind(',"G":1,"T":2},{"C":' + str(Quote_A) + ',"G":1,"T":3}')]

            quoteHplatz = "x" * len(Quote_H)
            quoteUplatz = "x" * len(Quote_U)
            quoteAplatz = "x" * len(Quote_A)

            dataAsString = dataAsString.replace('{"C":' + str(Quote_H) + ',"G":1,"T":1},{"C":' + str(Quote_U) + ',"G":1,"T":2},{"C":' + str(Quote_A) + ',"G":1,"T":3}', '{"C":' + str(quoteHplatz) + ',"G":1,"T":1},{"C":' + str(quoteUplatz) + ',"G":1,"T":2},{"C":' + str(quoteAplatz) + ',"G":1,"T":3}')

            Quotenliste.append(round(float(Quote_U),2))
            Quotenliste.append(round(float(Quote_A),2))


    #print("xbet Quoten done")

    #Spiele bekommen
    spielIndex1 = [m.start() for m in re.finditer('"homeTeam":{"@type":"SportsTeam","name":"', dataAsString)]
    spielIndex2 = [m.start() for m in re.finditer('"awayTeam":{"@type":"SportsTeam","name":"', dataAsString)]
    Spieleliste = []
    for extractSpiel in range(len(spielIndex1)):

        toBeExtracted1 = dataAsString[spielIndex1[extractSpiel]+len('"awayTeam":{"@type":"SportsTeam","name":"'):spielIndex1[extractSpiel]+len('"awayTeam":{"@type":"SportsTeam","name":"')+40]
        toBeExtracted2 = dataAsString[spielIndex2[extractSpiel]+len('"awayTeam":{"@type":"SportsTeam","name":"'):spielIndex2[extractSpiel]+len('"awayTeam":{"@type":"SportsTeam","name":"')+40]

        if "Heimmannschaft" not in toBeExtracted1:

            Heim = toBeExtracted1[0:toBeExtracted1.rfind('","sport":"')]
            Gast = toBeExtracted2[:toBeExtracted2.rfind('","sport":"')]
            Spiel = Heim + "-" + Gast

            if "(" not in Spiel and "{" not in Spiel:
                strinSpiel = "".join(Spiel.split())
                strinSpiel = strinSpiel.replace("BirminghamCity", "Birmingham")
                strinSpiel = strinSpiel.replace("NottinghamForest", "NottinghamF.")
                strinSpiel = strinSpiel.replace("FCMillwall", "MillwallFC")
                strinSpiel = strinSpiel.replace("SheffieldUnited", "SheffieldUtd")
                strinSpiel = strinSpiel.replace("AstonVilla", "AstonVillaFC")
                strinSpiel = strinSpiel.replace("FCBrentford", "BrentfordFC")
                strinSpiel = strinSpiel.replace("SheffieldWednesday", "SheffieldWed.")
                strinSpiel = strinSpiel.replace("WestBromwichAlbion", "WestBromwich")
                strinSpiel = strinSpiel.replace("RotherhamUnited", "RotherhamUtd")
                strinSpiel = strinSpiel.replace("FCMiddlesbrough", "Middlesbrough")
                strinSpiel = strinSpiel.replace("BlackburnRovers", "BlackburnRov.")
                Spieleliste.append(strinSpiel)
    #print("xbet Spiele done")
    #Connect Spiele und Quoten
    xbetDict = {}
    xbetDict["name"] = "Xbet"
    a = 0
    for Spielereignis in Spieleliste:
        if a < len(Quotenliste):
            xbetDict[Spielereignis] = Quotenliste[a:a+3]
            a += 3
    return(xbetDict)
