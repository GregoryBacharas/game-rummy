import oktoplay


def qow(hand, discard):
    if discard:
        getdis = False
        for card1 in hand:
            for card2 in hand[hand.index(card1)+1:]:
                if oktoplay.newrun([card1, card2, discard[0]]):
                    getdis = True
                    break
            else:
                continue
            break
        out = getdis * 'W' + (not getdis) * 'Q'
    else:
        out = 'Q'
    return out


def figtonum(card):
    card = card.replace('A', '1')
    card = card.replace('J', '11')
    card = card.replace('Q', '12')
    card = card.replace('K', '13')
    return card


def numtofig(card):
    if len(card) == 2:
        card = card.replace('1', 'A')
    else:
        card = card.replace('11', 'J')
        card = card.replace('12', 'Q')
        card = card.replace('13', 'K')
    return card


def newmove(hand, board, dis):
    moveregistered = False
    if len(hand) >= 3:
        for card1 in hand:
            for card2 in hand[hand.index(card1)+1:]:
                for card3 in hand[hand.index(card2)+1:]:
                    if oktoplay.newrun([card1, card2, card3]):
                        out = str(hand.index(card1)+1) + ' ' + str(hand.index(card2)+1) + ' ' + str(hand.index(card3)+1)
                        moveregistered = True
    if board and not moveregistered:
        for card in hand:
            for i in range(1, len(board)+1):
                if oktoplay.mergeinrun(board, i, [card])[0]:
                    out = str(i) + ':' + str(hand.index(card)+1)
                    moveregistered = True
    if dis and not moveregistered:
        if len(hand) == 1:
            out = 'D1'
        elif len(hand) == 2:
            out = 'D1'
        else:
            pairs = []
            for card1 in hand:
                for card2 in hand[hand.index(card1)+1:]:
                    card1 = figtonum(card1)
                    card2 = figtonum(card2)
                    if card1[1:] == card2[1:] or (card1[0] == card2[0] and abs(int(card1[1:])-int(card2[1:])) == 1):
                        card1 = numtofig(card1)
                        card2 = numtofig(card2)
                        pairs.append([card1, card2])
                    else:
                        card1 = numtofig(card1)
                        card2 = numtofig(card2)
                        for item in pairs:
                            if item.__contains__(card1):
                                break
                        else:
                            pairs.insert(0, [card1])
            out = 'D' + str(hand.index(pairs[0][0])+1)
            moveregistered = True
    if not moveregistered:
        out = ''
    return out
