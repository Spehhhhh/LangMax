import langdetect
import tiktoken

T = tiktoken.get_encoding("o200k_base")

length_dict = {}

for i in range(T.n_vocab):
    try:
        length_dict[i] = len(T.decode([i]))
    except:
        pass

# Sort by length
length_dict = dict(sorted(length_dict.items(), key=lambda item: -item[1]))

# Print the top 100 chinese words
tot = 0
for item in length_dict:
    try:
        if langdetect.detect(T.decode([item])) == "zh-cn":
            print(item, T.decode([item]))
            tot += 1
    except:
        pass
    if tot == 100:
        break
