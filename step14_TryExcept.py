# step14_TryExcept.py

if __name__ == "__main__":

    try:
        # 1. 입력 먼저
        num1_str: str = input("젯수 입력:")
        num2_str: str = input("피젯수 입력:")

        # 2. 형변환
        num1: int = int(num1_str)
        num2: int = int(num2_str)

        # 3. 계산 및 출력
        result = num2 / num1
        print(f"{num2} 를 {num1} 으로 나눈 결과값 : {result}")

    except ValueError as ve:
        print(ve)
        print("숫자 형식으로 입력해 주세요!")

    except ZeroDivisionError as ze:
        print(ze)                              # zde → ze 로 수정 ✅
        print("어떤 수를 0 으로 나눌수는 없습니다!")

    finally:
        print("중요한 마무리 작업을 합니다")

