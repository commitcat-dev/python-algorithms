# DB에 사용자의 비밀번호를 저장할 때, 1q2w3e!@#$ 패스워드 그대로 저장하지 않고 한 번 해싱해서 저장. (이 때, 서버마다 다른 해싱함수를 사용하려나?)
# • 해시 알고리즘이 다름 (sha256, bcrypt, argon2 등)
# •	솔트의 존재 여부와 방식이 다름 (없거나, 고정 솔트, 사용자별 랜덤 솔트 등)
# •	해시 반복 횟수(스트레칭 강도) 설정이 다름

# 파이썬 딕셔너리 사용법
dict = {}
dict[1] = "one"
dict[2] = "two"
print(dict)

dict["three"] = 3  # 이게 되네?
print(dict)

print(dict[1])
print(dict["three"])
# print(dict[3])

if 2 in dict:
    print("yes")

if not 3 in dict:
    print("yes")
