def root(g,n):
    r=n[0]
    c=n[1]
    fc=0
    sp=[]
    l=[(0,-1),(-1,0),(0,1),(1,0)]
    for i in range(r):
        for j in range(c):
            if g[i][j]==2:
                sp.append((i,j))
            elif g[i][j]==1:
                fc+=1
    mi=0
    while sp and fc>0:
        mi+=1
        for i in range(len(sp)):
            x,y=sp.pop(0)
            for m,n in l:
                x1=x+m
                y1=y+n
                if x1<0 or x1==r or y1<0 or y1==c or g[x1][y1]==0 or g[x1][y1]==2:
                          continue
                fc-=1
                g[x1][y1]=2
                sp.append((x1,y1))
    return mi if fc==0 else -1
n=[int(x) for x in input().split()]
g=[list(map(int,input().split())) for i in range(n[0])]
print(root(g,n))
    
        
                      
