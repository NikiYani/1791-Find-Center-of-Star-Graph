class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        fElem = edges[0][0]
        sElem = edges[0][1]
        
        if fElem == edges[1][0] or fElem == edges[1][1] :
            return fElem
        else :
            return sElem