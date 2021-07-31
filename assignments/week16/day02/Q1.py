class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None:
            print("List is None")
            return("")
        
        length = len(strs)
        if length == 0:
            print("List is empty")
            return("")
        
        if length == 1:
            print("List has just 1 string")
            return(strs[0])
        
        retStr = ""
        
        firstStr = strs[0]
        
        for i in range(len(firstStr)):
            for j in range(1, length):
                if i < len(strs[j]):
                    if firstStr[i] != strs[j][i]:
                        return(retStr)
                else:
                    return(retStr)
            retStr = retStr + firstStr[i]
        
        return(retStr)