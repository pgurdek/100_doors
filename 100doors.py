dooropened = 0
tab = [0] * 100


def Hunder_Doors(steps):
    for i in range(steps, len(tab),steps+1):
        if tab[i] == 0:
            tab[i] = 1
        elif tab[i] == 1:
            tab[i] = 0
    #print('Krok',steps,'Following doors are open:', tab)


for i in range(0,100,1):
    Hunder_Doors(i)


print('Otwarte drzwi to:')
for n,i in enumerate(tab):
    if i == 1:
        print(n+1,end=' ')
        dooropened +=1


print('\nDoors which are opened: ',dooropened)
