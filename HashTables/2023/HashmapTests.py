import unittest
from Hashmap import Hashmap
from unittest.mock import MagicMock


class HashmapTests(unittest.TestCase):

    def setUp(self):
        self.__sut = Hashmap()

    def test_add_insertsValue_Correctly(self):
        # arrange
        self.__sut.add('foo', 18)

        # act
        result = self.__sut.get('foo')

        # assert
        self.assertEqual(18, result)

    def test_add_updatesValue_Correctly(self):
        # arrange
        self.__sut.add('foo', 18)
        self.__sut.add('foo', 19)

        # act
        result = self.__sut.get('foo')

        # assert
        self.assertEqual(19, result)

        # assert
        self.__sut.add('foo', -100)
        result = self.__sut.get('foo')
        self.assertEqual(-100, result)

    def test_get_returnsValue_Correctly(self):
        # arrange
        self.__sut.add('foo', 18)

        # act
        result = self.__sut.get('foo')

        # assert
        self.assertEqual(18, result)

    def test_get_should_returnValue_Correctly_WhenCollisionsExists(self):

        # arrange
        self.__sut.hash = MagicMock(return_value=3)
        self.__sut.add('foo 1', 18)
        self.__sut.add('foo 2', 19)

        # act
        result = self.__sut.get('foo 2')

        # assert
        self.assertEqual(19, result)

    def test_delete_removesValue_Correctly_WhenCollisionExists_FirstCollision(self):

        # arrange
        self.__sut.hash = MagicMock(return_value=3)
        self.__sut.add('foo', 18)

        # act
        self.__sut.delete('foo')

        # assert
        with self.assertRaises(KeyError) as raises:
             self.__sut.get('foo')

    def test_delete_removesValue_Correctly_WhenCollisionExists_MiddleCollision(self):

        # arrange
        self.__sut.hash = MagicMock(return_value=3)
        self.__sut.add('foo1', 18)
        self.__sut.add('foo2', 19)
        self.__sut.add('foo3', -100)
        self.__sut.add('foo4', 1)

        # act
        self.__sut.delete('foo3')

        # assert
        with self.assertRaises(KeyError) as raises:
            self.__sut.get('foo3')

    def test_delete_removesValue_Correctly_WhenCollisionExists_LastCollision(self):

        # arrange
        self.__sut.hash = MagicMock(return_value=3)
        self.__sut.add('foo1', 18)
        self.__sut.add('foo2', 19)
        self.__sut.add('foo3', -100)
        self.__sut.add('foo4', 1)

        # act
        self.__sut.delete('foo4')

        # assert
        with self.assertRaises(KeyError) as raises:
            self.__sut.get('foo4')


if __name__ == '__main__':
    unittest.main()
