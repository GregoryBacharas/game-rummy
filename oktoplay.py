# def newrunold(cards):
#     cards = [card.replace('J', '11') for card in cards]
#     cards = [card.replace('Q', '12') for card in cards]
#     cards = [card.replace('K', '13') for card in cards]
#     cards = [card.replace('A', '1') for card in cards]
#     out = False
#     if len(cards) >= 3:
#         out = True
#         for card in cards:
#             if not ((card[0] == cards[0][0] and int(card[1:]) - cards.index(card) == int(cards[0][1:])) or (int(card[1:]) == int(cards[0][1:]))):
#                 out = False
#     return out


def newrun(cards):
    cards = [card.replace('J', '11') for card in cards]
    cards = [card.replace('Q', '12') for card in cards]
    cards = [card.replace('K', '13') for card in cards]
    cards = [card.replace('A', '1') for card in cards]
    out = False
    if len(cards) >= 3:
        cardswofig=[]
        for card in cards:
            cardswofig.append(card[1:])
        if cardswofig.count(cardswofig[0]) == len(cards):
            out = True
        else:
            figs = []
            for card in cards:
                figs.append(card[0])
            if figs.count(figs[0]) == len(cards):
                for num in cardswofig:
                    cardswofig[cardswofig.index(num)] = int(num) - cardswofig.index(num)
                if cardswofig.count(cardswofig[0]) == len(cards):
                    out = True
    return out


def mergeinrun(board, rownum, card):
    board = board[rownum-1]
    while board[-1] == '':
        board.remove('')
    card = card[0]
    board = [cd.replace('J', '11') for cd in board]
    board = [cd.replace('Q', '12') for cd in board]
    board = [cd.replace('K', '13') for cd in board]
    board = [cd.replace('A', '1') for cd in board]
    card = card.replace('J', '11')
    card = card.replace('Q', '12')
    card = card.replace('K', '13')
    card = card.replace('A', '1')
    out = False
    pos = -2
    if board[0][1:] == board[1][1:] and board[0][1:] == card[1:]:
        out = True
        pos = -1
    elif board[0][0] == card[0] and board[1][0] == card[0] and int(board[0][1:]) == int(card[1:]) + 1:
        out = True
        pos = 0
    elif board[0][0] == card[0] and board[1][0] == card[0] and int(board[-1][1:]) == int(card[1:]) - 1:
        out = True
        pos = -1
    return out, pos
