NumPlayers = int(input("How many Players?"))

PlayerLst = []
PlayerCount = []

for i in range (NumPlayers):
    PlayerLst.append(input("Enter name of player: "))

for k in range (len(PlayerLst)):
    PlayerCount.append(int(input('Enter start amount for player '+ PlayerLst[k] + ': ')))
def game():
    endgame = True
    while endgame:
        tot = 0
        for t in range(len(PlayerLst)):
            
            f = int(input('Enter amount '+ PlayerLst[t]+ ' lost/won: '))
            tot = tot + f
            PlayerCount[t] = PlayerCount[t] +f
        if not tot == 0:
            print('error in addition, consider undoing the changes above')
        ##print the balances
        for players in range(len(PlayerLst)):
            print(PlayerLst[players] , " : " ,PlayerCount[players])
            
        ## ask to continue the game
        if input('continue? y/n') == 'n':
            endgame = False

    #45
    #91
    #164
