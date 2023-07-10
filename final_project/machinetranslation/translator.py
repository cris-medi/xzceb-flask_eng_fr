from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    #write the code here
    frenchText =  MyMemoryTranslator('en-US', 'fr-FR').translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    englishText =  MyMemoryTranslator('fr-FR', 'en-US').translate(frenchText)
    return englishText
