# podzbiory z powtorzeniami w srodku -> jak nie biore np to nie biore jakich kolwiek 2

def mask_gen(lenth):
    
    def bins(num , lenth ):
        #returns binary representation with 0 in front of to fullfill
        bins = ""
        while num != 0:
            bins += str( num%2 )
            num = num//2
            
        bins = bins[::-1]
        while len(bins) < lenth :
            bins = "0" + bins
        return bins
    
    mask_list = [bins(i , lenth) for i in range(2**(lenth))]
    return mask_list

print(mask_gen(5))