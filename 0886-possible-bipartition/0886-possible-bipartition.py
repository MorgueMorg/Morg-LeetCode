class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        visited=[0]*n
        group=[-1]*n
        adj=[[] for _ in range(n)]
        for i,j in dislikes:
            adj[i-1].append(j-1)
            adj[j-1].append(i-1)
            
        for k in range(n):
            if visited[k]==0:
                lst=[[k,0]]
                visited[k]=1
                group[k]=0
                while lst:
                    x,c=lst.pop(0)
                    for i in adj[x]:
                        if visited[i]==0:
                            lst.append([i,(c+1)%2])
                            visited[i]=1
                            group[i]=(c+1)%2
                        else:
                            if group[i]!=(c+1)%2:
                                return False
        
        return True