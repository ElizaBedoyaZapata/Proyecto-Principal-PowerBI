import pandas as pd
import shutil

# Creating a dictionary that relates the variables with their sources (links)
variables = [
    'PIB',
    'ISE',
    'Inflación',
    'Tasa de desempleo en las 13 ciudades y nivel nacional',
    'Tasa de desempleo e inactivos',
    'Exportaciones',
    'importaciones',
    'Saldo en cuenta corriente',
    'Tasa de cambio de cierre (dólar y euro)',
    'Flujo de inversión extranjera directa',
    'Recaudo por año del GNC por tipo de impuesto',
    'Saldo de la deuda neta del GNC',
    'Utilización de la capacidad instalada',
    'Índice de producción industrial',
    'Índices de confianza industrial y confianza comercial', 
    'Índice de confianza del consumidor',
    'Licencia de construcción aprobadas por tipo y áreas censadas por estado de obra',
    'EMBIG en puntos básico (Colombia y algunas economías LATAM)',
    'Títulos de Deuda Pública de Colombia (TES) y EE.UU (Tesoros)',
    'Tasa cero cupón (Término 10 años)',
    'Crecimiento anual cartera bruta y vencida',
    'Índice de calidad y cubrimiento de cartera vencida',
    'Total establecimientos de crédito',
    'Rentabilidad patrimonial anual',
    'Margen ex-ante',
    'TES Pesos vs TES UVR 5 años'
    ]   

sources = [
    'https://www.dane.gov.co/index.php/estadisticas-por-tema/cuentas-nacionales/cuentas-nacionales-trimestrales/historicos-producto-interno-bruto-pib',
    'https://www.dane.gov.co/index.php/estadisticas-por-tema/cuentas-nacionales/indicador-de-seguimiento-a-la-economia-ise',
    'https://www.dane.gov.co/index.php/estadisticas-por-tema/precios-y-costos/indice-de-precios-al-consumidor-ipc/ipc-informacion-tecnica',
    'https://www.dane.gov.co/index.php/estadisticas-por-tema/mercado-laboral/empleo-y-desempleo',
    'https://www.dane.gov.co/index.php/estadisticas-por-tema/mercado-laboral/empleo-y-desempleo',
    'https://www.banrep.gov.co/es/estadisticas/exportaciones',
    'https://www.banrep.gov.co/es/estadistica/importaciones',
    'Calcular',
    'https://www.banrep.gov.co/es/estadisticas/monedas-disponibles',
    'https://www.banrep.gov.co/es/estadisticas/inversion-directa',
    'https://www.dian.gov.co/dian/cifras/Paginas/EstadisticasRecaudo.aspx',
    'https://www.banrep.gov.co/es/boletin-deuda-publica',
    'Por confirmar',
    'https://www.dane.gov.co/index.php/estadisticas-por-tema/industria/indice-de-produccion-industrial-ipi',
    'https://www.fedesarrollo.org.co/es/encuestas/empresarial-eoe',
    'https://www.fedesarrollo.org.co/es/encuestas/consumidor-eoc',
    'https://www.dane.gov.co/index.php/estadisticas-por-tema/construccion/censo-de-edificaciones',
    'https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/indicadores-de-riesgo-para-paises-emergentes-embig',
    'Por confirmar',
    'https://totoro.banrep.gov.co/analytics/saw.dll?Go&Action=prompt&NQUser=publico&NQPassword=publico123&path=%2Fshared%2FSeries%20Estad%C3%ADsticas_T%2F1.%20Tasas%20TES%2F1.1%20Tasa%20cero%20cup%C3%B3n%2F1.1.2%20Tasa%20cero%20cup%C3%B3n%20pesos&Options=rfd&lang=es',
    'Por confirmar',
    'Por confirmar',
    'Por confirmar',
    'Por confirmar',
    'Por confirmar',
    'Por confirmar'
    ]

links_data = {
    "Variable": variables,
    "Fuente": sources
}

# Creating and exporting a data frame
data = pd.DataFrame(links_data)
data.to_excel("enlaces.xlsx", sheet_name='Enlaces', engine='openpyxl')

# Moving the file to correct folder
shutil.move("enlaces.xlsx", "..\\Inputs")
