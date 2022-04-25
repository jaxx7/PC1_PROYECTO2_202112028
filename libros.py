libros =[
    {
        "id_book": "dlfkajs245adf",
        "book_author": "Miguel Asturias",
        "book_title": "Mi primer libro",
        "book_edition": 1,
        "book_editorial": "Pearson",
        "book_year": 2010,
        "book_description": "Una historia de suspenso...",
        "book_available_copies": 2,
        "book_unavailable_copies": 3,
        "book_copies": 5
    },
    {
        "id_book": "d58f7sd8f9ad8f5",
        "book_author": "Virgilio Mascal",
        "book_title": "Mi segundo libro",
        "book_edition": 2,
        "book_editorial": "Alba",
        "book_year": 2007,
        "book_description": "Una historia de acción...",
        "book_available_copies": 1,
        "book_unavailable_copies": 2,
        "book_copies": 3
    }
]


def validaLibro(posiblesDatos):

    error = []
    dato = {}

    try:
        posibleId= posiblesDatos["id_book"]
        if len(posibleId)>0:
            if existeID(posibleId):
                error.append('Id ya registrada')
            else:
                dato["id_book"] = posibleId
        else:
            error.append('El ID del libro no puede estar vacia')

    except KeyError:
        error.append('El ID del libro es requerida')

#iniciamos autor
    try:
        posibleId= posiblesDatos["book_author"]
        if len(posibleId)>0:
            if existeID(posibleId):
                error.append('author del libro ya registrado')
            else:
                dato["book_author"] = posibleId
        else:
            error.append('El author no puede estar vacio')

    except KeyError:
        error.append('El author es requerido')


#iniciamos titulo 
    try:
            posibleId= posiblesDatos["book_title"]
            if len(posibleId)>0:
                if existeID(posibleId):
                    error.append('El titulo del libro ya esta registrado')
                else:
                    dato["book_title"] = posibleId
            else:
                error.append('El titulo no puede estar vacio')

    except KeyError:
            error.append('El titulo es requerido')


#iniciamos edition
    try:
            posibleId= posiblesDatos["book_edition"]
           
            if existeID(posibleId):
                    error.append('Edicion del libro ya registrado')
            else:
                dato["book_edition"] = posibleId
           

    except KeyError:
            error.append('Laa edicion es requerida')

#iniciamos editorial
    try:
            posibleId= posiblesDatos["book_editorial"]
            if len(posibleId)>0:
                if existeID(posibleId):
                    error.append('Editorial del libro ya registrada')
                else:
                    dato["book_editorial"] = posibleId
            else:
                error.append('La Editorial no puede estar vacia')

    except KeyError:
            error.append('La Editorial es requerida')


#iniciamos año
    try:
            posibleId= posiblesDatos["book_year"]
            
            if existeID(posibleId):
                    error.append('El año del libro ya registrado')
            else:
                    dato["book_year"] = posibleId
    except KeyError:
            error.append('El año es requerido')



#iniciamos descripcion
    try:
            posibleId= posiblesDatos["book_description"]
            if len(posibleId)>0:
                if existeID(posibleId):
                    error.append('Descripcion del libro ya registrada')
                else:
                    dato["book_description"] = posibleId
            else:
                error.append('La Descripcion no puede estar vacia')

    except KeyError:
            error.append('La Descripcion es requerida')


#inciamos copias disponibles
    try:
            posibleId= posiblesDatos["book_available_copies"]
            
            if existeID(posibleId):
                    error.append('numero de copias ya registrado')
            else:
                    dato["book_available_copies"] = posibleId
    except KeyError:
            error.append('El numero de copias es requerido')

#iniciamos copias no disponibles
    try:
            posibleId= posiblesDatos["book_unavailable_copies"]
           
            if existeID(posibleId):
                    error.append('numero de copias ya registrado')
            else:
                    dato["book_unavailable_copies"] = posibleId
    except KeyError:
            error.append('El numero de copias es requerido')

#iniciamos copias 
    try:
            posibleId= posiblesDatos["book_copies"]
          
            if existeID(posibleId):
                    error.append('numero de copias ya registrado')
            else:
                    dato["book_copies"] = posibleId
    except KeyError:
            error.append('El numero de copias es requerido')

    if len(error) > 0:
        return [None, error]
    else:
        return [dato, None]

#ponemos si existe el ID
def existeID(id):
    posiblesIds = []
    for book in libros:
        try:
            posiblesIds.append(book['id_book'])
        except:
            pass

    return (id in posiblesIds)  




def ActualizarLibro(posiblesDatos):

    error = []
    try:
        ActualizaID= posiblesDatos["id_book"]
        if existeID(ActualizaID):

            updateData ={}

            try:
                updateData["book_author"] = posiblesDatos["book_author"]
            except KeyError:
                pass

            try:
                updateData["book_title"] = posiblesDatos["book_title"]
            except KeyError:
                pass

            try:
                updateData["book_editorial"] = posiblesDatos["book_editorial"]
            except KeyError:
                pass

            try:
                updateData["book_year"] = posiblesDatos["book_year"]
            except KeyError:
                pass

            try:
                updateData["book_description"] = posiblesDatos["book_description"]
            except KeyError:
                pass

            try:
                updateData["book_available_copies"] = posiblesDatos["book_available_copies"]
            except KeyError:
                pass

            try:
                updateData["book_unavailable_copies"] = posiblesDatos["book_unavailable_copies"]
            except KeyError:
                pass

            try:
                updateData["book_copies"] = posiblesDatos["book_copies"]
            except KeyError:
                pass

        for book in libros:
                if book['id_book'] == ActualizaID:
                    book.update(updateData)
                    return ['Modificado', error]
    except KeyError:
        error.append('El ID del libro es requerida')

        return ['', error]