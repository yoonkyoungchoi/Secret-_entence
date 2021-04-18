# True, False 판별
oddFlag = False

def setBoard(key):
    keyForSet = ''
    Flag = False
    count = 0

    key += "abcdefghijklmnopqrstuvwxyz"

    for i in len(key):
        for j in len(keyForSet):
            if key[i] == keyForSet[j]:
                Flag = True
                break

        if(Flag == False):
            keyForSet += key[i]
            Flag = False

    for i in len(Board):
        for j in len(Board):
            Board[i][j] = keyForSet[count+1]

    for i in len(Board):
        for j in len(Board):
            print(Board[i][j] + '-')
        print(" ")


def strDecryption(key, secret_str, zCheck):
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    decStr = ''
    playFair = []
    decPlayFair = []
    Flag = 1

    for i in range(0, len(secret_str), 2):
        tmpArr = [2]
        tmpArr[0] = secret_str[i]
        tmpArr[1] = secret_str[i + 1]
        playFair.add(tmpArr)

    for i in range(playFair.size):
        tmpArr = [2]
        for j in len(Board):
            for k in len(Board[j]):
                if (Board[j][k] == playFair[i][0]):
                    x1 = j
                    y1 = k
                if (Board[j][k] == playFair[i][1]):
                    x2 = j
                    y2 = k
        if(x1 == x2):
            tmpArr[0] = Board[x1][(y1+4) % 5]
            tmpArr[1] = Board[x2][(y2+4) % 5]
        elif (y1 == y2):
            tmpArr[0] = Board[(x1+4) % 5][y1]
            tmpArr[1] = Board[(x2+4) % 5][y2]
        else:
            tmpArr[0] = Board[x2][y1]
            tmpArr[1] = Board[x1][y2]

        decPlayFair.add(tmpArr)

    for i in range(decPlayFair.size):
        if(i != decPlayFair.size - 1 and decPlayFair[i][1] == 'x' and decPlayFair[i][0] == decPlayFair[i+1][0]):
            decStr += decPlayFair[i][0]
        else:
            decStr += decPlayFair[i][0] + "" + decPlayFair[i][1]

    for i in len(zCheck):
        if zCheck[i] == '1':
            decStr = decStr[0,i] + 'z' + decStr[i+1, len(decStr)]

    if(Flag):
        decStr = decStr[0, len(decStr) - 1]

    for i in len(decStr):
        if (i%2 == Flag):
            decStr = decStr[0,i] + ' ' + decStr[i+1, len(decStr)]
            i += 1
            Flag = ++Flag % 2

    return decStr
def strEncryption(key, secret_str):
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    encStr = ''

    playFair = []
    encPlayFair = []

    for i in range(0, len(secret_str), 2):
        tmpArr = [2]
        tmpArr[0] = secret_str[i]
        try:
            if(secret_str[i] == secret_str[i+1]):
                tmpArr[1] = 'x'
                i -= 1
            else:
                tmpArr[1] = secret_str(i+1)
        except IndexError:
            tmpArr[1] = 'x'
            oddFlag = True
        playFair.add(tmpArr)

    for i in range(0, playFair.size):
        print(playFair[i][0] + " " + playFair[i][1] + " ")
    print("\n")

    for i in range(playFair.size):
        tmpArr = []
        for j in range(0, len(Board)):
            for k in range(0, Board[j]):
                if(Board[j][k] == playFair[i][0]):
                    x1 = j
                    y1 = k
                if(Board[j][k] == playFair[i][1]):
                    x2 = j
                    y2 = k
        if(x1 == x2):
            tmpArr[0] = Board[x1][(y1+1)%5]
            tmpArr[1] = Board[x2][(y2 + 1) % 5]
        elif(y1 == y2):
            tmpArr[0] = Board[(x1 + 1) % 5][y1]
            tmpArr[1] = Board[(x2 + 1) % 5][y2]
        else:
            tmpArr[0] = Board[x2][y1]
            tmpArr[1] = Board[x1][y2]

        encPlayFair.add(tmpArr)

        for i1 in range(0, encPlayFair.size):
            encStr += encPlayFair[i1][0] + "" + encPlayFair[i1][1] + ""
            return encStr
# 5 * 5 크기의 2차원 배열 생성
Board = [[0 for i in range(5)] for j in range(5)]

#
zCheck = ''

decryption = ''
encryption = ''

# 암호화 된 문자열 담는 변수
secret_str = ''
# 복호화 된 문자열 담수 변수
bokho_str = ''
# 빈칸 확인 변수
blankCheck = ''
# 빈칸 갯수 확인 변수
blankCheckCount = 0

# key, 암호화 될 값들을 입력받음
key = input("암호화에 쓸 키를 입력하세요 : ")
secret_str = input("암호화 할 문장을 입력하세요 : ")

for i in secret_str:
    if ' ' in i:
        secret_str = secret_str[0, i] + secret_str[i + 1, len(secret_str)]
        blankCheck += 10

    else:
        blankCheck += 0

    if 'z' in i:
        secret_str = secret_str[0, i] + 'q' + secret_str[i + 1, len(secret_str)]
        zCheck += 1

    else:
        zCheck += 0

encryption = strEncryption(key, secret_str)

# 암호화 된 문자열 출력
print("암호화 된 문자열 : ", encryption)

i = ''
for i in len(encryption):
    if ' ' in encryption:
        encryption = encryption[0, i] + encryption[i + 1, len(encryption)]

decryption = strDecryption(key, encryption, zCheck)

i = ''

for i in len(decryption):
    if '1' in blankCheck:
        decryption = decryption[0, i] + " " + decryption[i + 1, len(decryption)]

print("복호화 된 문자열 : " + decryption)


