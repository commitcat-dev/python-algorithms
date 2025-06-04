# 문자열 해싱을 이용한 검색 함수 만들기


def polynomial_hash(str):
    p = 31
    m = 1_000_000_007
    hash_value = 0
    for char in str:
        hash_value = (hash_value * p + ord(char)) % m
    return hash_value


print(polynomial_hash("hello world"))
print(polynomial_hash("Hello world"))
print(polynomial_hash("Hello world!"))


def solution(string_list, query_list):
    res = []
    dict = {}
    for str in string_list:
        hash_value = polynomial_hash(str)
        dict[hash_value] = str

    for query in query_list:
        hash_value = polynomial_hash(query)
        if hash_value in dict:
            res.append(True)
        else:
            res.append(False)

    print(res)
    return res


res = solution(["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"])

print(res == [True, False, False, True])
