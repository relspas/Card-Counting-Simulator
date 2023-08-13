import os
import collections
import BlackJack

import numpy as np
import scipy.stats as stats
import pylab as pl
import matplotlib.pyplot as plt


GAMES = 500
SHOE_SIZE = 6
SHOE_PENETRATION = 0.25
BET_SPREAD = 20.0

PRINT_OUTPUT_PER_GAME = False

BASIC_OMEGA_II = {"Ace": 0, "Two": 1, "Three": 1, "Four": 2, "Five": 2, "Six": 2, "Seven": 1, "Eight": 0, "Nine": -1, "Ten": -2, "Jack": -2, "Queen": -2, "King": -2}
BASIC = {"Ace": 0, "Two": 0, "Three": 0, "Four": 0, "Five": 0, "Six": 0, "Seven": 0, "Eight": 0, "Nine": 0, "Ten": 0, "Jack": 0, "Queen": 0, "King": 0}
HI_LO = {"Ace": -1, "Two": 1, "Three": 1, "Four": 1, "Five": 1, "Six": 1, "Seven": 0, "Eight": 0, "Nine": 0, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}
K_O = {"Ace": -1, "Two": 1, "Three": 1, "Four": 1, "Five": 1, "Six": 1, "Seven": 1, "Eight": 0, "Nine": 0, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}
HI_OPT_I = {"Ace": 0, "Two": 0, "Three": 1, "Four": 1, "Five": 1, "Six": 1, "Seven": 0, "Eight": 0, "Nine": 0, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}
HI_OPT_II = {"Ace": 0, "Two": 1, "Three": 1, "Four": 2, "Five": 2, "Six": 1, "Seven": 1, "Eight": 0, "Nine": 0, "Ten": -2, "Jack": -2, "Queen": -2, "King": -2}
HALVES = {"Ace": -1, "Two": 0.5, "Three": 1, "Four": 1, "Five": 1.5, "Six": 1, "Seven": 0.5, "Eight": 0, "Nine": -0.5, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}
RED_SEVEN = {"Ace": -1, "Two": 1, "Three": 1, "Four": 1, "Five": 1, "Six": 1, "Seven": 0.5, "Eight": 0, "Nine": 0, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}
ZEN = {"Ace": -1, "Two": 1, "Three": 1, "Four": 2, "Five": 2, "Six": 2, "Seven": 1, "Eight": 0, "Nine": 0, "Ten": -2, "Jack": -2, "Queen": -2, "King": -2}

strategy_strs = ["BASIC_OMEGA_II", "BASIC", "HI_LO", "K_O", "HI_OPT_I", "HI_OPT_II", "HALVES", "RED_SEVEN", "ZEN"]
strategies = [BASIC_OMEGA_II,BASIC,HI_LO,K_O,HI_OPT_I,HI_OPT_II,HALVES,RED_SEVEN,ZEN]

#################
# shoe size vs. probability
#################
def shoe_size_vs_prob():
   gameCnt = 10000
   for shoe_size in range(2,9):
      bjSim = BlackJack.Simulator(gameCnt,shoe_size,SHOE_PENETRATION,BASIC_OMEGA_II,BET_SPREAD)
      bjSim.sim()
      moneys = sorted(bjSim.moneys)
      fit = stats.norm.pdf(moneys, np.mean(moneys), np.std(moneys))  # this is a fitting indeed
      labelName = "Shoe size = " + str(shoe_size)
      pl.plot(moneys, fit, '-o', label=labelName)
      # pl.hist(moneys, normed=True)
      pl.xlabel('# Hands Won - Lost')
      max_y = max(fit)  # Find the maximum y value
      max_x = moneys[fit.argmax()]  # Find the x value corresponding to the maximum y value
      pl.text(max_x, max_y, str((max_x, max_y)))
   plt.legend()
   pl.show()


#################
# shoe penetration vs. percent edge
#################
def shoe_penetration_vs_pecent_edge():
   gameCnt = 10000
   deckEdge = []
   for shoe_penetration in np.arange(0.1,0.9,0.1):
      bjSim = BlackJack.Simulator(gameCnt,SHOE_SIZE,shoe_penetration,BASIC_OMEGA_II,BET_SPREAD)
      bjSim.sim()
      deckEdge.append(100.0*bjSim.sume/bjSim.total_bet)
   pl.plot(np.arange(0.1,0.9,0.1), deckEdge, '-o')
   pl.xlabel('Shoe Penetration')
   pl.ylabel('Percent Edge')
   pl.title('shoe penetration vs. percent edge, OMEGA II Strategy, Bet Spread = 20')
   pl.show()

