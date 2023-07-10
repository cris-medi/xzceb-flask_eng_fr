from unittest import TestCase, main

from translator import englishToFrench, frenchToEnglish

class TestCaseTranslator(TestCase):

  def testEnglishToFrench(self):
    self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def testFrenchToenglish(self):
      self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

if __name__ == '__main__':
    main()