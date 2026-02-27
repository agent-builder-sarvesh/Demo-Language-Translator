from flask import Flask, request, render_template
from datetime import date
from deep_translator import GoogleTranslator

app = Flask(__name__)
datetoday2 = date.today().strftime("%d-%B-%Y")

@app.route('/')
def home():
    return render_template('home.html', datetoday2=datetoday2, res='')

@app.route('/translate', methods=['POST'])
def translate():
    input_text = request.form['sourcetext']
    targetlang = request.form['languages']

    try:
        result = GoogleTranslator(source='auto', target=targetlang).translate(input_text)
    except Exception as e:
        result = f"Error: {e}"

    return render_template('home.html', datetoday2=datetoday2, res=result)

if __name__ == '__main__':
    app.run(debug=True, port=5900)