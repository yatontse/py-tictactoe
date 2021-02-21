a = '1'
b = '2'
c = '3'
d = '4'
e = '5'
f = '6'
g = '7'
h = '8'
i = '9'
p = 'o'

def DisplayBoard():
    print(' {0} | {1} | {2} '.format(a, b, c) )
    print('---|---|---')
    print(' {0} | {1} | {2} '.format(d, e, f) )
    print('---|---|---')
    print(' {0} | {1} | {2} '.format(g, h, i) )

def GetUserInput():
    r = input('Enter the position you choose (1-9): ')
    r = int(r)
    return r

def PlaceChess(Pos, player):
    global a, b, c, d, e, f, g, h, i
    if Pos==1:
        a = player
    elif Pos==2:
        b = player
    elif Pos==3:
        c = player
    elif Pos==4:
        d = player
    elif Pos==5:
        e = player
    elif Pos==6:
        f = player
    elif Pos==7:
        g = player
    elif Pos==8:
        h = player
    elif Pos==9:
        i = player
    
def ChangePlayer(player):
    global p
    if player == 'o':
        p = 'x'
    else:
        p = 'o'

def PlayerWins(player):
    global a, b, c, d, e, f, g, h, i
    if (a == player) and (b == player) and (c == player):
        return True
    elif (d == player) and (e == player) and (f == player):
        return True
    elif (g == player) and (h == player) and (i == player):
        return True
    elif (a == player) and (d == player) and (g == player):
        return True
    elif (b == player) and (e == player) and (h == player):
        return True
    elif (c == player) and (f == player) and (i == player):
        return True
    elif (a == player) and (e == player) and (i == player):
        return True
    elif (c == player) and (e == player) and (g == player):
        return True
    else:
        return False

def IsDraw():
    global a, b, c, d, e, f, g, h, i
    if (a == '1') or (b == '2') or (c == '3') or (d == '4') or (e == '5') or (f == '6') or (g=='7') or (h=='8') or (i =='9'):
        return False
    else:
        return True

DisplayBoard()
while (not PlayerWins(p)) and (not IsDraw()):
    PlaceChess(GetUserInput(),p)
    DisplayBoard()
    if PlayerWins(p):
       print('Player ',p,' wins!')
    elif IsDraw():
        print('It is a draw.')
    else:
        ChangePlayer(p)

