from bintreeFile import Bintree
from LinkedQ import LinkedQ

def makechildren(startord):   #Skapar olika ordvariationer
    alfabetet = list("abcdefghijklmnopqrstuvwxyzåäö")
    children = []
    j = 0
    while j < len(startord):
        temp = list(startord)
        i = 0
        while i < len(alfabetet):
            temp[j] = alfabetet[i]
            if "".join(temp) in svenska:
                children.append("".join(temp))
            i += 1
        j += 1

    gamla = Bintree()
    gamla.put(startord)
    for child in children:
        if child not in gamla:
            gamla.put(child)
            print(child)
    return children

if __name__ == '__main__': # def main():
    startord = input("Välj ett startord" + "\n")
    slutord = input("Välj ett slutord" + "\n")

    svenska = Bintree()

    with open("word3.txt", "r", encoding="utf-8") as ordlista:
        for rad in ordlista:
            svenska.put(rad.strip())  # in i sökträdet
    # svenska.write()

    children = makechildren(startord)

    print("")