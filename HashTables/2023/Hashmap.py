from Node import Node


class Hashmap:

    def __init__(self, initialCapacity=100):
        self.count = 0
        self.__capacity = initialCapacity
        self.__list = [None] * self.__capacity
        self.__threshold = 0.7
        self.__capacityIncreaseFactor = 2

    def getCapacity(self):
        return len(self.__list)

    def hash(self, key: str) -> float:
        hashsum = 0

        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)  # Add (index + length of key) ^ (current char code)
            hashsum = hashsum % self.__capacity  # Perform modulus to keep hashsum in range [0, self.capacity - 1]

        return hashsum

    def __resizeIfNeeded(self) -> None:

        currentLoadFactor = self.count/self.__capacity

        if currentLoadFactor >= self.__threshold:

            # create new list with more capacity
            self.__capacity *= self.__capacityIncreaseFactor
            biggerList = [None] * self.__capacity

            # repoint current contents of the list to the bigger list
            for i, node in enumerate(self.__list):
                biggerList[i] = node

            # point list to our new biggerlist
            self.__list = biggerList

    def add(self, key: str, value: int) -> None:

        self.__resizeIfNeeded()

        hashedKey = self.hash(key)

        currentNode = self.__list[hashedKey]

        # when node exist add to end of linked list if not make a new one
        if currentNode is None:
            self.__list[hashedKey] = Node(key, value)
            self.count += 1
        else:

            # Go to the end of the linkedlist and append, except if it already exist udpate with new node
            while currentNode is not None:
                prev = currentNode

                # already exists
                if currentNode.key == key:
                    currentNode.value = value
                    return
                currentNode = currentNode.next

            prev.next = Node(key, value)
            self.count += 1

    def get(self, key: str) -> int:
        hashedKey = self.hash(key)
        currentNode = self.__list[hashedKey]

        if currentNode is None: raise KeyError('Key not found')

        while currentNode is not None:
            if currentNode.key == key: break
            currentNode = currentNode.next

        if currentNode is None: raise KeyError('Key not found')
        return currentNode.value

    def delete(self, key: str) -> None:
        hashedKey = self.hash(key)
        headNode = self.__list[hashedKey]

        # When trying to delete a non-existing key
        if headNode is None: raise KeyError('Key not found')

        currentNode = headNode

        # edge case: head node needs to be deleted
        if currentNode is not None and currentNode.key == key:

            # edge case: linkedlist of only 1 node
            if headNode.next is None:
                self.__list[hashedKey] = None
                self.count -= 1
                return

            # removing headnode and making next node the new headnode
            headNode = currentNode.next
            currentNode = None
            self.count -= 1
            return

        # removing when node is in the middle of the linked list
        while currentNode is not None:
            if currentNode.key == key:
                break
            prev = currentNode
            currentNode = currentNode.next

        # if key was not present in linked list
        if currentNode == None: return

        # Unlink the node from linked list and update linkedlist
        prev.next = currentNode.next

        currentNode = None
        self.count -= 1