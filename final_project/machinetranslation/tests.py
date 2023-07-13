from unittest import TestCase, main

from translator import englishToFrench, frenchToEnglish

class TestCaseTranslator(TestCase):

  def test_English_To_French_equal(self):
    """
      test english to france equal
    """
    self.assertEqual(englishToFrench('Hello'),'Bonjour')
  def test_English_To_French_not_equal(self):
    """
      test english to france not equal
    """
    self.assertNotEqual(englishToFrench('Hello'),'Hi')

  def test_French_To_english_equal(self):
    """
      test Frances to english equal
    """
    self.assertEqual(frenchToEnglish('Bonjour'),'Hi')
  def test_French_To_english_not_equal(self):
    """
      test Frances to english not equal
    """
    self.assertNotEqual(frenchToEnglish('Bonjour'),'hello')

if __name__ == '__main__':
    main()