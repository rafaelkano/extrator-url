#url = 'https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real'
url = ''

# Sanitização da URL
url = url.replace(' ', '')

# Validação da URL
if url == '':
    raise ValueError('A URL está vazia')

# Separa base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametro = url[indice_interrogacao+1:]
print(url_parametro)

# Busca o valor de um parâmetro
parametro_busca = 'moedaDestino'
indice_parametro = url_parametro.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametro.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametro[indice_valor:]
else:
    valor = url_parametro[indice_valor:indice_e_comercial]
print(valor)

