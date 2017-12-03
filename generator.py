from collections import *
from random import random

def normalize(counter):
    s = float(sum(counter.values()))
    return [(c,cnt/s) for c,cnt in counter.items()]
      
def train_char_lm(filename, order=4):
    f = open(filename, "r")
    data = f.read()
    lm = defaultdict(Counter)
    pad = "~" * order # Prepend one or more '~' so we know how things start later.
    data = pad + data
    for i in range(len(data)-order):
        history, char = data[i:i+order], data[i+order]
        lm[history][char] += 1

    outlm = {hist:normalize(chars) for hist, chars in lm.items()}
    f.close()
    return outlm

#order = 10
#print("training the generator...", end="")
#lm = train_char_lm("repo.txt", order=order)
# lm = train_char_lm("sherlock.txt", order=order)
# lm = train_char_lm("icd10.txt", order=order)
# lm = train_char_lm("obamacare.txt", order=order)
#print("done!")

def generate_letter(lm, history, order):
    history = history[-order:]
    dist = lm[history]
    x = random()
    for c,p in dist:
        x = x - p
        if x <= 0: 
            return c

def generate_text(lm, order, num_letters=200):
    history = "~" * order
    out = []
    for i in range(num_letters):
        c = generate_letter(lm, history, order)
        history = history[-order:] + c
        out.append(c)
    return "".join(out)

#print(generate_text(lm, order))