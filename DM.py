# DM n°1

import math as m
import time as t


def verif_facto(L):
    if L[-1] == 0:
        return (False)
    for k in range(1, len(L) + 1):
        if L[k - 1] < 0:
            return False
        if L[k - 1] > k:
            return False
    else:
        return True


def base_factorielle_versbase10(L):
    res = 0
    if verif_facto(L):
        for k in range(1, len(L) + 1):
            res = res + L[k - 1] * m.factorial(k)
        return res
    return 'liste fausse'


def CreerTabFacto(n):
    # condition i)
    i = 0
    res = [1]
    while True:
        # condition ii)
        i = i + 1
        res.append(m.factorial(i))
        fact = m.factorial(i + 1)
        # condition iii)
        if fact > n:
            return res


def recherche(k, t):
    if t[0] > k:
        return '[ERROR] - Le nombre %d est plus petit que %d - le premier terme de la liste' % (k, t[0])
    # if t[-1]<k:
    #    return(len(t)-1) #indice dernier élément liste
    # cette partie est optionelle car ajoute des lectures inutiles
    i = 0
    while i + 1 < len(t) and t[i + 1] <= k:
        i = i + 1
    return i


def recherche2(k, t):
    if t[0] > k:
        return '[ERROR] - Le nombre %d est plus petit que %d - le premier terme de la liste' % (k, t[0])
    min_index = 0
    max_index = len(t) - 1
    # On coninue tant que l'écart entre les deux index est > à 1
    while (max_index - min_index) > 1:
        i = m.ceil((max_index - min_index) / 2)  # Index au milieu
        if k > t[min_index + i]:
            min_index = min_index + i
        else:
            max_index = i
    return min_index


def base10_vers_basefactorielle(n):
    start_time = t.time() * 1000000  # en microsecondes
    # t.sleep(5), permet d'attendre 5s
    # liste des facto jusqu'à la première valeur plus grande que n
    l_fact = []
    max_top_index = 0
    while m.factorial(max_top_index) <= n:
        max_top_index += 1
        l_fact.append(m.factorial(max_top_index))

    # Initialisation des deux listes: res et enleve dernière valeur de l_fact
    top_index = recherche2(n, l_fact)
    res = []
    for k in range(0, top_index + 1):
        res.append(0)
    l_fact.pop()

    # Decomposition
    deltan = n
    # On parcourt la liste l_fact du plus grand au plus petit. Le range prend -1 comme second paramètre pour arriver jusqu'à 0. Le 3ème paramètre indique que l'on decremente de 1
    for k in range(len(res) - 1, -1, -1):
        l = 1
        while (deltan - l * l_fact[k]) >= 0:
            l += 1
        # On calcule le nouvel écart
        if l > 0:
            deltan = deltan - (l - 1) * l_fact[k]
            res[k] = l - 1
    diff_time = t.time() * 1000000 - start_time
    print('[INFO] - La durée est de %d microsecondes' % diff_time)
    return res


def tab_fibo(N):
    if N == 1:
        L = [1]
        return L
    if N == 2:
        L = [1, 2]
        return L
    Fprev = 1
    Fcurr = 2
    L = [1, 2]
    while len(L) < N:
        F = Fcurr + Fprev
        L.append(F)
        Fprev = Fcurr
        Fcurr = F
    return L


def decodage_nb(L):
    N = 0
    for k in range(1, len(L) + 1):
        N = N + L[k - 1] * (tab_fibo(k)[-1])
    return N


def recherche_plus_grand(n):
    top_index = 1
    while True:
        if tab_fibo(top_index)[-1] > n:
            return top_index - 2  # Il faut retirer un car on est un cran au dessus au moment du dernier if + Il faut retirer un car tab_fibo(top_index) va jusqu'à F rang top_index-1
        top_index += 1


def codage_nb(n):
    top_index = recherche_plus_grand(n)
    l_fact = tab_fibo(top_index + 1)
    l_ai = []
    for k in range(0, len(l_fact)):
        l_ai.append(0)

    # Decomposition
    for k in range(len(l_ai) - 1, -1, -1):
        if (n - l_fact[k]) >= 0:
            l_ai[k] = 1
            n = n - l_fact[k]
    return l_ai


def codage_liste(L):
    s = ""
    for k in range(0, len(L)):
        M = codage_nb(L[k])
        for i in range(0, len(M)):
            s = s + str(M[i])
        s = s + "1"
    return s


def decodage_liste(n):
    L = str(n).split('11')
    N = []
    for k in range(0, len(L) - 1):
        M = []
        s = str(L[k] + '1')
        for c in s:
            M.append(int(c))
        N.append(decodage_nb(M))
    return N


def premier00(L):
    is_zero = False
    for k in range(0, len(L)):
        if L[k] == 0:
            if is_zero:
                return k - 1
            else:
                is_zero = True
        else:
            is_zero = False
    return 'yesMaya'


def successeur(L):
    index = premier00(L)
    if index == 'yesMaya':
        return '[ERROR] - Aucune fois deux 0 consécutifs.'

    M = []
    for k in range(0, index):
        M.append(0)
    M.append(1)
    M.append(0)
    for k in range(index + 2, len(L)):
        M.append(L[k])
    return M


def construire(N):
    L = []
    res = []
    for k in range(1, N):
        L.append(0)
    res.append(L)

    for k in range(0, N):
        L = successeur(L)
        res.append(L)

    # Remove leading 0
    for k in range(0, len(res)):
        for i in range(len(res[k]) - 1, 0, -1):
            if res[k][i] == 0:
                res[k].pop()
            else:
                break
    return res
