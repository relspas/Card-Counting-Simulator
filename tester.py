import os
import collections

GAMES = 500
SHOE_SIZE = 6
SHOE_PENETRATION = 0.25
BET_SPREAD = 20.0

PRINT_OUTPUT_PER_GAME = False

# CHOOSE_BASIC_OMEGA_II = False
# CHOOSE_HI_LO = False
# CHOOSE_K_O = False
# CHOOSE_HI_OPT_I = False
# CHOOSE_HI_OPT_II = False
# CHOOSE_HALVES = False
# CHOOSE_RED_SEVEN = False
# CHOOSE_ZEN = False

strategies = ["CHOOSE_BASIC_OMEGA_II", "CHOOSE_HI_LO", "CHOOSE_K_O", "CHOOSE_HI_OPT_I", \
   "CHOOSE_HI_OPT_II", "CHOOSE_HALVES", "CHOOSE_RED_SEVEN", "CHOOSE_ZEN", "CHOOSE_BASIC"]

def clearAndSetStrategy(string):
   global CHOOSE_BASIC_OMEGA_II, CHOOSE_HI_LO, CHOOSE_K_O, CHOOSE_HI_OPT_I, \
   CHOOSE_HI_OPT_II, CHOOSE_HALVES, CHOOSE_RED_SEVEN, CHOOSE_ZEN, CHOOSE_BASIC
   CHOOSE_BASIC_OMEGA_II = False
   CHOOSE_HI_LO = False
   CHOOSE_K_O = False
   CHOOSE_HI_OPT_I = False
   CHOOSE_HI_OPT_II = False
   CHOOSE_HALVES = False
   CHOOSE_RED_SEVEN = False
   CHOOSE_ZEN = False
   if string == "CHOOSE_BASIC_OMEGA_II":
      CHOOSE_BASIC_OMEGA_II = True
   elif string == "CHOOSE_HI_LO":
      CHOOSE_HI_LO = True
   elif string == "CHOOSE_K_O":
      CHOOSE_K_O = True
   elif string == "CHOOSE_HI_OPT_I":
      CHOOSE_HI_OPT_I = True
   elif string == "CHOOSE_HI_OPT_II":
      CHOOSE_HI_OPT_II = True
   elif string == "CHOOSE_HALVES":
      CHOOSE_HALVES = True
   elif string == "CHOOSE_RED_SEVEN":
      CHOOSE_RED_SEVEN = True
   elif string == "CHOOSE_ZEN":
      CHOOSE_ZEN = True
   # else string == "CHOOSE_BASIC":
   #    pass


# CHOOSE_BASIC_OMEGA_II = True

#################
# shoe size vs. probability
#################
# for x in range(2,9):
#    SHOE_SIZE = x
#    execfile('BlackJack.py')
#    moneys = sorted(moneys)
#    fit = stats.norm.pdf(moneys, np.mean(moneys), np.std(moneys))  # this is a fitting indeed
#    labelName = "Shoe size = " + str(SHOE_SIZE)
#    pl.plot(moneys, fit, '-o', label=labelName)
#    # pl.hist(moneys, normed=True)
#    pl.xlabel('# Hands Won - Lost')
#    max_y = max(fit)  # Find the maximum y value
#    max_x = moneys[fit.argmax()]  # Find the x value corresponding to the maximum y value
#    pl.text(max_x, max_y, str((max_x, max_y)))
# plt.legend()
# pl.show()



#################
# #decks vs. percent edge
#################
# GAMES = 50000
# clearAndSetStrategy("CHOOSE_BASIC_OMEGA_II")
# deckEdge = []
# for x in range(2,9):
#    SHOE_SIZE = x
#    execfile('BlackJack.py')
#    deckEdge.append(100.0*sume/total_bet)
# pl.plot(range(2,9), deckEdge, '-o')
# pl.xlabel('# decks')
# pl.ylabel('Percent Edge')
# pl.title('Percent Edge vs. Shoe Size, OMEGA II Strategy, Bet Spread = 20')
# pl.show()

