#!/usr/bin/env python

import time
filePath=open("getGold.log",'r')

def test1():
	start =time.time()

	for line in filePath.readlines():
		uk=line.split(':')[1].strip(';')

	end = time.time()

	print end-start


if __name__ == "__main__":
	test1()
