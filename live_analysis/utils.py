
def printTableNeat(Arbmodel):

    Quoten = Arbmodel.quotes.tolist()
    Quoten = [str(i) for i in Quoten]

    Probs = list(Arbmodel.getProbabilities())
    Probs = [str(i) for i in Probs]

    Einsatz = Arbmodel.einsatz.tolist()
    Einsatz = [str(i) for i in Einsatz]

    Profit = list(Arbmodel.getProfit())
    Profit = [str(i) for i in Profit]

    möglich, Margin = Arbmodel.arbitrageOpportunity()
    if möglich:
        print("\nEine Arbitragewette ist möglich mit einem Profit von: " + str(Margin) + "%\n")
        print("Quoten:\t\t\t" + "\t".join(Quoten))
        print("Wahrscheinlichkeiten:\t" + "\t".join(Probs))
        print("Einsätze:\t\t" + "\t".join(Einsatz))
        print("Profit:\t\t\t" + "\t".join(Profit))
    else:
        print("Eine Arbitragewette ist NICHT möglich" + str(Margin) + "%\n\n")


# quoten = input("GIVE ME SOME QUOTES:\n")
# quotenliste = [float(x.strip()) for x in quoten.split(',')]

# Arb = arbitrageModel(quotenliste, gesamtEinsatz = 12.5)
# printTableNeat(Arb)
