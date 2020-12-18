def wordBreak(s, dict):
    seen=set()
    queue= collections.deque([s])

    for word in dict:
        if s.startswith(word):
            new_word=s[len(word):]
            if new_word=="":
                return True
            if new_word not in seen:
                queue.append(new_word)
                seen.add(new_word)
    return False