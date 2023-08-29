from flask import Flask, jsonify, request

app = Flask(__name__)

animes = [{
        'id': 1,
        'titulo': 'Naruto',
        'poster': 'https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx20-YJvLbgJQPCoI.jpg',
        'categoria': 'Action, Adventure',
        'rating': 0.79,
        'reviews': 491149,
        'season': '2002-2007',
        'tipo': 'TV Show'
    },
    {
        'id': 2,
        'titulo': 'Dragon Ball Super',
        'poster': 'https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx21175-EH06qlfF8TnB.jpg',
        'categoria': 'Action, Adventure',
        'rating': 0.72,
        'reviews': 144519,
        'season': '2015-2018',
        'tipo': 'TV Show'
    }
    
    ]  # Almacenar los datos de los animes en una lista.

# Ruta de la pagina principal
@app.route('/')
def index():
    return '¡Hola, mundo! Esta es mi primera API con Flask.'

# Ruta para obtener la lista de todos los animes (GET)
@app.route('/anime', methods=['GET'])
def animes_mostrar():
    return animes

# Ruta para crear un anime (POST)
@app.route('/anime', methods=['POST'])
def crear_anime():
    anime = {
        "id": int(request.form.get('id')),
        'titulo': request.form.get('titulo'),
        'poster': request.form.get('poster'),
        'categoria': request.form.get('categoria'),
        'rating': float(request.form.get('rating')),
        'reviews': int(request.form.get('reviews')),
        'season': request.form.get('season'),
        'tipo': request.form.get('tipo')
    }
    animes.append(anime)
    return jsonify("Anime agregado correctamente")

# Ruta para obtener un anime por su ID (GET)
@app.route('/anime/<int:id>', methods=['GET'])
def obtener_anime(id):  
    for anime in animes:
        if anime["id"] == int(id):
            return jsonify (anime)
    return jsonify("Anime no encontrado, AGREGALO!!")

# Ruta para eliminar un anime por su ID (DELETE)
@app.route('/anime/<int:id>', methods=['DELETE'])
def eliminar_anime(id):
    for anime in animes:
        if anime['id'] == id:
            animes.remove(anime)
            return jsonify("Anime eliminado exitosamente")
    return jsonify("Anime no encontrado")

# Ruta para actualizar un anime por su ID (PUT)
@app.route('/anime/<int:id>', methods=['PUT'])
def actualizar_anime(id):
    for anime in animes:
        if anime["id"] == id:
            anime["titulo"] = request.form.get("titulo")
            anime["poster"] = request.form.get("poster")
            anime["categoria"] = request.form.get("categoria")
            anime["rating"] = float(request.form.get("rating"))
            anime["reviews"] = int(request.form.get("reviews"))
            anime["season"] = request.form.get("season")
            anime["tipo"] = request.form.get("tipo")
            return jsonify("Actualizado correctamente")
    return jsonify("Anime no encontrado")


# Ruta para actualizar parcialmente por su ID (PATCH)
@app.route("/anime/<int:id>", methods=["PATCH"])
def actualizar_parcialmente(id):
    for anime in animes:
        if anime["id"] == id:
            if request.form.get("titulo") != None:
                anime["titulo"] = request.form.get("titulo")
            if request.form.get("poster") != None:
                anime["poster"] = request.form.get("poster")
            if request.form.get("cateforia") != None:
                anime["categoria"] = request.form.get("categoria")
            if request.form.get("ratings") != None:
                anime["rating"] = float(request.form.get("rating"))
            if request.form.get("reviews") != None:
                anime["reviews"] = int(request.form.get("reviews"))
            if request.form.get("seasons") != None:
                anime["season"] = request.form.get("season")
            if request.form.get("tipo") != None:
                anime["tipo"] = request.form.get("tipo")
            return jsonify("Actualizado correctamente") 
if __name__ == '__main__':
    app.run(debug=True)
