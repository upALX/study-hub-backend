import pathlib
from collections import Counter

entries = pathlib.Path("../uses").iterdir()
print('Entries path: ', entries)

extensions = [entry.suffix for entry in entries if entry.is_file()]

print(extensions)

print(Counter(extensions))