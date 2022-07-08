def kwonly(a,*b,c=3,**d):
    print(a,b,c,d)
    
kwonly(1, * (2, 3) , **dict(x=4, у=5)) 

