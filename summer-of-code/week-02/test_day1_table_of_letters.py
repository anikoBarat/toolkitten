from day1_homework import letter_counter
import unittest


class TestLetterCounter(unittest.TestCase):
    def testLogicForA(self):

        container = letter_counter("testfile_for_letter_counter.txt")

        def testCounterLogicForLetterA(self):
            assertEquals(container["a"], 3)

        def testCounterLogicForLetterD(self):
            assertEquals(container["d"], 2)
        
        def testCounterLogicForLetterZ(self):
            assertEquals(container["z"], 1)
        
        def testInvalidStatement(self):
            assertNotEquals(container["a"], 23)


unittest.main()
