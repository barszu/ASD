"""
mamy dzieci one maja klocki o roznych wysokosciach, chcemy zbudowac z nich wieze
kazde dziecko ma swoj zestaw klockow

kazde dziecko uklda wieze z klockow.

zostalo zlosciwe dziecko reszta sie zdespawnowala i zacyna dobudowywac swoja wieze z klockow innych dzieci

chce to zrobic przekladajac najmniejsza mozliwa ilosc klockow

"""

"""
Solution:

Trzeba patrzec na wszystkie wierze nie mozemy pominac tych najnizzych,

interesuje nas wykokosc wierzy T, przegladamy wszystkie wieze sciagamy z nich najwieksze klocki do momentu az bedziemy miec najwyzsza wieze

T - rozwazyc wszytskie mozliwosci -> hmax - hmin -> mozna szukac polowkowo -> O(logn)
"""