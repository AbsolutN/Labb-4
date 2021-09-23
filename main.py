""" Uppgift 1 """

from bintreeFile import Bintree
from LinkedQ import LinkedQ

svenska = Bintree()

with open("word3.txt", "r", encoding="utf-8") as ordlista:
    
    startord = input("Välj ett startord")
    slutord = input("Välj ett slutord")
    
    for rad in ordlista :
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end=" ")
        else:
            svenska.put(ordet)             # in i sökträdet
     makechildren(startord)
print("\n")

def makechildren(startord):
    # makechildren ska systematiskt gå igenom alla sätt att byta ut en bokstav i startordet (aöt, böt, ..., söö), kolla att det nya ordet finns i
    # ordlistan men inte finns i gamla och i så fall skriva ut det nya ordet på skärmen och lägga in det i gamla.
    
    children = []
    alfabetet = "abcdefghijklmnopqrstuvwxyzåäö"
    barn = ""
    for bokstav in startord:
        while bokstav != (lfabet.find(bokstav)-1)
            index = (alfabet.find(bokstav)+1) % 29
            barn = barn + startord.replace(bokstav,alfabet[index])
            return barn
        children = children.append(barn)
    return children


class Node(object):        
    def __init__(self, stamfar, currency=1, parent=None):
        # problemträdsobjekt
        self.amount = amount          # belopp
        self.currency = currency      # valuta, SEK, USD,...
        self.parent = None            # förälderpekare

def makechildren(node):
   # Skapar barn och lägger dom i kön


#Inläsning av växlingskurserna 
q = LinkedQ()
urmoder = Node() 
q.enqueue(urmoder)
try:
    while not q.isEmpty():
        node = q.dequeue()
        makechildren(node)
        # I makechildren görs "raise Klar(kedja)"
    print("Ingen lönsam växling")
except Klar as k: 
    print("Växla fort:", k)



# if det finns en väg en väg till ordet: 
#    print("Det finns en väg till ordet")
# else:
#    print ("Det finns inte en väg till ordet")






gamla = Bintree()

with open("dumbarn.txt", "w", encoding="utf-8") as dumbarnsfil:
    for rad in dumbarnsfil:
        rad_list = rad.split(" ")
        for ordet in rad_list:
            if ordet not in gamla:
                gamla.put(ordet)
                if ordet in svenska:
                    print(ordet, end=" ")
