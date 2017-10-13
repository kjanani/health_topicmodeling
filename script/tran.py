#!/usr/bin/env python
#coding=utf-8
# Function: translate the results from BTM
# Input:
#    mat/pw_z.k20

import sys

# return:    {wid:w, ...}
def read_voca(pt):
    voca = {}
    for l in open(pt):
        wid, w = l.strip().split('\t')[:2]
        voca[int(wid)] = w
    return voca

# voca = {wid:w,...}
def read_topwords(pt, voca):
    k = 0
    for l in open(pt):
        vs = [float(v) for v in l.split()]
        wvs = zip(range(len(vs)), vs)
        wvs = sorted(wvs, key=lambda d:d[1], reverse=True)
        tmps = ' '.join(['%s:%f' % (voca[w], v) for w,v in wvs[:10]])
        print '%d|%s' % (k, tmps)
        k += 1

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: python %s <K>' % sys.argv[0]
        print '\tK is the number of topics'
        exit()
        
    K = int(sys.argv[1])
    data_dir = '../data/'
    voca_pt = data_dir + 'voca.txt'
    voca = read_voca(voca_pt)    
    W = len(voca)
    print 'K:%d, n(W):%d' % (K, W)

    zw_pt = data_dir + 'mat/pw_z.k%d' %  K
    read_topwords(zw_pt, voca)            
