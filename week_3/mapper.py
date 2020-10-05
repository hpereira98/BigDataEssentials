
import sys
import re


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

for line in sys.stdin:
    try:
        article_id, text = line.strip().split('\t', 1)
    except ValueError as e:
        continue
    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
    for word in words:
        eprint("reporter:counter:Wiki stats,Total words,%d" % 1)
        print("%s\t%d" % (word.lower(), 1))
