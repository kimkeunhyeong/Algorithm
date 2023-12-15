def check_string(start_position):
    position = start_position
    string = ""
    stack = []
    flag = False

    while position < str_len:
        char = origin[position]
        if char == "(":
            str_plus, position = check_string(position + 1)
            string += str_plus
            while stack:
                # 그냥 다 pop해버리면 우선순위 문제 생김
                if stack[-1] == "+" or stack[-1] == "-":
                    break
                string += stack.pop()
        elif char == ")":
            while stack:
                string += stack.pop()
            return string, position
        else:
            if char.isalpha():
                string += char
                while stack:
                    if stack[-1] == "+" or stack[-1] == "-":
                        break
                    string += stack.pop()
            elif char == "*" or char == "/":
                stack.append(char)
            else:
                while stack:
                    string += stack.pop()
                stack.append(char)
        position += 1

    while stack:
        string += stack.pop()

    return string, position

origin = input().rstrip()
str_len = len(origin)

print(check_string(0)[0])