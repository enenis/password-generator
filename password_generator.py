import random

word_upper=["A","B","C","D"]
word_lower=["a","b","c","d"]
word_number=[1,2,3]


for i in range(4):
    q_list = [random.choice(word_upper+word_lower+word_number) for i in range(6)]
    print(q_list)
