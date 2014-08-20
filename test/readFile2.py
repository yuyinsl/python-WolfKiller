#!/usr/bin/env python

import time
filePath=open("getGold.log",'r')

def test2():
        start = time.time()
        for line in filePath:
                uk=line.split(':')[1].strip(';')
        end = time.time()
        print end-start

if __name__ == "__main__":
        test2()
                 
