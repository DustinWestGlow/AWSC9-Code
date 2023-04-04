import csv


ciphertext = ""
with open("ciphertext.txt") as reader:
    ciphertext = reader.read()



# unsorted list of english letters and their frequencies
uns_eng_frq = []
# https://docs.python.org/3/library/csv.html
with open('uns_eng_frq.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        # 'a': 0.08167
        letter = str(row[0]).lower()
        frequency = float(row[1])
        obj = {
            letter: frequency
        }
        uns_eng_frq.append(obj)
print(uns_eng_frq)
# https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/#howtosortdatawiththesortedmethod
# keep as list of tuples for our needs and purposes
sorted_frequencies = sorted(uns_eng_frq) #, key=lambda x:x, reverse=True)
with open("srt_eng_frq.csv", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for frq in sorted_frequencies:
        writer.writerow([sorted_frequencies[0], sorted_frequencies[1]])

    

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