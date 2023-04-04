from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)
openai.api_key = 'Agregar mi API Key'
conversacion = []

@app.route('/', methods= ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.form['pregunta']:
        pregunta = 'Yo: ' + request.form['pregunta']
         

        response = openai.Completion.create(
             engine = 'text-davinci-003',
             prompt = pregunta,
            temperature = 0.5,
            max_token = 150,
            top_p = 1,
            frecuency_penalty = 0,
            presence_penalty = 0.6,
        )

        respuesta = 'AI' + response.choices[0].text.strip()
        conversacion.append(pregunta)
        conversacion.append(respuesta)

        return render_template('index.html', chat= conversacion)
    
    else:
        return render_template('index.html')

    
if __name__ == '__main__':
    app.run(debug=True, port=5000)