amount = int(input("대부금액(만원):"))
interest = float(input("이자율(%): "))
years = int(input("기간(년): "))

my_i = interest / 1200
monthInput = my_i /(1-(1+my_i)**(-12* years)) * amount

print("월불입금:",monthInput, "원")