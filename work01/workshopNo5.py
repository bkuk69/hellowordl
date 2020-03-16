number = input("숫자를 입력: ")
digitIdx = number.find(".")
print("소수점 이상 자리수:", digitIdx)
print("소수점 이하 자리수:" ,len(number)-digitIdx-1)