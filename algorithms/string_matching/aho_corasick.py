class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end_of_word = False
        self.fallback = None
        self.parent = None


class Queue:
    def __init__(self):
        self.queue = []
        self.front = None
        self.rear = None
        self.n = 0

    def enqueue(self, element):
        if self.n == 0:
            self.front = 0
            self.rear = 0
        elif self.n > 0:
            self.rear += 1
        self.queue.append(element)
        self.n += 1

    def dequeue(self):
        if self.n == 0:
            print("Underflow")
            sys.exit()
        self.queue.pop(self.front)
        if self.n == 1:
            self.front = None
            self.rear = None
        elif self.n > 1:
            self.rear -= 1
        self.n -= 1


class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def char_to_index(self, character):
        return ord(character) - ord('a')

    def insert(self, key):
        current = self.root
        for char in key:
            index = self.char_to_index(char)
            if not current.children[index]:
                current.children[index] = self.get_node()
            current = current.children[index]
        current.is_end_of_word = True

    def fallbacks(self):
        que = Queue()
        for child in 
