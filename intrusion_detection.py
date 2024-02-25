from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
import numpy as np
from matplotlib import pyplot as plt
import os

chunk_len = 10

def split_to_chunks(data, chunk_len):
    output = []
    for line in data:
        chunks = []
        for i in range(0, len(line), chunk_len):
            if i+chunk_len > len(line):
                chunks.append(line[i:len(line)] + line[0:i + chunk_len - len(line)])
            else:
                chunks.append(line[i:i+chunk_len])
        chunks[-1] += '\n'
        output.extend(chunks)
    return output

def process_train_data():
    data = np.loadtxt('syscalls/snd-cert/snd-cert.train', dtype='str')
    chunks = split_to_chunks(data, chunk_len)
    np.savetxt('syscalls/snd-cert/train_data.txt', chunks , fmt="%s")

def process_test_data():
    dir = 'syscalls/snd-cert/'
    for f in os.listdir(dir):
        if f.split('.')[-1] == 'test':
            data = np.loadtxt(os.path.join(dir,f), dtype='str')
            labels = np.loadtxt(os.path.join(dir, f[:-5] + '.labels'), dtype=int)
            data_zero = []
            data_one = []
            for i, label in enumerate(labels):
                if label == 0:
                    data_zero.append(data[i])
                elif label == 1:
                    data_one.append(data[i])
            chunks_zero = split_to_chunks(data_zero, chunk_len)
            chunks_one = split_to_chunks(data_one, chunk_len)
            np.savetxt('syscalls/snd-cert/test_data_0.txt', chunks_zero, fmt="%s")
            np.savetxt('syscalls/snd-cert/test_data_1.txt', chunks_one, fmt="%s")

process_train_data()
process_test_data()