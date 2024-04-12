
def generate_dic(names, goals, goals_avoided, assists):
    """generate_dic es una funcion que recibe un string, tres listas y las convierte en un diccionario de claves de tipo string y valores de tipo lista en la cual el primer elemento son los goles, el segundo los goles evitados y el tercero las asistencias.
    Names es un string con todos los jugadores.
    Goals es una lista de todos los goles de cada jugador.
    Goals_avoided es una lista de los goles evitados de cada jugador.
    Assists es una lista de todas las asistencias de cada jugador. 
    """
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
    """conocer_goleador recorre el diccionario y devuleve en una tupla el nombre y cantidad de goles del goleador.
    dic es una estructura diccionario de claves string (nombre del jugador) y valores de tipo lista, en la cual el primer elemento son los goles, el segundo los goles evitados y el tercero las asistencias del jugador.
    """
    max = -1
    for name,stats in dic.items():
        if stats[0] >= max:
            max_scorer = name
            max = stats[0]
    return max_scorer, max

def most_influential(dic,values):
    """conocer_influyente recorre el diccionario buscando el jugador con mas puntos y devuelve en una tupla su nombre y cantidad de puntos.
    dic es una estructura diccionario de claves string (nombre del jugador) y valores de tipo lista, en la cual el primer elemento son los goles, el segundo los goles evitados y el tercero las asistencias del jugador.
    values es un diccionario que tiene los valores de cada estadistica.
    """
    max = -1
    for name,stats in dic.items():
        points = 0
        points += stats[0] * values["goals"] + stats[1] * values["goals_avoided"] + stats[2] * values["assists"]
        if points >= max:
            most_influential = name
            max = points
    return most_influential, max

def goals_average(dic,matches_played):
    """goals_average recorre un diccionario contando los goles totales y esa cantidad la divide por la cantidad de partidados jugados, obteniendo el promedio de gol por partido.
    dic es una estructura diccionario de claves string (nombre del jugador) y valores de tipo lista, en la cual el primer elemento son los goles, el segundo los goles evitados y el tercero las asistencias del jugador.
    matches_played es un integer de los partidos jugados de la temporada.
    """
    goals = 0
    for name in dic:
        goals += dic[name][0]
    return goals / matches_played if matches_played != 0 else 0

def maxscorer_average(dic, matches_played):
    """promedio_goleador invoca a conocer_goleador y divide sus goles por la cantidad de partidos jugados en la temporada para obtener su promedio de gol por partido.
    dic es una estructura diccionario de claves string (nombre del jugador) y valores de tipo lista, en la cual el primer elemento son los goles, el segundo los goles evitados y el tercero las asistencias del jugador.
    matches_played es un integer de los partidos jugados de la temporada.
    """
    max_scorer = maxscorer(dic)
    average = max_scorer[1] / matches_played if matches_played != 0 else 0
    return average