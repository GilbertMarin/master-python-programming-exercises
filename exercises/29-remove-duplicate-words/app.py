lines = ["hello", "world", "and", "practice", "makes", "perfect", "and", "hello", "world", "again"]

def deleteAndOrder(line):
    return sorted(set(line))


print(deleteAndOrder(lines))
