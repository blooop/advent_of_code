def readstrings(path: str):
    with open(path, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]
