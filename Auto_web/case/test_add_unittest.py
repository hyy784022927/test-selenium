import unittest


class IntegerArithmetiTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("打开")

    @classmethod
    def tearDownClass(self):
        print("关闭")

    # def setUp(self):
    #     print("打开")
    #
    # def tearDown(self):
    #     print("关闭")

    def testAdd(self):
        '''111111'''
        print("111111")
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMulitply(self):
        '''222222'''
        print("222222")
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)



if __name__ == '__main__':
    unittest.main()
