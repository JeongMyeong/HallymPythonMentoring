### 코드작성/실행결과 작성 부분의 주석을 지우고 직접 작성하시오.
### 이름 : 권채영


### 16. 아래 코드의 출력 결과를 예상하시오.
print(3==5)
print(3<5)

# False
# True


### 17. 아래 코드의 출력 결과를 예상하시오.
if False:
    print("1")
    print("2")
else:
    print("3")
print("4")

# 1
# 2
# 4

### 18. 사용자에게 숫자 하나를 입력받고, 입력받은 숫자에 13을 더해 출력하는 코드를 작성하시오.

num=int(input(숫자를 입력하세요 :))
print(num+13)


### 19. 사용자로부터 숫자 세개를 입력받아 가장 큰 숫자를 출력하는 코드를 작성하시오.
# 입력 ex)
# num1 입력 : 10
# num2 입력 : 9
# num3 입력 : 25
# 25

num1=int(input(숫자를 입력하세요 :))
num2=int(input(숫자를 입력하세요 :))
num3=int(input(숫자를 입력하세요 :))
num_list=[num1,num2,num3]
print(max(num_list))

### 20. 사용자로부터 점수를 입력받아 해당하는 학점을 출력하는 코드를 작성하시오.
#점수|학점
#---|---
#81~100|A
#61~80|B
#41~60|C
#21~40|D
#0~20|E
##### 출력 예시
# - 당신의 학점은 B 입니다.

# score=int(input("점수를 입력하세요 :"))
if score<=100 and score >=81:
    print("당신의 학점은 A 입니다.")
elif score<=60:
    print("당신의 학점은 B 입니다.")
elif score<=40:
    print("당신의 학점은 C 입니다.")
elif score<=20:
    print("당신의 학점은 D 입니다.")
elif score<=20 and score>=0:
    print("당신의 학점은 E 입니다.")
else:
    print('점수를 잘못입력했습니다.")

