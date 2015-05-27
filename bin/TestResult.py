class TestResult(object):


		def __init__(self, status, message):
			self.status = status
			self.message = message

		def status(self):
			return self.status

		def message(self):
			return self.message