""" Uppgift 1 """

from bintreeFile import Bintree
from LinkedQ import LinkedQ 


def main():
    startord = input("Välj ett startord"+ "\n")
    slutord = input("Välj ett slutord"+ "\n")

    svenska = Bintree()

    with open("word3.txt", "r", encoding="utf-8") as ordlista:
      for rad in ordlista :
          ordet = rad.strip()            # Ett trebokstavsord per rad
          svenska.put(ordet)             # in i sökträdet
    makechildren(startord)

def makechildren(startord):
    # makechildren ska systematiskt gå igenom alla sätt att byta ut en bokstav i startordet (aöt, böt, ..., söö), kolla att det nya ordet finns i
    # ordlistan men inte finns i gamla och i så fall skriva ut det nya ordet på skärmen och lägga in det i gamla.
    
    children = []
    alfabetet = "abcdefghijklmnopqrstuvwxyzåäö"
    barn = ""

    for bokstav in startord:
      pre_bokstavsindex = int(alfabetet.find(bokstav)-1)
      peri_bokstavsindex = int(alfabetet.find(bokstav))
      while peri_bokstavsindex != pre_bokstavsindex:
          index = (alfabetet.find(bokstav)+1) % 29
          barn = barn + startord.replace(bokstav,alfabetet[index])
          return barn
      children = children.append(barn)
    return children


class Node():        
   def __init__(self, stamfar):
        # problemträdsobjekt
        self.stamfar = startord       
        self.parent = None            # förälderpekare


# if det finns en väg en väg till ordet: 
#    print("Det finns en väg till ordet")
# else:
#    print ("Det finns inte en väg till ordet")





# gamla = Bintree()

# with open("dumbarn.txt", "w", encoding="utf-8") as dumbarnsfil:
#     for rad in dumbarnsfil:
#         rad_list = rad.split(" ")
#         for ordet in rad_list:
#             if ordet not in gamla:
#                 gamla.put(ordet)
#                 if ordet in svenska:
#                     print(ordet, end=" ")
