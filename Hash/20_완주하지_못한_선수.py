p1 = ["leo", "kiki", "eden"]
c1 = ["eden", "kiki"]
r1 = "leo"

p2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
c2 = ["josipa", "filipa", "marina", "nikola"]
r2 = "vinko"

p3 = ["mislav", "stanko", "mislav", "ana"]
c3 = ["stanko", "ana", "mislav"]
r3 = "mislav"

p4 = ["stanko", "ana", "ana", "ana", "ana"]
c4 = ["stanko", "ana", "ana", "ana"]
r4 = "ana"


def solution(participant, completion) -> str:
    dict = {}
    for c in completion:
        if not c in dict:
            dict[c] = 1
        else:
            dict[c] += 1

    print(dict)

    for p in participant:
        if not p in dict:
            return p
        else:
            dict[p] -= 1
            if dict[p] < 0:
                return p

            # if dict[p] == 1:
            #     return p
            # else:
            #     dict[p] = 1
    print(dict)
    return ""


print(r1 == solution(p1, c1))
print(r2 == solution(p2, c2))
print(r3 == solution(p3, c3))
print(r4 == solution(p4, c4))
