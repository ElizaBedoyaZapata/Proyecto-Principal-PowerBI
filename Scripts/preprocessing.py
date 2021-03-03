import pandas as pd
import shutil
from shareplum import Site
from shareplum.site import Version
from shareplum import Office365

# SharePoint
user_name = '@eafit.edu.co'
password = ''

authcookie = Office365('https://eafit.sharepoint.com', username=user_name, password=password).GetCookies()
site = Site('https://eafit.sharepoint.com/sites/Proyectoinformedecoyunturaeconomica/', version=Version.v2016, authcookie=authcookie)

folder = site.Folder('Documentos Compartidos/General')
allfiles = folder.files

#De aqui tomo la relative_url (server relative url) del archivo que necesitamos, en este caso es el "último", ya que es el
#primero que se subió al sharepoint
#Esto solo lo tengo que usar para la identificar la relative url
vistazo_file_info = allfiles[-1]
relative_url = vistazo_file_info['ServerRelativeUrl']
nombre_actual_archivo = vistazo_file_info['Name']

data = folder.get_file('NData vistazo 1.09.2020 .xlsx') #O poner aqui nombre_actual_archivo
with open('holu.xlsx', 'wb') as f:
    f.write(data)
    f.close()

relative_url
nombre_actual_archivo 


# Organizing files

# Preprocessing: Production


# Preprocessing: Prices


#eliminar columnas sin encabezado
df.drop(df.filter(regex="Unname"),axis=1, inplace=True)


#eliminar una columna en especifico
del df['Expectativas']

"""
seleccionar solo los datos necesarios
se borran las últimas n filas 
k es la nueva fila que se agregó de información (ej, ya no es hasta dic 2020, sino que se agregó enero 2021)
"""

k=1
n=28-k

df.drop(df.tail(n).index, 
        inplace = True) 
# Preprocessing: Labor
# Preprocessing: External sector
# Preprocessing: Fiscal
# Preprocessing: Finance

# Export data