#################
# pdf of count
#################
def PDF_of_cnt():
   for strategy,strategy_str in zip(strategies,strategy_strs):
      bjSim = BlackJack.Simulator(GAMES,SHOE_SIZE,SHOE_PENETRATION,strategy,BET_SPREAD)
      bjSim.sim()
      countings = sorted(bjSim.countings)
      fit = stats.norm.pdf(countings,np.mean(countings), np.std(countings))
      pl.plot(countings, fit, label=strategy_str)

   pl.ylabel('Probability')
   pl.xlabel('Count')
   pl.title('PDF of the true count')
   plt.legend()
   pl.show()

#################
# PMF of count Bar Chart
#################
def PMF_of_cnt():
   for y in range(0, 3):
      strategy = strategies[y]
      strat_str = strategy_strs[y]

      bjSim = BlackJack.Simulator(GAMES,SHOE_SIZE,SHOE_PENETRATION,strategy,BET_SPREAD)
      bjSim.sim()
      countings = [round(x) for x in bjSim.countings]
      countings = sorted(countings)
      unique, counts = np.unique(countings, return_counts=True)
      countDict = dict(zip(unique, [float(x)/len(countings) for x in counts]))
      # weights = np.ones_like(countings)/len(countings)
      width = 0.3
      # D = countDict
      D = collections.OrderedDict(sorted(countDict.items()))
      print(D)
      # plt.bar(range(len(D)), D.values(), align='center')
      # plt.xticks(range(len(D)), D.keys())
      plt.bar([x+width*y for x in D.keys()], 
         D.values(), 
         width, align='center',label=strat_str)
   # plt.xticks(D.keys(), D.keys())
   plt.xticks(range(-11,11))
   pl.ylabel('Probability')
   pl.xlabel('Count')
   pl.title('PMF of the true count')
   x1,x2,y1,y2 = plt.axis()
   plt.axis((-10,10,y1,y2))
   plt.legend()
   pl.show()



#################
# PMF of money won/lost per game
#################
def PMF_of_money_won_lost_per_game():
   gameCnt = 250 #games per data point
   for strategy,strategy_str in zip(strategies,strategy_strs):
      bjSim = BlackJack.Simulator(gameCnt,SHOE_SIZE,SHOE_PENETRATION,strategy,BET_SPREAD)
      sums = []
      for z in range(0,30): #data points
         bjSim.sim()
         sums.append(bjSim.sume)
      sums = sorted(sums)
      fit = stats.norm.pdf(sums, np.mean(sums), np.std(sums))  # this is a fitting indeed
      pl.plot(sums, fit, label=strategy_str)
   pl.xlabel('Money won/lost per 2500 games')
   plt.legend()
   pl.title('PMF of money won/lost per 2500 games')
   pl.show()


################
#PMF of money won/lost per game w/ bet spread sweep
################
def PMF_of_money_won_lost_per_game_w_bet_spread_sweep():
   strategy = strategies[6]
   gameCnt = 20
   for bet_spread_i in range(10, 80, 10):
      bet_spread = float(bet_spread_i)
      sums = []
      bjSim = BlackJack.Simulator(gameCnt,SHOE_SIZE,SHOE_PENETRATION,strategy,bet_spread)
      for z in range(0,25):
         bjSim.sim()
         sums.append(bjSim.sume)
      sums = sorted(sums)
      fit = stats.norm.pdf(sums, np.mean(sums), np.std(sums))  # this is a fitting indeed
      currLabel = "BET_SPREAD="+str(bet_spread)
      pl.plot(sums, fit, label=currLabel)
   pl.xlabel('Money won/lost per 500 games')
   plt.legend()
   pl.title('PMF of money won/lost per 500 games using RED SEVEN Strategy')
   pl.show()

################
#PMF of edge 
################
def PMF_of_edge():
   gameCnt = 1 #games per data point
   for strategy,strategy_str in zip(strategies,strategy_strs):
      edges = []
      bjSim = BlackJack.Simulator(gameCnt,SHOE_SIZE,SHOE_PENETRATION,strategy,BET_SPREAD)
      for z in range(0,100): #data points
         bjSim.sim()
         edges.append(100.0*bjSim.sume/bjSim.total_bet)
      edges = sorted(edges)
      fit = stats.norm.pdf(edges, np.mean(edges), np.std(edges))  # this is a fitting indeed
      pl.plot(edges, fit, label=strategy_str)
   pl.xlabel('Edge per 1000 games')
   plt.legend()
   pl.title('Edge per 1000 games')
   pl.show()

if __name__=="__main__":
   # shoe_size_vs_prob()
   # shoe_penetration_vs_pecent_edge()
   # PDF_of_cnt()
   # PMF_of_cnt()
   PMF_of_money_won_lost_per_game()
   # PMF_of_money_won_lost_per_game_w_bet_spread_sweep()
   # PMF_of_edge()