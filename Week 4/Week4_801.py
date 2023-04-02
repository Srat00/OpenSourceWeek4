inputStr, outputStr = input('문자열을 입력하세요 >> '), ''
length = len(inputStr)

for i in range(0, length):
    outputStr += inputStr[length - (i + 1)]

print("내용을 거꾸로 출력  >> " + outputStr)