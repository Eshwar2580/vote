import unittest
from vote import vote
class testgrade(unittest.TestCase):
    def vt(self):
        self.assertEqual(vote(20),'Eligible for Voting!')
    def vt(self):
        self.assertEqual(vote(16),'Not Eligible for Voting!')


if __name__=='__main__':
    unittest.main()