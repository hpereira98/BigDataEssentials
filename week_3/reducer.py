
import sys

current_key = None
word_sum = 0

for line in sys.stdin:
    try:
        key, count = line.strip().split('\t', 1)
        count = int(count)
    except ValueError as e:
        continue
    if current_key != key:
        if current_key:
            print("%s\t%d" % (current_key, word_sum))
        word_sum = 0
        current_key = key
    word_sum += count

if current_key:
    print("%s\t%d" % (current_key, word_sum))
