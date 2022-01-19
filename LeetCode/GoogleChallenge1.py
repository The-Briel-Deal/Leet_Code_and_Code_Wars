from re import sub


def solution(s):
    length_s = len(s)
    max = 1
    for i in range(1, length_s):
        if length_s % i == 0:
            sub_s = s[:i]
            number = s.count(sub_s)
            if number == (length_s / i) and number > max:
                max = number
    return max


print(solution("fasfasfas"))
