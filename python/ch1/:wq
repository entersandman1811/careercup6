import unittest

def is_unique(strg):
	if len(strg)>128:
	    return True
	indexes = [0 for _ in range(128)]
	
	for i in strg:
		if  indexes[ord(i) - 97 ] == -1:
			return False
		indexes[ord(i) - 97 ] = -1
	return True
	
class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
    # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
            # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
