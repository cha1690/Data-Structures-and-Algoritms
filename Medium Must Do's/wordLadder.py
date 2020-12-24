def ladder(beginWord,endWord,wordList):
    setWordList = set(wordList)
    queue = collections.deque([(beginWord,1)])

    while queue:
        word, count = queue.popLeft()

        if word == endWord:
            return count

        for i in range(len(word)):
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                newWord = word[:i]+letter+word[i+1:]

                if newWord in setWordList:
                    setWordList.remove(newWord)
                    queue.append((newWord,count+1))

    return 0