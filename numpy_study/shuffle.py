import numpy as np

index = np.arange(20)
np.random.shuffle(index)
print(index[0:14])
print(index[14:16])
print(index[16:20])

a = [1,2,3]
b = [4,5,6]
c = np.vstack((a, b))
d = np.hstack((a, b))
print(c)
print(d)
np.random.shuffle(c)
print(c)

with open('words_set.txt', 'r', encoding='utf-8') as f:
    all_texts = [line.strip() for line in f.readlines()]

with open('labels_set.txt', 'r', encoding='utf-8') as f:
    all_labels = [line.strip() for line in f.readlines()]

index = [i for i in range(len(all_texts))]
np.random.shuffle(index)

x_train = [all_texts[i] for i in index]
y_train = [all_labels[i] for i in index]
