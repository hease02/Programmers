import queue

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def reverse_string(string):
    return string[::-1]

class Node(object):
    def __init__(self, key, end=0, idx=0):
        self.key = key
        self.end = end
        self.idx = idx
        self.child = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None) #초기화

    def insert(self, word, idx):
        cur = self.head

        end_check = len(word)

        for n, char in enumerate(word):
            if char not in cur.child:
                if (n + 1) == end_check:
                    cur.child[char] = Node(char, end_check, idx)
                else:
                    cur.child[char] = Node(char)

            cur = cur.child[char]

    def search(self, word):
        cur = self.head

        word_size = len(word)

        que = queue.Queue()
        que.put(cur)

        while que.empty() is False:
            q = que.get()

            if char in q.child:
                q.put(q.child[char])
            if '?' in q.child:
                q.put(q.child['?'])

            if char not in q.child and '?' not in q.child:
                return False

            if q.end == word_size:

def solution(words, queries):
    answer = [0 for _ in range(len(queries))]

    trie = Trie()

    for idx, query in enumerate(queries):
        if query.startswith('?'):
            query = reverse_string(query)

        trie.insert(query, idx)

    for n, word in enumerate(words):
        trie.search(word)
        trie.search(reverse_string(word))


    return answer


print(solution(words, queries))
