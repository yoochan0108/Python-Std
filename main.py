def tax_calc(money):
  return money * 0.35

def pay_tax(tax):
  print("thank you for paying", tax)

pay_tax(tax_calc(150000000))

#return
#tax_calc(money)이 함수는 tax_calc(150000000) 이 숫자를 가지고 실행시킴
#그럼 money * 0.35 이 식에서 비율의 결과를 받게 되는데, 이게 우리에게 값을 줌
#그 준 값이 return이다
#return 이란, 함수 바깥으로 값을 보낸다는 의미