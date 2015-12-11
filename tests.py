import sys
import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.discover("./tests")
    unittest.TextTestRunner(verbosity=1).run(tests)
