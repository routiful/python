EXCHANGE_RATE_FROM_USD_TO_KRW = 1000
EXCHANGE_RATE_FROM_JPY_TO_USD = 8/1000 


# 원(￦)에서 달러($)로 바꿔주는 함수
def krw_to_usd(won):
    dollar = won / EXCHANGE_RATE_FROM_USD_TO_KRW
    return dollar

# 달러($)에서 엔(￥)로 바꿔주는 함수
def usd_to_jpy(dollars):
    yen = dollars / EXCHANGE_RATE_FROM_JPY_TO_USD
    return yen

# 원(￦)으로 각각 얼마인가요?
amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]
print("한국 화폐: " + str(amounts))
 
# amounts를 원(￦)에서 달러($)로 바꿔주기
num = 0
while num < len(amounts):
    amounts[num] = krw_to_usd(amounts[num])
    num += 1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(amounts))

# amounts를 달러($)에서 엔(￥)으로 바꿔주기
num = 0
while num < len(amounts):
    amounts[num] = usd_to_jpy(amounts[num])
    num += 1

# 엔(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(amounts))