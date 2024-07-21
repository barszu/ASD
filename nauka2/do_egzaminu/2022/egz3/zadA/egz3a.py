from egz3atesty import runtests

def minMeetingRooms(intervals:list[list[int]]) -> int :
    # przedzialy to (a,b) nie [a,b]
    start = [s for [s,e] in intervals] #lista zawierajce wszystkie poczatki
    end = [e for [s,e] in intervals] #lista zawierajaca wszystkie konce
    start.sort()
    end.sort()
    #wygeneruje nam to male niegryzace sie przedzialy
    max_layer , layer = 0 , 0
    e , s = 0 , 0 #pointery
    while s < len(intervals): #dalej nie ma sensu iterowac bo layery sie juz tylko zmniejszac beda bo nie rozpoczynam spotkan
        if start[s] <= end[e]: #spotkanie e jeszcze trwa i nie da sie w tym pokoju
            s += 1 #sprubuj rozpoczac kolejne
            layer += 1
        else: #spotkanie e skonczylo sie mozna rozpoczac w tym pokoju
            e += 1
            layer += -1
            
        max_layer = max( max_layer , layer )
    return max_layer

def snow( T, I ):
    # tu prosze wpisac wlasna implementacje
    return minMeetingRooms(I)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