#################
# pdf of count
#################
# for strategy in strategies:
#    clearAndSetStrategy(strategy)
#    execfile('BlackJack.py')
#    countings = sorted(countings)
#    fit = stats.norm.pdf(countings,np.mean(countings), np.std(countings))
#    pl.plot(countings, fit, label=strategy)

# pl.ylabel('Probability')
# pl.xlabel('Count')
# pl.title('PDF of the true count')
# plt.legend()
# pl.show()

#################
# PMF of count Bar Chart
#################
# for y in range(0, 3):
#    strategy = strategies[y]
#    clearAndSetStrategy(strategy)
#    execfile('BlackJack.py')
#    countings = [round(x) for x in countings]
#    countings = sorted(countings)
#    unique, counts = np.unique(countings, return_counts=True)
#    countDict = dict(zip(unique, [float(x)/len(countings) for x in counts]))
#    # weights = np.ones_like(countings)/len(countings)
#    width = 0.3
#    # D = countDict
#    D = collections.OrderedDict(sorted(countDict.items()))
#    print D
#    # plt.bar(range(len(D)), D.values(), align='center')
#    # plt.xticks(range(len(D)), D.keys())
#    plt.bar([x+width*y for x in D.keys()], 
#       D.values(), 
#       width, align='center',label=strategy)
# # plt.xticks(D.keys(), D.keys())
# plt.xticks(range(-11,11))
# pl.ylabel('Probability')
# pl.xlabel('Count')
# pl.title('PMF of the true count')
# x1,x2,y1,y2 = plt.axis()
# plt.axis((-10,10,y1,y2))
# plt.legend()
# pl.show()



#################
# PMF of money won/lost per game
#################
# for y in range(0, len(strategies)):
#    strategy = strategies[y]
#    clearAndSetStrategy(strategy)

#    sums = []
#    for z in range(0,30): #data points
#       GAMES = 2500 #games per data point
#       execfile('BlackJack.py')
#       sums.append(sume)
#    sums = sorted(sums)
#    fit = stats.norm.pdf(sums, np.mean(sums), np.std(sums))  # this is a fitting indeed
#    pl.plot(sums, fit, label=strategy)
# pl.xlabel('Money won/lost per 2500 games')
# plt.legend()
# pl.title('PMF of money won/lost per 2500 games')
# pl.show()


################
#PMF of money won/lost per game w/ bet spread sweep
################
# strategy = strategies[6]
# clearAndSetStrategy(strategy)
# for y in range(10, 80, 10):
#    BET_SPREAD = float(y)
#    sums = []
#    for z in range(0,25):
#       GAMES = 500
#       execfile('BlackJack.py')
#       sums.append(sume)
#    sums = sorted(sums)
#    fit = stats.norm.pdf(sums, np.mean(sums), np.std(sums))  # this is a fitting indeed
#    currLabel = "BET_SPREAD="+str(y)
#    pl.plot(sums, fit, label=currLabel)
# pl.xlabel('Money won/lost per 500 games')
# plt.legend()
# pl.title('PMF of money won/lost per 500 games using RED SEVEN Strategy')
# pl.show()

################
#PMF of edge 
################
for y in range(8,9):
   strategy = strategies[y]
   clearAndSetStrategy(strategy)

   edges = []
   for z in range(0,100): #data points
      GAMES = 1 #games per data point
      execfile('BlackJack.py')
      edges.append(100.0*sume/total_bet)
   edges = sorted(edges)
   fit = stats.norm.pdf(edges, np.mean(edges), np.std(edges))  # this is a fitting indeed
   pl.plot(edges, fit, label=strategy)
pl.xlabel('Edge per 1000 games')
plt.legend()
pl.title('Edge per 1000 games')
pl.show()
