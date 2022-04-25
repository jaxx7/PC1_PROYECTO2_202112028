
usuarios =[
    {
        "id_user": "2df4e5f87r51d",
        "user_name": "Juan José Arevalo",
        "user_nickname": "juanjo",
        "user_password": "my_pasword123",
        "user_rol": "Estudiante",
        "available": True
    }
]

def validausuario(posiblesDatos):

    error = []
    dato = {}

    try:
        posibleId= posiblesDatos["id_user"]
        if len(posibleId)>0:
            if existeID(posibleId):
                error.append('Id ya registrada')
            else:
                dato["id_user"] = posibleId
        else:
            error.append('El ID de usuario no puede estar vacia')

    except KeyError:
        error.append('El ID de usuario es requerida')

#iniciamos nombre de usuario
    try:
        posibleId= posiblesDatos["user_name"]
        if len(posibleId)>0:
            if existeID(posibleId):
                error.append('Usuario ya registrado')
            else:
                dato["user_name"] = posibleId
        else:
            error.append('El Usuario no puede estar vacio')

    except KeyError:
        error.append('El usuario es requerido')

#nickname
   
    try:
        posibleId= posiblesDatos["user_nickname"]
        if len(posibleId)>0:
            if existeID(posibleId):
                error.append('nickname ya registrado')
            else:
                dato["user_nickname"] = posibleId
        else:
            error.append('El nickname de usuario no puede estar vacio')

    except KeyError:
        error.append('El nickname de usuario es requerido')

#contraseña

    try:
        posibleId= posiblesDatos["user_password"]
        if len(posibleId)>0:
            if existeID(posibleId):
                error.append('La contraseña ya registrada')
            else:
                dato["user_password"] = posibleId
        else:
            error.append('La contraseña de usuario no puede estar vacia')

    except KeyError:
        error.append('La contraseña de usuario es requerida')
    
#rol

    try:
        posibleId= posiblesDatos["user_rol"]
        if len(posibleId)>0:
            if existeID(posibleId):
                error.append('El rol ya esta registrado')
            else:
                dato["user_rol"] = posibleId
        else:
            error.append('El Rol de usuario no puede estar vacio')

    except KeyError:
        error.append('El Rol de usuario es requerido')


#available

    try:
        posibleId= posiblesDatos["available"]
    
        if existeID(posibleId):
                error.append('Estado ya registrado')
        else:
                dato["available"] = posibleId
       

    except KeyError:
        error.append('El Estado de usuario es requerido')

    if len(error) > 0:
        return [None, error]
    else:
        return [dato, None]


def existeID(id):
    posiblesIds = []
    for user in usuarios:
        try:
            posiblesIds.append(user['id_user'])
        except:
            pass

    return (id in posiblesIds)    

def Actualizarusuario(posiblesDatos):

    error = []
    try:
        ActualizaID= posiblesDatos["id_user"]
        if existeID(ActualizaID):

            updateData ={}

            try:
                updateData["user_name"] = posiblesDatos["user_name"]
            except KeyError:
                pass

            try:
                updateData["user_nickname"] = posiblesDatos["user_nickname"]
            except KeyError:
                pass

            try:
                updateData["user_password"] = posiblesDatos["user_password"]
            except KeyError:
                pass

            try:
                updateData["user_rol"] = posiblesDatos["user_rol"]
            except KeyError:
                pass

            try:
                updateData["available"] = posiblesDatos["available"]
            except KeyError:
                pass

        for user in usuarios:
                if user['id_user'] == ActualizaID:
                    user.update(updateData)
                    return ['Modificado', error]
    except KeyError:
        error.append('El ID de usuario es requerida')

        return ['', error]