def missing(a):
    n=a[-1]
    sum=0
    r=n*(n+1)//2
    t=sum(a)
    print(r-t)
a=[1,2,3,5,6,7,8]
missing(a)