import string

def generate_dic(names, goals, goals_avoided, assists):
    """generate_dic es una funcion que recibe cuatro listas y las convierte en un diccionario de claves de tipo string y valores de tipo lista"""
   
    names_list = names.replace(",","").split()

    dic = {}
    for i in range(10):
        stats = []
        stats.append(goals[i])
        stats.append(goals_avoided[i])
        stats.append(assists[i])
        dic[names_list[i]] = stats.copy()
    return dic
