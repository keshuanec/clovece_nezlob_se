from random import choices



def vodici_pole(n):   # tato funkce mi tvoří string 1234567890 s opakovanim tak abych mel stejne mnozstvi znaku jako je pocet poli v clovicku n
    """
    vytvori radu cisel v podobe 1234567890123.... tak aby celkove mnozstvi cislic bylo ¨n¨
    :param n: int - pocet poli
    :return: str
    """
    return ("1234567890" * ((n // 10) + 1))[:n]

def throw_dice(roll_bias: float):
    """
    hod kostkou
    :param roll_bias: pravdepodobnost hodu cisla ¨6¨
    :return: vrati nahodny int 1-6
    """

    roll_tuple = (1,2,3,4,5,6)
    rest_chance = ((1 - roll_bias) / 5)
    roll = choices(roll_tuple, weights=(rest_chance, rest_chance, rest_chance, rest_chance, rest_chance, roll_bias), k=1)[0]
    return roll

def total_throw_list(roll_bias: float):
    """
    kolik je celkovy hod? Seznam.
    :param roll_bias: pravdepodobnost hodu ¨6¨
    :return: celkovy hod v podobe seznamu cislic (napr. [6, 6, 4] nebo [3] atd...)
    """
    result = []
    throw = throw_dice(roll_bias)
    while throw == 6:
        result.append(throw)
        throw = throw_dice(roll_bias)
    result.append(throw)
    return result

def total_throw(roll_bias: float):
    """
    kolik je celkovy hod? Hodnota.
    :param roll_bias: pravdepodobnost hodu ¨6¨
    :return: celkovy hod v podobe int. Soucet hodu v pripade hazeni sestek
    """
    return sum(total_throw_list(roll_bias))



def move_figure(figure_pos: int):
    pass
    """

    :param figure_pos: vstupni pozice figurky
    :param total_throw: celkovy hod
    :return: figure_pos -
    """


#print(vodici_pole(42))