''' Tests for basic commands and statements in PyBasic '''
import unittest
import sys
sys.path.append('../src/')
import PyBasic

class TestBasicCommands(unittest.TestCase):
    ''' Tests for basic commands and statements in PyBasic '''
    def test_print_statement_string(self):
        ''' Test if the output of PRINT is as expected '''

        command = 'PRINT "HELLO WORLD"'
        output = PyBasic.execute(command)
        self.assertEqual(output, 'HELLO WORLD')


if __name__ == '__main__':
    unittest.main()
