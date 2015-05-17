#! /usr/bin/python
import unittest

class SiteParserTest(unittest.TestCase):


	def testTry(self):
		self.assertEqual('foo'.upper(), "FOO")
	

if __name__ == '__main__':
	unittest.main()