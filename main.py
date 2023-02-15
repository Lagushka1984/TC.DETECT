from sys import argv
import cv2
import numpy as np
from nomeroff_net import pipeline
from nomeroff_net.tools import unzip

from frametype import *
from tcdetect import TCdetect

from time import time, sleep

def readConfig(path: str):
	with open(path) as config:
		frametypes = []
		debug = None
		zone = None
		dl = None
		objects = config.readlines()
		for obj in objects:
			mt, fn, nm = obj.split('=')
			if mt == 'debug':
				debug = eval(fn)
			if mt == 'image':
				frametypes += [ImageType(fn, nm.strip())]
			if mt == 'video':
				frametypes += [VideoType(fn, nm.strip())]
			if mt == 'rtps':
				frametypes += [RTPSType(fn, nm.strip())]
			if mt == 'xy':
				zone = eval(fn)
			if mt == 'time':
				dl = int(fn)
		return debug, frametypes, zone, dl

def main(ways: list, debug: bool, zone: tuple, dl: int):
	detect = TCdetect(ways, zone)
	while True:
		frames, rst = detect()
		if debug:
			print(rst)
			for i in range(len(ways)):
				cv2.imshow(ways[i].name, np.array(frames[i], dtype=np.uint8))
				if cv2.waitKey(1) == ord('q'):
					break
		with open('data.csv', 'a') as file:
			for rs in rst:
				file.write(rs)
		cv2.waitKey(dl)


if __name__ == '__main__':
	if len(argv) != 2:
		print('no config filename')
		exit(1)
	debug, ways, zone, dl = readConfig(argv[1])
	if len(ways) == 0:
		print('no video sources')
		exit(1)
	try:
		main(ways, debug, zone, dl)
	except Exception as e:
		print(e)
