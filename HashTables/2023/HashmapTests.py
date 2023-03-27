import unittest
from Hashmap import Hashmap


class HashmapTests(unittest.TestCase):

    def setUp(self):
        self.__sut = Hashmap()

    def test_get_returnsValue_Correctly(self):
        # arrange
        self.__sut.add('foo', 18)

        # act
        result = self.__sut.get('foo')

        # assert
        self.assertEqual(18, result)

    @unittest.skip("Need to change hash method to always return same value")
    def test_get_should_returnValue_Correctly_WhenCollisionsExists(self):
        # arrange
        self.__sut.add('foo 1', 18)
        self.__sut.add('foo 2', 19)

        # act
        result = self.__sut.get('foo 2')

        # assert
        self.assertEqual(19, result)

if __name__ == '__main__':
    unittest.main()
