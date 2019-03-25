PRIZE = 50000000
INTEREST_RATE = 0.12

PRESENT = 1988
FUTURE = 2016

FUTURE_APART = 1100000000

year = PRESENT
money = PRIZE
while year < FUTURE:
    interest = money * INTEREST_RATE
    money = money + interest
    year = year + 1

if (money > FUTURE_APART):
    print("{}원 차이로 동일 아저씨의 말씀이 맞습니다.".format(int(money - FUTURE_APART)))
else:
    print("{}원 차이로 미란 아주머니의 말씀이 맞습니다.".format(int(FUTURE_APART - money)))