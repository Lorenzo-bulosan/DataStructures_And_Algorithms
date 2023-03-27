class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return "Node: (%s, %s) -> Node: %s>" % (self.key, self.value, self.next is not None)

    def __repr__(self):
        return str(self)
