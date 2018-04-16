class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end_of_word = False
        self.fallback = None
        self.parent = None
        self.word_list = []


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
        element = self.queue.pop(self.front)
        if self.n == 1:
            self.front = None
            self.rear = None
        elif self.n > 1:
            self.rear -= 1
        self.n -= 1
        return element


class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def char_to_index(self, character):
        return ord(character) - ord('a')

    def make_trie(self, key):
        current = self.root
        for char in key:
            index = self.char_to_index(char)
            if not current.children[index]:
                current.children[index] = self.get_node()
                current.children[index].parent = current
            current = current.children[index]
        current.is_end_of_word = True
        current.word_list.append(key)

    def fallbacks(self):
        que = Queue()
        not_none_children = (child for child in self.root.children if child is not None)
        for child in not_none_children:
            child.fallback = self.root
            que.enqueue(child)
        while(len(que.queue) != 0):
            element = que.dequeue()
            child_gen = (child for child in element.children if child is not None)
            if child_gen:
                for child in child_gen:
                    child_index = element.children.index(child)
                    fallback_node = element.fallback
                    while fallback_node is not None:
                        if fallback_node.children[child_index] is not None:
                            child.fallback = fallback_node.children[child_index]
                            if len(child.fallback.word_list) > 0:
                                child.word_list.append(*child.fallback.word_list)
                            que.enqueue(child)
                            break
                        else:
                            fallback_node = fallback_node.fallback
                    if fallback_node is None:
                        child.fallback = self.root
                        que.enqueue(child)

    def matching(self, text):
        match_dict = {}
        text_length = len(text)
        position = 0
        current = self.root
        while position < text_length:
            char = text[position]
            index = self.char_to_index(char)
            if current.children[index]:
                current = current.children[index]
                if len(current.word_list) > 0:
                    for word in current.word_list:
                        if word not in match_dict:
                            match_dict[word] = 1
                        else:
                            match_dict[word] += 1
                position += 1
            else:
                if current.fallback == None:
                    position += 1
                else:
                    current = current.fallback
        return match_dict


def main():  #make trie for the keys to be matched to the text
    trie = Trie()
    trie.make_trie("a")
    trie.make_trie("ab")
    trie.make_trie("bc")
    trie.make_trie("aab")
    trie.make_trie("aac")
    trie.make_trie("bd")
    trie.fallbacks()

    text = input("Enter text: ")
    # text = "bcaaab"
    print(trie.matching(text))


if __name__ == "__main__":
    main()
