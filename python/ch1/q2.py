import unittest

def check_perm(str1, str2):
    idx = [0 for _ in range(128)]
    for i in str1:
        idx[ord(i)] +=1
                   
    for i in str2:
        if idx[ord(i)] == 0:
            return False
        idx[ord(i)] -=1
    return sum(idx) == 0 


class Test(unittest.TestCase):
    dataT  = [("abba", "abab")]
    dataF  = [("abab", "b")]

    
    def test_perm(self):

        for t in self.dataT:
            actual = check_perm(*t)
            self.assertTrue(actual)

        for f in self.dataF:
            actual = check_perm(*f)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
