months = int(input("월수: "))
years = months // 12
month = months % 12
print("{0}개월은 {1}년 {2}월".format(months, years, month))