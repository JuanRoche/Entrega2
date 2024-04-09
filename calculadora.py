
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

def maxscorer(dic):
    """conocer_goleador recorre el diccionario y devuleve en una tupla el nombre y cantidad de goles del goleador"""
    max = -1
    for name in dic:
        # valor del dic = [goles, goles evitados, asistencias]
        if dic[name][0] >= max:
            max_scorer = name
            max = dic[name][0]
    return max_scorer, max

def most_influential(dic,values):
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

def goals_average(dic,matches_played):
    """goals_average recorre un diccionario contando los goles totales y esa cantidad la divide por la cantidad de partidados jugados, obteniendo el promedio de gol por partido."""
    goals = 0
    for name in dic:
        goals += dic[name][0]
    return goals / matches_played if matches_played != 0 else 0

def maxscorer_average(dic, matches_played):
    """promedio_goleador invoca a conocer_goleador y divide sus goles por la cantidad de partidos jugados en la temporada para obtener su promedio de gol por partido."""
    max_scorer = maxscorer(dic)
    average = max_scorer[1] / matches_played if matches_played != 0 else 0
    return average