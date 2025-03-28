import unittest
from mathmanager import mathmanager

class mathmanagertest(unittest.TestCase):
	def testAdd(self):
		math = mathmanager()
		self.assertEqual(math.add(0, 3), 3)

	def testSubtract(self):
		math = mathmanager()
		self.assertEqual(math.subtract(0, 3), -3)

	def testMultiply(self):
		math = mathmanager()
		self.assertEqual(math.multiply(0, 3), 0)

	def testInterest(self):
		math= mathmanager()
		self.assertEqual(math.interest (1000, 1), 3)

	def testInterest1(self):
		math= mathmanager()
		self.assertEqual(math.interest (1000, 2), 3)

	def testInterest2(self):
		math= mathmanager()
		self.assertEqual(math.interest (1000, 3), -2)

#run test to show where it may fail, use all possible values for a particular function.
