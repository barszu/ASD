"""
Bucket sort - sortowanie kubelkowe

A - tablica liczb wymierne(float)
0 <= A[i] < 1 
el A byly wygenerowane zgodnie z rozkladem jednostajnym

n - rozmiar tablicy

tworzymy n kubelkow (list) i wrzucamy odpowiednie el do kubelkow
kubelek 0 ,  kubelek 1
  [0;1/n) , [1/n ; 2/n) ...
  
kubelki sortujemy np rekurencyjnie albo bubble sort np bo male beda
prepisujemy dane z kubelkow w kolejnosci odpowiedniej

zlozonosc 0(n)

"""

# select algoritm
"""
Magiczbe 5-tki -> znajdowanie na jakim id bylby el po sortnieciu
zlozonosc O(n)
A - tablica n liczb
1. Podziel A na grupy po te 5 el
2. Znajdz mediane dla kazdej grupy
3. Szukamy pivota -> mediana median
4. Partiotion dla pivot'a
5. if x jest na pozycji k -> return x
   if x jest na pozycji dalszej niz k to szukaj
   rekurencyjnie w lewej czesci tablicy 
   a jak nie to prawej
"""