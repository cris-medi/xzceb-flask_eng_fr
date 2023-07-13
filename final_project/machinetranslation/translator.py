"""
traductor
"""
from deep_translator import MyMemoryTranslator

def englishToFrench(english_text):
    """
      function para traducir texto de ingles a frances
    """
    #write the code here
    french_text =  MyMemoryTranslator('en-US', 'fr-FR').translate(english_text)
    return french_text

def frenchToEnglish(french_text):
    """
      function para traducir texto de frances a ingles
    """
    #write the code here
    english_text =  MyMemoryTranslator('fr-FR', 'en-US').translate(french_text)
    return english_text
