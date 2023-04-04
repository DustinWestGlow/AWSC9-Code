import csv
import random

# count frequency of letters in ciphertext
# ciphertext = "uihjkcaldcbu" a.k.a. nonsense
ciphertext = ""
with open("ciphertext.txt") as reader:
    ciphertext = reader.read()
# {'a': 0, 'b': 0, ...}
abc = "".join([chr(x + ord('a')) for x in range(26)])
zeros = [0] * len(abc)
ctx_count = dict(zip(abc, zeros))
for c in ciphertext:
    if not c.isalpha():
        continue
    ctx_count[c.lower()] += 1
# {'a': 5, 'b': 14, ...}
# print(ctx_count)

# sort ciphertext letter frequencies (descending)
# R, S, F, I...
frequency_ciphertext = []
# https://stackoverflow.com/questions/4859292/how-can-i-get-a-random-key-value-pair-from-a-dictionary
# for sorting runs
for i in range(len(ctx_count)):
    # find most abundant letter
    abundant_letter = random.choice(list(ctx_count.keys()))
    for key in ctx_count:
        if ctx_count[key] >= ctx_count[abundant_letter]:
            abundant_letter = key
    # append it
    frequency_ciphertext.append(abundant_letter)
    # https://www.freecodecamp.org/news/python-remove-key-from-dictionary/
    # remove it and repeat for next highest letters
    del ctx_count[abundant_letter]
print(frequency_ciphertext)



# # unsorted list of english letters and their frequencies
eng_count = {}
# # https://docs.python.org/3/library/csv.html
with open('uns_eng_frq.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        # 'a': 0.08167
        letter = str(row[0]).lower()
        frequency = float(row[1])
        eng_count[letter] = frequency
# print(eng_count)
# sort ciphertext letter frequencies (descending)
# R, S, F, I...
frequency_english = []
# https://stackoverflow.com/questions/4859292/how-can-i-get-a-random-key-value-pair-from-a-dictionary
# for sorting runs
for i in range(len(eng_count)):
    # find most abundant letter
    abundant_letter = random.choice(list(eng_count.keys()))
    for key in eng_count:
        if eng_count[key] >= eng_count[abundant_letter]:
            abundant_letter = key
    # append it
    frequency_english.append(abundant_letter)
    # https://www.freecodecamp.org/news/python-remove-key-from-dictionary/
    # remove it and repeat for next highest letters
    del eng_count[abundant_letter]
print(frequency_english)

mapper = dict(zip(frequency_ciphertext, frequency_english))
print(mapper)







# # https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/#howtosortdatawiththesortedmethod
# # keep as list of tuples for our needs and purposes
# sorted_frequencies = sorted(uns_eng_frq) #, key=lambda x:x, reverse=True)
# with open("srt_eng_frq.csv", newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     for frq in sorted_frequencies:
#         writer.writerow([sorted_frequencies[0], sorted_frequencies[1]])

    

# for i in range(len(eng_freq)):
#     eng_freq[i] = eng_freq[i] * 100.0
# freq_mapper = []
# sorting_max = 0
# sorting_mapper = 0
# maxes = []
# for i in range(len(eng_freq)):
#     for j in range(len(eng_freq)):
#         if eng_freq[j]] >= sorting_max and j not in maxes:
#             sorting_max = eng_freq[j]
#             maxes.append(j)
#         freq_mapper.append(j)
#         sorting_mapper += 1


# # https://gist.github.com/randallmorey/dea827d6f1c48374bdea0d2f5a320a16
# # http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/

# # https://stackoverflow.com/questions/51804790/in-place-modification-of-python-lists
# #  frequencies [8.16, 1.49, 2.78, ...] for ['a', 'b', 'c', ...]

# cph_counter = [0] * (ord('z')-ord('a')+1)
# total_characters = 0
# for c in ciphertext:
#     if not c.isalpha():
#         continue
#     c = c.lower()
#     alp_map = ord(c) - ord('a')
#     cph_counter[alp_map] += 1
#     total_characters += 1
# for count in cph_counter:
#     cph_freq
# cph_freq = []


# frq_map = dict(zip(cph_freq, eng_freq))

# plaintext = ""
# print(eng_freq)
# # print(cph_freq)
# # print(frq_map)
# for c in ciphertext:
#     if not c.islower():
#         plaintext += c
#         continue
#     plaintext += frq_map[c]

# # print(plaintext)