
from flask import Flask , jsonify, request
from libros import ActualizarLibro, libros, validaLibro

app =Flask (__name__)

from usuarios import usuarios, validausuario, Actualizarusuario


#INSERTAR USUARIO

@app.route("/user", methods=['POST'])
def createUser():

    validationRes = validausuario(request.json)
    response = {}

    if validationRes[0]:
        usuarios.append(validationRes[0])
        response = {"msg": "Creado correctamente",
                    "status": 200}
    else:
        response = {"msg": "Error", "status": 400,
                    "errors": validationRes[1]}

    return jsonify(response)

#ACTUALIZAR USUARIO

@app.route("/user", methods=['PUT'])
def actualizarUser():

    actualizarusuario = Actualizarusuario(request.json)
    response = {}

    if actualizarusuario[0]:
        usuarios.append(actualizarusuario[0])
        response = {"msg": "Actualizado correctamente",
                    "status": 200}
    else:
        response = {"msg": "Error", "status": 400,
                    "errors": actualizarusuario[1]}

    return jsonify(response)

#VER USUARIOS

@app.route("/user/<string:id_user>")
def getUser(id_user):
    usuarioFound = [usuarios for usuarios in usuarios if usuarios['id_user'] == id_user]
    return jsonify({"user": usuarioFound[0]})

# @app.route("/user/<user_id>", methods=['GET'])
# def getUser(user_id):
#     response = {}

#     validationRes = searchUser(user_id)
#     if validationRes[0]:
#         response = validationRes[0]
#     else:
#         response = {"msg": "Informacion no encontrada", "status": 400}
#     return jsonify(response)


#CREAR LIBROS
@app.route("/book", methods=['POST'])
def createBook():

    validationRes = validaLibro(request.json)
    response = {}

    if validationRes[0]:
        libros.append(validationRes[0])
        response = {"msg": "Creado correctamente",
                    "status": 200}
    else:
        response = {"msg": "Error", "status": 400,
                    "errors": validationRes[1]}

    return jsonify(response)

#ACTUALIZAR LIBROS

@app.route("/book", methods=['PUT'])
def actualizarBook():

    actualizarlibro = ActualizarLibro(request.json)
    response = {}

    if actualizarlibro[0]:
        libros.append(actualizarlibro[0])
        response = {"msg": "Actualizado correctamente",
                    "status": 200}
    else:
        response = {"msg": "Error", "status": 400,
                    "errors": actualizarlibro[1]}

    return jsonify(response)

#VER LIBROS
@app.route("/book/<string:id_book>", methods=['GET'])
def getBook(id_book):
    bookFound = [libros for libros in libros if libros['id_book'] == id_book]
    return jsonify({"Libro": bookFound[0]})

#ELIMINAR LIBROS
@app.route("/book/<string:id_book>", methods=['DELETE'])
def deleteUser(id_book):
    bookFound = [libros for libros in libros if libros['id_book'] == id_book]
    if len(bookFound)> 0:
        libros.remove(bookFound[0])
        return jsonify({
            "msg": "Libro eliminado correctamente",
            "status": 200
        })

    return jsonify({"msg": "Libro no existe"})


# @app.route('/book', methods=['POST'])
# def addBook():
#     new_book = {
#         "isbn": request.json['isbn'],
#         "autor": request.json['autor'],
#         "title": request.json['title'],
#         "edition": request.json['edition'],
#         "year": request.json['year'],
#         "no_copies": request.json['no_copies'],
#         "no_available_copies": request.json['no_available_copies'],
#         "no_bookshelf": request.json['no_bookshelf'],
#         "no_bookshelf_row": request.json['no_bookshelf_row']
#     }
#     libros.append(new_book)
#     return jsonify({"message": "Libro agregado exitosamente", "libros": libros})

if __name__== '__main__':
    app.run(debug=True, port=4000)