import math

with open('bd.txt', 'r', encoding='utf-8') as file:
    bd_file = file.read()
    bd = bd_file.split('\n')
    arr_bing = []

    for i in range(len(bd) - 1):
        k = 0
        arr_bing.append([])
        arr_bing[i].append('')

        while bd[i][k].isdigit():
            arr_bing[i][0] += bd[i][k]
            k += 1
        arr_bing[i].append([])
        while k < len(bd[i]):
            if bd[i][k] == '#':
                arr_bing[i][1].append('')
                k += 1
                while k < len(bd[i]) and bd[i][k] != '#':
                    arr_bing[i][1][-1] += bd[i][k]
                    k += 1
            elif bd[i][k] == '_':
                k += 1
                arr_bing[i][1][-1] += '_'
                if k < len(bd[i]) and bd[i][k] == '(':
                    k += 1
                    while k < len(bd[i]) and bd[i][k] != ')':
                        arr_bing[i][1][-1] += bd[i][k]
                        k += 1
                    if k < len(bd[i]) and bd[i][k] == ')':
                        k += 1
                else:
                    arr_bing[i][1][-1] += bd[i][k]
            elif bd[i][k] == '@':
                arr_bing[i].append('')
                k += 1
                while k < len(bd[i]) and bd[i][k] != '@':
                    arr_bing[i][-1] += bd[i][k]
                    k += 1
                k -= 1
            else:
                if bd[i][k] != ' ' and bd[i][k] != '\t':
                    arr_bing[i][1].append(str(bd[i][k]))
            k += 1

with open('bd_fiz.txt', 'r', encoding='utf-8') as data_file:
    data = data_file.read()
    data = data.split('\n')
    data_hope = []

for i in range(len(data)):
    hope = data[i].split(' : ')
    data_hope.append(hope)

a = input('Введите физическую величину (букву или словами), которую хотите найти из формул: ')
for i in range(len(data_hope) - 1):
    if a == data_hope[i][1]:
        a = data_hope[i][0]
        break
print(a)
aaa = []
e = 0
for i in range(len(arr_bing)):
    if (a in arr_bing[i][1]) and not (arr_bing[i][3] in aaa):
        e += 1
        print(f'{e}.', arr_bing[i][3])
        aaa.append(arr_bing[i][3])
b = int(input('Выберите номер закона, в котором находится ваша формула: '))

eee = []
re = 0
for i in range(len(arr_bing)):
    if (aaa[b - 1] == arr_bing[i][3]) and not (arr_bing[i][1] in eee):
        if a in arr_bing[i][1]:
            re += 1
            print(f'{re}.', arr_bing[i][1], arr_bing[i][2])
            eee.append(arr_bing[i][1])
