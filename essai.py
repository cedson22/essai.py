'''print("hello!")
a = [19,20,19,"malanda","malanda",19,20, "Cédric","Makosso","Cédric"]
print(a,len(a), sep='\n')
c= {"malanda":a.count("malanda"),"Cédric": a.count("Cédric"),"Makosso":a.count("Makosso"), 19:a.count(19),20:a.count(20) }

print(c.values(), c.keys(), sep='\n')
print("malanda".upper().count("A"))'''

def premier(n):
    """Cette fonction vérifie si l'entier n est premier ou non"""
    if n in range (2):
        return False
    else:
        for i in range (2,n):
            if (n % i) == 0:
                return False
    return True

'''x = int(input())
for i in range(2,x):
    if (premier(i) == True) :
        print(i)'''


def prime_numbers(nb):
    ''' Cette fonction permet de recevoir  un nombre entier nb et renvoie la liste des nb premiers nombres premiers.'''

    if type(nb) is int and nb >= 0:
        a = []
        i= 2
        while len(a) < nb :
            if premier (i)== True:
                a.append(i)
                i +=1
            else :
                i +=1
        return a
    else:
        c = 'None'
        return c


print(prime_numbers(-1))

# anagramme
def anagrammes(v, w):
    " Ce programme permet de savoir si v et w sont des annagramme"
    if len(v) != len(w):
        return 'False'
    else:
        for i in v:
            if i not in w:
                return 'False'
                break
            else:
                continue
            return 'True'

print(anagrammes('marion', 'romina'))
#%%
print('hello!')
