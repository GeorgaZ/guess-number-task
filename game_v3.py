"""Игра угадай число.

Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Функция принимает загаданное число и возвращает число попыток.

    Сначала устанавливаем в какой половине находится искомое число.
    Затем в какой четверти.
    Затем в какой 1/8.
    Далее угадываем число перебором.
    Таким образом кол-во попыток не превысит 15.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: _Число попыток
    """
    count = 0
    max = 100
    predict = max//2
    # условие не фиксирует какой должна быть старотовая точка угадывания,
    # поэтому я взял середину отрезка за точку старта

    if number == predict:
        count += 1  # проверяем попали ли мы сразу
        return count

    if number > predict:
        predict = round(predict*1.5)  # ограничеваем диапазон поиска четвертью
        count += 1
        if number > predict:
            predict += predict//6
            count += 1
        else:
            predict -= predict//6
            count += 1
    else:
        predict = round(predict*0.5)
        count += 1
        if number > predict:
            predict += predict//2
            count += 1
        else:
            predict -= predict//2
            count += 1

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count


def score_game(random_predict) -> int:
    """
    За какое количство попыток в среднем за 1000 подходов угадывает алгоритм.

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))
    # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
