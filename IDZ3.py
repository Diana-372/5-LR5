import os
from datetime import datetime

def search(path, current_range, max_range, check_time):
    dir=os.scandir(path)
    if current_range >= max_range[1]:
        return
    try:
        for i in dir:
            if i.is_dir():
                os.chdir(i.path)
                search(i.path, current_range + 1, max_range, check_time)
            elif i.is_file() and current_range>=max_range[0]:
                if os.path.getmtime(i)>check_time:
                    result.append(i)
                    if current_range in counter:
                        counter[current_range]=int(counter[current_range])+1
                    else:
                        counter[current_range]='1'
    except:
        exp.append(i)



input_parametrs=input('Введите входные параметы Путь:\ -(начальная глубина поиска) -(конечная глубина поиска)')
input_parametrs=input_parametrs.split(' -')

path=input_parametrs[0]

try:
    dt_now=str(datetime.now()).split('-')
    dt_now[0]=str(int(dt_now[0])-1)
    check_time=datetime.strptime('-'.join(dt_now), '%Y-%m-%d %H:%M:%S.%f').timestamp()
    result=[]
    counter={}
    exp=[]

    max_range=(int(input_parametrs[1]), int(input_parametrs[2]))
    os.chdir(input_parametrs[0])

    search(path, 1, max_range, check_time)

    print("Всего результатов по заданным параметрам - ", len(result))
    print("\nПолный список результатов:")
    for i in result:
        print(i.path)

    print("\n")
    for i in counter:
        print(f"Результатов на уровне {i} - {counter[i]}")
    print("\nИсключений не обработанно", len(exp))
    print("Полный список исключений:")
    for i in exp:
        print(i.path)
except:
    print("Неверна задан путь или параметр")

final=input('Нажмите любую кнопку для окончания работы программы.')
