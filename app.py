import json
import os
import folium
#import webview
from folium.plugins import TagFilterButton
from geopy.geocoders import Bing
from pymongo import MongoClient
from flask import Flask, redirect, request, flash, render_template, render_template_string, session


app = Flask(__name__)
app.config['SECRET_KEY'] = "Ti-Malta"
client = MongoClient('mongodb+srv://alvarosalvino:gruPzOlFAW1BfADK@imap.aznrbqq.mongodb.net/?retryWrites=true&w=majority&appName=imap')
db = client['imapdb']
collection = db['usercolecao']

#window = webview.create_window('Mapa de Polos Malta', app)

logado = False


@app.route('/')
def home():
    session['logado'] = False
    return render_template("login.html")


@app.route('/user')
def user():
    if 'logado' in session and session['logado'] == True:
        return render_template("usuario.html")
    else:
        return redirect('/')

@app.route('/mapolo')
def mapolo():
    if 'logado' in session and session['logado'] == True:
        polos_coordenadas = list(db['mapacolecao'].find())
        polos_mapa = folium.Map(location=[-5.1188834018636795, -42.803002102827975], zoom_start=5, control_scale=True,
                                world_copy_jump=True, no_wrap=True)
        folium.LayerControl().add_to(polos_mapa)
        tags = []
        for polo_coordenada in polos_coordenadas:
            latitude, longitude = map(float, polo_coordenada['endereco'].split())
            coordenadas = (latitude, longitude)
            polo_coordenada['popup'] = str(polo_coordenada['polo']+' '+polo_coordenada['parceiro']+' '+polo_coordenada['parceiro_local'])
            tags.extend([polo_coordenada['polo'], polo_coordenada['parceiro'], polo_coordenada['parceiro_local']])
            folium.Marker(coordenadas, popup=polo_coordenada['popup'], tags=[polo_coordenada['polo'], polo_coordenada['parceiro'], polo_coordenada['parceiro_local']]).add_to(polos_mapa)

        tags.sort()  # Ordena as tags em ordem alfabética
        TagFilterButton(tags).add_to(polos_mapa)
        polos_mapa.get_root().render()
        header = polos_mapa.get_root().header.render()
        body_html = polos_mapa.get_root().html.render()
        script = polos_mapa.get_root().script.render()
        return render_template_string(
            """
                <!DOCTYPE html>
                <html>
                    <head>
                        {{ header|safe }}
                    </head>
                    <body>
                        {% include "models/model-header-mapa.html" %}
                        {{ body_html|safe }}
                        <script>
                            {{ script|safe }}
                        </script>
                    </body>
                </html>
            """,
            header=header,
            body_html=body_html,
            script=script,
        )

    else:
        return redirect('/')


@app.route("/login", methods=['POST'])
def login():
    usuario = request.form.get('nome')
    senha = request.form.get('senha')
    usercolecao = collection.find_one({'nome': usuario, 'senha': senha})
    print(collection.find_one())
    if usercolecao:
        session['logado'] = True
        return redirect('/user')
    else:
        flash('Usuário Inválido')
        return redirect("/")

@app.route("/inserirpolo", methods=['GET', 'POST'])
def inserirpolo():
    if 'logado' in session and session['logado'] == True:
        if request.method == 'POST':
            polo = request.form.get('polo')
            parceiro = request.form.get('parceiro')
            parceiro_local = request.form.get('parceiro_local')
            endereco = request.form.get('endereco')
            novo_polo = {"polo": polo, "parceiro": parceiro, "parceiro_local": parceiro_local, "endereco": endereco}
            db['mapacolecao'].insert_one(novo_polo)
            return redirect('/user')
        else:
            return render_template("novopolo.html")
    else:
        return redirect('/')


@app.route("/novopolo", methods=['GET', 'POST'])
def insere_instituicao():
    if 'logado' in session and session['logado'] == True:
        if request.method == 'POST':
            geolocator = Bing(api_key="Al-_22HyOgNBpnd_1y9JqJB82qwqya-LHAfkvtszL6HT6gUuxc8C-Khq9whz63IQ")
            polo = request.form.get('polo')
            parceiro = request.form.get('parceiro')
            parceiro_local = request.form.get('parceiro_local')
            cidade = request.form.get('cidade')
            location = geolocator.geocode(cidade)
            endereco = f"{location.latitude} {location.longitude}"
            novo_polo = {
                "polo": polo,
                "parceiro": parceiro,
                "parceiro_local": parceiro_local,
                "endereco": endereco
            }
            db['mapacolecao'].insert_one(novo_polo)
            flash('Inserção bem sucedida')
        return render_template("novopolo.html")
    else:
        return redirect('/')



if __name__ == '__main__':
#    webview.start()
    app.run(debug=False)
