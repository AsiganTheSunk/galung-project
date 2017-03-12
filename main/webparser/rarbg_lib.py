#!/usr/bin/python

#from magnet2torrent import m2t_create
#from simple_torrent_client import st_client

# Load configuration File, Default Url, ProxyList
# "For Updating"

# "<Default Url>" = https://www.rarbg.to/torrents.php?search=

def rarbg_request_constructor (title, season, episode):
    r = (title.replace(" ","%20") + '%20S'+ season + 'E' + episode)
    print r
    return (r)

def rarbg_search (url):
    r = requests.get (url, verify=True)
    return (r)

def rarbg_parser (content):
    soup = BeautifulSoup (content.text, "html.parser")
    table = soup.findAll('table', {"class":"lista2t"})

    myMagnetList = []
    mySeedList = []
    myLeechList = []
    mySizeList = []
    myNameList = []

    for row in table:
        data_name = 
        for name in data_name:
            myNameList.append()
            
# Devuelve todo a modo de lista, la aproximacion que se me ocurre ahora
# recuperar todos los elementos por posicion dentro de la propia lista recuperada
# que seria recuperar la unidad de informacion, en este caso el bloque y luego iterar.

# kat_request_constructor -> kat_request_builder():
# **    -> "Unable to build de Request, missing Parameters"
# rarbg_request_constructor -> rarbg_request_builder():

# kat_search (url, magnet_flag):
# rarbg_search (url, magnet_flag): 
#   con el flag lo que busco es tener la busqueda standar de la lista
#   a la par que puedo pedirle que busque el magnet del subrecurso y lo lance
#   * Si no se consigue respuesta de la direccion principal, se intenta de los proxies
#  ** que se conozcan -> "The web it's loading slow or not responding (<Default Url>)"
#  **                   -> "Trying to reach out using some proxy (<Proxy Name>)"
#  **                   -> "Unable to connect - Error (<Code Error>) - (404, 408, 500)"
#  **                   -> ""
 
# rarbg_parser(content):
#   **  -> Some values could not been retrieved (Setted to default values)"
#   **  -> Unable to find (Name, Size, Seeds, Leechs, Magnet)
#   retrieve: block list of 'td', retrieve the subvalues

# Deberia crear una clase que tenga como objetos la lista de listas, sobre los datos
# de los torrents que se hayan podido conseguir

# recuperar el tpb_lib 

# Externalizar el tratamiento de datos con pandas a otro modulo
# El Modulo ese cargaria un fichero de configuración en el que se podran
# settear criterios de busqueda (<Health>, <Size>, <hunt_flag>)

# rarbg_batch_creator(content, A_flag):
#   <- call for some info on nº of episodes
#   <- inicializacion del bucle de busqueda.
#   <- obtencion de lista preliminar
#   <- seleccion de paquete
#   <- Creacion y Almaceamiento de Magnet en la Biblioteca, Opcion Futura Compartir
#   <- Overlay sobre la forma en la que se disponen las caratulas dentro del propio Xbmc


# Futuro: Crossreference los 3 resultados de los Trackers y crear aquella lista que
# Tenga mejor media de salud.
# Actualmente solo busco la funcionalidad individual de cada uno de los 3 parsers.


# Funcionamiento normal de esta libreria, se recibe una llamada a esta libreria
# con la peticion sobre la busqueda de un contenido multimedia
# el constructor valida y envia la peticion
# la peticion es pasada al parser
# inicializacion de la lista de objetos.
# inicializacion del parseo
# llamada a tratmiento de datos
# obtencion de resultados preliminares
# decision del usuario
# cierre de uso de la libreria.


# Tareas pendientes de los modulos de recuperacion de magnets
#   * -> Hacer que permita la multi-descarga
#   **  -> Añadir flags de control
#   **  -> Añadir manejo de Excepciones


# Refinar la linea de comandos, para que sea facil implementar una interfaz para el plugin
# Siempre que se pueda CClient <-> Modulo Interfaz <-> Usuario

# Mirar como implementar un MAN sencillo e ir construyendo la parte de la memoria + documentacion
# para la memoria que requerira este proyecto.

# Ir ordenando aquellos links relevantes para poder ponerlos en la bibliografia utilizada.
# ** -> Con referencia a esto buscar el link que me ponia la expresion regular para volcar la
# salida a un stdio especifico para poder pasearla y mostrarla en forma de barra de progreso.

# Mirar ffmpeg, buscar una serie de presets ya echos, ya se refinaran luego (<Medium>, <High>)
# añadir entrada en MAN sobre presets

# Leer algo de como implementar el servicio de "<JellyFish>"
# Lanzaria un servicio que conectaria los 2 nodos, Slave-Master type
# Lanzando el reproductor que soporte esto, a ver si se puede hacer algo
# con el reproductor que tiene integrado

# Custom Filters
# -> Setup de estos si es posible en un futuro

# Posible distribucion de carga entre nodos de una misma red siempre y cuando tengan el
# servicio corriendo

# Sniffer, mirar de como implementar uno sencillo, que lo que haga sea cambiar el
# numero de conexiones y velocidades de descarga en la red. Suponiendo que esta escuchando
# una serie de puertos previamente configurados

# Revisar como tratar los ficheros para la alineacion de audios.

# Recupera Meta-Datos de IMBD, Rotten Tomatoes + Incrustarlos en el fichero.
# Construir modulo que crea los arboles de directorios y renombra los ficheros

# Scheluder para lanzar las tareas de forma periodica "(<Scheluder-Service>)"

# Mirar como fucan los addons en xmbc, para poder trabajar en la parte del interface, que
# a dia de hoy aun no tengo muy claro como voy a hacerla, necesitare ver que voy necesitado
#
# Aun asi deberia <Pantalla Carga> -> FST: <"Setting up the Environment">
#                                   -> SND_X: Search Box, Configuration, "Catalog", "Recomended" 
#                                   ->  Configuration:
#                                   ->  "<Sniffer> <Scheluder> <Setup> <Others-About> <ffmpeg>"

# Resultados en listas clickables
#   -> Poner Colores en base a la salud??

# Reconstruir el parser de kat, katproxy y algun proxie ya conocido
# ahoy....

