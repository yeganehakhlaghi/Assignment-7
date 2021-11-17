import random
boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
result=[]
for i in range(len(boys)):
    g=random.choice(girls)
    b=random.choice(boys)
    boys.remove(b)
    girls.remove(g)
    marrid=[b,g]
    result.append(marrid)

print(result)
