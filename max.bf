# Вывести наибольшее из двух чисел

# первая ячейка отвечает за первое число
# вторая ячейка отвечает за вторая число
# третья ячейка отвечает за накопление максимума
# четвертая ячейка отвечает за проверку равенства 0 второй ячейки
# пятая ячейка отвечает за флаг который говорит о том что вторая ячейка оказалась больше
# шестая ячейка это буферная для второй нужна для выхода из цикла


, # ввод первого числа

>, # ввод второго числа

< # вернулись на первое

>>>>+<<<< # делаем флаг в пятой который будет меняться если вторая оказалась меньше
# пока в первой не 0
[
    ->- # уменьшили обе ячейки на 1
    >+ # пошли в третью и увеличили ее на 1
    < # вернулись на вторую

    >>+ # пошли на четвертую как флаг для условия
    << # снова вернулись на вторую
    [
        >>-<< # удалили флаг
        [->>>>+<<<<] # перекладываем значение из второй в 6 чтобы выйти из цикла
    ]
    >> # если флаг не поменялся в четвертой
    [
        # значит во второй оказался ноль
        >-< # удаляем флаг из пятой
        <<< # то идем на первую
        [
            ->>+<< # переносим остаток первого в третью
        ]
        >>>[-] # идем снова на 4 и обнуляем
    ]

    # возвращаем обратно значение из 6 во вторую
    >>[-<<<<+>>>>] # пока в 6 не станет пусто



    <<<<< # вернулись обратно на первую
]
>>>> # идем проверять флаг
[
    <<< # идем на вторую
    [
        ->+< # переносим ее остаток в третью
    ]
    >>>- # вернуться обратно на флаг в 6
]
<< # вернулись в третью
. # вывод
