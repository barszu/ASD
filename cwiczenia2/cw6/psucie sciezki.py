# czy istnieje taka krawedz taka ze jesli ja usuniemy to dlugosc najkrotszej sciezki sie zwiekszy

# usuwaj kazda krawedz -> i sprawdz bfs

# pusc bfs i zbierz wszystkie sciezki (najkrotsze) do punktu y
# zbuduj z tego nowy graf, szukamy waskiego gardla

# najkrotsze sciezki mozna rozpoznac tak ze puscic z 2 stron BFS, zapamietujac dystnas od start i koniec
# wierzcholek nalezy do najkrotszej sciezki jesli dystans od startu + dystans do konca = dystans od startu do konca
