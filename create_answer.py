def cr_answer(math):
    answer = f'Минимальное значение: {math.min}\n' \
             f'Максимальное значение: {math.max}\n' \
             f'Количество интервалов: {math.count_int}\n' \
             f'Длина интервала: {math.length}\n' \
             f'Среднее значение: {math.average_value}\n' \
             f'Дисперсия: {math.dispersion}\n' \
             f'Среднее квадратное отклонение: {math.root_of_dispersion}\n' \
             f'Мода: {math.fashion}\n' \
             f'Медиана: {math.median}\n' \
             f'Ассиметрия: {math.asymmetry}\n' \
             f'Коэффициент эксцесса: {math.excess}\n'
    return answer