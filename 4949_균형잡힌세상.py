from sys import stdin
check_strings = [*map(str.rstrip, stdin.readlines())]
check_strings.pop()

result = []
open = ["(", "["]
close = [")", "]"]

for string in check_strings:
    stack = []
    for i in string:
        if i in open:
            stack.append(i)
        elif i in close:
            if not stack:
                result.append("no")
                break
            elif i == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    result.append("no")
                    break
            elif i == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    result.append("no")
                    break
    else:
        if stack:
            result.append("no")
        else:
            result.append("yes")
print(*result, sep="\n")