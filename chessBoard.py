from itertools import permutations                                              # importing libs

blackSquareIcon = '\u2B1B'                                                      # icons
whiteSquareIcon = '\u2B1C'
queensIcon = '\U0001f451'

def createChessBoard(n):                                                        # func to creat base chessboard
    chessBoard = []
    rowEven, rowOdd = '', ''

    for i in range(n):
        rowEven += blackSquareIcon + ' ' if i%2 != 0 else whiteSquareIcon + " "
        rowOdd += whiteSquareIcon + ' ' if i%2 != 0 else blackSquareIcon + " "
    for i in range(n):
        chessBoard.append(rowEven) if i%2 == 0 else chessBoard.append(rowOdd)
        
    return chessBoard


def printChessBoard(chessBoard,setOfCombo):                                     # func to print chessboard
    # avaz kardan jaye index va item va moratab kardanshon
    tempDict = {}
    combolist = []
    for i in range(len(setOfCombo)):
        tempDict[i] = setOfCombo[i]

    reversedDict = dict([(value, key) for key, value in tempDict.items()])

    for i in sorted(reversedDict.keys()):
        x = reversedDict[i]+1
        combolist.append(x)

    print(combolist)

    nQueen = len(setOfCombo)
    temp = [] + chessBoard

    # gharar dadan vazir dar safhe
    for i in range(len(setOfCombo)):
        string = temp[i]
        n = setOfCombo[i]
        string = string[0:2*n] + queensIcon + string[(n*2)+1: ]
        temp[i] = string
    
    # print greftan va neveshtan dar file
    for item in temp:
        print(item)
        
    temp = [] + chessBoard

    print('\n')


def possibleLocation(nQueen):                                                       # finding correct location for queens  
    numSolution = 0
    soton = range(nQueen)
    chessBoard = createChessBoard(nQueen)
    for eachCombination in permutations(soton):
        if nQueen == len(set(eachCombination[i]+i for i in soton)) == len(set(eachCombination[i]-i for i in soton)):
            numSolution += 1
            print('Solution Number :' , str(numSolution) , '')
            printChessBoard(chessBoard,eachCombination)


nQueen = int(input('Input Number of Queens : '))                                    # input for the number of queens
while nQueen <= 3:
    nQueen = int(input("Number of Queens Can\'t Be Less Than or Equal to 3\nInput Number of Queens : "))

possibleLocation(nQueen)