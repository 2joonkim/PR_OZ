# 사용자로부터 이름과 나이를 입력 받아, "안녕하세요, [이름]님! 당신은 [나이]살입니다." 라고 출력하는 함수 greet_user를 작성하세요.
def greet_user(name, age):
    print(f"안녕하세요, {name}님! 당신은 {age}살입니다.")
greet_user("김이준", 31)

# 여러 숫자를 입력받아 그 합계를 반환하는 함수 sum_numbers를 작성하세요. 이 때, 가변 매개변수를 사용하세요.
def sum_numbers(*n):
    return(n)
print(sum_numbers(1,2,3))

# 사용자의 이름을 출력하는 함수 print_name을 작성하세요. 만약 이름이 주어지지 않았다면, 기본값으로 "익명"을 사용하세요.
def print_name(name="이준"):
    print(name)
print_name()

# 사용자의 이름, 나이, 성별을 출력하는 함수 print_info를 작성하세요. 이 때, 모든 매개변수는 키워드 매개변수로만 받도록 하세요.
def print_info(name, age, sex):
    print(f'이름: {name}\n나이: {age}\n성별: {sex}\n')
print_info('김이준', 31, '남자')

# 두 개의 정수를 받아 합을 반환하는 함수 add를 작성하세요. 매개변수와 반환값에 타입 어노테이션을 추가하세요.
def add_number (a : int, b : int) -> int:
    return a + b
print (add_number(1,2))

# 0부터 시작하여 n까지의 숫자 중에서 홀수만 생성하는 제너레이터 odd_numbers를 작성하세요.
def odd_numbers (n):
    for num in range(1, n+1, 2):
        yield num
for num in odd_numbers(10):
    print(num)

# 두 숫자를 더하는 람다 함수를 작성하고, 이를 변수에 할당한 후 사용하세요.
add = lambda x, y: x + y
print (add(3,3))

# 사용자로부터 3개의 숫자를 입력받아, 이를 튜플로 만든 후 최소값과 최대값을 출력하는 함수 min_max를 작성하세요.
def min_max():
    num_1 = int(input('첫번째 숫자 입력'))
    num_2 = int(input('두번째 숫자 입력'))
    num_3 = int(input('세번째 숫자 입력'))
    numbers = (num_1, num_2, num_3)
    min_value = min(numbers)
    max_value = max(numbers)
    print (f'최소값 : {min_value}')
    print (f'최대값 : {max_value}')
min_max()

# 주어진 숫자가 짝수인지 확인하는 함수 is_even을 작성하세요. 짝수라면 True를, 아니라면 False를 반환하세요. 함수 내에서 조기 리턴을 활용하세요.
def is_even(number):
    if number % 2 == 0:
        return True
    return False

# 팩토리얼을 계산하는 재귀 함수 factorial을 작성하세요.
def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 문자열 리스트를 받아, 각 문자열의 길이를 출력하는 함수 print_lengths를 작성하세요.
def print_lengths(s):
    for i in s :
        print (f'{i}의 길이는 {len(i)}이다.')
strings = ["apple", "watermelon", "fishbread"]
print_lengths(strings)

# 두 문자열을 받아서 긴 문자열을 반환하는 함수 longer_string을 작성하세요. 만약 두 문자열의 길이가 같다면, 첫 번째 문자열을 반환하세요.
def longer_string(string1, string2):
    if len(string1) >= len(string2):
        return string1
    else:
        return string2
