def compress(chars):
    read=write=0
    while read < len(chars):
        chars[read], freq = char, 0
        while read < len(chars) and chars[read] == char:
            read+=1
            freq+=1
        chars[write]=char
        write+=1
        if freq > 1:
            for ch in str(freq):
                chars[write] = ch
                write+=1
    return write