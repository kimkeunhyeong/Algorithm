from sys import stdin

input = stdin.readline
target = numbers = input().rstrip()
target = int(target)
broken_cnt = int(input())
broken = None
length = len(numbers)

if broken_cnt:
    broken = set(map(int, input().split()))

avail_btn = set(i for i in range(10))
if broken:
    avail_btn -= broken

if avail_btn:
    avail_btn = list(avail_btn)
    avail_btn.sort()
    avail_str_set = set(map(str, avail_btn))
current = 100

if current == target: # 누를 필요 없는경우
    print(0)
else:
    # 시작값으로 target과 100의 차를 설정, +, -만 사용하는 경우 (== 모든 버튼이 부서진 경우)
    candidate = abs(target - current)

    if not broken:
        # 모두 사용가능한 경우, 100에서 움직이거나 번호를 누르는 게 가장 빠를 것
        candidate = min(candidate, length)
    else:
        if len(avail_btn):
            # 0에서 가는게 가장 빠른 경우(0~49)
            if avail_btn[0] == 0:
                candidate = min(candidate, target + 1)
            # 일부만 사용가능한 경우
            # 한자리 크게?
            if avail_btn[0] != 0:
                temp = str(avail_btn[0]) * (length + 1)
                candidate = min(candidate, int(temp) - target + length + 1)
            else:
                if broken_cnt < 9:
                    temp = str(avail_btn[1]) + "0" * length
                    candidate = min(candidate, int(temp) - target + length + 1)
            # 한자리 작게?
            if avail_btn[-1] != 0 and length > 1: # else인 경우 사용 가능한 버튼이 0뿐이므로 검사하지 않음
                temp = str(avail_btn[-1]) * (length - 1)
                candidate = min(candidate, target - int(temp) + length - 1)
            # 같은 자릿수?
            # 첫번째는 gap이 작은걸로 선택. but... 59999만 만들 수 있고, 50000이 target일 때, 49999를 만들 수 있다면?
            # --> if first_digit available, first_digit +-도 확인해봐야함
            first_digit = int(numbers[0])
            plus = sorted(filter(lambda x : x > first_digit, avail_btn))
            minus = sorted(filter(lambda x : x < first_digit, avail_btn))
            if plus: # x > target이므로 나머지 자리는 모두 min_btn
                temp = str(plus[0]) + str(avail_btn[0]) * (length - 1)
                candidate = min(candidate, int(temp) - target + length)
            if minus and minus[-1]: # x < target이므로 나머지 자리는 모두 max_btn
                temp = str(minus[-1]) + str(avail_btn[-1]) * (length - 1)
                candidate = min(candidate, target - int(temp) + length)
            if first_digit in avail_btn:
                start = first_digit * (10 ** (length - 1))
                checklist = [i for i in range(start, start + 10 ** (length - 1))]
                for i in range(len(checklist)):
                    for digit in set(str(checklist[i])):
                        if digit not in avail_str_set:
                            break
                    else:
                        checklist[i] = abs(checklist[i] - target) + length
                candidate = min(candidate, min(checklist))
    print(candidate)