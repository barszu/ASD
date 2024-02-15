a = "i349j3j1xqb1a2av09dz8wv0x4p0rxyf3gfd"
b = "dibb5zydwaqdyb9nd22h7ig8p36vc32vnt88"
T = [a,b]

def cnt_letters(s:str) -> int:
    letters_cnt = 0
    for c in s:
        if c.isalpha: letters_cnt +=1
    return letters_cnt

Data = [(len(word),cnt_letters(word),word) for word in T]
print(Data)
