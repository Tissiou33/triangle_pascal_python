#Programme d'affichage du triangle de pascal

liste = [[1]]
def fonction():
    while True:
        try:
            nbr_ligne = int(input(" Entrer le nombre de ligne du triangle "))
        
            for k in range(nbr_ligne+1):
                new = [1]
                free = liste[-1]
                i=0
                #print(free)
                for z in range(2,k+1):
                    new.append(0)
                    if (z==k):
                        new[-1]=1
                        liste.append(new)
                        
                    if (z !=k and k >2): 
                        if (i<z and i< len(free)-1):
                            new[-1] = free[i]+free[i+1]
                    i +=1 
            return liste
                    
        except ValueError:
            print("Entrer un entier")
            
def execution ():
    reponse= "oui"
    valie = ["non","NON","Non","nOn"]
    while (reponse not in valie) :
        fonction()
        for l in liste :
            for el in l:
                print(el , end=" ")
            print("\n")
        reponse = input("Voulez vous reprendre ?")
        
execution()