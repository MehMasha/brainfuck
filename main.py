# s = input()

with open('max.bf', encoding='utf-8') as f:
    s = f.read()

s1 = ''
for i in s:
    if i in '+-><.,[]':
        s1 += i

s = s1
print(s[105:])

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
            # Если условие цика не выаполняется, то надо перейти на ]
            if array[i] == 0:
                # Убираем этот цикл из стека
                stack.pop()
                # Если раньше уже видели конец этого цикла
                if last_closing:
                    # То переходим в конец и обнуляем его
                    j = last_closing
                    last_closing = None
                # Если конец цикла не встречали
                if last_closing is None:
                    in_cycles = 0
                    # То топаем до конца цикла, пропуская все вложенные
                    while s[j] != ']' or in_cycles != 0:
                        j += 1
                        if s[j] == '[':
                            in_cycles += 1
                        elif s[j] == ']' and in_cycles:
                            in_cycles -= 1
                            j += 1
        case ']':
            start = stack[-1]
            j = start - 1
            last_closing = j
        case '.':
            print(array[i], chr(array[i])) 
        case ',':
            a = int(input()) % 256
            array[i] = a
    j += 1


print(*array[:10])

# интерпретатор не работает :(