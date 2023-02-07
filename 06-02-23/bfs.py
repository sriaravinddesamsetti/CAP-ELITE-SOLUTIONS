class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code her
        v=[]
        q=[]
        q.append(0)
        v.append(0)
        while q:
            a=q.pop(0)
            for i in adj[a]:
                if i not in v:
                    v.append(i)
                    q.append(i)
        return v
            
