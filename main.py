s = input()
n = 30000
array = [0] * n
i = 0
stack = []
j = 0
last_closing = None


while j < len(s):
    symbol = s[j]
    match symbol:
        case '>':
            i = (i + 1) % n
        case '<':
            i = (i - 1) % n
        case '+':
            array[i] = (array[i] + 1) % 256
        case '-':
            array[i] = (array[i] - 1) % 256
        case '[':
            # Новый цикл, которого еще не было
            if j not in stack:
                stack.append(j)
            
            if array[i] != 0:
                pass
            elif array[i] == 0:
                stack.pop()
                # перенос на ]
                if last_closing:
                    j = last_closing
                    last_closing = None
                else:
                    in_cycles = 0
                    while s[j] != ']' or in_cycles != 0:
                        j += 1
                        if s[j] == '[':
                            in_cycles += 1
                        elif s[j] == ']' and in_cycles:
                            in_cycles -= 1
        case ']':
            start = stack[-1]
            j = start - 1
        case '.':
            print(array[i], chr(array[i])) 
        case ',':
            a = int(input())
            array[i] = a
    j += 1


print(*array[:100])


# ++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.