def sum(a, b):
    return a+b

def sub(a, b):
    return a-b
    
def add(a, b):
    if type(a) != type(b):
        print("자료형을 확인해주세요")
        return
    else:
        result = sum(a, b)
    return result
    
# 파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수이다
# 만약에 python mod2.py처럼 직접 실행할 경우, mod2.py의 __name__ 변수에는 "__main__" 이라는 값이 자동으로 저장하게 됨
# 하지만 파이썬 쉘이나 다른 파이썬 모듈에서 import 할 경우에는 __name__ 변수에 자기자신의 이름이 저장됨
# 즉, mod2라는 모듈이름이 __name__ 변수에 저장된다
if __name__ == "__main__":
    print(add("a", 1))
    print(add(1, 1))
    print(add(10, 10.4))