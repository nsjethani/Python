import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # optimization step: for each word, we store all possible neighbours
        # i.e. for a word dog, 3 entires are created
        '''
        *og -> dog
        d*g -> dog
        do* -> dog
        '''
        if not beginWord or not endWord or not wordList:
            return None
        n = len(wordList[0])
        near_words = collections.defaultdict(list)
        for word in wordList:
            for i in range(n):
                near_words[word[0:i]+"*"+word[i+1:n]].append(word)
        q = []
        q.append((beginWord, 1))
        visited = {}
        visited[beginWord] = True
        while q:
            cur, l = q.pop(0)
            for i in range(n):
                near  = near_words[cur[0:i]+"*"+cur[i+1:n]]
                for word in near:
                    if word == endWord:
                        return l+1
                    if word not in visited:
                        q.append((word, l + 1))
                        visited[word] = True
                near_words[cur[0:i] + "*" + cur[i + 1:n]] = []
        return 0

l = ["hot","dot","dog","lot","log","cog"]
s=Solution()
print(s.ladderLength("hit","cog",l))