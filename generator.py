import random
'''
You have x clones and you all play. You can choose between 10€ and 1000€.
If multiple players pick 1000€ noone gets 1000€ but everyone who picked 10€ gets 10€.
But If only 1 player picks 1000€ gets their payout.
All of you think the same and can't communicate but you're allowed to use rng
'''

def ranumb(x):
    return (random.randint(1,x))
clones=int (input("How many players? "))
runs=int (input("How many tests? "))
chance=int (input("How many possible outputs? "))
happened=False
occurences=0
no_occurences=0
avg_gain=0
arr=[]
for i in range (0, runs):
    for k in range (0, clones):
        double=0
        a=ranumb(chance)
        arr.append(a)
        for j in range (len(arr)):
            if arr[j]==1:
                double=double+1
            if double>=2:
                happened=True
    if happened==True:
        occurences=occurences+1
    elif  double==0:
        no_occurences=no_occurences+1
    happened=False
    if double==1:
        avg_gain=(avg_gain+(((1000+10*(clones-1))-avg_gain)/(i+1)))
    else:
        avg_gain=(avg_gain+(((+10*(clones-double))-avg_gain)/(i+1)))

    arr.clear()
    double=0

print("Times you lost: " + str(occurences))
print("success rate: "+ str(round((100-((no_occurences+occurences)/runs)*100),3))+ "%")
print("low success rate: "+ str(round(((no_occurences)/runs)*100,3))+ "%")
print("failure rate: "+ str(round(((occurences)/runs)*100,3))+ "%")
print("average win: "+ str(round(avg_gain,2)) + "€")