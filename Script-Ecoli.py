import pandas as pd   #importo la biblioteca PANDAS para poder usar sus funciones
pd.read_csv("ecoli.data").head() # abro el archivo 

# Attribute Information: 
# protein: Accession number for the SWISS-PROT database.
# mcg: McGeoch's method for signal sequence recognition.
# gvh: Von Heijne's method for signal sequence recognition.
# lip: Von Heijne's Signal Peptidase II consensus sequence score.
# chg: Presence of charge on N-terminus of predicted lipoproteins.
# aac: Score of discriminant analysis of the amino acid content of outer membrane and periplasmic proteins.
# alm1: Score of the ALOM membrane spanning region prediction program.
# alm2: Score of ALOM program after excluding putative cleavable signal regions from the sequence.
# site: Localization site: cp (cytoplasm); im (inner membrane without signal sequence);
# pp (perisplasm); imU (inner membrane, uncleavable signal sequence); om (outer membrane);
# omL (outer membrane lipoprotein); imL (inner membrane lipoprotein); imS (inner membrane, cleavable signal sequence).

# Fuente del dataset: https://archive.ics.uci.edu/ml/datasets/Ecoli
# Dicha data estaba separada por espacios y no por comas y no tenía los títulos.
# Para lograr obtener lo que se ve en el notebook lo que hize fue utilizar la consola de 
# linux para abrir un programa de edición de textos llamado "vim". Use la siguiente expresión
# regular: %s/ \+/,/g    significados:  %(en toda la línea) s(sustituí) /un espacio\
# (donde haya un espacio) +/ (o más de uno) /,/ (reemplazalo por solamente una coma)
# /g (g de global, es decir no solo a la primer línea, sino globalmente a todo el documento)
# y finalmente los títulos de las columnas fueron agregadas a mano.

ecoli = pd.read_csv("ecoli.data") # lo guardo en un objeto (asignación)

type(ecoli) # me va a decir que es un dataframe.
 
ecoli.dtypes # para ver que tipo de cosas contiene mi dataframe uso la función dtypes

#object: significa que es un objeto (texto) osea una cadena de caracteres (string)
#float: significa que es un número con coma

ecoli.columns #para ver las columnas

# Para ver las dimensiones del dataframe utilizo la función shape:

ecoli.shape

# obtengo una tupla, por lo cual los datos son inmutables. 
# La misma me informa el n° de filas y el n° de columnas respectivamente.

#puedo corroborarlo de la siguiente manera:

a = ecoli.shape
type(a)

ecoli.head() #con la función head veo las primeras 5 líneas de mi dataframe

ecoli.tail() #con la función tail veo las últimas 5 líneas de mi dataframe

#para ver las líneas comprendidas entre las observaciones 200 y 215 hago así:

ecoli.head(216).tail(16) 

#uso PIPE(tuberia):la salida de un resultado, entra en otra función.
#hay que ponerlo así ya que los índices en python arrancan del número 0.

ecoli['protein'].head()  #selecciono una columna

ecoli.protein.head() #otra forma de hacer lo mismo

pd.unique(ecoli['site']) #para ver los diferentes sitios de localización q hay (no repetidos)

sites = pd.unique(ecoli['site']) 

len(sites) #para contarlas

ecoli['site'].nunique() #también se puede de esta manera # no hace falta grabar variable.

## Por lo cual hay 8 sitios de localización diferentes para las proteínas de e.coli ##

ecoli.describe()    # para obtener estadísticas básicas de los valores numéricos del dataset

ecoli['alm1'].min() #para ver específicamente el valor mínimo de la columna 'alm1'

# Datos agrupados por sitios

data_agrupada = ecoli.groupby('site')

data_agrupada.describe() # Estadísticas para todas las columnas numéricas agrupadas por sitio

data_agrupada.count()

data_agrupada.protein.count() # para ver solamente la columna de proteinas y me las cuente
# agrupadas por sitios

data_agrupada.protein.count().sort_values(ascending=False) #ordeno de > a <

## Puedo observar como es la distribución de las proteínas en los distintas localizaciones 
             # posibles de la bacteria e.coli ordenadas en forma descendente ##

# Puedo pedir especificamente la cantidad de proteínas que tiene un sitio determinado:
# Como por ejemplo la cantidad de proteínas citoplasmáticas de la bacteria.
data_agrupada.site.count()['cp']

site_protein = ecoli.groupby(['site','protein'])                    #AGRUPO 2 COLUMNAS
site_protein.count().head()

# de esta manera puedo ver las proteínas que se encuentran en cada sitio.

site_protein.describe().head()

%matplotlib inline # para que las imágenes aparezcan insertadas en el Notebook

localization = data_agrupada.protein.count()

grafica = localization.plot(kind='bar', title= "Proteins localization sites")
grafica.set_xlabel("sites")
grafica.set_ylabel("number of proteins")

# De esta manera puedo observar en un gráfico de barras como se distribuyen las distintas
# proteínas de E.coli en las diferentes localizaciónes celulares.
