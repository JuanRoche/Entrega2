
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


def calcular_goleador(dic):
    max = -1
    for name in dic:
        # valor del dic = [goles, goles evitados, asistencias]
        if dic[name][0] >= max:
            max_scorer = name
            max = dic[name][0]
    return max_scorer, max

