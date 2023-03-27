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

        return hashsum # return 10 # to test collisions

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

        return currentNode.value
