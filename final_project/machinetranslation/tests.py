from unittest import TestCase, main

from translator import englishToFrench, frenchToEnglish

class TestCaseTranslator(TestCase):

  def testEnglishToFrench(self):
    self.assertEqual(englishToFrench('Hello'),'Bonjour')
    self.assertNotEqual(englishToFrench('Hello'),'Hi')

    def testFrenchToenglish(self):
      self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
      self.assertNotEqual(frenchToEnglish('Bonjour'),'hello')

if __name__ == '__main__':
    main()