import unittest
from pyjulia import *

class TestPyJulia(unittest.TestCase):
    def test_pyjulia_functions(self):
        julia_module = pyjulia.Pyjulia("./example.jl")
        test_args = [2, 3, 4]
        
        
        sum_func = julia_module.call_func("add", test_args)

        self.assertEqual(sum_func, 9)

if __name__ == "__main__":
    unittest.main() 