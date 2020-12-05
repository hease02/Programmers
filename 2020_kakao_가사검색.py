words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def reverse_string(string):
    return string[::-1]

class Node(object):
    def __init__(self, key, cnt=0):
        self.key = key
        self.cnt = cnt
        self.child = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head

        for char in word:
            if char not in cur.child:
                cur.child[char] = Node(char)

            cur.cnt += 1
            cur = cur.child[char]

        cur.cnt += 1

    def search(self, query):
        cur = self.head

        answer = 0

        for char in query:
            if char in cur.child:
                cur = cur.child[char]
            elif char is not "?":
                return 0

            if char is '?':
                answer = cur.cnt
                return answer

        return answer

def solution(words, queries):
    answer = [0 for _ in range(len(queries))]

    trie = [Trie() for _ in range(10001)]
    reverse_trie = [Trie() for _ in range(10001)]

    for word in words:
        trie[len(word)].insert(word)
        reverse_trie[len(word)].insert(reverse_string(word))

    for idx, query in enumerate(queries):
        if query.startswith('?'):
            query = reverse_string(query)
            answer[idx] = reverse_trie[len(query)].search(query)
        else:
            answer[idx] = trie[len(query)].search(query)

    return answer

print(solution(words, queries))