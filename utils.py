#!/usr/bin/python3

import marshal
from snownlp.utils.frequency import AddOneProb
import gzip
from snownlp import sentiment, SnowNLP
import matplotlib.pyplot as plt

import os
from sys import platform
from datetime import datetime
import numpy as np

def download_moving(cookies, path='./inputs/msgs.txt'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if platform == "linux" or platform == "linux2":
        os.system("./shuoshuoLinux -c '%s' -t '%s'" % (cookies, path))    
    else:
        raise ValueError

def save_result(qq_msgs="./inputs/msgs.txt", path='./results/trend.png'):
    times = []
    sentences = []
    score = []
    with open(qq_msgs, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    plt.figure(0, figsize=(7, 5))

    for line in lines:
        if len(line.split('\t')) != 2:
            continue
        time_str, sentence = line.split('\t')
        time = int(time_str)
        s = SnowNLP(sentence)

        times.append(time)
        sentences.append(sentence)
        score.append(s.sentiments)

    
    
    var_x = np.linspace(times[0], times[-1], 10000)
    var_y = np.full(10000, 0.5)

    plt.plot(var_x, var_y, color='red')
    plt.plot(times, score)

    ticks = times[::20]
    plt.xticks(ticks, [datetime.fromtimestamp(t).strftime('%Y-%m-%d') for t in ticks])
    plt.ylabel("neg **************** pos")
    plt.yticks(())
    plt.tight_layout()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    plt.savefig(path)
    plt.close()