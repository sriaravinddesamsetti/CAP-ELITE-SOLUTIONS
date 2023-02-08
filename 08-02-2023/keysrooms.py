def trav(mat,i,j,c):
            if i<0 or i>len(mat) j<0 or j>len(mat[0]) :
                return
            if mat[i][j]==0:
                return c
            else:
                c+=1
            return min(trav(mat,i+1,j,c),trav(mat,i-1,j,c),trav(mat,i,j-1,c),trav(mat,i,j+1,c)
