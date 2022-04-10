def abs_for_math(x):
    return max(-x, x)


def analyze_asymmetry_module(element):
    result = ['', '']
    element_for_degree = abs_for_math(element)
    if element_for_degree <= 0.25:
        result[0] = f'{element} <= 0.25'
        result[1] = 'незначительная'
    elif 0.25 < element_for_degree < 0.5:
        result[0] = f'0.25 < {element} < 0.5'
        result[1] = 'умеренная'
    elif element_for_degree >= 0.5:
        result[0] = f'{element} >= 0.5'
        result[1] = 'существенная'
    return result


def analyze_asymmetry_sign(element):
    result = ''
    if element > 0:
        result = 'левостороняя'
    elif elemnt < 0:
        result = 'правостороняя'
    elif element == 0:
        result = 'без смещения'
    return result


def analyze_excess_sign(element):
    result = ['', '']
    if element > 0:
        result[0] = f'{element} > 0'
        result[1] = 'более высоким'
    elif element < 0:
        result[0] = f'{element} < 0'
        result[1] = 'более низким и пологим'
    elif element == 0:
        result[0] = f'{element} = 0'
        result[1] = 'похожим на'
    return result


def cr_answer(math):
    degree_asymmetry = analyze_asymmetry_module(math.asymmetry)
    sing_asymmetry = analyze_asymmetry_sign(math.asymmetry)
    asymmetry_string = f"Так как {degree_asymmetry[0]},\n то ассиметрия {degree_asymmetry[1]} и {sing_asymmetry}."
    sign_excess = analyze_excess_sign(math.excess)
    excess_string = f'Так как {sign_excess[0]},\n то эмперическое распределение является {sign_excess[1]}\n относительно ' \
                    f'эталонного нормального распределенная.'
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
             f'{asymmetry_string}\n' \
             f'{excess_string}\n' \
             f'Коэффициент эксцесса: {math.excess}\n'
    return answer
