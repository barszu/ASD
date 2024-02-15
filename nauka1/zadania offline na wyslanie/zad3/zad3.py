from zad3testy import runtests
# Bartlomiej Szubiak
# Idea algorytmu: tworzymy tablice 2D zawierajaca w i-tym wierszu wszystkie str majace dlugosc i -> str roznej dl napewno nie sa rownowazne
# zmniejszamy przez to problem plus nie ma problemu z ich porownywaniem (str)
# te str (tej samej dl) obracamy (tj tok -> kot)(t>k) i przez to zmniejszamy problem rownowaznosci str do ich rownosci
# sortujemy mini_tab bucket_sortem
# zliczamy ilosc wystapien wyrazow danych przez to zliczajac moc slowa -> przechodzimy przez wszytskie wiersze(mini_tab) i znajdujemy najwieksza moc
# szacowana zlozonosc O(N + n*log(n))

def the_longest_str_in_tab(T):
    longest=0
    for i in range(len(T)):
        dl=len(T[i])
        if dl>longest: longest=dl
    return longest

def create_data_tab(data,T):
    for i in range(len(T)):
        wyraz=T[i]
        dl=len(wyraz)
        data[dl].append(wyraz) 

def obroc_wyrazy(T_str):
    i=0
    for s in T_str:
        if s[0]>s[-1]:
            T_str[i]=s[::-1]
        i+=1

def count_el(el,T):
    cnt=0
    for w in T:
        if w==el : cnt+=1
    return cnt

def bucket_sort(tab_str,p,n): #n znana dl str , p-pozycja
    if p==n: return #p(max val)=n-1
    lenth=len(tab_str)
    if lenth<2: return
    el0=tab_str[0]
    if (tab_str == ([el0]*lenth)): return
    #str sa tej samej dlugosci
    wiaderka_cnt=[0]*26 #ile jest str co na tej pozycji maja litere np a
    wiaderka_zawartosc= [ [] for _ in range(26) ]
    # 0 - a
    for s in tab_str:
        litera_wiodaca=s[p]
        pozycja=ord(litera_wiodaca)-97
        wiaderka_cnt[pozycja] += 1
        wiaderka_zawartosc[pozycja].append(s)
    
    i=0
    j=0
    for mini_tab in wiaderka_zawartosc:
        len_mini_tab = wiaderka_cnt[i]
        if len_mini_tab<1 : 
            i+=1
            continue
        bucket_sort(mini_tab,p+1,n)
        tab_str[j:j+len_mini_tab]=mini_tab
        if j+len_mini_tab > lenth-1:
            tab_str[j::]=mini_tab
            break
        j+=len_mini_tab
        i+=1
         
def compare_srt(tab_of_str,dl_str,n):
    obroc_wyrazy(tab_of_str)
    bucket_sort(tab_of_str,0,dl_str)
    maxy=0
    last_el=""
    for wyraz in tab_of_str:
        if (wyraz==last_el): continue
        # cnt = tab_of_str.count(wyraz)
        cnt = count_el(wyraz,tab_of_str)
        if cnt > maxy : maxy=cnt
        last_el=wyraz
    return maxy

def strong_string(T):
    longest_str=the_longest_str_in_tab(T)
    # longest_str=10
    data=[ [] for _ in range(longest_str+1) ]
    # i wiersz -> el o dl i
    create_data_tab(data,T)
    najnaj=0
    i=0
    for tab_str in data:
        len_tab_str=len(tab_str)
        if(len_tab_str<najnaj): continue
        moc=compare_srt(tab_str , i , len_tab_str)
        if moc>najnaj: najnaj=moc
        i += 1
    return najnaj


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )


