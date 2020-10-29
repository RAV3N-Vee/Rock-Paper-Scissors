from random import randint
c={'rock':1, 'paper':2, 'scissors':3}
p=input('Your choice ')
p2=randint(1,4)
p1=p.lower()
d= c[p1]-p2
o=list(c.keys())[list(c.values()).index(2)]
if d==0:
    print(('TIE vs {}').format(o))
elif p1=='rock':
    if d==-1:
        print(('WIN vs {}').format(o))
    else:
        print((':( vs {}').format(o))
elif d==1:
        print(('WIN vs {}').format(o))
else:
    print((':( vs {}').format(o))