bb = int(input('Выберите номер формулы, в котором находится ваша буква: '))
print(eee[bb - 1])
def sorting(letter, work_part, com_part):
    snd_base = []
    if not (work_part[0] in ('-', '+')):
        work_part.insert(0, '+')
    if not (com_part[0] in ('-', '+')):
        com_part.insert(0, '+')

    fst_num = 0
    while fst_num < len(com_part):
        int_fst = []

        if com_part[fst_num] == '-' and fst_num < len(com_part):
            fst_num += 1
            if com_part[fst_num] == '(':
                int_fst.append(com_part[fst_num - 1])
                while fst_num + 1 < len(com_part) and not (com_part[fst_num + 1] in ('-', '+')):
                    if com_part[fst_num] == '(':
                        while com_part[fst_num] != ')':
                            int_fst.append(com_part[fst_num])
                            fst_num += 1
                    else:
                        int_fst.append(com_part[fst_num])
                        fst_num += 1
                int_fst.append(com_part[fst_num])
                if letter in int_fst:
                    snd_base += int_fst
                else:
                    if int_fst and int_fst[0] == '-':
                        int_fst[0] = '+'
                    else:
                        int_fst[0] = '-'
                    work_part += int_fst
            else:
                work_part += ['+', com_part[fst_num]]
                fst_num += 1
        elif com_part[fst_num] == '+' and fst_num < len(com_part):
            fst_num += 1
            if com_part[fst_num] == '(':
                int_fst.append(com_part[fst_num - 1])
                while fst_num + 1 < len(com_part) and not (com_part[fst_num + 1] in ('-', '+')):
                    if com_part[fst_num] == '(':
                        while com_part[fst_num] != ')':
                            int_fst.append(com_part[fst_num])
                            fst_num += 1
                    else:
                        int_fst.append(com_part[fst_num])
                        fst_num += 1
                int_fst.append(com_part[fst_num])
                if letter in int_fst:
                    snd_base += int_fst
                else:
                    if int_fst and int_fst[0] == '-':
                        int_fst[0] = '+'
                    else:
                        int_fst[0] = '-'
                    work_part += int_fst
            else:
                work_part += ['-', com_part[fst_num]]
                fst_num += 1
        elif com_part[fst_num] in ('*', '/', '^'):
            if com_part[fst_num] in ('*', '/', '^'):
                fst_num -= 2
                work_part = work_part[:-2]

            while fst_num + 1 < len(com_part) and not (com_part[fst_num + 1] in ('-', '+')):
                if com_part[fst_num + 1] == '(':
                    while com_part[fst_num] != ')':
                        int_fst.append(com_part[fst_num])
                        fst_num += 1
                else:
                    int_fst.append(com_part[fst_num])
                    fst_num += 1
            int_fst.append(com_part[fst_num])
            if letter in int_fst:
                snd_base += int_fst
            else:
                if int_fst and int_fst[0] == '-':
                    int_fst[0] = '+'
                else:
                    int_fst[0] = '-'
                work_part += int_fst
        else:
            fst_num += 1


    tired = []
    trd_base = []
    snd_num = 0
    if snd_base:
        if snd_base[0] == '-':
            tired = []
        while snd_num + 1 < len(snd_base):
            int_snd = []
            if snd_base[snd_num] == '*' and snd_base[snd_num + 1] != letter:
                snd_num += 1
                if snd_base[snd_num] == '(':
                    while snd_base[snd_num] != ')':
                        int_snd.append(snd_base[snd_num])
                        snd_num += 1
                    int_snd.append(snd_base[snd_num])
                    if letter in int_snd:
                        trd_base += int_snd
                    else:
                        tired = int_snd + tired
                        work_part = ['('] + work_part + [')', '/'] + tired
                    snd_num += 1
                else:
                    work_part = ['('] + work_part + [')', '/', snd_base[snd_num]]
                    snd_num += 1
            elif snd_base[snd_num] == '/' and snd_base[snd_num + 1] != letter:
                snd_num += 1
                if snd_base[snd_num] == '(':
                    while snd_base[snd_num] != ')':
                        int_snd.append(snd_base[snd_num])
                        snd_num += 1
                    int_snd.append(snd_base[snd_num])
                    if letter in int_snd:
                        trd_base += int_snd
                    else:
                        tired = int_snd + tired
                        work_part = ['('] + work_part + [')', '*'] + tired
                else:
                    work_part = ['('] + work_part + [')', '*', snd_base[snd_num]]
                    snd_num += 1
            elif snd_base[snd_num] == '^' and snd_base[snd_num + 1] != letter:
                snd_num += 1
                if snd_base[snd_num] == '(':
                    ww = snd_num - 2
                    while snd_base[snd_num] != ')':
                        int_snd.append(snd_base[snd_num])
                        snd_num += 1
                    int_snd.append(snd_base[snd_num])
                    if letter in int_snd:
                        trd_base += int_snd
                    else:
                        tired = int_snd + tired
                        if snd_base[ww] == letter:
                            work_part = ['('] + work_part + [')', '^', '(', '1', '/'] + tired + [')']
                        else:
                            work_part = work_part + ['^'] + tired
                else:
                    if snd_base[snd_num - 1] == letter:
                        work_part = ['('] + work_part + [')', '^', '(', '1', '/', snd_base[snd_num], ')']
                    else:
                        work_part = work_part + ['^', snd_base[snd_num]]

                    snd_num += 1
            elif snd_base[snd_num] != letter and snd_base[snd_num + 1] != letter:
                snd_num += 1
                if snd_base[snd_num] == '(':
                    while snd_base[snd_num] != ')':
                        int_snd.append(snd_base[snd_num])
                        snd_num += 1
                    int_snd.append(snd_base[snd_num])
                    if letter in int_snd:
                        trd_base += int_snd
                    else:
                        tired = int_snd + tired
                        work_part = ['('] + work_part + [')', '/'] + tired
                    snd_num += 1
                else:
                    if not (snd_base[snd_num] in ('-', '+', '*', '/', '^', '(', ')')):
                        work_part = ['('] + work_part + [')', '/'] + [snd_base[snd_num]]
                        snd_num += 1
                    else:
                        snd_num += 1
            elif snd_base[snd_num + 1] == letter or snd_base[snd_num] == letter:
                snd_num += 1
            tired = []
        if snd_base[snd_base.index(letter) - 1] == '/':
            work_part = ['1', '/', '('] + work_part + [')']

    if letter in work_part:
        jjj = work_part.index(letter)
        work_part.pop(jjj)
        work_part.pop(jjj - 1)

    if com_part[com_part.index(letter) - 1] == '-':
        work_part = ['('] + work_part + [')', '*', '-1']
    if trd_base:
        trd_base = trd_base[:-1]
        trd_base.pop(0)
    return [work_part, trd_base]


arr = eee[bb - 1]

arr_p = []
let = a

equ = arr.index('=')
m_index = arr.index(let)
arr_p = arr_p + [let, '=']
main_difference = m_index - equ

arr_com = []
arr_work = []
if main_difference < 0:
    for i in range(len(arr)):
        if i < equ:
            arr_com.append(arr[i])
        elif i > equ:
            arr_work.append(arr[i])

elif main_difference > 0:
    for i in range(len(arr)):
        if i > equ:
            arr_com.append(arr[i])
        elif i < equ:
            arr_work.append(arr[i])

arr_work = sorting(let, arr_work, arr_com)
arr_com = arr_work[1]
arr_work = arr_work[0]
while arr_com:
    arr_work = sorting(let, arr_work, arr_com)
    arr_com = arr_work[1]
    arr_work = arr_work[0]
arr_p += arr_work


print(*arr_p)