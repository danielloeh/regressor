class TestCase(object):

	def __init__(self, name, url, height, width, waitInMs):
		self.name = name
		self.url = url
		self.width = width
		self.height = height
		self.waitInMs = waitInMs


	def name(self):
		return self.name

	def url(self):
		return self.url

	def width(self):
		return self.width

	def height(self):
		return self.height

	def waitInMs(self):
		return self.waitInMs