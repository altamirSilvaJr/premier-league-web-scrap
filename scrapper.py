import requests as req
from bs4 import BeautifulSoup
import json

#acessando página para pegar os dados
page = req.request('GET', 'https://www.premierleague.com/tables?co=1&se=363&ha=-1').text

#transformando o html em um objeto do BeautifulSOup
soup = BeautifulSoup(page, 'html.parser')

#soup = soup.findAll('tbody', {'class':"tableBodyContainer isPL"})

linhas = soup.findAll('tr', {'data-compseason':"363"})


dicionario = {}
for i in range(len(linhas)):
    dicionario[i] = {}

count = 0

for linha in linhas:
    dicionario[count]['time'] = linha.findAll('span', {'class':'long'})[0].text
    dicionario[count]['jogos'] = linha.findAll('td', {'class':False, 'id':False})[0].text
    dicionario[count]['vitorias'] = linha.findAll('td', {'class':False, 'id':False})[1].text
    dicionario[count]['empates'] = linha.findAll('td', {'class':False, 'id':False})[2].text
    dicionario[count]['derrotas'] = linha.findAll('td', {'class':False, 'id':False})[3].text
    dicionario[count]['gols_pro'] = linha.findAll('td', {'class':'hideSmall'})[0].text
    dicionario[count]['gols_contra'] = linha.findAll('td', {'class':'hideSmall'})[1].text
    saldo_gols = linha.findAll('td', {'class':False, 'id':False})[4].text
    saldo_gols = saldo_gols.replace(" ","")
    saldo_gols = saldo_gols.replace("\n","")
    dicionario[count]['saldo_gols'] = saldo_gols
    dicionario[count]['pontos'] = linha.findAll('td', {'class':'points'})[0].text
    count = count + 1

# for i in range(len(teams)):
#     dicionario[i] = {}
#     dicionario[i]['time'] = teams[i].text

#print(dicionario)

json_dictionary = json.dumps(dicionario, indent=4)
print(json_dictionary)