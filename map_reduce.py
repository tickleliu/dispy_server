# -*- coding:utf-8 -*-
""" 
@author:mlliu
@file: map_reduce.py 
@time: 2018/07/17 
"""


# a version of word frequency example from mapreduce tutorial

def mapper(doc):
    # input reader and map function are combined
    import os
    import time
    words = []
    time.sleep(50)
    with open(os.path.join('/home/liuml/workspace/dispydemo', doc)) as fd:
        for line in fd:
            words.extend((word.lower(), 1) for word in line.split() \
                         if len(word) > 3 and word.isalpha())
    return words


def reducer(words):
    # we should generate sorted lists which are then merged,
    # but to keep things simple, we use dicts
    word_count = {}
    for word, count in words:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += count
    # print('reducer: %s to %s' % (len(words), len(word_count)))
    return word_count


if __name__ == '__main__':
    import dispy, logging

    # assume nodes node1 and node2 have 'doc1', 'doc2' etc. on their
    # local storage, so no need to transfer them
    map_cluster = dispy.JobCluster(mapper, nodes=["serverx41", "serverx42", "serverx44", "serverx43"], secret='secret',
                                   reentrant=True, ping_interval=10, pulse_interval=10)
    # any node can work on reduce
    reduce_cluster = dispy.JobCluster(reducer, nodes=["serverx41", "serverx42", "serverx44", "serverx43"],
                                      secret='secret', reentrant=True, pulse_interval=10)
    map_jobs = []
    for f in ['client.py', 'fabfile.py', 'host.py', 'server.py']:
        job = map_cluster.submit(f)
        map_jobs.append(job)
    reduce_jobs = []
    for map_job in map_jobs:
        words = map_job()
        if not words:
            print(map_job.exception)
            continue
        # simple partition
        n = 0
        while n < len(words):
            m = min(len(words) - n, 1000)
            reduce_job = reduce_cluster.submit(words[n:n + m])
            reduce_jobs.append(reduce_job)
            n += m
    # reduce
    word_count = {}
    for reduce_job in reduce_jobs:
        words = reduce_job()
        if not words:
            print(reduce_job.exception)
            continue
        for word, count in words.items():
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += count
    # sort words by frequency and print
    for word in sorted(word_count, key=lambda x: word_count[x], reverse=True):
        count = word_count[word]
        print(word, count)
    reduce_cluster.print_status()
