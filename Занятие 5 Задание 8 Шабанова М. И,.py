def longest_same_sequence(s):    
    lng,tmp = 1,1
    
    for i in range(len(s)-1,0,-1):
        if s[i]==s[i-1]:
            tmp += 1
        else: 
            if tmp > lng:
                lng = tmp
            tmp = 1
    
    if tmp > lng: 
        lng = tmp        
    
    return lng
