from zad6testy import runtests
# Bartlomiej Szubiak
# Dzialanie algorytmu:
# Defakto mamy doczynienia z grafem dwudzielmym wiec
# dla kazdego czlowieka w grafie przydzielam maszyne (obojetnie jaka z tych na ktorych moze pracowac) (uzywam DFS zmodyfikowanego z wykladu )
# wtedy kiedy moge to zrobić tz. kiedy maszyna nie jest juz okupywana przez inna osobe
# gdyby sie jednak okazalo ze maszyna jest okupywana uzywajac dfs sprawdzam czy moge tego okupanta do innej osoby przypisac 
# (dzieje sie to rekurencyjnie w dol grafu)
# algorytm jest zachlanny i podejmuje lokalne decyzje ktore sa potencjalnie najlepszymi
# wazne jest ze dla danego przeszukania grafu uzywamy tej samej tablicy visited aby sie nie zapetlac m.in , poniewaz to wywolanie dfs bezposrednio dotyczy u
# poprzez uzywanie pair_V nie mamy kolizji oznaczen (bo jestesmy w stanie rozrozniac co jest osoba a co maszyna) dlatego nie przepisuje grafu
# tz. DFS zawsze wywolywany jest na osobie i jej dotyczy nie na maszynie
# 
# zlonosc O(V*(V+E)) gdzie V to ilosc osob , E ilosc "krawedzi" miedzy osobami a maszynami

def DFS_find_path(M,u,pair_V,pair_U):
    n=len(M) #ilosc ludzi
    visited=[False]*n
    
    #robie 2 przeskoki czlowiekA -> maszyna_alfa -> 
    def DFS_visit(M,human): #odwiedznie danego wierzcholka 
        nonlocal visited , pair_U, pair_V
        visited[human]=True
        for machine in M[human]: #v maszyna dla u
            assigned_human = pair_V[machine] #przypisany czlowiek do maszyny na ktora sie patrzy human
            
            if assigned_human == None : #nie przypisano maszynie czlowieka wogole
                pair_V[machine] = human
                pair_U[human] = machine
                return True
            
            if not visited[assigned_human]: #pracownik pracujacy na tej maszynie nie odwiedzony # if not visited[v]:
                if DFS_visit(M , assigned_human): #zagladamy glebiej po ewentualny swap
                    # udalo sie cos znalezc glebiej (inne przypisanie) co zwalnia to przypisanie
                    pair_V[machine] = human
                    pair_U[human] = machine
                    return True
        return False
    
    return DFS_visit(M,u) #rekurencyja sciezka w dol


def binworker(M):
    n = len(M)
    result = 0
    #u->v
    pair_U = [None] * n #T[czlowiek] -> maszyna
    pair_V = [None] * (n + 1) #T[maszyna] -> czlowiek

    for u in range(n):
        if pair_U[u] is None: #nie przypisano maszyne czlowiekowi u
            if DFS_find_path(M,u,pair_V,pair_U): #czy udalo sie przypisac maszyne
                result += 1

    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
