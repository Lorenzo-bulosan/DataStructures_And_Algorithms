from Node import Node


class Hashmap:

    def __init__(self):
        self.capacity = 100
        self.__list = [None] * self.capacity

    def hash(self, key: str) -> float:
        hashsum = 0

        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)  # Add (index + length of key) ^ (current char code)
            hashsum = hashsum % self.capacity  # Perform modulus to keep hashsum in range [0, self.capacity - 1]

        # return hashsum
        return 10

    def add(self, key: str, value: int) -> None:

        self.capacity += 1
        hashedKey = self.hash(key)

        currentNode = self.__list[hashedKey]

        # when node exist add to end of linked list if not make a new one
        if currentNode is None:
            self.__list[hashedKey] = Node(key, value)
        else:
            prev = currentNode

            while currentNode is not None:
                prev = currentNode
                currentNode = currentNode.next

            prev.next = Node(key, value)

    def get(self, key: str) -> int:
        hashedKey = self.hash(key)
        currentNode = self.__list[hashedKey]

        if currentNode is None: return None

        while currentNode is not None:
            if currentNode.key == key: break
            currentNode = currentNode.next

        if currentNode is None: return None
        return currentNode.value

    def delete(self, key: str) -> None:
        hashedKey = self.hash(key)
        headNode = self.__list[hashedKey]

        # When trying to delete a non-existing key
        if headNode is None: return

        temp = headNode

        # edge case: head node needs to be deleted
        if temp is not None and temp.key == key:

            # edge case: linkedlist of only 1 node
            if headNode.next is None:
                self.__list[hashedKey] = None
                return

            headNode = temp.next
            temp = None
            return

        # Search for the key to be deleted
        while temp is not None:
            if temp.key == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if temp == None: return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None
