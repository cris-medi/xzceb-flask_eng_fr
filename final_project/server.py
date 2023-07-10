from machinetranslation.translator import frenchToEnglish, englishToFrench
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def routerEnglishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    print(textToTranslate)
    print(request.args.to_dict())
    # Write your code here
    return englishToFrench(textToTranslate)

@app.route("/frenchToEnglish")
def routerFrenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return frenchToEnglish(textToTranslate)

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
