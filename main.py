from bintreeFile import Bintree
from LinkedQ import LinkedQ 

def makechildren(startord):  
    children = []
    alfabetet = "abcdefghijklmnopqrstuvwxyzåäö"
    barn = ""

    for bokstav1 in startord:
      for bokstav2 in alfabetet:
        barn = startord.replace(bokstav1,bokstav2)
        children.append(barn)
    return children


def main():
    startord = input("Välj ett startord"+ "\n")
    slutord = input("Välj ett slutord"+ "\n")

    svenska = Bintree()

    with open("word3.txt", "r", encoding="utf-8") as ordlista:
      for rad in ordlista:
          svenska.put(rad.strip())             # in i sökträdet

    #svenska.write()
    
    children = makechildren(startord)
    gamla = Bintree()
    for child in children:
      if child in svenska:
        if child not in gamla:
          gamla.put(child)
   # gamla.write()

    q = LinkedQ()
    while not q.isEmpty():
      nod = q.dequeue()
    makechildren(nod, q)

  
main()

