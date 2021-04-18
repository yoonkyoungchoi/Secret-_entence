def setBoard(key):
    keyForSet = ''
    Flag = False
    count = 0

    key += "abcdefghijklmnopqrstuvwxyz"

    for i in len(key):


def strDecryption(key, secret_str, zCheck):
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    decStr = ''

def strEncryption(key, secret_str):
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    encStr = ''

# 5 * 5 크기의 2차원 배열 생성
Board = [[0 for i in range(5)] for j in range(5)]

# True, False 판별
charCounter = False
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


