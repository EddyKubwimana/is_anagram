def frequency(word1, word2):
    from collections import Counter
    freq1 ={}
    freq2 = {}
    if len(word1) != len(word2):
        return False
    
    for i in word1:
        if  i in freq1:
            freq1[i] += 1
                
        else:
            freq1[i]= 1
    for i in word2:
        if  i in freq2:
            freq2[i] += 1
                
        else:
            freq2[i]= 1


    if Counter(freq1) == Counter(freq2):
        return True
    else:
        return False

print(frequency("ga", "ag"))
    

            
    
