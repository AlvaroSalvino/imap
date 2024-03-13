import json
import os
import folium
#import webview
from folium.plugins import TagFilterButton, FastMarkerCluster
from pymongo import MongoClient
from flask import Flask, redirect, request, flash, render_template, render_template_string
from selenium.webdriver.common.by import By

connection_string = "mongodb+srv://alvarosalvino:Dmxsfsqp%40159@imap.aznrbqq.mongodb.net/?authSource=admin"
client = MongoClient(connection_string)
db_connection = client["imapdb"]
print(db_connection)
collection = db_connection.get_collection("usercolecao")
print(collection)


search_filter = {"nome": "Alvaro"}
response = collection.find(search_filter)

for registry in response: print(registry)

app = Flask(__name__)
app.config['SECRET_KEY'] = "Ti-Malta"

#window = webview.create_window('Mapa de Polos Malta', app)





arquivos = os.listdir()
logado = False


@app.route('/')
def home():
    global logado
    logado = False
    return render_template("login.html")

@app.route('/user')
def user():
    if os.path.exists("C:\\Polos_Malta_Map\\output\\Mapa Polos Malta\\mapas.json"):
        global logado
        if logado == True:
            return render_template("usuario.html")
        if logado == False:
            return redirect('/')

@app.route('/mapolo')
def mapolo():
    global logado
    if logado == True:
        polo = []
        parceiro = []
        parceiro_local = []
        endereco = []
        keys = ('polo', 'parceiro', 'parceiro_local', 'endereco')
        polos_coordenadas = []
        with open("C:\\Polos_Malta_Map\\output\\Mapa Polos Malta\\mapas.json") as file:
            data = json.load(file)
            for i in data:
                polos_coordenadas.append({key: i[key] for key in keys})
                polo.append('polo')
                parceiro.append('parceiro')
                parceiro_local.append('parceiro_local')
                endereco.append('endereco')
        for polo_coordenada in polos_coordenadas:
            latitude, longitude = polo_coordenada['endereco'].split("{")[-1].split("{")[0].split()
            ipolo = polo_coordenada['polo']
            iparceiro = polo_coordenada['parceiro']
            iparceiro_local = polo_coordenada['parceiro_local']
            polo_coordenada['ipolo'] = str(ipolo)
            polo_coordenada['iparceiro'] = str(iparceiro)
            polo_coordenada['iparceiro_local'] = str(iparceiro_local)
            polo_coordenada['latitude'] = float(latitude)
            polo_coordenada['longitude'] = float(longitude)
            polo_coordenada['popup'] = str(ipolo+' '+iparceiro+' '+iparceiro_local)
        polos_mapa = folium.Map(location=[-5.1188834018636795, -42.803002102827975], zoom_start=5, control_scale=True,
                                world_copy_jump=True, no_wrap=True)
        folium.LayerControl().add_to(polos_mapa)
        for polo_coordenada in polos_coordenadas:
            coordenadas = (polo_coordenada['latitude'], polo_coordenada['longitude'])
            marcador = coordenadas
            folium.Marker(coordenadas, popup=polo_coordenada['popup'], tags=[marcador]).add_to(polos_mapa)


        TagFilterButton(marcador).add_to(polos_mapa)
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

    if logado == False:
        return redirect('/')

    # polos_mapa.add_child(folium.LatLngPopup()

@app.route("/login", methods=['POST'])
def login():
    global logado
    usuario = request.form.get('nome')
    senha = request.form.get('senha')
    teste = db.users.users.find({'nome'}, {'senha'})
    print(teste)
    lista = usuarios
    for c in usuarios:
        cont = 0
        for c in lista:
            cont+=1
            if usuario == c['nome'] and senha == c['senha']:
                logado = True
                return redirect('/user')
            if cont >= len(lista):
                flash('Usuáio Inválido')
                return redirect("/")


@app.route("/inserirpolo")
def inserirpolo():
    global logado
    if logado == True:
        return render_template("novopolo.html")
    if logado == False:
        return redirect('/')

@app.route("/novopolo", methods=['POST'])
def insere_instituicao():
    global logado
    if logado == True:
        polos = []
        polo = request.form.get('polo')
        parceiro = request.form.get('parceiro')
        parceiro_local = request.form.get('parceiro_local')
        endereco = request.form.get('endereco')
        polos = [
            {
                "polo": polo,
                "parceiro": parceiro,
                "parceiro_local": parceiro_local,
                "endereco": endereco
            }
        ]
        with open("C:\\Polos_Malta_Map\\output\\Mapa Polos Malta\\mapas.json") as mapas:
            mapa = json.load(mapas)

        mapaNovo = mapa + polos

        with open("C:\\Polos_Malta_Map\\output\\Mapa Polos Malta\\mapas.json", 'w') as gravarMapas:
            json.dump(mapaNovo, gravarMapas, indent=4)
            flash('Inserção bem sucedida')
        return render_template("novopolo.html")
    if logado == False:
        return redirect('/')


if __name__ == '__main__':
#    webview.start()
    app.run(debug=False)
