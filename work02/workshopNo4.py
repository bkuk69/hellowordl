amount =[]

amount.append(float(input("SPY투자금액(만원) :")))
amount.append(float(input("QQQ투자금액(만원) :")))
amount.append(float(input("EEM투자금액(만원) :")))
amount.append(float(input("VVX투자금액(만원) :")))

amountSum = sum(amount)
print("종류   비율")
print("---------------")
print("SPY\t", amount[0]/amountSum * 100)
print("QQQ\t", amount[1]/amountSum * 100)
print("EEM\t", amount[2]/amountSum * 100)
print("VXX\t", amount[3]/amountSum * 100)

print("전체 투자 금액(만원):", amountSum)