from zad3testy import runtests

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

# def is_equal(a,b,n):
#     for i in range(n):
#         if a[i]!=b[i]:
#             return False
#     return True

def compare_srt(tab_of_str,dl_str,n):
    # n=len(tab_of_str)
    if (n<1) : return 0
    tab_laczen=[1]*n #ile podobnych str jest z tym
    maxy=0
    tab_of_str.sort()
    obroc_wyrazy(tab_of_str)
    for i in range(n):
        for j in range(i+1,n):
            a=tab_of_str[i]
            b=tab_of_str[j]
            # c=b[::-1]
            # if (a==b) or (a==c):
            if (a==b):
                tab_laczen[i] += 1
                tab_laczen[j] += 1
            # if is_equal(a,b,dl_str):
            #     tab_laczen[i] += 1
            #     tab_laczen[j] += 1
                if tab_laczen[i] > maxy : maxy=tab_laczen[i]
    # optynmalizacja ? max=my_maxi_na ifach(tab_laczen[i]) po +1
    # return max(tab_laczen)
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
        # if (i+1<najnaj): continue #nwm czm dziala? przypadek? 
        
        moc=compare_srt(tab_str , i , len_tab_str)
        if moc>najnaj: najnaj=moc
        i += 1
    a=1
    return najnaj


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
# print(strong_string(['yrghcrsbkz', 'zkbsrchgry', 'wvyxchyfwhityvarcd', 'gf', 'zcna', 'vqdkdatklmbs', 'pepsfi', 'hknsjqnkfy', 'upkxypalctunir', 'vizynyhmjqpmdezghs', 'ng', 'whwjybwzanmfah', 'hcxozararors', 'kzwtshcdqhodcpmbknil']))

