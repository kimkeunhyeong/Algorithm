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
                string += stack.pop()
        elif char == ")":
            while stack:
                string += stack.pop()
            return string, position
        else:
            if char.isalpha():
                string += char
                if flag:
                    while stack:
                        string += stack.pop()
                    flag = False
            elif char == "*" or char == "/":
                flag = True
                stack.append(char)
            else:
                stack.append(char)
        position += 1

    while stack:
        string += stack.pop()

    return string, position

origin = input().rstrip()
str_len = len(origin)
print(check_string(0)[0])