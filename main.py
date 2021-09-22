from bintreeFile import Bintree

svenska = Bintree()

with open("word3.txt", "r", encoding="utf-8") as svenskfil:
    
    startord = input("Välj ett startord")
    slutord = input("Välj ett slutord")
    
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end=" ")
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")

gamla = Bintree()

with open("dumbarn.txt", "w", encoding="utf-8") as dumbarnsfil:
    for rad in dumbarnsfil:
        rad_list = rad.split(" ")
        for ordet in rad_list:
            if ordet not in gamla:
                gamla.put(ordet)
                if ordet in svenska:
                    print(ordet, end=" ")
