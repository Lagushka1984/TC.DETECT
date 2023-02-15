from nomeroff_net import pipeline
from nomeroff_net.tools import unzip
from frametype import FrameType
from datetime import datetime
from buffer import Buffer

class TCdetect:
	pipeType: str = "number_plate_detection_and_reading"
	imageType: str = "opencv"
	buffer: list = []

	def __init__(self, fts: FrameType, zone):
		self.fts = fts
		self.zone = zone
		self.pipe = pipeline(self.pipeType, self.imageType)

	def __call__(self):
		frames = self.getframes()
		output = self.getzip(frames)
		output = self.gettext(output)
		output = self.getstr(output)
		return frames, output

	def gettext(self, output):
		(_, _, _, _, _, _, _, _, texts)  = unzip(output)
		result = []
		for text in texts:
			if len(text) != 0:
				text = text[0]
				if len(text) == 9:
					result += [text]
				else:
					result += ['']
			else:
				result += ['']
		return result

	def getzip(self, frames: list):
		return self.pipe(frames)
	
	def getstr(self, data: tuple) -> list:
		result = []
		for i in range(len(self.fts)):
			tc = data[i]
			tcs = [buffer.tc for buffer in self.buffer]
			if tc not in tcs:
				self.buffer += [Buffer(tc, 5)]
			else:
				for buffer in self.buffer:
					if buffer.tc == tc:
						buffer.amount += 1
						buffer.work += 1
					if buffer.amount >= buffer.repeat and buffer.tc != '':
						cam = self.fts[i].name
						now = datetime.now()
						time = now.strftime('%H:%M:%S')
						date = now.strftime('%d.%m.%Y')
						rst = f'{tc},{cam},{time},{date}\n'
						result += [rst]
						self.buffer.pop(self.buffer.index(buffer))
					elif buffer.work > buffer.amount and buffer.work > buffer.repeat:
						self.buffer.pop(self.buffer.index(buffer))
		return result

	def getframes(self) -> list:
		frames = []
		for ft in self.fts:
			frames += [ft()[self.zone[0]:self.zone[1], self.zone[2]:self.zone[3]]]
		return frames