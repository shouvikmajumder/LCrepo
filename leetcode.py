# contains duplicate 
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Group Anagrams

def groupanagrams(strs):
    check = {}
    outputlst = []
    for i in strs:
        x = ",".join(sorted(i))
        if x not in check:
            check[x] = [i]
        elif x in check:
            check[x].append(i)
    
    
    for i in list(check.values()):
        outputlst.append(i)
    return outputlst    
        
    

    #This is O(n) time complexity
strs = ["act","pots","tops","cat","stop","hat"]
print(groupanagrams(strs))
