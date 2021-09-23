class Node:
    # class för att skapa noder till min linkedQ kö

    def __init__(self, value):
        # håller koll på värdet (value) av noden samt referens till nästa (next) nod
        self.value = value
        self.next = None


class LinkedQ:

    def __init__(self):
        # håller koll på första och sista värdet i kön
        # värdet från början på första och sista är alltid None
        self.__first = None
        self.__last = None

    def isEmpty(self):
        # kollar om kön är tom
        if self.__first is None:
            # Returnerar True om den är tom
            return True
        else:
            # Returnerar False om den inte är tom
            return False

    def enqueue(self, startord):
        # Lägger till nytt objekt sist i kön
        stamfar = Node(startord)
        # Skapar en ny nod
        if self.__first is None:
            # Om listan är tom
            self.__first = stamfar
            self.__last = self.__first
            # Blir första och sista värdet i kön samma
        else:
            # Om listan innehåller någonting
            self.__last.next = new_node
            # Vi ändrar den sista nodens referens från None till vår nya nod
            self.__last = new_node
            # ersätter sista värdet i kön med vår nya nod

    def dequeue(self):
        # Tar bort den första noden i kön samt returnerar värdet
        if self.__first is not None:
            # Om listan inte är tom
            x = self.__first.value
            # Sparar första värdet i vår kö
            self.__first = self.__first.next
            # Ersätter första värdet med den nod som är näst först
            return x
            # Returnerar värdet på noden som vi tog bort


q = LinkedQ()
print(q.isEmpty())
