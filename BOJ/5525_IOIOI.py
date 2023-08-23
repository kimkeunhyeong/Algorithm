from sys import stdin

input = stdin.readline

N = int(input())
str_len = int(input())
string = input()

target_string = "I" + "OI" * N
target_len = len(target_string)
index = string.find(target_string)

if index == -1:
    print(0)
else:
    cnt = 1
    index += 1
    end_index = str_len - target_len
    check_index = index + target_len - 1
    
    while index <= end_index:
        if string[check_index] == "O" and string[check_index + 1] == "I":
            index += 2
            check_index += 2
            cnt += 1
        else:
            substr_index = string[index:].find(target_string)
            if substr_index == -1:
                break
            else:
                index += substr_index + 1
                check_index = index + target_len - 1
                cnt += 1
    print(cnt)