# you can change following no. of man\woman and\or preference list
# 'm' is for married/engaged man/woman
# 's' is for single man/woman
# 'p' is for keeping track of proposed woman
# M is preference dictionary for all man
# W is preference dictionary for all woman
n=int(input("enter no. of man or woman : "))
m={'m1':'s','m2':'s','m3':'s'}
w={'w1':'s','w2':'s','w3':'s'}
'''
M={'m1':['p','w1','w2','w3'],'m2':['p','w1','w2','w3'],'m3':['p','w2','w3','w1']}
W={'w1':['m2','m1','m3'],'w2':['m1','m3','m2'],'w3':['m1','m2','m3']}
'''
M={'m1':['p','w2','w1','w3'],'m2':['p','w2','w1','w3'],'m3':['p','w1','w3','w2']}
W={'w1':['m1','m3','m2'],'w2':['m2','m1','m3'],'w3':['m3','m1','m2']}

S={'m1':None,'m2':None,'m3':None}
#copy keys of dictionary m to man-list
man=[]
for a in m:
    man.append(a)
z=0
# initially a=m1
a=man[z]
while z<n:
    # temp is man's preference list and a is selected man
    temp=M[a]    
    # man is single and there exist a woman in list who isn't proposed by selected man
    if m[a]=='s' and temp[n]!='p':
        # i is for keeping track of p(proposed woman)
        i=0
        while temp[i]!='p':
            i=i+1
        # if woman not proposed by man is single
        if w[temp[i+1]]=='s':
            S[a]=temp[i+1]
            m[a]='m'
            w[temp[i+1]]='m'
            z=z+1
        # if woman is not single
        else:
            temp1=W[temp[i+1]]
            j=0
            for b in S:
                if S[b]==temp[i+1]:
                    # b is old husband/fiance of woman
                    pre=temp1.index(b)
                    # a is the man who proposed woman
                    post=temp1.index(a)
                    c=b
            # check if woman preferes a to its current partner c
            # here b isn't c because of for loop
            if pre>post:
                S[a]=temp[i+1]
                m[a]='m'
                S[c]=None
                m[c]='s'
                # c is single now so we have to find his partner
                z=man.index(c)
        # change track of proposed woman        
        t=temp[i+1]
        temp[i+1]=temp[i]
        temp[i]=t
        i=i+1
        M[a]=temp
        # we have to check for IndexError
        try:
            if z<n:
               a=man[z]
        except:
            break
    else:
        z=z+1
        a=man[z]
        continue
                
                
                

        
            
            
            
            
            
                

            
