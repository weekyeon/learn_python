def sum(a, b):
    return a+b
	
def safe_sum(a, b):
    if type(a) != type(b):
        print("자료형을 확인해주세요")
        return
    else:
        result = sum(a, b)
    return result