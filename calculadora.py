
def generate_dic(names, goals, goals_avoided, assists):
    """generate_dic es una funcion que recibe cuatro listas y las convierte en un diccionario de claves de tipo string y valores de tipo lista"""
   
    names_list = names.replace(",","").split()

    dic = {}
    for i in range(len(names_list)):
        stats = []
        stats.append(goals[i])
        stats.append(goals_avoided[i])
        stats.append(assists[i])
        dic[names_list[i]] = stats.copy()
    return dic

def conocer_goleador(dic):
    """conocer_goleador recorre el diccionario y devuleve en una tupla el nombre y cantidad de goles del goleador"""
    max = -1
    for name in dic:
        # valor del dic = [goles, goles evitados, asistencias]
        if dic[name][0] >= max:
            max_scorer = name
            max = dic[name][0]
    return max_scorer, max

def conocer_influyente(dic,values):
    """conocer_influyente recorre el diccionario buscando el jugador con mas puntos y devuelve en una tupla su nombre y cantidad de puntos."""
    max = -1
    for name in dic:
        stats = dic[name]
        points = 0
        points += stats[0] * values["goals"] + stats[1] * values["goals_avoided"] + stats[2] * values["assists"]
        if points >= max:
            most_influential = name
            max = points
    return most_influential, max

