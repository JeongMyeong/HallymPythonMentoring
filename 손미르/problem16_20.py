### 코드작성/실행결과 작성 부분의 주석을 지우고 직접 작성하시오.
### 이름 : OOO
#손미르

### 16. 아래 코드의 출력 결과를 예상하시오.
print(3==5)
print(3<5)

# 실행결과 작성 (실행결과는 주석으로 쓸 것.)
#False
#True

### 17. 아래 코드의 출력 결과를 예상하시오.
if False:
    print("1")
    print("2")
else:
    print("3")
print("4")

#3
#4

### 18. 사용자에게 숫자 하나를 입력받고, 입력받은 숫자에 13을 더해 출력하는 코드를 작성하시오.
num=int(input("숫자 하나를 입력하시오:"))
print(num+13)



### 19. 사용자로부터 숫자 세개를 입력받아 가장 큰 숫자를 출력하는 코드를 작성하시오.
# 입력 ex)
# num1 입력 : 10
# num2 입력 : 9
# num3 입력 : 25
# 25
num1 = int(input("num1 입력 : "))
num2 = int(input("num2 입력 : "))
num3 = int(input("num3 입력 : "))

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

# 코드 작성
score = int(input("점수를 입력하시오 (0~100) : "))

if score>=81:
    grade = "A"
elif score>=61 and score<81:
    grade = "B"
elif score>=41 and score<61:
    grade = "C"
elif score>=21 and score<41:
    grade = "D"
else:
    grade = "E"

print("당신의 학점은 {} 입니다.".format(grade))
