import deckfn
import oktoplay
import botplayer
from prettytable import PrettyTable


def disphand(handno):
    outpt = PrettyTable(hands[handno])
    outpt.add_row([*range(1, hands[handno].__len__() + 1)])
    if discard:
        print(outpt.get_string(header=True, border=True, title='Your Cards   |   Discard: ' + discard[0]))
    else:
        print(outpt.get_string(header=True, border=True, title='Your Cards   |   Discard: None'))
    return


def dispboard(board):
    for row in board:
        while len(row) < len(max(board, key=len)):
            row.append('')
    if board:
        outpt = PrettyTable()
        for row in board:
            outpt.add_row(row)
        print(outpt.get_string(header=False, border=True, title='Board'))
    return


def numtocards(hand, num):
    try:
        cards = []
        if len(num) >= 3:
            if num[1] == ':':
                return cards
        while True:
            if num.find(' ') < 0:
                cards.append(hand[int(num)-1])
                break
            else:
                cards.append(hand[int(num[:num.find(' ')])-1])
                num = num[num.find(' ') + 1:]
    except:
        cards = ['♥15']
    return cards


players = int(input('Number of players: '))
bot = False
if players == 2:
    bot = bool(int(input('Bot on  |  Bot off   (1/0)')))
cardsforeachplayer = (players == 2) * 10 + (players == 3 or players == 4) * 7 + (players == 5 or players == 6) * 6
stock = deckfn.deckrand()
hands = []
board = []
for i in range(1, players+1):
    hands.append(deckfn.decksort(stock[0:cardsforeachplayer]))
    del stock[0:cardsforeachplayer]
discard = [stock[0]]
del stock[0]
gameison = True
while gameison:
    for player in range(players):
        dis = True
        if not (bot and player == 1):
            print('\n\n\n\n\n\nPlayer ' + str(player + 1))
        if not bot:
            input() #off if bot is on
        if not (bot and player == 1):
            dispboard(board)
            disphand(player)
        if bot and player == 1:
            newcard = botplayer.qow(hands[player], discard)
        else:
            newcard = input('\nDraw from deck | Get discard  (Q/W)  >').upper()
        #botplayer
        if not stock:
            discard.reverse()
            stock = discard[:]
            discard = []
        while newcard != 'Q' and newcard != 'W':
            print('Wrong input.')
            newcard = input('\nDraw from deck | Get discard  (Q/W)  >').upper()
        if newcard == 'Q':
            if not (bot and player == 1):
                print('New card: ' + stock[0])
            hands[player] = deckfn.decksort(hands[player] + [stock[0]])
            del stock[0]
            if not stock:
                discard.reverse()
                stock = discard[:]
                discard = []
        else:
            hands[player] = deckfn.decksort(hands[player] + [discard[0]])
            del discard[0]
        if not (bot and player == 1):
            dispboard(board)
            disphand(player)
        if bot and player == 1:
            cardstoplay = botplayer.newmove(hands[player], board, dis)
        else:
            cardstoplay = input('Choose cards to play  >')
        #botplayer
        while cardstoplay or dis:
            if cardstoplay:
                if (cardstoplay[0].upper() == 'D' and dis) or len(cardstoplay) >= 3:
                    if cardstoplay.find(' ') < 0 and cardstoplay[0].upper() == 'D' and dis:
                        dis = False
                        cardstoplay = cardstoplay[1:]
                        discard.insert(0, numtocards(hands[player], cardstoplay)[0])
                        del hands[player][int(cardstoplay)-1]
                        break
                    elif cardstoplay.find(' ') < 0 and oktoplay.mergeinrun(board, int(cardstoplay[0]), numtocards(hands[player], cardstoplay[2:]))[0]:
                        dis = False
                        if oktoplay.mergeinrun(board, int(cardstoplay[0]), numtocards(hands[player], cardstoplay[2:]))[1] == 0:
                            board[int(cardstoplay[0])-1].insert(0, numtocards(hands[player], cardstoplay[2:])[0])
                        else:
                            board[int(cardstoplay[0]) - 1].append(numtocards(hands[player], cardstoplay[2:])[0])
                        del hands[player][int(cardstoplay[2:])-1]
                    elif oktoplay.newrun(numtocards(hands[player], cardstoplay)):
                        dis = False
                        board.append(numtocards(hands[player], cardstoplay))
                        for card in numtocards(hands[player], cardstoplay):
                            hands[player].remove(card)
                else:
                    print('Wrong input.')
            if not (bot and player == 1):
                dispboard(board)
                disphand(player)
            if bot and player == 1:
                cardstoplay = botplayer.newmove(hands[player], board, dis)
            else:
                cardstoplay = input('Choose cards to play  >')
            #botplayer
    for player in range(players):
        if not hands[player]:
            print('Player ' + str(player + 1) + ' won!')
            gameison = False
            break
