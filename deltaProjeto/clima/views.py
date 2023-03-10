import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request, estadoSelecionado=None):
   estado = ""
   if request.method == 'POST':
      estado = request.POST.get('estadoSelecionado', None)

   baseURL = "https://apiadvisor.climatempo.com.br/api/v1/locale/city?state={}&country=BR&token=511da671c39f877ff8525f098bab378b"
   apiData = baseURL.format(estado)

   response = requests.get(apiData).json()

   # usar variável response para utilizar API online gratuita
   # usar variável jsons para utilizar json offline

   data = []
   cont = 0
   for i in response:
      if i['state'] == estado:
         climaDicionario = {
            "id" : response[cont]['id'],
            "estado" : response[cont]['state'],
            "cidade" : response[cont]['name']
         }
         data.append(climaDicionario)
      cont+=1

   resultado = {"data" : data}

   return render(request, 'clima/index.html', resultado)

def editar(request):
   data = {
      'state': 'John Doe',
      'city': 'john.doe@example.com'
   }
   response = requests.get('https://apiadvisor.climatempo.com.br/api/v1/locale/city?country=BR&token=511da671c39f877ff8525f098bab378b', data=data)

   localizacao = response.json()

   if request.method == 'POST':
       estado = request.POST.get('estado')
       cidade = request.POST.get('cidade')

       localizacao['estado'] = estado
       localizacao['cidade'] = cidade

       response = requests.put('https://apiadvisor.climatempo.com.br/api/v1/locale/city?country=BR&token=511da671c39f877ff8525f098bab378b', data=localizacao)

       if response.status_code == 200:
           return render("Funcionou")

   return render(request, 'editar_localizacao.html', {'localizacao': localizacao})

def deletar(request, id):
   id.delete()

jsons = [
   {
      "id":8285,
      "name":"Abadia de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8529,
      "name":"Abadia dos Dourados",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8286,
      "name":"Abadi\u00e2nia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6868,
      "name":"Abaet\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7696,
      "name":"Abaetetuba",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7996,
      "name":"Abaiara",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4050,
      "name":"Aba\u00edra",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4603,
      "name":"Abar\u00e9",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6273,
      "name":"Abarracamento",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6959,
      "name":"Abati\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5049,
      "name":"Abdon Batista",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5050,
      "name":"Abelardo Luz",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5916,
      "name":"Abel Figueiredo",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6274,
      "name":"Abra\u00e3o",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6324,
      "name":"Abrantes",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3258,
      "name":"Abre Campo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6352,
      "name":"Abreu e Lima",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3563,
      "name":"Abreul\u00e2ndia",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3259,
      "name":"Acaiaca",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5672,
      "name":"A\u00e7ail\u00e2ndia",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4139,
      "name":"Acajutiba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7697,
      "name":"Acar\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7997,
      "name":"Acarape",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7998,
      "name":"Acara\u00fa",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6040,
      "name":"Acari",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7187,
      "name":"Acau\u00e3",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5786,
      "name":"Acegu\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7999,
      "name":"Acopiara",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4397,
      "name":"Acorizal",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5893,
      "name":"Acrel\u00e2ndia",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":8287,
      "name":"Acre\u00fana",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6041,
      "name":"A\u00e7u",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6876,
      "name":"A\u00e7ucena",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4653,
      "name":"Adamantina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8288,
      "name":"Adel\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4654,
      "name":"Adolfo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6960,
      "name":"Adrian\u00f3polis",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5216,
      "name":"Adustina",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5378,
      "name":"Afogados da Ingazeira",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6275,
      "name":"Afonso Arinos",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6042,
      "name":"Afonso Bezerra",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8188,
      "name":"Afonso Cl\u00e1udio",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6033,
      "name":"Afonso Cunha",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7249,
      "name":"Afr\u00e2nio",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7698,
      "name":"Afu\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4655,
      "name":"Agiss\u00ea",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4709,
      "name":"Agrestina",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7188,
      "name":"Agricol\u00e2ndia",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5051,
      "name":"Agrol\u00e2ndia",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5052,
      "name":"Agron\u00f4mica",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5964,
      "name":"\u00c1gua Azul do Norte",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":9109,
      "name":"\u00c1gua Boa",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6961,
      "name":"\u00c1gua Boa",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8530,
      "name":"\u00c1gua Boa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6339,
      "name":"\u00c1gua Branca",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7189,
      "name":"\u00c1gua Branca",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4307,
      "name":"\u00c1gua Branca",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3086,
      "name":"\u00c1gua Clara",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3159,
      "name":"\u00c1gua Comprida",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5053,
      "name":"\u00c1gua Doce",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4786,
      "name":"\u00c1gua Doce do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8189,
      "name":"\u00c1gua Doce do Norte",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":4649,
      "name":"\u00c1gua Fria",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8289,
      "name":"\u00c1gua Fria de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4656,
      "name":"Agua\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8290,
      "name":"\u00c1gua Limpa",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3260,
      "name":"Aguanil",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6043,
      "name":"\u00c1gua Nova",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7250,
      "name":"\u00c1gua Preta",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5787,
      "name":"\u00c1gua Santa",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7251,
      "name":"\u00c1guas Belas",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5054,
      "name":"\u00c1guas Brancas",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4657,
      "name":"\u00c1guas da Prata",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5055,
      "name":"\u00c1guas de Chapec\u00f3",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4658,
      "name":"\u00c1guas de Lind\u00f3ia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4659,
      "name":"\u00c1guas de Santa B\u00e1rbara",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6520,
      "name":"\u00c1guas de S\u00e3o Pedro",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8531,
      "name":"\u00c1guas F\u00e9rreas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6759,
      "name":"\u00c1guas Formosas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5056,
      "name":"\u00c1guas Frias",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8291,
      "name":"\u00c1guas Lindas de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5057,
      "name":"\u00c1guas Mornas",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7649,
      "name":"\u00c1guas Vermelhas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5788,
      "name":"Agudo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4660,
      "name":"Agudos",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6962,
      "name":"Agudos do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8190,
      "name":"\u00c1guia Branca",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":4787,
      "name":"Aguiar",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3565,
      "name":"Aguiarn\u00f3polis",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":6276,
      "name":"Agulhas Negras",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6869,
      "name":"Aimor\u00e9s",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5363,
      "name":"Aiquara",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8000,
      "name":"Aiuaba",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3888,
      "name":"Aiuruoca",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4661,
      "name":"Ajapi",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5789,
      "name":"Ajuricaba",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6529,
      "name":"Alagoa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7528,
      "name":"Alagoa Grande",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4788,
      "name":"Alagoa Nova",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7252,
      "name":"Alagoinha",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7529,
      "name":"Alagoinha",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7190,
      "name":"Alagoinha do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6413,
      "name":"Alagoinhas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4662,
      "name":"Alambari",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3261,
      "name":"Albertina",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6277,
      "name":"Alberto Torres",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5693,
      "name":"Albuquerque",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4524,
      "name":"Alc\u00e2ntara",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8001,
      "name":"Alc\u00e2ntaras",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4789,
      "name":"Alcantil",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":9110,
      "name":"Alcantilado",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3148,
      "name":"Alcin\u00f3polis",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6414,
      "name":"Alcoba\u00e7a",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4663,
      "name":"Aldeia da Serra",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8392,
      "name":"Aldeias Altas",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5790,
      "name":"Alecrim",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8191,
      "name":"Alegre",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5791,
      "name":"Alegrete",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7191,
      "name":"Alegrete do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5792,
      "name":"Alegria",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8532,
      "name":"Al\u00e9m Para\u00edba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7699,
      "name":"Alenquer",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6963,
      "name":"Alexandra",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6044,
      "name":"Alexandria",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8533,
      "name":"Alexandrita",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8292,
      "name":"Alex\u00e2nia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6870,
      "name":"Alfenas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8192,
      "name":"Alfredo Chaves",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":4664,
      "name":"Alfredo Marcondes",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3262,
      "name":"Alfredo Vasconcelos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5058,
      "name":"Alfredo Wagner",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4790,
      "name":"Algod\u00e3o de Janda\u00edra",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7700,
      "name":"Algodoal",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4791,
      "name":"Alhandra",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7253,
      "name":"Alian\u00e7a",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3566,
      "name":"Alian\u00e7a do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4214,
      "name":"Almadina",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3567,
      "name":"Almas",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7701,
      "name":"Almeirim",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6871,
      "name":"Almenara",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6045,
      "name":"Almino Afonso",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6964,
      "name":"Almirante Tamandar\u00e9",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5793,
      "name":"Almirante Tamandar\u00e9 do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8293,
      "name":"Alo\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3263,
      "name":"Alpercata",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5794,
      "name":"Alpestre",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4665,
      "name":"Alphaville",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6872,
      "name":"Alpin\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6765,
      "name":"Alta Floresta",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5720,
      "name":"Alta Floresta d'Oeste",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":4666,
      "name":"Altair",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7702,
      "name":"Altamira",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4185,
      "name":"Altamira do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6965,
      "name":"Altamira do Paran\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8002,
      "name":"Altaneira",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6966,
      "name":"Alt\u00e3nia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3253,
      "name":"Alterosa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7254,
      "name":"Altinho",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4667,
      "name":"Altin\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5795,
      "name":"Alto Alegre",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5773,
      "name":"Alto Alegre",
      "state":"RR",
      "country":"BR  "
   },
   {
      "id":4668,
      "name":"Alto Alegre",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6240,
      "name":"Alto Alegre do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5721,
      "name":"Alto Alegre do Parecis",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":4723,
      "name":"Alto Alegre do Pindar\u00e9",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":9111,
      "name":"Alto Araguaia",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5059,
      "name":"Alto Bela Vista",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":9112,
      "name":"Alto Boa Vista",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3264,
      "name":"Alto Capara\u00f3",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9113,
      "name":"Alto Coit\u00e9",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6053,
      "name":"Alto do Rodrigues",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5796,
      "name":"Alto Feliz",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":9114,
      "name":"Alto Gar\u00e7as",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8294,
      "name":"Alto Horizonte",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3265,
      "name":"Alto Jequitib\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7192,
      "name":"Alto Long\u00e1",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6967,
      "name":"Alt\u00f4nia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":9115,
      "name":"Alto Paraguai",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6968,
      "name":"Alto Para\u00edso",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5722,
      "name":"Alto Para\u00edso",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":8295,
      "name":"Alto Para\u00edso de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3213,
      "name":"Alto Paran\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5669,
      "name":"Alto Parna\u00edba",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6969,
      "name":"Alto Piquiri",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3266,
      "name":"Alto Rio Doce",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8193,
      "name":"Alto Rio Novo",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7193,
      "name":"Altos",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8003,
      "name":"Alto Santo",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":9116,
      "name":"Alto Taquari",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4669,
      "name":"Alum\u00ednio",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6810,
      "name":"Alvar\u00e3es",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":3267,
      "name":"Alvarenga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4670,
      "name":"\u00c1lvares Florence",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6521,
      "name":"\u00c1lvares Machado",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4671,
      "name":"\u00c1lvaro de Carvalho",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4672,
      "name":"Alvinl\u00e2ndia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3268,
      "name":"Alvin\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3568,
      "name":"Alvorada",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5797,
      "name":"Alvorada",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3269,
      "name":"Alvorada de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5723,
      "name":"Alvorada d'Oeste",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":7194,
      "name":"Alvorada do Gurgu\u00e9ia",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6970,
      "name":"Alvorada do Igua\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8296,
      "name":"Alvorada do Norte",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6971,
      "name":"Alvorada do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5774,
      "name":"Amajari",
      "state":"RR",
      "country":"BR  "
   },
   {
      "id":7671,
      "name":"Amambai",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":7802,
      "name":"Amap\u00e1",
      "state":"AP",
      "country":"BR  "
   },
   {
      "id":4725,
      "name":"Amap\u00e1 do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6972,
      "name":"Amapor\u00e3",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7255,
      "name":"Amaraji",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5798,
      "name":"Amaral Ferrador",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8297,
      "name":"Amaralina",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7195,
      "name":"Amarante",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4726,
      "name":"Amarante do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8534,
      "name":"Amarantina",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7545,
      "name":"Amargosa",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5895,
      "name":"Amatur\u00e1",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":3046,
      "name":"Am\u00e9lia Rodrigues",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7814,
      "name":"Am\u00e9rica Dourada",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4673,
      "name":"Americana",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8298,
      "name":"Americano do Brasil",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4674,
      "name":"Am\u00e9rico Brasiliense",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4675,
      "name":"Am\u00e9rico de Campos",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5799,
      "name":"Ametista do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8004,
      "name":"Amontada",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8299,
      "name":"Amorin\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4792,
      "name":"Amparo",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4676,
      "name":"Amparo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6278,
      "name":"Amparo",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4493,
      "name":"Amparo de S\u00e3o Francisco",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":3270,
      "name":"Amparo do Serra",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6973,
      "name":"Amp\u00e9re",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4548,
      "name":"Anadia",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6415,
      "name":"Anag\u00e9",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6974,
      "name":"Anahy",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5917,
      "name":"Anaj\u00e1s",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4727,
      "name":"Anajatuba",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4677,
      "name":"Anal\u00e2ndia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5896,
      "name":"Anam\u00e3",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":3569,
      "name":"Anan\u00e1s",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7703,
      "name":"Ananindeua",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8300,
      "name":"An\u00e1polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5918,
      "name":"Anapu",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4027,
      "name":"Anapurus",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5694,
      "name":"Anast\u00e1cio",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3124,
      "name":"Anauril\u00e2ndia",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8194,
      "name":"Anchieta",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5060,
      "name":"Anchieta",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3858,
      "name":"Andara\u00ed",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6975,
      "name":"Andir\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3918,
      "name":"Andorinha",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8535,
      "name":"Andradas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6279,
      "name":"Andrade Pinto",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4294,
      "name":"Andradina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5800,
      "name":"Andr\u00e9 da Rocha",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8536,
      "name":"Andrel\u00e2ndia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4295,
      "name":"Angatuba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3271,
      "name":"Angel\u00e2ndia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3177,
      "name":"Ang\u00e9lica",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":7256,
      "name":"Angelim",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5061,
      "name":"Angelina",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3211,
      "name":"Angical",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7196,
      "name":"Angical do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3570,
      "name":"Angico",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":6057,
      "name":"Angicos",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6280,
      "name":"Angra dos Reis",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3236,
      "name":"Anguera",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3163,
      "name":"\u00c2ngulo",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4438,
      "name":"Anhandui",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8301,
      "name":"Anhanguera",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4296,
      "name":"Anhembi",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":9117,
      "name":"Anhumas",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4297,
      "name":"Anhumas",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8302,
      "name":"Anicuns",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8393,
      "name":"Anil",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7197,
      "name":"An\u00edsio de Abreu",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5062,
      "name":"Anita Garibaldi",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5063,
      "name":"Anit\u00e1polis",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5897,
      "name":"Anori",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":6281,
      "name":"Anta",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5801,
      "name":"Anta Gorda",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5064,
      "name":"Anta Gorda",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3965,
      "name":"Antas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6976,
      "name":"Antonina",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8005,
      "name":"Antonina do Norte",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7198,
      "name":"Ant\u00f4nio Almeida",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8006,
      "name":"Ant\u00f4nio Bezerra",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7815,
      "name":"Ant\u00f4nio Cardoso",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3889,
      "name":"Ant\u00f4nio Carlos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5065,
      "name":"Ant\u00f4nio Carlos",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3272,
      "name":"Ant\u00f4nio Dias",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7816,
      "name":"Ant\u00f4nio Gon\u00e7alves",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3149,
      "name":"Ant\u00f4nio Jo\u00e3o",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6058,
      "name":"Ant\u00f4nio Martins",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6977,
      "name":"Ant\u00f4nio Olinto",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5509,
      "name":"Ant\u00f4nio Prado",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8537,
      "name":"Ant\u00f4nio Prado de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4227,
      "name":"Aparecida",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4300,
      "name":"Aparecida",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8303,
      "name":"Aparecida de Goi\u00e2nia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6320,
      "name":"Aparecida de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4299,
      "name":"Aparecida de S\u00e3o Manuel",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4298,
      "name":"Aparecida d'Oeste",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8304,
      "name":"Aparecida do Rio Doce",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3571,
      "name":"Aparecida do Rio Negro",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3166,
      "name":"Aparecida do Taboado",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6282,
      "name":"Aperib\u00e9",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8195,
      "name":"Apiac\u00e1",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":9118,
      "name":"Apiac\u00e1s",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4301,
      "name":"Apia\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6241,
      "name":"Apicum-A\u00e7u",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5066,
      "name":"Api\u00fana",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6059,
      "name":"Apodi",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4256,
      "name":"Apor\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8305,
      "name":"Apor\u00e9",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4140,
      "name":"Apuarema",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6978,
      "name":"Apucarana",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5898,
      "name":"Apu\u00ed",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":8007,
      "name":"Apuiar\u00e9s",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4497,
      "name":"Aquidab\u00e3",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6979,
      "name":"Aquidaban",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6547,
      "name":"Aquidauana",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8008,
      "name":"Aquiraz",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5067,
      "name":"Arabut\u00e3",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4795,
      "name":"Ara\u00e7agi",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3273,
      "name":"Ara\u00e7a\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4502,
      "name":"Aracaju",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4302,
      "name":"Ara\u00e7ariguama",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3176,
      "name":"Ara\u00e7\u00e1s",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8009,
      "name":"Aracati",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4257,
      "name":"Aracatu",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4303,
      "name":"Ara\u00e7atuba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7817,
      "name":"Araci",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8538,
      "name":"Aracitaba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8010,
      "name":"Aracoiaba",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7257,
      "name":"Ara\u00e7oiaba",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4304,
      "name":"Ara\u00e7oiaba da Serra",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8196,
      "name":"Aracruz",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8306,
      "name":"Ara\u00e7u",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6874,
      "name":"Ara\u00e7ua\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7532,
      "name":"Aragar\u00e7as",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8307,
      "name":"Aragoi\u00e2nia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3572,
      "name":"Aragominas",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3573,
      "name":"Araguacema",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3574,
      "name":"Aragua\u00e7u",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4398,
      "name":"Araguaiana",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3575,
      "name":"Aragua\u00edna",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4399,
      "name":"Araguainha",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4728,
      "name":"Araguan\u00e3",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3576,
      "name":"Araguan\u00e3",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4110,
      "name":"Araguapaz",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8308,
      "name":"Araguapaz",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8539,
      "name":"Araguari",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7540,
      "name":"Araguatins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8394,
      "name":"Araioses",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5190,
      "name":"Aral Moreira",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4604,
      "name":"Aramari",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5510,
      "name":"Arambar\u00e9",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4028,
      "name":"Arame",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4306,
      "name":"Aramina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4308,
      "name":"Arandu",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8540,
      "name":"Arantina",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4309,
      "name":"Arape\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6404,
      "name":"Arapiraca",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3577,
      "name":"Arapoema",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8541,
      "name":"Araponga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6980,
      "name":"Arapongas",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8542,
      "name":"Arapor\u00e3",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6981,
      "name":"Arapoti",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5695,
      "name":"Arapu\u00e1",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8543,
      "name":"Arapu\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6982,
      "name":"Arapu\u00e3",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3195,
      "name":"Araputanga",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5068,
      "name":"Araquari",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4793,
      "name":"Arara",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5069,
      "name":"Ararangu\u00e1",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4310,
      "name":"Araraquara",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4312,
      "name":"Araras",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8011,
      "name":"Ararend\u00e1",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4729,
      "name":"Arari",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5511,
      "name":"Araric\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8012,
      "name":"Araripe",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7258,
      "name":"Araripina",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6283,
      "name":"Araruama",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4794,
      "name":"Araruna",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6983,
      "name":"Araruna",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4605,
      "name":"Arataca",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5512,
      "name":"Aratiba",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4910,
      "name":"Aratu",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8013,
      "name":"Aratuba",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4606,
      "name":"Aratu\u00edpe",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4503,
      "name":"Arau\u00e1",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6984,
      "name":"Arauc\u00e1ria",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8544,
      "name":"Ara\u00fajos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6873,
      "name":"Arax\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5356,
      "name":"Arceburgo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4313,
      "name":"Arco-\u00cdris",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8545,
      "name":"Arcos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7259,
      "name":"Arcoverde",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3212,
      "name":"Areado",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6286,
      "name":"Areal",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4315,
      "name":"Arealva",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7530,
      "name":"Areia",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4699,
      "name":"Areia Branca",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4504,
      "name":"Areia Branca",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4796,
      "name":"Areia de Bara\u00fanas",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4797,
      "name":"Areial",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4316,
      "name":"Areias",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4317,
      "name":"Arei\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7546,
      "name":"Arembepe",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4286,
      "name":"Aren\u00e1polis",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8309,
      "name":"Aren\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6060,
      "name":"Ar\u00eas",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8546,
      "name":"Argirita",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8547,
      "name":"Aricanduva",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6875,
      "name":"Arinos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9119,
      "name":"Aripuan\u00e3",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5724,
      "name":"Ariquemes",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":4346,
      "name":"Ariranha",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6985,
      "name":"Ariranha do Iva\u00ed",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5070,
      "name":"Armaz\u00e9m",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8014,
      "name":"Arneiroz",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7199,
      "name":"Aroazes",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7531,
      "name":"Aroeiras",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":83452,
      "name":"Aroeiras do Itaim",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7200,
      "name":"Arraial",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7818,
      "name":"Arraial d'Ajuda",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6288,
      "name":"Arraial do Cabo",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3578,
      "name":"Arraias",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5513,
      "name":"Arroio do Meio",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5514,
      "name":"Arroio do Padre",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5515,
      "name":"Arroio do Sal",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5516,
      "name":"Arroio dos Ratos",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5517,
      "name":"Arroio do Tigre",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5518,
      "name":"Arroio Grande",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5071,
      "name":"Arroio Trinta",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7594,
      "name":"Arruda",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4347,
      "name":"Artur Nogueira",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8310,
      "name":"Aruan\u00e3",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4348,
      "name":"Aruj\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5072,
      "name":"Arvoredo",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5519,
      "name":"Arvorezinha",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5073,
      "name":"Ascurra",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4349,
      "name":"Asp\u00e1sia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6986,
      "name":"Assa\u00ed",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8015,
      "name":"Assar\u00e9",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4350,
      "name":"Assis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7709,
      "name":"Assis Brasil",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":6987,
      "name":"Assis Chateaubriand",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4798,
      "name":"Assun\u00e7\u00e3o",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7201,
      "name":"Assun\u00e7\u00e3o do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8548,
      "name":"Astolfo Dutra",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6668,
      "name":"Astorga",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6669,
      "name":"Atalaia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7722,
      "name":"Atalaia",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5899,
      "name":"Atalaia do Norte",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":5074,
      "name":"Atalanta",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8549,
      "name":"Atal\u00e9ia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4351,
      "name":"Atibaia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8197,
      "name":"Atilio Vivacqua",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":3579,
      "name":"Augustin\u00f3polis",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5919,
      "name":"Augusto Corr\u00eaa",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8550,
      "name":"Augusto de Lima",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5520,
      "name":"Augusto Pestana",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6061,
      "name":"Augusto Severo",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5521,
      "name":"\u00c1urea",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7819,
      "name":"Aurelino Leal",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4352,
      "name":"Auriflama",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8311,
      "name":"Auril\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8016,
      "name":"Aurora",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5075,
      "name":"Aurora",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5920,
      "name":"Aurora do Par\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":3580,
      "name":"Aurora do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7772,
      "name":"Autazes",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":4353,
      "name":"Ava\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4354,
      "name":"Avanhandava",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4355,
      "name":"Avar\u00e9",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5921,
      "name":"Aveiro",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6289,
      "name":"Avelar",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7202,
      "name":"Avelino Lopes",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8312,
      "name":"Avelin\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4186,
      "name":"Axix\u00e1",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3581,
      "name":"Axix\u00e1 do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4704,
      "name":"Baba\u00e7ul\u00e2ndia",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8395,
      "name":"Bacabal",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4730,
      "name":"Bacabeira",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4731,
      "name":"Bacuri",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4732,
      "name":"Bacurituba",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4356,
      "name":"Bady Bassitt",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8551,
      "name":"Baependi",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5522,
      "name":"Bag\u00e9",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5922,
      "name":"Bagre",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4803,
      "name":"Ba\u00eda da Trai\u00e7\u00e3o",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6062,
      "name":"Ba\u00eda Formosa",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7820,
      "name":"Baian\u00f3polis",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5923,
      "name":"Bai\u00e3o",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7821,
      "name":"Baixa Grande",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3953,
      "name":"Baixa Grande do Ribeiro",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8017,
      "name":"Baixio",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8198,
      "name":"Baixo Guandu",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7773,
      "name":"Balbina",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":4357,
      "name":"Balbinos",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8552,
      "name":"Baldim",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8313,
      "name":"Baliza",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5076,
      "name":"Balne\u00e1rio Arroio do Silva",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5077,
      "name":"Balne\u00e1rio Barra do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5078,
      "name":"Balne\u00e1rio Cambori\u00fa",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5080,
      "name":"Balne\u00e1rio Gaivota",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4769,
      "name":"Balne\u00e1rio Pi\u00e7arras",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5523,
      "name":"Balne\u00e1rio Pinhal",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4358,
      "name":"B\u00e1lsamo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6670,
      "name":"Balsa Nova",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8396,
      "name":"Balsas",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6290,
      "name":"Baltazar",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6877,
      "name":"Bambu\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8018,
      "name":"Banabui\u00fa",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4359,
      "name":"Bananal",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7569,
      "name":"Bananeiras",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3274,
      "name":"Bandeira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8553,
      "name":"Bandeira do Sul",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5081,
      "name":"Bandeirante",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6671,
      "name":"Bandeirantes",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5696,
      "name":"Bandeirantes",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3582,
      "name":"Bandeirantes do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5924,
      "name":"Bannach",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6291,
      "name":"Banquete",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7822,
      "name":"Banza\u00ea",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5526,
      "name":"Bar\u00e3o",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4360,
      "name":"Bar\u00e3o de Antonina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3277,
      "name":"Bar\u00e3o de Cocais",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5524,
      "name":"Bar\u00e3o de Cotegipe",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3228,
      "name":"Bar\u00e3o de Graja\u00fa",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6292,
      "name":"Bar\u00e3o de Juparan\u00e3",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7595,
      "name":"Bar\u00e3o de Melga\u00e7o",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3278,
      "name":"Bar\u00e3o de Monte Alto",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5525,
      "name":"Bar\u00e3o do Triunfo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4799,
      "name":"Bara\u00fana",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6063,
      "name":"Bara\u00fana",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7650,
      "name":"Barbacena",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8019,
      "name":"Barbalha",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4361,
      "name":"Barbosa",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6672,
      "name":"Barbosa Ferraz",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5925,
      "name":"Barcarena",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6064,
      "name":"Barcelona",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7774,
      "name":"Barcelos",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":4362,
      "name":"Bariri",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7547,
      "name":"Barra",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6293,
      "name":"Barra Alegre",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5082,
      "name":"Barra Bonita",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4363,
      "name":"Barra Bonita",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5527,
      "name":"Barrac\u00e3o",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6673,
      "name":"Barrac\u00e3o",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7823,
      "name":"Barra da Estiva",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3997,
      "name":"Barra d'Alc\u00e2ntara",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7260,
      "name":"Barra de Guabiraba",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6294,
      "name":"Barra de Maca\u00e9",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4801,
      "name":"Barra de Santana",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4800,
      "name":"Barra de Santa Rosa",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7723,
      "name":"Barra de Santo Ant\u00f4nio",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8199,
      "name":"Barra de S\u00e3o Francisco",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6295,
      "name":"Barra de S\u00e3o Jo\u00e3o",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4802,
      "name":"Barra de S\u00e3o Miguel",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7724,
      "name":"Barra de S\u00e3o Miguel",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":7596,
      "name":"Barra do Bugres",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4364,
      "name":"Barra do Chap\u00e9u",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7824,
      "name":"Barra do Cho\u00e7a",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6864,
      "name":"Barra do Corda",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6346,
      "name":"Barra do Gar\u00e7as",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5528,
      "name":"Barra do Guarita",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5083,
      "name":"Barra do Ibiraquera",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6674,
      "name":"Barra do Jacar\u00e9",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6416,
      "name":"Barra do Mendes",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3583,
      "name":"Barra do Ouro",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":6297,
      "name":"Barra do Pira\u00ed",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5529,
      "name":"Barra do Quara\u00ed",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5530,
      "name":"Barra do Ribeiro",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5531,
      "name":"Barra do Rio Azul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7825,
      "name":"Barra do Rocha",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5084,
      "name":"Barra do Sa\u00ed",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4505,
      "name":"Barra dos Coqueiros",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4365,
      "name":"Barra do Turvo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4366,
      "name":"Barra do Una",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5532,
      "name":"Barra Funda",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7826,
      "name":"Barra Grande",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3275,
      "name":"Barra Longa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6298,
      "name":"Barra Mansa",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7203,
      "name":"Barras",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6299,
      "name":"Barra Seca",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5085,
      "name":"Barra Velha",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8020,
      "name":"Barreira",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7548,
      "name":"Barreiras",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7204,
      "name":"Barreiras do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4684,
      "name":"Barreirinha",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":8397,
      "name":"Barreirinhas",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7261,
      "name":"Barreiros",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4367,
      "name":"Barretos",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4368,
      "name":"Barrinha",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8021,
      "name":"Barro",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8314,
      "name":"Barro Alto",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7827,
      "name":"Barro Alto",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7828,
      "name":"Barrocas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7205,
      "name":"Barro Duro",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3584,
      "name":"Barrol\u00e2ndia",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4607,
      "name":"Barro Preto",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8022,
      "name":"Barroquinha",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5533,
      "name":"Barros Cassal",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3276,
      "name":"Barroso",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6031,
      "name":"Barro Vermelho",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6654,
      "name":"Barueri",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4369,
      "name":"Bastos",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":9081,
      "name":"Bataguassu",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3226,
      "name":"Bataipor\u00e3",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":7206,
      "name":"Batalha",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6405,
      "name":"Batalha",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":4370,
      "name":"Batatais",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6443,
      "name":"Baturit\u00e9",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6655,
      "name":"Bauru",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5697,
      "name":"Ba\u00fas",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":7597,
      "name":"Bauxi",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7570,
      "name":"Bayeux",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4371,
      "name":"Bebedouro",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6444,
      "name":"Beberibe",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8023,
      "name":"Bela Cruz",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8398,
      "name":"Bel\u00e1gua",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3150,
      "name":"Bela Vista",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6675,
      "name":"Bela Vista da Caroba",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5491,
      "name":"Bela Vista de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3279,
      "name":"Bela Vista de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4733,
      "name":"Bela Vista do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6676,
      "name":"Bela Vista do Para\u00edso",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7207,
      "name":"Bela Vista do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5086,
      "name":"Bela Vista do Toldo",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7704,
      "name":"Bel\u00e9m",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4804,
      "name":"Bel\u00e9m",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7725,
      "name":"Bel\u00e9m",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":7262,
      "name":"Bel\u00e9m de Maria",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7263,
      "name":"Bel\u00e9m de S\u00e3o Francisco",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4708,
      "name":"Bel\u00e9m do Brejo do Cruz",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7208,
      "name":"Bel\u00e9m do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6300,
      "name":"Belford Roxo",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3280,
      "name":"Belmiro Braga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7829,
      "name":"Belmonte",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5087,
      "name":"Belmonte",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7830,
      "name":"Belo Campo",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6879,
      "name":"Belo Horizonte",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7264,
      "name":"Belo Jardim",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7726,
      "name":"Belo Monte",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":7705,
      "name":"Belo Monte",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":2964,
      "name":"Belo Oriente",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3281,
      "name":"Belo Vale",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7706,
      "name":"Belterra",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7831,
      "name":"Bem-Bom",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6303,
      "name":"Bemposta",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7209,
      "name":"Beneditinos",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4277,
      "name":"Benedito Leite",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5088,
      "name":"Benedito Novo",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5926,
      "name":"Benevides",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6811,
      "name":"Benjamin Constant",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":5534,
      "name":"Benjamin Constant do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4372,
      "name":"Bento de Abreu",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6065,
      "name":"Bento Fernandes",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5535,
      "name":"Bento Gon\u00e7alves",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4734,
      "name":"Bequim\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3282,
      "name":"Berilo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3283,
      "name":"Berizal",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4805,
      "name":"Bernardino Batista",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4373,
      "name":"Bernardino de Campos",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4735,
      "name":"Bernardo do Mearim",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3585,
      "name":"Bernardo Say\u00e3o",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4374,
      "name":"Bertioga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7210,
      "name":"Bertol\u00ednia",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3284,
      "name":"Bert\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5900,
      "name":"Beruri",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":4203,
      "name":"Betania",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7211,
      "name":"Bet\u00e2nia do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6880,
      "name":"Betim",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7265,
      "name":"Bezerros",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3285,
      "name":"Bias Fortes",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3286,
      "name":"Bicas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5089,
      "name":"Bigua\u00e7u",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4375,
      "name":"Bilac",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3287,
      "name":"Biquinhas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4376,
      "name":"Birigui",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4377,
      "name":"Biritiba-Mirim",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3966,
      "name":"Biritinga",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6677,
      "name":"Bituruna",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5090,
      "name":"Blumenau",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8200,
      "name":"Boa Esperan\u00e7a",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7598,
      "name":"Boa Esperan\u00e7a",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6678,
      "name":"Boa Esperan\u00e7a",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6881,
      "name":"Boa Esperan\u00e7a",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6679,
      "name":"Boa Esperan\u00e7a do Igua\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4378,
      "name":"Boa Esperan\u00e7a do Sul",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7212,
      "name":"Boa Hora",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6417,
      "name":"Boa Nova",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6304,
      "name":"Boa Sorte",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6305,
      "name":"Boaventura",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4806,
      "name":"Boa Ventura",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6680,
      "name":"Boa Ventura de S\u00e3o Roque",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6445,
      "name":"Boa Viagem",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5775,
      "name":"Boa Vista",
      "state":"RR",
      "country":"BR  "
   },
   {
      "id":4807,
      "name":"Boa Vista",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5392,
      "name":"Boa Vista",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":6681,
      "name":"Boa Vista da Aparecida",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5536,
      "name":"Boa Vista das Miss\u00f5es",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5537,
      "name":"Boa Vista do Buric\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5538,
      "name":"Boa Vista do Cadeado",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8399,
      "name":"Boa Vista do Gurupi",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5539,
      "name":"Boa Vista do Incra",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5901,
      "name":"Boa Vista do Ramos",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":5540,
      "name":"Boa Vista do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7832,
      "name":"Boa Vista do Tupim",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7727,
      "name":"Boca da Mata",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6812,
      "name":"Boca do Acre",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":5541,
      "name":"Boca do Monte",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7213,
      "name":"Bocaina",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4379,
      "name":"Bocaina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3288,
      "name":"Bocaina de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5091,
      "name":"Bocaina do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6882,
      "name":"Bocaiuva",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6682,
      "name":"Bocai\u00fava do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6066,
      "name":"Bod\u00f3",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7266,
      "name":"Bodoc\u00f3",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5698,
      "name":"Bodoquena",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4380,
      "name":"Bofete",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4381,
      "name":"Boi\u00e7ucanga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4382,
      "name":"Boituva",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5542,
      "name":"Bojuru",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5092,
      "name":"Bombinhas",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7267,
      "name":"Bom Conselho",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6883,
      "name":"Bom Despacho",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3193,
      "name":"Bom Jardim",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6306,
      "name":"Bom Jardim",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4693,
      "name":"Bom Jardim",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5093,
      "name":"Bom Jardim da Serra",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4326,
      "name":"Bom Jardim de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3289,
      "name":"Bom Jardim de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4808,
      "name":"Bom Jesus",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6067,
      "name":"Bom Jesus",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5543,
      "name":"Bom Jesus",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5095,
      "name":"Bom Jesus",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6988,
      "name":"Bom Jesus",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6229,
      "name":"Bom Jesus da Cachoeira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7549,
      "name":"Bom Jesus da Lapa",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3290,
      "name":"Bom Jesus da Penha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7833,
      "name":"Bom Jesus da Serra",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4736,
      "name":"Bom Jesus das Selvas",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5492,
      "name":"Bom Jesus de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3890,
      "name":"Bom Jesus do Amparo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":81720,
      "name":"Bom Jesus do Araguaia",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3291,
      "name":"Bom Jesus do Galho",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6307,
      "name":"Bom Jesus do Itabapoana",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8201,
      "name":"Bom Jesus do Norte",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5094,
      "name":"Bom Jesus do Oeste",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6308,
      "name":"Bom Jesus do Querendo",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4383,
      "name":"Bom Jesus dos Perd\u00f5es",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6683,
      "name":"Bom Jesus do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3586,
      "name":"Bom Jesus do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7707,
      "name":"Bom Jesus do Tocantins",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4737,
      "name":"Bom Lugar",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5544,
      "name":"Bom Princ\u00edpio",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6989,
      "name":"Bom Princ\u00edpio do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5545,
      "name":"Bom Progresso",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3119,
      "name":"Bom Repouso",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5096,
      "name":"Bom Retiro",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5546,
      "name":"Bom Retiro do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3292,
      "name":"Bom Sucesso",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5097,
      "name":"Bom Sucesso",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7599,
      "name":"Bom Sucesso",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4809,
      "name":"Bom Sucesso",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6685,
      "name":"Bom Sucesso",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4384,
      "name":"Bom Sucesso de Itarar\u00e9",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6684,
      "name":"Bom Sucesso do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5776,
      "name":"Bonfim",
      "state":"RR",
      "country":"BR  "
   },
   {
      "id":8554,
      "name":"Bonfim",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6990,
      "name":"Bonfim do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4385,
      "name":"Bonfim Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4327,
      "name":"Bonfin\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3142,
      "name":"Bonfin\u00f3polis de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4608,
      "name":"Boninal",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5927,
      "name":"Bonito",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6548,
      "name":"Bonito",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":7834,
      "name":"Bonito",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7268,
      "name":"Bonito",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8555,
      "name":"Bonito de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4810,
      "name":"Bonito de Santa F\u00e9",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4328,
      "name":"Bon\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4199,
      "name":"Boqueir\u00e3o",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5547,
      "name":"Boqueir\u00e3o do Le\u00e3o",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6991,
      "name":"Boqueir\u00e3o do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4506,
      "name":"Boquim",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":7835,
      "name":"Boquira",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4387,
      "name":"Bor\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4386,
      "name":"Borac\u00e9ia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6813,
      "name":"Borba",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":4388,
      "name":"Borborema",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7573,
      "name":"Borborema",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8556,
      "name":"Borda da Mata",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4389,
      "name":"Borebi",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5548,
      "name":"Boror\u00e9",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6686,
      "name":"Borraz\u00f3polis",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5549,
      "name":"Bossoroca",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6884,
      "name":"Botelhos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4390,
      "name":"Botucatu",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8557,
      "name":"Botumirim",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7836,
      "name":"Botupor\u00e3",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5098,
      "name":"Botuver\u00e1",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5550,
      "name":"Bozano",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5099,
      "name":"Bra\u00e7o do Norte",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5100,
      "name":"Bra\u00e7o do Trombudo",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5551,
      "name":"Braga",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7708,
      "name":"Bragan\u00e7a",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4391,
      "name":"Bragan\u00e7a Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6687,
      "name":"Braganey",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6688,
      "name":"Bragantina",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7728,
      "name":"Branquinha",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":9082,
      "name":"Brasil\u00e2ndia",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8558,
      "name":"Brasil\u00e2ndia de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6689,
      "name":"Brasil\u00e2ndia do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3587,
      "name":"Brasilandia do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4425,
      "name":"Brasil\u00e9ia",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":6992,
      "name":"Brasileira",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8173,
      "name":"Bras\u00edlia",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":6885,
      "name":"Bras\u00edlia de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7806,
      "name":"Brasil Novo",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":3130,
      "name":"Brasnorte",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3143,
      "name":"Bras\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3891,
      "name":"Br\u00e1s Pires",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4392,
      "name":"Bra\u00fana",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8559,
      "name":"Bra\u00fanas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3979,
      "name":"Brazabrantes",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8174,
      "name":"Brazl\u00e2ndia",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":7269,
      "name":"Brej\u00e3o",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8202,
      "name":"Brejetuba",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6068,
      "name":"Brejinho",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7270,
      "name":"Brejinho",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3588,
      "name":"Brejinho de Nazar\u00e9",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4224,
      "name":"Brejo",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4393,
      "name":"Brejo Alegre",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7271,
      "name":"Brejo da Madre de Deus",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4738,
      "name":"Brejo de Areia",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7574,
      "name":"Brejo do Cruz",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6995,
      "name":"Brejo do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7575,
      "name":"Brejo dos Santos",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7837,
      "name":"Brej\u00f5es",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4507,
      "name":"Brejo Grande",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":7807,
      "name":"Brejo Grande do Araguaia",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7838,
      "name":"Brejol\u00e2ndia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8024,
      "name":"Brejo Santo",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7808,
      "name":"Breu Branco",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7809,
      "name":"Breves",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4117,
      "name":"Brit\u00e2nia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5552,
      "name":"Brochier",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4394,
      "name":"Brodowski",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4395,
      "name":"Brotas",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7839,
      "name":"Brotas de Maca\u00fabas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8560,
      "name":"Brumadinho",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7840,
      "name":"Brumado",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5101,
      "name":"Brun\u00f3polis",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5102,
      "name":"Brusque",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5310,
      "name":"Bueno Brand\u00e3o",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8561,
      "name":"Buen\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7272,
      "name":"Buenos Aires",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7841,
      "name":"Buerarema",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8562,
      "name":"Bugre",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7273,
      "name":"Bu\u00edque",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7710,
      "name":"Bujari",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":7810,
      "name":"Bujaru",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8203,
      "name":"Burarama",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":4396,
      "name":"Buri",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4401,
      "name":"Buritama",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7600,
      "name":"Buriti",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8400,
      "name":"Buriti",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3936,
      "name":"Buriti Alegre",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4278,
      "name":"Buriti Bravo",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4187,
      "name":"Buriticupu",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4329,
      "name":"Buriti de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6998,
      "name":"Buriti dos Lopes",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6999,
      "name":"Buriti dos Montes",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3345,
      "name":"Buriti do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4330,
      "name":"Buritin\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7842,
      "name":"Buritirama",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4739,
      "name":"Buritirama",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7651,
      "name":"Buritis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5725,
      "name":"Buritis",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":4402,
      "name":"Buritizal",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6887,
      "name":"Buritizeiro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5553,
      "name":"Buti\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6309,
      "name":"B\u00fazios",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6814,
      "name":"Caapiranga",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7576,
      "name":"Caapor\u00e3",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5699,
      "name":"Caarap\u00f3",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":7843,
      "name":"Caatiba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7577,
      "name":"Cabaceiras",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7844,
      "name":"Cabaceiras do Paragua\u00e7u",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3128,
      "name":"Cabeceira Grande",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3133,
      "name":"Cabeceiras",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7000,
      "name":"Cabeceiras do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7578,
      "name":"Cabedelo",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5726,
      "name":"Cabixi",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":6353,
      "name":"Cabo de Santo Agostinho",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6310,
      "name":"Cabo de S\u00e3o Tom\u00e9",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6314,
      "name":"Cabo Frio",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3144,
      "name":"Cabo Verde",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4441,
      "name":"Cabr\u00e1lia Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4442,
      "name":"Cabre\u00fava",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7274,
      "name":"Cabrob\u00f3",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6315,
      "name":"Cabu\u00e7u",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5103,
      "name":"Ca\u00e7ador",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4443,
      "name":"Ca\u00e7apava",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5554,
      "name":"Ca\u00e7apava do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5727,
      "name":"Cacaul\u00e2ndia",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":5555,
      "name":"Cacequi",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6347,
      "name":"C\u00e1ceres",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7845,
      "name":"Cachoeira",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3356,
      "name":"Cachoeira Alta",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8563,
      "name":"Cachoeira da Prata",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4331,
      "name":"Cachoeira de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8564,
      "name":"Cachoeira de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3892,
      "name":"Cachoeira de Paje\u00fa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7811,
      "name":"Cachoeira do Arari",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6182,
      "name":"Cachoeira do Campo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9120,
      "name":"Cachoeira do Piri\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7579,
      "name":"Cachoeira dos \u00cdndios",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5556,
      "name":"Cachoeira do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":1868,
      "name":"Cachoeira Dourada",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3134,
      "name":"Cachoeira Dourada",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4740,
      "name":"Cachoeira Grande",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4444,
      "name":"Cachoeira Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6316,
      "name":"Cachoeiras de Macacu",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5557,
      "name":"Cachoeirinha",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3346,
      "name":"Cachoeirinha",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4204,
      "name":"Cachoeirinha",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8204,
      "name":"Cachoeiro de Itapemirim",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7580,
      "name":"Cacimba de Areia",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7581,
      "name":"Cacimba de Dentro",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7582,
      "name":"Cacimbas",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4254,
      "name":"Cacimbinhas",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5558,
      "name":"Cacique Doble",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5728,
      "name":"Cacoal",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":4445,
      "name":"Caconde",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5650,
      "name":"Ca\u00e7u",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7846,
      "name":"Cacul\u00e9",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4614,
      "name":"Ca\u00e9m",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8565,
      "name":"Caetan\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4609,
      "name":"Caetanos",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6888,
      "name":"Caet\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7275,
      "name":"Caet\u00e9s",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6819,
      "name":"Caetit\u00e9",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4610,
      "name":"Cafarnaum",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6690,
      "name":"Cafeara",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4446,
      "name":"Cafel\u00e2ndia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6691,
      "name":"Cafel\u00e2ndia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6692,
      "name":"Cafezal do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4447,
      "name":"Caiabu",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8566,
      "name":"Caiana",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3135,
      "name":"Caiap\u00f4nia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5559,
      "name":"Caibat\u00e9",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5104,
      "name":"Caibi",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5560,
      "name":"Cai\u00e7ara",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7583,
      "name":"Cai\u00e7ara",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6069,
      "name":"Cai\u00e7ara do Norte",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6070,
      "name":"Cai\u00e7ara do Rio do Vento",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6071,
      "name":"Caic\u00f3",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4448,
      "name":"Caieiras",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7847,
      "name":"Cairu",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4449,
      "name":"Caiu\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4450,
      "name":"Cajamar",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4741,
      "name":"Cajapi\u00f3",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4742,
      "name":"Cajari",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4451,
      "name":"Cajati",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7584,
      "name":"Cajazeiras",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7001,
      "name":"Cajazeiras do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7585,
      "name":"Cajazeirinhas",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4452,
      "name":"Cajobi",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7729,
      "name":"Cajueiro",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":7002,
      "name":"Cajueiro da Praia",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8567,
      "name":"Cajuri",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4453,
      "name":"Cajuru",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7276,
      "name":"Cal\u00e7ado",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7803,
      "name":"Cal\u00e7oene",
      "state":"AP",
      "country":"BR  "
   },
   {
      "id":1917,
      "name":"Caldas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7586,
      "name":"Caldas Brand\u00e3o",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":9144,
      "name":"Caldas do Jorro",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6526,
      "name":"Caldas Novas",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4332,
      "name":"Caldazinha",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7848,
      "name":"Caldeir\u00e3o Grande",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7003,
      "name":"Caldeir\u00e3o Grande do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6317,
      "name":"Calheiros",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6693,
      "name":"Calif\u00f3rnia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5105,
      "name":"Calmon",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6694,
      "name":"Cal\u00f3geras",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7277,
      "name":"Calumbi",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3188,
      "name":"Camacan",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7849,
      "name":"Cama\u00e7ari",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8568,
      "name":"Camacho",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6338,
      "name":"Camala\u00fa",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3189,
      "name":"Camamu",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":2518,
      "name":"Camanducaia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5700,
      "name":"Camapu\u00e3",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":5561,
      "name":"Camaqu\u00e3",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6354,
      "name":"Camaragibe",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5562,
      "name":"Camargo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6695,
      "name":"Cambar\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5563,
      "name":"Cambar\u00e1 do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6696,
      "name":"Camb\u00e9",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6697,
      "name":"Cambira",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5106,
      "name":"Cambori\u00fa",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6318,
      "name":"Cambuci",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3178,
      "name":"Cambu\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8569,
      "name":"Cambuquira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4454,
      "name":"Camburi",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":9121,
      "name":"Camet\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8025,
      "name":"Camocim",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7278,
      "name":"Camocim de S\u00e3o F\u00e9lix",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8570,
      "name":"Campan\u00e1rio",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8571,
      "name":"Campanha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7730,
      "name":"Campestre",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6889,
      "name":"Campestre",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5564,
      "name":"Campestre da Serra",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4333,
      "name":"Campestre de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4743,
      "name":"Campestre do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4334,
      "name":"Campina\u00e7u",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5107,
      "name":"Campina da Alegria",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6698,
      "name":"Campina da Lagoa",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5565,
      "name":"Campina das Miss\u00f5es",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4455,
      "name":"Campina do Monte Alegre",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6699,
      "name":"Campina do Sim\u00e3o",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7587,
      "name":"Campina Grande",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6700,
      "name":"Campina Grande do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4721,
      "name":"Campinal",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7601,
      "name":"Campin\u00e1polis",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4456,
      "name":"Campinas",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7004,
      "name":"Campinas do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5566,
      "name":"Campinas do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7652,
      "name":"Campina Verde",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4218,
      "name":"Campinorte",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5108,
      "name":"Campo Alegre",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7731,
      "name":"Campo Alegre",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3141,
      "name":"Campo Alegre de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7850,
      "name":"Campo Alegre de Lourdes",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7005,
      "name":"Campo Alegre do Fidalgo",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8572,
      "name":"Campo Azul",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6890,
      "name":"Campo Belo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5109,
      "name":"Campo Belo do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5567,
      "name":"Campo Bom",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6701,
      "name":"Campo Bonito",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7588,
      "name":"Campo de Santana",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4508,
      "name":"Campo do Brito",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6319,
      "name":"Campo do Coelho",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5330,
      "name":"Campo do Meio",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6702,
      "name":"Campo do Tenente",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5110,
      "name":"Campo Er\u00ea",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5185,
      "name":"Campo Florido",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7851,
      "name":"Campo Formoso",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7732,
      "name":"Campo Grande",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6340,
      "name":"Campo Grande",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6760,
      "name":"Campo Grande",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":5802,
      "name":"Campo Grande",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7007,
      "name":"Campo Grande do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6703,
      "name":"Campo Largo",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7008,
      "name":"Campo Largo do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":83453,
      "name":"Campo Limpo de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4457,
      "name":"Campo Limpo Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6704,
      "name":"Campo Magro",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7009,
      "name":"Campo Maior",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6705,
      "name":"Campo Mour\u00e3o",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5568,
      "name":"Campo Novo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5729,
      "name":"Campo Novo de Rond\u00f4nia",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":7602,
      "name":"Campo Novo do Parecis",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5803,
      "name":"Campo Redondo",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5678,
      "name":"Campos Altos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4100,
      "name":"Campos Belos",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5569,
      "name":"Campos Borges",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3227,
      "name":"Campos de J\u00falio",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4458,
      "name":"Campos do Jord\u00e3o",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6356,
      "name":"Campos dos Goytacazes",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6357,
      "name":"Campos El\u00edseos",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5371,
      "name":"Campos Gerais",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3347,
      "name":"Campos Lindos",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5111,
      "name":"Campos Novos",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4459,
      "name":"Campos Novos Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7571,
      "name":"Campos Sales",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4335,
      "name":"Campos Verdes",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7603,
      "name":"Campo Verde",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7279,
      "name":"Camutanga",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8573,
      "name":"Cana\u00e3",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9122,
      "name":"Cana\u00e3 dos Caraj\u00e1s",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4400,
      "name":"Cana Brava do Norte",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7733,
      "name":"Canaf\u00edstula",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":4460,
      "name":"Canan\u00e9ia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7734,
      "name":"Canapi",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":1899,
      "name":"Can\u00e1polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4611,
      "name":"Can\u00e1polis",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7604,
      "name":"Canarana",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7852,
      "name":"Canarana",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4461,
      "name":"Canas",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8574,
      "name":"Cana Verde",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7010,
      "name":"Canavieira",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6820,
      "name":"Canavieiras",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7853,
      "name":"Candeal",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7854,
      "name":"Candeias",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3184,
      "name":"Candeias",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5730,
      "name":"Candeias do Jamari",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":5570,
      "name":"Candel\u00e1ria",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7855,
      "name":"Candiba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6706,
      "name":"C\u00e2ndido de Abreu",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5571,
      "name":"C\u00e2ndido God\u00f3i",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4749,
      "name":"C\u00e2ndido Mendes",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4462,
      "name":"C\u00e2ndido Mota",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4463,
      "name":"C\u00e2ndido Rodrigues",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4512,
      "name":"C\u00e2ndido Sales",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5572,
      "name":"Candiota",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6707,
      "name":"Cand\u00f3i",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5573,
      "name":"Canela",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5112,
      "name":"Canelinha",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5804,
      "name":"Canguaretama",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5574,
      "name":"Cangu\u00e7u",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4509,
      "name":"Canhoba",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":7280,
      "name":"Canhotinho",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8026,
      "name":"Canind\u00e9",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4510,
      "name":"Canind\u00e9 de S\u00e3o Francisco",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4464,
      "name":"Canitar",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5575,
      "name":"Canoas",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4877,
      "name":"Canoeiros",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5113,
      "name":"Canoinhas",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7856,
      "name":"Cansan\u00e7\u00e3o",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":9143,
      "name":"Cant\u00e1",
      "state":"RR",
      "country":"BR  "
   },
   {
      "id":6358,
      "name":"Cantagalo",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6708,
      "name":"Cantagalo",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8575,
      "name":"Cantagalo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4744,
      "name":"Cantanhede",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7011,
      "name":"Canto do Buriti",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7857,
      "name":"Canudos",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5576,
      "name":"Canudos do Vale",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7775,
      "name":"Canutama",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":9123,
      "name":"Capanema",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6709,
      "name":"Capanema",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5114,
      "name":"Cap\u00e3o Alto",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4465,
      "name":"Cap\u00e3o Bonito",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5577,
      "name":"Cap\u00e3o Bonito do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5578,
      "name":"Cap\u00e3o da Canoa",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5579,
      "name":"Cap\u00e3o do Cip\u00f3",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5580,
      "name":"Cap\u00e3o do Le\u00e3o",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6891,
      "name":"Capara\u00f3",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4046,
      "name":"Capela",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":4511,
      "name":"Capela",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":5581,
      "name":"Capela de Santana",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4466,
      "name":"Capela do Alto",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7858,
      "name":"Capela do Alto Alegre",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8576,
      "name":"Capela Nova",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7653,
      "name":"Capelinha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8577,
      "name":"Capetinga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7589,
      "name":"Capim",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8578,
      "name":"Capim Branco",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7859,
      "name":"Capim Grosso",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":1914,
      "name":"Capin\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5115,
      "name":"Capinzal",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4745,
      "name":"Capinzal do Norte",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8027,
      "name":"Capistrano",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5582,
      "name":"Capit\u00e3o",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8579,
      "name":"Capit\u00e3o Andrade",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7012,
      "name":"Capit\u00e3o de Campos",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3444,
      "name":"Capit\u00e3o En\u00e9as",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7013,
      "name":"Capit\u00e3o Gerv\u00e1sio Oliveira",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6710,
      "name":"Capit\u00e3o Le\u00f4nidas Marques",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":9124,
      "name":"Capit\u00e3o Po\u00e7o",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":5186,
      "name":"Capit\u00f3lio",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4467,
      "name":"Capivari",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5116,
      "name":"Capivari de Baixo",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5583,
      "name":"Capivari do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7711,
      "name":"Capixaba",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":7281,
      "name":"Capoeiras",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6336,
      "name":"Caponga",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8580,
      "name":"Caputira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5584,
      "name":"Cara\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6359,
      "name":"Carabu\u00e7u",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5777,
      "name":"Caracara\u00ed",
      "state":"RR",
      "country":"BR  "
   },
   {
      "id":7014,
      "name":"Caracol",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3235,
      "name":"Caracol",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4468,
      "name":"Caraguatatuba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8581,
      "name":"Cara\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7860,
      "name":"Cara\u00edbas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3387,
      "name":"Cara\u00edva",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6032,
      "name":"Caraj\u00e1s",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6711,
      "name":"Carambe\u00ed",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8582,
      "name":"Carana\u00edba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8583,
      "name":"Caranda\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6892,
      "name":"Carangola",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6360,
      "name":"Carapebus",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4469,
      "name":"Carapicu\u00edba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8205,
      "name":"Carapina",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6893,
      "name":"Caratinga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7776,
      "name":"Carauari",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7590,
      "name":"Cara\u00fabas",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5805,
      "name":"Cara\u00fabas",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7015,
      "name":"Cara\u00fabas do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7861,
      "name":"Caravelas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5585,
      "name":"Carazinho",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6894,
      "name":"Carbonita",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4612,
      "name":"Cardeal da Silva",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4470,
      "name":"Cardoso",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6361,
      "name":"Cardoso Moreira",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8584,
      "name":"Carea\u00e7u",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7777,
      "name":"Careiro",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7778,
      "name":"Careiro da V\u00e1rzea",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":8206,
      "name":"Cariacica",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8028,
      "name":"Caridade",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7016,
      "name":"Caridade do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6821,
      "name":"Carinhanha",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3251,
      "name":"Carira",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":8029,
      "name":"Carir\u00e9",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8030,
      "name":"Cariria\u00e7u",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3348,
      "name":"Cariri do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8031,
      "name":"Cari\u00fas",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7605,
      "name":"Carlinda",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6712,
      "name":"Carl\u00f3polis",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5586,
      "name":"Carlos Barbosa",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3187,
      "name":"Carlos Chagas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5587,
      "name":"Carlos Gomes",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8585,
      "name":"Carm\u00e9sia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6362,
      "name":"Carmo",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6895,
      "name":"Carmo da Cachoeira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8586,
      "name":"Carmo da Mata",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3031,
      "name":"Carmo de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8587,
      "name":"Carmo do Cajuru",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5322,
      "name":"Carmo do Parana\u00edba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6896,
      "name":"Carmo do Rio Claro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4336,
      "name":"Carmo do Rio Verde",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3349,
      "name":"Carmol\u00e2ndia",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4513,
      "name":"Carm\u00f3polis",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":8588,
      "name":"Carm\u00f3polis de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7282,
      "name":"Carna\u00edba",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7862,
      "name":"Carna\u00edba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7863,
      "name":"Carna\u00edba do Sert\u00e3o",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5806,
      "name":"Carna\u00faba dos Dantas",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5807,
      "name":"Carnaubais",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8032,
      "name":"Carnaubal",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7283,
      "name":"Carnaubeira da Penha",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8589,
      "name":"Carneirinho",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7735,
      "name":"Carneiros",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5778,
      "name":"Caroebe",
      "state":"RR",
      "country":"BR  "
   },
   {
      "id":6865,
      "name":"Carolina",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7284,
      "name":"Carpina",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8590,
      "name":"Carrancas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7591,
      "name":"Carrapateira",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3350,
      "name":"Carrasco Bonito",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":6355,
      "name":"Caruaru",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4746,
      "name":"Carutapera",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8591,
      "name":"Carvalh\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8592,
      "name":"Carvalhos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7779,
      "name":"Carvoeiro",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":4471,
      "name":"Casa Branca",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8593,
      "name":"Casa Grande",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6418,
      "name":"Casa Nova",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5588,
      "name":"Casca",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8594,
      "name":"Cascalho Rico",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6713,
      "name":"Cascavel",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6238,
      "name":"Cascavel",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8033,
      "name":"Cascavel",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3351,
      "name":"Caseara",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5589,
      "name":"Caseiros",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6363,
      "name":"Casimiro de Abreu",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7285,
      "name":"Casinhas",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7592,
      "name":"Casserengue",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3060,
      "name":"C\u00e1ssia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4472,
      "name":"C\u00e1ssia dos Coqueiros",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7672,
      "name":"Cassil\u00e2ndia",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":5590,
      "name":"Cassino",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":9125,
      "name":"Castanhal",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7606,
      "name":"Castanheira",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5731,
      "name":"Castanheiras",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":3937,
      "name":"Castel\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8207,
      "name":"Castelo",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7017,
      "name":"Castelo do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4473,
      "name":"Castilho",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3357,
      "name":"Castro",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6419,
      "name":"Castro Alves",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6897,
      "name":"Cataguases",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7533,
      "name":"Catal\u00e3o",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4474,
      "name":"Catanduva",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5117,
      "name":"Catanduvas",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6714,
      "name":"Catanduvas",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8034,
      "name":"Catarina",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3893,
      "name":"Catas Altas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8595,
      "name":"Catas Altas da Noruega",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4710,
      "name":"Catende",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4475,
      "name":"Catigu\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6325,
      "name":"Catingal",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7593,
      "name":"Catingueira",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4613,
      "name":"Catol\u00e2ndia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7328,
      "name":"Catol\u00e9 do Rocha",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6420,
      "name":"Catu",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5591,
      "name":"Catu\u00edpe",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8596,
      "name":"Catuji",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8035,
      "name":"Catunda",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4337,
      "name":"Catura\u00ed",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4009,
      "name":"Caturama",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7329,
      "name":"Caturit\u00e9",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8597,
      "name":"Catuti",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8036,
      "name":"Caucaia",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5199,
      "name":"Cavalcante",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6311,
      "name":"Cavalheiro",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6530,
      "name":"Caxambu",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5118,
      "name":"Caxambu do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8401,
      "name":"Caxias",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5592,
      "name":"Caxias do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7018,
      "name":"Caxing\u00f3",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5808,
      "name":"Cear\u00e1-Mirim",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4279,
      "name":"Cedral",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4476,
      "name":"Cedral",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8037,
      "name":"Cedro",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7286,
      "name":"Cedro",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4515,
      "name":"Cedro de S\u00e3o Jo\u00e3o",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":8598,
      "name":"Cedro do Abaet\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8175,
      "name":"Ceil\u00e2ndia",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":5119,
      "name":"Celso Ramos",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5593,
      "name":"Centen\u00e1rio",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3352,
      "name":"Centen\u00e1rio",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3214,
      "name":"Centen\u00e1rio do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6421,
      "name":"Central",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8599,
      "name":"Central de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4747,
      "name":"Central do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":2013,
      "name":"Centralina",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4748,
      "name":"Centro do Guilherme",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8402,
      "name":"Centro Novo do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4720,
      "name":"Cerejeiras",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":3980,
      "name":"Ceres",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4477,
      "name":"Cerqueira C\u00e9sar",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4478,
      "name":"Cerquilho",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5594,
      "name":"Cerrito",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6715,
      "name":"Cerro Azul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5595,
      "name":"Cerro Branco",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4718,
      "name":"Cerro Cor\u00e1",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5597,
      "name":"Cerro Grande",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5596,
      "name":"Cerro Grande do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5598,
      "name":"Cerro Largo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4888,
      "name":"Cerro Negro",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4479,
      "name":"Ces\u00e1rio Lange",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6716,
      "name":"C\u00e9u Azul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4338,
      "name":"Cezarina",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8600,
      "name":"Ch\u00e1cara",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7287,
      "name":"Ch\u00e3 de Alegria",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7288,
      "name":"Ch\u00e3 Grande",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8601,
      "name":"Chal\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5599,
      "name":"Chapada",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3353,
      "name":"Chapada da Natividade",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3358,
      "name":"Chapada de Areia",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8602,
      "name":"Chapada do Norte",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7607,
      "name":"Chapada dos Guimar\u00e3es",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3208,
      "name":"Chapada Ga\u00facha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3136,
      "name":"Chapad\u00e3o do C\u00e9u",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4889,
      "name":"Chapad\u00e3o do Lageado",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7673,
      "name":"Chapad\u00e3o do Sul",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":7667,
      "name":"Chapadinha",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4890,
      "name":"Chapec\u00f3",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7736,
      "name":"Ch\u00e3 Preta",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":4480,
      "name":"Charqueada",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5600,
      "name":"Charqueadas",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5601,
      "name":"Charrua",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8038,
      "name":"Chaval",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4481,
      "name":"Chavantes",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":9126,
      "name":"Chaves",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8603,
      "name":"Chiador",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5602,
      "name":"Chiapetta",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6717,
      "name":"Chopinzinho",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8039,
      "name":"Chor\u00f3",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8040,
      "name":"Chorozinho",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4615,
      "name":"Chorroch\u00f3",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5605,
      "name":"Chu\u00ed",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3988,
      "name":"Chumbo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5732,
      "name":"Chupinguaia",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":5608,
      "name":"Chuvisca",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6718,
      "name":"Cianorte",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6423,
      "name":"C\u00edcero Dantas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6719,
      "name":"Cidade Ga\u00facha",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5342,
      "name":"Cidade Ocidental",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4068,
      "name":"Cidel\u00e2ndia",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5622,
      "name":"Cidreira",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6822,
      "name":"Cip\u00f3",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8604,
      "name":"Cipot\u00e2nea",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5628,
      "name":"Cir\u00edaco",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6188,
      "name":"Cisneiros",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3182,
      "name":"Claraval",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8605,
      "name":"Claro dos Po\u00e7\u00f5es",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4072,
      "name":"Cl\u00e1udia",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8606,
      "name":"Cl\u00e1udio",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4020,
      "name":"Clementina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6720,
      "name":"Clevel\u00e2ndia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3230,
      "name":"Coaraci",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7542,
      "name":"Coari",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7021,
      "name":"Cocal",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7019,
      "name":"Cocal de Telha",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7020,
      "name":"Cocal dos Alves",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4891,
      "name":"Cocal do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7608,
      "name":"Cocalinho",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3137,
      "name":"Cocalzinho de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3998,
      "name":"Cocos",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6815,
      "name":"Codaj\u00e1s",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":8403,
      "name":"Cod\u00f3",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6364,
      "name":"Coelho da Rocha",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8404,
      "name":"Coelho Neto",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8607,
      "name":"Coimbra",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4439,
      "name":"Coimbra",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":7737,
      "name":"Coit\u00e9 do N\u00f3ia",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":7022,
      "name":"Coivaras",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":9127,
      "name":"Colares",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8208,
      "name":"Colatina",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7609,
      "name":"Col\u00edder",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4021,
      "name":"Colina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7668,
      "name":"Colinas",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5629,
      "name":"Colinas",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4339,
      "name":"Colinas do Sul",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3359,
      "name":"Colinas do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3360,
      "name":"Colm\u00e9ia",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7610,
      "name":"Colniza",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4022,
      "name":"Col\u00f4mbia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6721,
      "name":"Colombo",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6365,
      "name":"Col\u00f4nia",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4209,
      "name":"Col\u00f4nia do Gurgu\u00e9ia",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7023,
      "name":"Col\u00f4nia do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7738,
      "name":"Col\u00f4nia Leopoldina",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5630,
      "name":"Col\u00f4nia Nova",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5631,
      "name":"Colorado",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3249,
      "name":"Colorado",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5733,
      "name":"Colorado do Oeste",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":8608,
      "name":"Coluna",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3361,
      "name":"Combinado",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8609,
      "name":"Comendador Gomes",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6366,
      "name":"Comendador Levy Gasparian",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8610,
      "name":"Comercinho",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7611,
      "name":"Comodoro",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3183,
      "name":"Concei\u00e7\u00e3o",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3168,
      "name":"Concei\u00e7\u00e3o da Aparecida",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8209,
      "name":"Concei\u00e7\u00e3o da Barra",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6234,
      "name":"Concei\u00e7\u00e3o da Barra de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4149,
      "name":"Concei\u00e7\u00e3o da Feira",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7654,
      "name":"Concei\u00e7\u00e3o das Alagoas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8611,
      "name":"Concei\u00e7\u00e3o das Pedras",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8612,
      "name":"Concei\u00e7\u00e3o de Ipanema",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6367,
      "name":"Concei\u00e7\u00e3o de Jacare\u00ed",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6368,
      "name":"Concei\u00e7\u00e3o de Macabu",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4150,
      "name":"Concei\u00e7\u00e3o do Almeida",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":9128,
      "name":"Concei\u00e7\u00e3o do Araguaia",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7024,
      "name":"Concei\u00e7\u00e3o do Canind\u00e9",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6185,
      "name":"Concei\u00e7\u00e3o do Capim",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8210,
      "name":"Concei\u00e7\u00e3o do Castelo",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":3117,
      "name":"Concei\u00e7\u00e3o do Coit\u00e9",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4031,
      "name":"Concei\u00e7\u00e3o do Ibitipoca",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4151,
      "name":"Concei\u00e7\u00e3o do Jacu\u00edpe",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8405,
      "name":"Concei\u00e7\u00e3o do Lago A\u00e7u",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3397,
      "name":"Concei\u00e7\u00e3o do Mato Dentro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8613,
      "name":"Concei\u00e7\u00e3o do Par\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3239,
      "name":"Concei\u00e7\u00e3o do Rio Verde",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8614,
      "name":"Concei\u00e7\u00e3o dos Ouros",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3362,
      "name":"Concei\u00e7\u00e3o do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4029,
      "name":"Conchal",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4030,
      "name":"Conchas",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4892,
      "name":"Conc\u00f3rdia",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":9129,
      "name":"Conc\u00f3rdia do Par\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7289,
      "name":"Condado",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7330,
      "name":"Condado",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7550,
      "name":"Conde",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7331,
      "name":"Conde",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6422,
      "name":"Conde\u00faba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5632,
      "name":"Condor",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8615,
      "name":"C\u00f4nego Marinho",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8616,
      "name":"Confins",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7612,
      "name":"Confresa",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7332,
      "name":"Congo",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5311,
      "name":"Congonhal",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6898,
      "name":"Congonhas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8617,
      "name":"Congonhas do Norte",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6722,
      "name":"Congonhinhas",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3153,
      "name":"Conquista",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6233,
      "name":"Conquista d'Oeste",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6899,
      "name":"Conselheiro Lafaiete",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3180,
      "name":"Conselheiro Mairinck",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8618,
      "name":"Conselheiro Pena",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6369,
      "name":"Conservat\u00f3ria",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8619,
      "name":"Consola\u00e7\u00e3o",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5633,
      "name":"Constantina",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6900,
      "name":"Contagem",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6723,
      "name":"Contenda",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4215,
      "name":"Contendas do Sincor\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8620,
      "name":"Coqueiral",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8211,
      "name":"Coqueiral",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5634,
      "name":"Coqueiro Baixo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5635,
      "name":"Coqueiros do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7739,
      "name":"Coqueiro Seco",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8621,
      "name":"Cora\u00e7\u00e3o de Jesus",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4428,
      "name":"Cora\u00e7\u00e3o de Maria",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6724,
      "name":"Corb\u00e9lia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6370,
      "name":"Cordeiro",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4035,
      "name":"Cordeir\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4090,
      "name":"Cordeiros",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4893,
      "name":"Cordilheira Alta",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8622,
      "name":"Cordisburgo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8623,
      "name":"Cordisl\u00e2ndia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8041,
      "name":"Corea\u00fa",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7333,
      "name":"Coremas",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4128,
      "name":"Corguinho",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4055,
      "name":"Coribe",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8624,
      "name":"Corinto",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6725,
      "name":"Corn\u00e9lio Proc\u00f3pio",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8625,
      "name":"Coroaci",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4036,
      "name":"Coroados",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8406,
      "name":"Coroat\u00e1",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5679,
      "name":"Coromandel",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5636,
      "name":"Coronel Barros",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5637,
      "name":"Coronel Bicaco",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6726,
      "name":"Coronel Domingos Soares",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5809,
      "name":"Coronel Ezequiel",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8626,
      "name":"Coronel Fabriciano",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4894,
      "name":"Coronel Freitas",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5810,
      "name":"Coronel Jo\u00e3o Pessoa",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4618,
      "name":"Coronel Jo\u00e3o S\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7025,
      "name":"Coronel Jos\u00e9 Dias",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4037,
      "name":"Coronel Macedo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4895,
      "name":"Coronel Martins",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8627,
      "name":"Coronel Murta",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8628,
      "name":"Coronel Pacheco",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":83454,
      "name":"Coronel Pilar",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7613,
      "name":"Coronel Ponce",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":9083,
      "name":"Coronel Sapucaia",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6727,
      "name":"Coronel Vivida",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8629,
      "name":"Coronel Xavier Chaves",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8630,
      "name":"C\u00f3rrego Danta",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6371,
      "name":"C\u00f3rrego da Prata",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8631,
      "name":"C\u00f3rrego do Bom Jesus",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5651,
      "name":"C\u00f3rrego do Ouro",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6331,
      "name":"C\u00f3rrego do Ouro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6372,
      "name":"C\u00f3rrego do Ouro",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8632,
      "name":"C\u00f3rrego Fundo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8633,
      "name":"C\u00f3rrego Novo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4896,
      "name":"Correia Pinto",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7026,
      "name":"Corrente",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4205,
      "name":"Correntes",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6373,
      "name":"Correntezas",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7551,
      "name":"Correntina",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7290,
      "name":"Cort\u00eas",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6549,
      "name":"Corumb\u00e1",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":2598,
      "name":"Corumb\u00e1 de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4118,
      "name":"Corumba\u00edba",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4038,
      "name":"Corumbata\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6728,
      "name":"Corumbata\u00ed do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5734,
      "name":"Corumbiara",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":4897,
      "name":"Corup\u00e1",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7740,
      "name":"Coruripe",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":4039,
      "name":"Cosm\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4040,
      "name":"Cosmorama",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3969,
      "name":"Costa do Sau\u00edpe",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5735,
      "name":"Costa Marques",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":5701,
      "name":"Costa Rica",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4152,
      "name":"Cotegipe",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4041,
      "name":"Cotia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5638,
      "name":"Cotipor\u00e3",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7614,
      "name":"Cotrigua\u00e7u",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8634,
      "name":"Couto de Magalh\u00e3es de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3363,
      "name":"Couto Magalh\u00e3es",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5639,
      "name":"Coxilha",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":9084,
      "name":"Coxim",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":7334,
      "name":"Coxixola",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7741,
      "name":"Cra\u00edbas",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8042,
      "name":"Crate\u00fas",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5617,
      "name":"Crato",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4042,
      "name":"Cravinhos",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4429,
      "name":"Cravol\u00e2ndia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4898,
      "name":"Crici\u00fama",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3293,
      "name":"Cris\u00f3lia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8635,
      "name":"Cris\u00f3lita",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4153,
      "name":"Cris\u00f3polis",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5640,
      "name":"Crissiumal",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8636,
      "name":"Cristais",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4043,
      "name":"Cristais Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5375,
      "name":"Cristal",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3364,
      "name":"Cristal\u00e2ndia",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7027,
      "name":"Cristal\u00e2ndia do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8212,
      "name":"Cristal do Norte",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5641,
      "name":"Cristal do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8637,
      "name":"Crist\u00e1lia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4440,
      "name":"Cristalina",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":7534,
      "name":"Cristalina",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8638,
      "name":"Cristiano Otoni",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3981,
      "name":"Cristian\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8639,
      "name":"Cristina",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4516,
      "name":"Cristin\u00e1polis",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":7028,
      "name":"Cristino Castro",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4619,
      "name":"Crist\u00f3polis",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5379,
      "name":"Cri\u00fava",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3853,
      "name":"Crix\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3365,
      "name":"Crix\u00e1s do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8043,
      "name":"Croat\u00e1",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4065,
      "name":"Crom\u00ednia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8640,
      "name":"Crucil\u00e2ndia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8044,
      "name":"Cruz",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4044,
      "name":"Cruz\u00e1lia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5380,
      "name":"Cruz Alta",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5381,
      "name":"Cruzaltense",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7552,
      "name":"Cruz das Almas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7335,
      "name":"Cruz do Esp\u00edrito Santo",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8176,
      "name":"Cruzeiro",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":4045,
      "name":"Cruzeiro",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8641,
      "name":"Cruzeiro da Fortaleza",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6729,
      "name":"Cruzeiro do Igua\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3215,
      "name":"Cruzeiro do Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5382,
      "name":"Cruzeiro do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4908,
      "name":"Cruzeiro do Sul",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":3250,
      "name":"Cruzeiro do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5811,
      "name":"Cruzeta",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8642,
      "name":"Cruz\u00edlia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3186,
      "name":"Cruz Machado",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6730,
      "name":"Cruzmaltina",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4047,
      "name":"Cubat\u00e3o",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7336,
      "name":"Cubati",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7615,
      "name":"Cuiab\u00e1",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4690,
      "name":"Cuit\u00e9",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7337,
      "name":"Cuit\u00e9 de Mamanguape",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7338,
      "name":"Cuitegi",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5736,
      "name":"Cujubim",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":4101,
      "name":"Cumari",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7291,
      "name":"Cumaru",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":9130,
      "name":"Cumaru do Norte",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4517,
      "name":"Cumbe",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6187,
      "name":"Cumuruxatiba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4048,
      "name":"Cunha",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4899,
      "name":"Cunha Por\u00e3",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4900,
      "name":"Cunhata\u00ed",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8643,
      "name":"Cuparaque",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7292,
      "name":"Cupira",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7864,
      "name":"Cura\u00e7\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7029,
      "name":"Curimat\u00e1",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4034,
      "name":"Curion\u00f3polis",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6731,
      "name":"Curitiba",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4901,
      "name":"Curitibanos",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6732,
      "name":"Curi\u00fava",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7030,
      "name":"Currais",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5812,
      "name":"Currais Novos",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7339,
      "name":"Curral de Cima",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8644,
      "name":"Curral de Dentro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9131,
      "name":"Curralinho",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7031,
      "name":"Curralinhos",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7032,
      "name":"Curral Novo do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7340,
      "name":"Curral Velho",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":9132,
      "name":"Curu\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":9133,
      "name":"Curu\u00e7\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":5383,
      "name":"Curumim",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8407,
      "name":"Cururupu",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4320,
      "name":"Curvel\u00e2ndia",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8645,
      "name":"Curvelo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4206,
      "name":"Custodia",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7804,
      "name":"Cutias",
      "state":"AP",
      "country":"BR  "
   },
   {
      "id":4340,
      "name":"Damian\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7341,
      "name":"Dami\u00e3o",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4341,
      "name":"Damol\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3366,
      "name":"Darcin\u00f3polis",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3999,
      "name":"D\u00e1rio Meira",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8646,
      "name":"Datas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5384,
      "name":"David Canabarro",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4023,
      "name":"Davin\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4750,
      "name":"Davin\u00f3polis",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6531,
      "name":"Delfim Moreira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3120,
      "name":"Delfin\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5215,
      "name":"Delmiro Gouveia",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8647,
      "name":"Delta",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7033,
      "name":"Demerval Lob\u00e3o",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4033,
      "name":"Denise",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5702,
      "name":"Deod\u00e1polis",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8045,
      "name":"Deputado Irapuan Pinheiro",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5385,
      "name":"Derrubadas",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4051,
      "name":"Descalvado",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4902,
      "name":"Descanso",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8648,
      "name":"Descoberto",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7342,
      "name":"Desterro",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3398,
      "name":"Desterro de Entre Rios",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8649,
      "name":"Desterro do Melo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6733,
      "name":"Dez de Maio",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5386,
      "name":"Dezesseis de Novembro",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4052,
      "name":"Diadema",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7343,
      "name":"Diamante",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6734,
      "name":"Diamante d'Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6735,
      "name":"Diamante do Norte",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6740,
      "name":"Diamante do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7655,
      "name":"Diamantina",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7616,
      "name":"Diamantino",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3367,
      "name":"Dian\u00f3polis",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4056,
      "name":"Dias d'\u00c1vila",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5388,
      "name":"Dilermando de Aguiar",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8650,
      "name":"Diogo de Vasconcelos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8651,
      "name":"Dion\u00edsio",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4903,
      "name":"Dion\u00edsio Cerqueira",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4342,
      "name":"Diorama",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4053,
      "name":"Dirce Reis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7034,
      "name":"Dirceu Arcoverde",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4518,
      "name":"Divina Pastora",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":8652,
      "name":"Divin\u00e9sia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3170,
      "name":"Divino",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3399,
      "name":"Divino das Laranjeiras",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3392,
      "name":"Divino de S\u00e3o Louren\u00e7o",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":4054,
      "name":"Divinol\u00e2ndia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8653,
      "name":"Divinol\u00e2ndia de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8654,
      "name":"Divin\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4343,
      "name":"Divin\u00f3polis de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3368,
      "name":"Divin\u00f3polis do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8655,
      "name":"Divisa Alegre",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8656,
      "name":"Divisa Nova",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8657,
      "name":"Divis\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4061,
      "name":"Dobrada",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4062,
      "name":"Dois C\u00f3rregos",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5394,
      "name":"Dois Irm\u00e3os",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5391,
      "name":"Dois Irm\u00e3os das Miss\u00f5es",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4032,
      "name":"Dois Irm\u00e3os do Buriti",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3369,
      "name":"Dois Irm\u00e3os do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5397,
      "name":"Dois Lajeados",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4563,
      "name":"Dois Riachos",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6741,
      "name":"Dois Vizinhos",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4063,
      "name":"Dolcin\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7617,
      "name":"Dom Aquino",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4091,
      "name":"Dom Bas\u00edlio",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4070,
      "name":"Dom Bosco",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8658,
      "name":"Dom Cavati",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3951,
      "name":"Dom Eliseu",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7035,
      "name":"Dom Expedito Lopes",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5398,
      "name":"Dom Feliciano",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8213,
      "name":"Domingos Martins",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7036,
      "name":"Domingos Mour\u00e3o",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7037,
      "name":"Dom Inoc\u00eancio",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8659,
      "name":"Dom Joaquim",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4154,
      "name":"Dom Macedo Costa",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5399,
      "name":"Dom Pedrito",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6034,
      "name":"Dom Pedro",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5400,
      "name":"Dom Pedro de Alc\u00e2ntara",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8660,
      "name":"Dom Silv\u00e9rio",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8661,
      "name":"Dom Vi\u00e7oso",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4904,
      "name":"Dona Emma",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8662,
      "name":"Dona Euz\u00e9bia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5401,
      "name":"Dona Francisca",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7344,
      "name":"Dona In\u00eas",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6374,
      "name":"Dor\u00e2ndia",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8663,
      "name":"Dores de Campos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8664,
      "name":"Dores de Guanh\u00e3es",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3885,
      "name":"Dores do Indai\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8214,
      "name":"Dores do Rio Preto",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8665,
      "name":"Dores do Turvo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8666,
      "name":"Dores\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6742,
      "name":"Dorizon",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7293,
      "name":"Dormentes",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3244,
      "name":"Douradina",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3151,
      "name":"Douradina",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4064,
      "name":"Dourado",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8667,
      "name":"Douradoquara",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6761,
      "name":"Dourados",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6743,
      "name":"Doutor Ant\u00f4nio Paranhos",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6744,
      "name":"Doutor Camargo",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5402,
      "name":"Doutor Maur\u00edcio Cardoso",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4905,
      "name":"Doutor Pedrinho",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5403,
      "name":"Doutor Ricardo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5813,
      "name":"Doutor Severiano",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6745,
      "name":"Doutor Ulysses",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4024,
      "name":"Doverl\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4069,
      "name":"Dracena",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4075,
      "name":"Duartina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6072,
      "name":"Duas Barras",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7345,
      "name":"Duas Estradas",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3371,
      "name":"Duer\u00e9",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4076,
      "name":"Dumont",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4703,
      "name":"Duplo C\u00e9u",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8408,
      "name":"Duque Bacelar",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6073,
      "name":"Duque de Caxias",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8668,
      "name":"Durand\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4077,
      "name":"Echapor\u00e3",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8215,
      "name":"Ecoporanga",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":3138,
      "name":"Edealina",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3139,
      "name":"Ed\u00e9ia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5902,
      "name":"Eirunep\u00e9",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":5703,
      "name":"Eldorado",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4078,
      "name":"Eldorado",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":9134,
      "name":"Eldorado dos Caraj\u00e1s",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":5404,
      "name":"Eldorado do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7038,
      "name":"Elesb\u00e3o Veloso",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4079,
      "name":"Elias Fausto",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7039,
      "name":"Eliseu Martins",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5079,
      "name":"Elisi\u00e1rio",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7865,
      "name":"El\u00edsio Medrado",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6532,
      "name":"El\u00f3i Mendes",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7346,
      "name":"Emas",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4080,
      "name":"Emba\u00faba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4082,
      "name":"Embu das Artes",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4081,
      "name":"Embu-Gua\u00e7u",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4083,
      "name":"Emilian\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5405,
      "name":"Encantado",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6746,
      "name":"Encantado d'Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5814,
      "name":"Encanto",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7866,
      "name":"Encruzilhada",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5406,
      "name":"Encruzilhada do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3463,
      "name":"En\u00e9as Marques",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6747,
      "name":"Engenheiro Beltr\u00e3o",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8669,
      "name":"Engenheiro Caldas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4084,
      "name":"Engenheiro Coelho",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8670,
      "name":"Engenheiro Navarro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6074,
      "name":"Engenheiro Passos",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6075,
      "name":"Engenheiro Paulo de Frontin",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6326,
      "name":"Engenheiro Pontes",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5407,
      "name":"Engenho Velho",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4906,
      "name":"Enseada de Brito",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8671,
      "name":"Entre Folhas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5408,
      "name":"Entre-Iju\u00eds",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6762,
      "name":"Entre Rios",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4907,
      "name":"Entre Rios",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7867,
      "name":"Entre Rios",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8672,
      "name":"Entre Rios de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6748,
      "name":"Entre Rios do Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5409,
      "name":"Entre Rios do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5903,
      "name":"Envira",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7712,
      "name":"Epitaciol\u00e2ndia",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":5815,
      "name":"Equador",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5410,
      "name":"Erebango",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5411,
      "name":"Erechim",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8046,
      "name":"Erer\u00ea",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7868,
      "name":"\u00c9rico Cardoso",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4909,
      "name":"Ermo",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5412,
      "name":"Ernestina",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5413,
      "name":"Erval Grande",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8673,
      "name":"Erv\u00e1lia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5414,
      "name":"Erval Seco",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4912,
      "name":"Erval Velho",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7294,
      "name":"Escada",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5415,
      "name":"Esmeralda",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8674,
      "name":"Esmeraldas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8675,
      "name":"Espera Feliz",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7347,
      "name":"Esperan\u00e7a",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5416,
      "name":"Esperan\u00e7a do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6763,
      "name":"Esperan\u00e7a Nova",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3372,
      "name":"Esperantina",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7040,
      "name":"Esperantina",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4096,
      "name":"Esperantin\u00f3polis",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6764,
      "name":"Espig\u00e3o Alto do Igua\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5737,
      "name":"Espig\u00e3o do Oeste",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":7656,
      "name":"Espinosa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5816,
      "name":"Esp\u00edrito Santo",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3400,
      "name":"Esp\u00edrito Santo do Dourado",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4085,
      "name":"Esp\u00edrito Santo do Pinhal",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4087,
      "name":"Esp\u00edrito Santo do Turvo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7869,
      "name":"Esplanada",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5417,
      "name":"Espumoso",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5418,
      "name":"Esta\u00e7\u00e3o",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4519,
      "name":"Est\u00e2ncia",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":3375,
      "name":"Est\u00e2ncia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5419,
      "name":"Est\u00e2ncia Velha",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5420,
      "name":"Esteio",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6312,
      "name":"Esteios",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8676,
      "name":"Estiva",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4088,
      "name":"Estiva Gerbi",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6076,
      "name":"Estrada Nova",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4097,
      "name":"Estreito",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5421,
      "name":"Estrela",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8677,
      "name":"Estrela Dalva",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4564,
      "name":"Estrela de Alagoas",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":4089,
      "name":"Estrela d'Oeste",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8678,
      "name":"Estrela do Indai\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4115,
      "name":"Estrela do Norte",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4344,
      "name":"Estrela do Norte",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3154,
      "name":"Estrela do Sul",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5422,
      "name":"Estrela Velha",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7553,
      "name":"Euclides da Cunha",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4116,
      "name":"Euclides da Cunha Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5423,
      "name":"Eug\u00eanio de Castro",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8679,
      "name":"Eugen\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3223,
      "name":"Eun\u00e1polis",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8047,
      "name":"Eus\u00e9bio",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8680,
      "name":"Ewbank da C\u00e2mara",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5312,
      "name":"Extrema",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5817,
      "name":"Extremoz",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7295,
      "name":"Exu",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7348,
      "name":"Fagundes",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5424,
      "name":"Fagundes Varela",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4345,
      "name":"Faina",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6077,
      "name":"Falc\u00e3o",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6533,
      "name":"Fama",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8681,
      "name":"Faria Lemos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8048,
      "name":"Farias Brito",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7444,
      "name":"Faro",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6766,
      "name":"Farol",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5425,
      "name":"Farroupilha",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4131,
      "name":"Fartura",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7041,
      "name":"Fartura do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4010,
      "name":"F\u00e1tima",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3373,
      "name":"F\u00e1tima",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5704,
      "name":"F\u00e1tima do Sul",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6768,
      "name":"Faxinal",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6767,
      "name":"Faxinal do C\u00e9u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4913,
      "name":"Faxinal dos Guedes",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5426,
      "name":"Faxinal do Soturno",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5427,
      "name":"Faxinalzinho",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4219,
      "name":"Fazenda Nova",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6769,
      "name":"Fazenda Rio Grande",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5428,
      "name":"Fazenda Vilanova",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6804,
      "name":"Feij\u00f3",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":4259,
      "name":"Feira da Mata",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7554,
      "name":"Feira de Santana",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4565,
      "name":"Feira Grande",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":7296,
      "name":"Feira Nova",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4520,
      "name":"Feira Nova",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4751,
      "name":"Feira Nova do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8682,
      "name":"Fel\u00edcio dos Santos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5818,
      "name":"Felipe Guerra",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8683,
      "name":"Felisburgo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8684,
      "name":"Felixl\u00e2ndia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5429,
      "name":"Feliz",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4566,
      "name":"Feliz Deserto",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3991,
      "name":"Feliz Natal",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6770,
      "name":"F\u00eanix",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6771,
      "name":"Fernandes Pinheiro",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8685,
      "name":"Fernandes Tourinho",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7297,
      "name":"Fernando de Noronha",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4752,
      "name":"Fernando Falc\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5819,
      "name":"Fernando Pedroza",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4132,
      "name":"Fernand\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4133,
      "name":"Fernando Prestes",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4134,
      "name":"Fern\u00e3o",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4135,
      "name":"Ferraz de Vasconcelos",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7805,
      "name":"Ferreira Gomes",
      "state":"AP",
      "country":"BR  "
   },
   {
      "id":7298,
      "name":"Ferreiros",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8686,
      "name":"Ferros",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8687,
      "name":"Fervedouro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6772,
      "name":"Figueira",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4500,
      "name":"Figueir\u00e3o",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3374,
      "name":"Figueir\u00f3polis",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7618,
      "name":"Figueir\u00f3polis d'Oeste",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3200,
      "name":"Filad\u00e9lfia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3376,
      "name":"Filad\u00e9lfia",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3231,
      "name":"Firmino Alves",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3380,
      "name":"Firmin\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4567,
      "name":"Flexeiras",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6773,
      "name":"Flora\u00ed",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5820,
      "name":"Flor\u00e2nia",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4138,
      "name":"Flora Rica",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6774,
      "name":"Flor da Serra do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4914,
      "name":"Flor do Sert\u00e3o",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4141,
      "name":"Floreal",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7299,
      "name":"Flores",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5430,
      "name":"Flores da Cunha",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4119,
      "name":"Flores de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7042,
      "name":"Flores do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6775,
      "name":"Floresta",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7300,
      "name":"Floresta",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4092,
      "name":"Floresta Azul",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7445,
      "name":"Floresta do Araguaia",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7043,
      "name":"Floresta do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7657,
      "name":"Florestal",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6776,
      "name":"Florest\u00f3polis",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6078,
      "name":"Floriano",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7044,
      "name":"Floriano",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5431,
      "name":"Floriano Peixoto",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4915,
      "name":"Florian\u00f3polis",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6777,
      "name":"Fl\u00f3rida",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4142,
      "name":"Fl\u00f3rida Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4143,
      "name":"Flor\u00ednia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6816,
      "name":"Fonte Boa",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":5432,
      "name":"Fontoura Xavier",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6534,
      "name":"Formiga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5433,
      "name":"Formigueiro",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6527,
      "name":"Formosa",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8409,
      "name":"Formosa da Serra Negra",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6778,
      "name":"Formosa do Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5490,
      "name":"Formosa do Rio Preto",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4916,
      "name":"Formosa do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8688,
      "name":"Formoso",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8315,
      "name":"Formoso",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3377,
      "name":"Formoso do Araguaia",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5434,
      "name":"Forquetinha",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8049,
      "name":"Forquilha",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4918,
      "name":"Forquilhinha",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8050,
      "name":"Fortaleza",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8689,
      "name":"Fortaleza de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8410,
      "name":"Fortaleza dos Nogueiras",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5435,
      "name":"Fortaleza dos Valos",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3378,
      "name":"Fortaleza do Taboc\u00e3o",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8051,
      "name":"Fortim",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8411,
      "name":"Fortuna",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8690,
      "name":"Fortuna de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6779,
      "name":"Foz do Igua\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6780,
      "name":"Foz do Jord\u00e3o",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4919,
      "name":"Fraiburgo",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4144,
      "name":"Franca",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7045,
      "name":"Francin\u00f3polis",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6781,
      "name":"Francisco Alves",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7046,
      "name":"Francisco Ayres",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8691,
      "name":"Francisco Badar\u00f3",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6782,
      "name":"Francisco Beltr\u00e3o",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5821,
      "name":"Francisco Dantas",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8692,
      "name":"Francisco Dumont",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7047,
      "name":"Francisco Macedo",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4145,
      "name":"Francisco Morato",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8693,
      "name":"Francisc\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8694,
      "name":"Francisco S\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7048,
      "name":"Francisco Santos",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4146,
      "name":"Franco da Rocha",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8052,
      "name":"Frecheirinha",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5436,
      "name":"Frederico Westphalen",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8695,
      "name":"Frei Gaspar",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8696,
      "name":"Frei Inoc\u00eancio",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8697,
      "name":"Frei Lagonegro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7349,
      "name":"Frei Martinho",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7301,
      "name":"Frei Miguelinho",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4521,
      "name":"Frei Paulo",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4920,
      "name":"Frei Rog\u00e9rio",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8699,
      "name":"Fronteira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8698,
      "name":"Fronteira dos Vales",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7049,
      "name":"Fronteiras",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8700,
      "name":"Fruta de Leite",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5393,
      "name":"Frutal",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4147,
      "name":"Frutal do Campo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5822,
      "name":"Frutuoso Gomes",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6079,
      "name":"Fuma\u00e7a",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8216,
      "name":"Fund\u00e3o",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6080,
      "name":"Funil",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8701,
      "name":"Funil\u00e2ndia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4127,
      "name":"Furnas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4436,
      "name":"Furquim",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4148,
      "name":"Gabriel Monteiro",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7350,
      "name":"Gado Bravo",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6081,
      "name":"Galdino",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4155,
      "name":"G\u00e1lia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8702,
      "name":"Galil\u00e9ia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5823,
      "name":"Galinhos",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4921,
      "name":"Galv\u00e3o",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8177,
      "name":"Gama",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":7302,
      "name":"Gameleira",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":83132,
      "name":"Gameleira de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8703,
      "name":"Gameleiras",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7870,
      "name":"Gandu",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7303,
      "name":"Garanhuns",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6235,
      "name":"Garapuava",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4522,
      "name":"Gararu",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4156,
      "name":"Gar\u00e7a",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5705,
      "name":"Garcias",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4163,
      "name":"Gard\u00eania",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5437,
      "name":"Garibaldi",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4922,
      "name":"Garopaba",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7446,
      "name":"Garraf\u00e3o do Norte",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":5438,
      "name":"Garruchos",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4923,
      "name":"Garuva",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4924,
      "name":"Gaspar",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4164,
      "name":"Gast\u00e3o Vidigal",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7619,
      "name":"Ga\u00facha do Norte",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5439,
      "name":"Gaurama",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7871,
      "name":"Gavi\u00e3o",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4173,
      "name":"Gavi\u00e3o Peixoto",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6082,
      "name":"Gavi\u00f5es",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7050,
      "name":"Geminiano",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5440,
      "name":"General C\u00e2mara",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7620,
      "name":"General Carneiro",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6783,
      "name":"General Carneiro",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4523,
      "name":"General Maynard",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4174,
      "name":"General Salgado",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8053,
      "name":"General Sampaio",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5824,
      "name":"Genipabu",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5441,
      "name":"Gentil",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7872,
      "name":"Gentio do Ouro",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6083,
      "name":"Getul\u00e2ndia",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4175,
      "name":"Getulina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5442,
      "name":"Get\u00falio Vargas",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7051,
      "name":"Gilbu\u00e9s",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4305,
      "name":"Girau do Ponciano",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5443,
      "name":"Giru\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8704,
      "name":"Glaucil\u00e2ndia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4176,
      "name":"Glic\u00e9rio",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6084,
      "name":"Glic\u00e9rio",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4260,
      "name":"Gl\u00f3ria",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5494,
      "name":"Gl\u00f3ria de Dourados",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4404,
      "name":"Gl\u00f3ria d'Oeste",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7304,
      "name":"Gl\u00f3ria do Goit\u00e1",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5444,
      "name":"Glorinha",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4537,
      "name":"Gluc\u00ednio",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4753,
      "name":"Godofredo Viana",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6784,
      "name":"Godoy Moreira",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8705,
      "name":"Goiabeira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7305,
      "name":"Goiana",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8706,
      "name":"Goian\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3247,
      "name":"Goian\u00e1polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3938,
      "name":"Goiandira",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7535,
      "name":"Goian\u00e9sia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4194,
      "name":"Goian\u00e9sia do Par\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6861,
      "name":"Goi\u00e2nia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5825,
      "name":"Goianinha",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8316,
      "name":"Goianira",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3379,
      "name":"Goianorte",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5653,
      "name":"Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3381,
      "name":"Goiatins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5652,
      "name":"Goiatuba",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6785,
      "name":"Goioer\u00ea",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6786,
      "name":"Goioxim",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8707,
      "name":"Gon\u00e7alves",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8412,
      "name":"Gon\u00e7alves Dias",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7873,
      "name":"Gongogi",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8708,
      "name":"Gonzaga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8709,
      "name":"Gouv\u00eaa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3140,
      "name":"Gouvel\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8413,
      "name":"Governador Archer",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4925,
      "name":"Governador Celso Ramos",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5826,
      "name":"Governador Dix-Sept Rosado",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6242,
      "name":"Governador Edison Lob\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8414,
      "name":"Governador Eug\u00eanio Barros",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5738,
      "name":"Governador Jorge Teixeira",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":4874,
      "name":"Governador Lindenberg",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8415,
      "name":"Governador Luiz Rocha",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7874,
      "name":"Governador Mangabeira",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8416,
      "name":"Governador Newton Bello",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6243,
      "name":"Governador Nunes Freire",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6085,
      "name":"Governador Portela",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8710,
      "name":"Governador Valadares",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8054,
      "name":"Gra\u00e7a",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4280,
      "name":"Gra\u00e7a Aranha",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4526,
      "name":"Gracho Cardoso",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6787,
      "name":"Graciosa",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7669,
      "name":"Graja\u00fa",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5446,
      "name":"Gramado",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5445,
      "name":"Gramado dos Loureiros",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5447,
      "name":"Gramado Xavier",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6788,
      "name":"Grandes Rios",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7306,
      "name":"Granito",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8055,
      "name":"Granja",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4177,
      "name":"Granja Viana",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8056,
      "name":"Granjeiro",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8711,
      "name":"Gr\u00e3o Mogol",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4927,
      "name":"Gr\u00e3o Par\u00e1",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7307,
      "name":"Gravat\u00e1",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5448,
      "name":"Gravata\u00ed",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4928,
      "name":"Gravatal",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8057,
      "name":"Groa\u00edras",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5827,
      "name":"Grossos",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8712,
      "name":"Grupiara",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5449,
      "name":"Guabiju",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4929,
      "name":"Guabiruba",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8217,
      "name":"Gua\u00e7u\u00ed",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7052,
      "name":"Guadalupe",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5450,
      "name":"Gua\u00edba",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4178,
      "name":"Guai\u00e7ara",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4179,
      "name":"Guaimb\u00ea",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6789,
      "name":"Guaipor\u00e3",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6791,
      "name":"Gua\u00edra",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4180,
      "name":"Gua\u00edra",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6790,
      "name":"Guaira\u00e7\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8058,
      "name":"Guai\u00faba",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5904,
      "name":"Guajar\u00e1",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":5739,
      "name":"Guajar\u00e1-Mirim",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":4261,
      "name":"Guajeru",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5828,
      "name":"Guamar\u00e9",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6792,
      "name":"Guamiranga",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7555,
      "name":"Guanambi",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3370,
      "name":"Guanh\u00e3es",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8713,
      "name":"Guap\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4181,
      "name":"Guapia\u00e7u",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4182,
      "name":"Guapiara",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6086,
      "name":"Guapimirim",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6793,
      "name":"Guapirama",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4183,
      "name":"Guapiranga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5654,
      "name":"Guap\u00f3",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5451,
      "name":"Guapor\u00e9",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6794,
      "name":"Guaporema",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8178,
      "name":"Guar\u00e1",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":4226,
      "name":"Guar\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7351,
      "name":"Guarabira",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4184,
      "name":"Guara\u00e7a\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6553,
      "name":"Guaraci",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4198,
      "name":"Guaraci",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8714,
      "name":"Guaraciaba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4930,
      "name":"Guaraciaba",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8059,
      "name":"Guaraciaba do Norte",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8715,
      "name":"Guaraciama",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3382,
      "name":"Guara\u00ed",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8317,
      "name":"Guara\u00edta",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7572,
      "name":"Guaramiranga",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4931,
      "name":"Guaramirim",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3145,
      "name":"Guaran\u00e9sia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6555,
      "name":"Guarani",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8716,
      "name":"Guarani",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6554,
      "name":"Guarania\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5452,
      "name":"Guarani das Miss\u00f5es",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8318,
      "name":"Guarani de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4207,
      "name":"Guarani d'Oeste",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4210,
      "name":"Guarant\u00e3",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7621,
      "name":"Guarant\u00e3 do Norte",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8218,
      "name":"Guarapari",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6993,
      "name":"Guarapuava",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6556,
      "name":"Guaraque\u00e7aba",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8717,
      "name":"Guarar\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4211,
      "name":"Guararapes",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4212,
      "name":"Guararema",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7875,
      "name":"Guaratinga",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4231,
      "name":"Guaratinguet\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6557,
      "name":"Guaratuba",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4932,
      "name":"Guarda do Emba\u00fa",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6323,
      "name":"Guarda dos Ferreiros",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3129,
      "name":"Guarda-Mor",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6213,
      "name":"Guardinha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4232,
      "name":"Guare\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4233,
      "name":"Guariba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7053,
      "name":"Guaribas",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3983,
      "name":"Guarinos",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4234,
      "name":"Guaruj\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4933,
      "name":"Guaruj\u00e1 do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4235,
      "name":"Guarulhos",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6087,
      "name":"Guarus",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4935,
      "name":"Guat\u00e1",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4934,
      "name":"Guatamb\u00fa",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4236,
      "name":"Guatapar\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6088,
      "name":"Guaxindiba",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5680,
      "name":"Guaxup\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6089,
      "name":"Guia de Pacoba\u00edba",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3875,
      "name":"Guia Lopes da Laguna",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8718,
      "name":"Guidoval",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4754,
      "name":"Guimar\u00e3es",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8719,
      "name":"Guimar\u00e2nia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7622,
      "name":"Guiratinga",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8720,
      "name":"Guiricema",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":2057,
      "name":"Gurinhat\u00e3",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7352,
      "name":"Gurinh\u00e9m",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8219,
      "name":"Guriri",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7353,
      "name":"Gurj\u00e3o",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7447,
      "name":"Gurup\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":3383,
      "name":"Gurupi",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4237,
      "name":"Guzol\u00e2ndia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5453,
      "name":"Harmonia",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8319,
      "name":"Heitora\u00ed",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8721,
      "name":"Heliodora",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7876,
      "name":"Heli\u00f3polis",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6558,
      "name":"Hercul\u00e2ndia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4238,
      "name":"Hercul\u00e2ndia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5454,
      "name":"Herval",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4936,
      "name":"Herval d'Oeste",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5455,
      "name":"Herveiras",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3863,
      "name":"Hidrol\u00e2ndia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3865,
      "name":"Hidrol\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8060,
      "name":"Hidrol\u00e2ndia",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8320,
      "name":"Hidrolina",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4239,
      "name":"Holambra",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6559,
      "name":"Hon\u00f3rio Serpa",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6329,
      "name":"Honor\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8061,
      "name":"Horizonte",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5456,
      "name":"Horizontina",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4240,
      "name":"Hortol\u00e2ndia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7054,
      "name":"Hugo Napole\u00e3o",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5457,
      "name":"Hulha Negra",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5458,
      "name":"Humait\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7543,
      "name":"Humait\u00e1",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":4755,
      "name":"Humberto de Campos",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3152,
      "name":"Humildes",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4241,
      "name":"Iacanga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4275,
      "name":"Iaciara",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4242,
      "name":"Iacri",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7877,
      "name":"Ia\u00e7u",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8722,
      "name":"Iapu",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4243,
      "name":"Iaras",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7308,
      "name":"Iati",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6560,
      "name":"Ibaiti",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5459,
      "name":"Ibarama",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8062,
      "name":"Ibaretama",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4244,
      "name":"Ibat\u00e9",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4568,
      "name":"Ibateguara",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8220,
      "name":"Ibatiba",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6561,
      "name":"Ibema",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8723,
      "name":"Ibertioga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8725,
      "name":"Ibi\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5460,
      "name":"Ibia\u00e7\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6562,
      "name":"Ibiaci",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8724,
      "name":"Ibia\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4937,
      "name":"Ibiam",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8063,
      "name":"Ibiapina",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7354,
      "name":"Ibiara",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3868,
      "name":"Ibiassuc\u00ea",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7878,
      "name":"Ibicara\u00ed",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4938,
      "name":"Ibicar\u00e9",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7879,
      "name":"Ibicoara",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3970,
      "name":"Ibicu\u00ed",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8064,
      "name":"Ibicuitinga",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7309,
      "name":"Ibimirim",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7880,
      "name":"Ibipeba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7881,
      "name":"Ibipetuba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7882,
      "name":"Ibipitanga",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6563,
      "name":"Ibipor\u00e3",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4245,
      "name":"Ibiporanga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3921,
      "name":"Ibiquera",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4247,
      "name":"Ibir\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8726,
      "name":"Ibiracatu",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8727,
      "name":"Ibiraci",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8221,
      "name":"Ibira\u00e7u",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5461,
      "name":"Ibiraiaras",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7883,
      "name":"Ibiraj\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7310,
      "name":"Ibirajuba",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4939,
      "name":"Ibirama",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7884,
      "name":"Ibirapitanga",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7885,
      "name":"Ibirapu\u00e3",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5462,
      "name":"Ibirapuit\u00e3",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4246,
      "name":"Ibirarema",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7886,
      "name":"Ibirataia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6535,
      "name":"Ibirit\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5463,
      "name":"Ibirub\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4620,
      "name":"Ibitiara",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6090,
      "name":"Ibitigua\u00e7u",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4249,
      "name":"Ibitinga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6091,
      "name":"Ibitioca",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6335,
      "name":"Ibitira",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8222,
      "name":"Ibitirama",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8223,
      "name":"Ibitirui",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7887,
      "name":"Ibitit\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8728,
      "name":"Ibiti\u00fara de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4250,
      "name":"Ibitiuva",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6284,
      "name":"Ibitup\u00e3",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6092,
      "name":"Ibituporanga",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8729,
      "name":"Ibituruna",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4251,
      "name":"Ibi\u00fana",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7888,
      "name":"Ibotirama",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8065,
      "name":"Icapu\u00ed",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4940,
      "name":"I\u00e7ara",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8730,
      "name":"Icara\u00ed de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6564,
      "name":"Icara\u00edma",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4281,
      "name":"Icatu",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4252,
      "name":"Ic\u00e9m",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3118,
      "name":"Ichu",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5618,
      "name":"Ic\u00f3",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6351,
      "name":"Icoaraci",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8224,
      "name":"Iconha",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5829,
      "name":"Ielmo Marinho",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4253,
      "name":"Iep\u00ea",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6408,
      "name":"Igaci",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3190,
      "name":"Igapor\u00e3",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4255,
      "name":"Igara\u00e7u do Tiet\u00ea",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7355,
      "name":"Igaracy",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4258,
      "name":"Igara\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4266,
      "name":"Igarapava",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8731,
      "name":"Igarap\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7448,
      "name":"Igarap\u00e9-A\u00e7u",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8417,
      "name":"Igarap\u00e9 do Meio",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8418,
      "name":"Igarap\u00e9 Grande",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7449,
      "name":"Igarap\u00e9-Miri",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7311,
      "name":"Igarassu",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4271,
      "name":"Igarat\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8732,
      "name":"Igaratinga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4262,
      "name":"Igarit\u00e9",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7889,
      "name":"Igrapi\u00fana",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6409,
      "name":"Igreja Nova",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5464,
      "name":"Igrejinha",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6093,
      "name":"Iguaba Grande",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3971,
      "name":"Igua\u00ed",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8066,
      "name":"Iguape",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4272,
      "name":"Iguape",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4711,
      "name":"Iguaraci",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6565,
      "name":"Iguara\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3122,
      "name":"Iguatama",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5706,
      "name":"Iguatemi",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":5619,
      "name":"Iguatu",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6566,
      "name":"Iguatu",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8733,
      "name":"Ijaci",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5465,
      "name":"Iju\u00ed",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4273,
      "name":"Ilhabela",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4274,
      "name":"Ilha Comprida",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4527,
      "name":"Ilha das Flores",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":7890,
      "name":"Ilha de Boipeba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":9140,
      "name":"Ilha de Comandatuba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4074,
      "name":"Ilha de Maraj\u00f3",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4288,
      "name":"Ilha do Cardoso",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6567,
      "name":"Ilha do Mel",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6568,
      "name":"Ilha do Sol",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6094,
      "name":"Ilha Grande",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7055,
      "name":"Ilha Grande",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4289,
      "name":"Ilha Solteira",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7556,
      "name":"Ilh\u00e9us",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4941,
      "name":"Ilhota",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8734,
      "name":"Ilic\u00ednea",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5466,
      "name":"Il\u00f3polis",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7356,
      "name":"Imaculada",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4942,
      "name":"Imaru\u00ed",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6095,
      "name":"Imbari\u00ea",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7891,
      "name":"Imbassa\u00ed",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6569,
      "name":"Imba\u00fa",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5467,
      "name":"Imb\u00e9",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8735,
      "name":"Imb\u00e9 de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4943,
      "name":"Imbituba",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6570,
      "name":"Imbituva",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4944,
      "name":"Imbuia",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5468,
      "name":"Imigrante",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6866,
      "name":"Imperatriz",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8321,
      "name":"Inaciol\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6571,
      "name":"In\u00e1cio Martins",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7312,
      "name":"Inaj\u00e1",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3240,
      "name":"Inaj\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6096,
      "name":"Inconfid\u00eancia",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3084,
      "name":"Inconfidentes",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8736,
      "name":"Indaiabira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5708,
      "name":"Indai\u00e1 do Sul",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":5707,
      "name":"Indai\u00e1 Grande",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4945,
      "name":"Indaial",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4290,
      "name":"Indaiatuba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":9085,
      "name":"Ind\u00e1polis",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8067,
      "name":"Independ\u00eancia",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5469,
      "name":"Independ\u00eancia",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4291,
      "name":"Indiana",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6572,
      "name":"Indian\u00f3polis",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8737,
      "name":"Indian\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4292,
      "name":"Indiapor\u00e3",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8322,
      "name":"Indiara",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4528,
      "name":"Indiaroba",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4405,
      "name":"Indiava\u00ed",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4691,
      "name":"Ing\u00e1",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8738,
      "name":"Inga\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7313,
      "name":"Ingazeira",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5470,
      "name":"Inhacor\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7892,
      "name":"Inhambupe",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7450,
      "name":"Inhangapi",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":3964,
      "name":"Inhapi",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8739,
      "name":"Inhapim",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8740,
      "name":"Inha\u00fama",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6097,
      "name":"Inhomirim",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7056,
      "name":"Inhuma",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3984,
      "name":"Inhumas",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8741,
      "name":"Inimutaba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6098,
      "name":"Ino\u00e3",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4107,
      "name":"Inoc\u00eancia",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4293,
      "name":"In\u00fabia Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4946,
      "name":"Iomer\u00ea",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8742,
      "name":"Ipaba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6862,
      "name":"Ipameri",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3221,
      "name":"Ipanema",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5830,
      "name":"Ipangua\u00e7u",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8068,
      "name":"Ipaporanga",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8743,
      "name":"Ipatinga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3810,
      "name":"Ipau\u00e7u",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8069,
      "name":"Ipaumirim",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5471,
      "name":"Ip\u00ea",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4539,
      "name":"Ipecaet\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3811,
      "name":"Iper\u00f3",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3812,
      "name":"Ipe\u00fana",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6099,
      "name":"Ipiabas",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":2066,
      "name":"Ipia\u00e7u",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7893,
      "name":"Ipia\u00fa",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3813,
      "name":"Ipigu\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6100,
      "name":"Ipi\u00edba",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4947,
      "name":"Ipira",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7894,
      "name":"Ipir\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6573,
      "name":"Ipiranga",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":81121,
      "name":"Ipiranga de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":81721,
      "name":"Ipiranga do Norte",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7057,
      "name":"Ipiranga do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5472,
      "name":"Ipiranga do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6101,
      "name":"Ipituna",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5905,
      "name":"Ipixuna",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7451,
      "name":"Ipixuna do Par\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7314,
      "name":"Ipojuca",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4948,
      "name":"Ipom\u00e9ia",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5219,
      "name":"Ipor\u00e1",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6574,
      "name":"Ipor\u00e3",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4949,
      "name":"Ipor\u00e3 do Oeste",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3814,
      "name":"Iporanga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8070,
      "name":"Ipu",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3815,
      "name":"Ipu\u00e3",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4950,
      "name":"Ipua\u00e7u",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7315,
      "name":"Ipubi",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6102,
      "name":"Ipuca",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5831,
      "name":"Ipueira",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3384,
      "name":"Ipueiras",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8071,
      "name":"Ipueiras",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8744,
      "name":"Ipui\u00fana",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4951,
      "name":"Ipumirim",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7895,
      "name":"Ipupiara",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8072,
      "name":"Iracema",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5779,
      "name":"Iracema",
      "state":"RR",
      "country":"BR  "
   },
   {
      "id":6575,
      "name":"Iracema do Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3816,
      "name":"Iracem\u00e1polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4952,
      "name":"Iraceminha",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5473,
      "name":"Ira\u00ed",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8745,
      "name":"Ira\u00ed de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3909,
      "name":"Irajuba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7896,
      "name":"Iramaia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5906,
      "name":"Iranduba",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":4953,
      "name":"Irani",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3817,
      "name":"Irapu\u00e3",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3818,
      "name":"Irapuru",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4621,
      "name":"Iraquara",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4622,
      "name":"Irar\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4954,
      "name":"Irati",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6994,
      "name":"Irati",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8073,
      "name":"Irau\u00e7uba",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7897,
      "name":"Irec\u00ea",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6576,
      "name":"Iretama",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4955,
      "name":"Irine\u00f3polis",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7452,
      "name":"Irituia",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4000,
      "name":"Irundiara",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8225,
      "name":"Irupi",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7058,
      "name":"Isa\u00edas Coelho",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4220,
      "name":"Israel\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4962,
      "name":"It\u00e1",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5474,
      "name":"Itaara",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7357,
      "name":"Itabaiana",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4529,
      "name":"Itabaiana",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4530,
      "name":"Itabaianinha",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6321,
      "name":"Itabat\u00e3",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3245,
      "name":"Itabela",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3819,
      "name":"Itaber\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7557,
      "name":"Itaberaba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5655,
      "name":"Itabera\u00ed",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4531,
      "name":"Itabi",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":8746,
      "name":"Itabira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8747,
      "name":"Itabirinha de Mantena",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8748,
      "name":"Itabirito",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6103,
      "name":"Itabora\u00ed",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6523,
      "name":"Itabuna",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4705,
      "name":"Itacaj\u00e1",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8749,
      "name":"Itacambira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8750,
      "name":"Itacarambi",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6424,
      "name":"Itacar\u00e9",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6817,
      "name":"Itacoatiara",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7316,
      "name":"Itacuruba",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5475,
      "name":"Itacurubi",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6104,
      "name":"Itacuru\u00e7\u00e1",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4057,
      "name":"Itaet\u00e9",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4001,
      "name":"Itagi",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3232,
      "name":"Itagib\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3972,
      "name":"Itagimirim",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6322,
      "name":"Itagua\u00e7u",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8226,
      "name":"Itagua\u00e7u",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":4157,
      "name":"Itagua\u00e7u da Bahia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6105,
      "name":"Itagua\u00ed",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3238,
      "name":"Itaguaj\u00e9",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8751,
      "name":"Itaguara",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8323,
      "name":"Itaguari",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8324,
      "name":"Itaguaru",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3385,
      "name":"Itaguatins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3820,
      "name":"Ita\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7317,
      "name":"Ita\u00edba",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8074,
      "name":"Itai\u00e7aba",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7059,
      "name":"Itain\u00f3polis",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4956,
      "name":"Itai\u00f3polis",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6106,
      "name":"Itaipava",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8227,
      "name":"Itaipava",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8419,
      "name":"Itaipava do Graja\u00fa",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8752,
      "name":"Itaip\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6108,
      "name":"Itaipu",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6107,
      "name":"Itaipua\u00e7u",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6577,
      "name":"Itaipul\u00e2ndia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8075,
      "name":"Itaitinga",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7453,
      "name":"Itaituba",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8325,
      "name":"Itaj\u00e1",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5832,
      "name":"Itaj\u00e1",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4957,
      "name":"Itaja\u00ed",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6109,
      "name":"Itajara",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3821,
      "name":"Itajobi",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3822,
      "name":"Itaju",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6536,
      "name":"Itajub\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3224,
      "name":"Itaju do Col\u00f4nia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5606,
      "name":"Itaju\u00edpe",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6110,
      "name":"Italva",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":9141,
      "name":"Itamarac\u00e1",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5395,
      "name":"Itamaraju",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8753,
      "name":"Itamarandiba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5907,
      "name":"Itamarati",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":8754,
      "name":"Itamarati de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4158,
      "name":"Itamari",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8755,
      "name":"Itambacuri",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6578,
      "name":"Itambarac\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6579,
      "name":"Itamb\u00e9",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3973,
      "name":"Itamb\u00e9",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7318,
      "name":"Itamb\u00e9",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8756,
      "name":"Itamb\u00e9 do Mato Dentro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6111,
      "name":"Itambi",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8228,
      "name":"Itamira",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8757,
      "name":"Itamogi",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6537,
      "name":"Itamonte",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4430,
      "name":"Itamotinga",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6230,
      "name":"Itamuri",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4093,
      "name":"Itanagra",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3823,
      "name":"Itanha\u00e9m",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6538,
      "name":"Itanhandu",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":81722,
      "name":"Itanhang\u00e1",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3974,
      "name":"Itanh\u00e9m",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8758,
      "name":"Itanhomi",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8759,
      "name":"Itaobim",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8229,
      "name":"Itaoca",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":3824,
      "name":"Ita\u00f3ca",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6112,
      "name":"Itaocara",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7536,
      "name":"Itapaci",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":2165,
      "name":"Itapagipe",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5620,
      "name":"Itapaj\u00e9",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6524,
      "name":"Itaparica",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7898,
      "name":"Itap\u00e9",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4159,
      "name":"Itapebi",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8760,
      "name":"Itapecerica",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3825,
      "name":"Itapecerica da Serra",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8420,
      "name":"Itapecuru Mirim",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6580,
      "name":"Itapejara d'Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4958,
      "name":"Itapema",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8230,
      "name":"Itapemirim",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6581,
      "name":"Itaperu\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6113,
      "name":"Itaperuna",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7319,
      "name":"Itapetim",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6425,
      "name":"Itapetinga",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3826,
      "name":"Itapetininga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8761,
      "name":"Itapeva",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3827,
      "name":"Itapeva",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3828,
      "name":"Itapevi",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7899,
      "name":"Itapicuru",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8076,
      "name":"Itapipoca",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3830,
      "name":"Itapira",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4959,
      "name":"Itapiranga",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6818,
      "name":"Itapiranga",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":8326,
      "name":"Itapirapu\u00e3",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3829,
      "name":"Itapirapu\u00e3 Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3386,
      "name":"Itapiratins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":6236,
      "name":"Itapirucu",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7320,
      "name":"Itapissuma",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5365,
      "name":"Itapitanga",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4650,
      "name":"Itapi\u00fana",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4960,
      "name":"Itapo\u00e1",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4961,
      "name":"Itapocu",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3831,
      "name":"It\u00e1polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3131,
      "name":"Itapor\u00e3",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3388,
      "name":"Itapor\u00e3 do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3992,
      "name":"Itaporanga",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3832,
      "name":"Itaporanga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4532,
      "name":"Itaporanga d'Ajuda",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":7358,
      "name":"Itapororoca",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5740,
      "name":"Itapu\u00e3 do Oeste",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":5476,
      "name":"Itapuca",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3833,
      "name":"Itapu\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3834,
      "name":"Itapura",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7900,
      "name":"Itapura",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5656,
      "name":"Itapuranga",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3835,
      "name":"Itaquaquecetuba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4540,
      "name":"Itaquara",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8231,
      "name":"Itaquari",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5477,
      "name":"Itaqui",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7674,
      "name":"Itaquira\u00ed",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":7321,
      "name":"Itaquitinga",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8232,
      "name":"Itarana",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":3859,
      "name":"Itarantim",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3836,
      "name":"Itarar\u00e9",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8077,
      "name":"Itarema",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3837,
      "name":"Itariri",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4120,
      "name":"Itarum\u00e3",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5479,
      "name":"Itati",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6114,
      "name":"Itatiaia",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8762,
      "name":"Itatiaiu\u00e7u",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3838,
      "name":"Itatiba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5478,
      "name":"Itatiba do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3201,
      "name":"Itatim",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3839,
      "name":"Itatinga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8078,
      "name":"Itatira",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7245,
      "name":"Itatuba",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5833,
      "name":"Ita\u00fa",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4406,
      "name":"Ita\u00faba",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5910,
      "name":"Itaubal",
      "state":"AP",
      "country":"BR  "
   },
   {
      "id":8327,
      "name":"Itau\u00e7u",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8763,
      "name":"Ita\u00fa de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4715,
      "name":"Itaueira",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4108,
      "name":"Itaum",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8764,
      "name":"Ita\u00fana",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6582,
      "name":"Ita\u00fana do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8233,
      "name":"Ita\u00fanas",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8765,
      "name":"Itaverava",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8766,
      "name":"Itinga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8421,
      "name":"Itinga do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7623,
      "name":"Itiquira",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3840,
      "name":"Itirapina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3841,
      "name":"Itirapu\u00e3",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7558,
      "name":"Itiru\u00e7u",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6426,
      "name":"Iti\u00faba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3842,
      "name":"Itobi",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7901,
      "name":"Itoror\u00f3",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3843,
      "name":"Itoror\u00f3 do Paranapanem",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3845,
      "name":"Itu",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3883,
      "name":"Itua\u00e7u",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4160,
      "name":"Ituber\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8767,
      "name":"Itueta",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6539,
      "name":"Ituiutaba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7537,
      "name":"Itumbiara",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8768,
      "name":"Itumirim",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3844,
      "name":"Itupeva",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7454,
      "name":"Itupiranga",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4963,
      "name":"Ituporanga",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8769,
      "name":"Iturama",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8770,
      "name":"Itutinga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3846,
      "name":"Ituverava",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7902,
      "name":"Iui\u00fa",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8234,
      "name":"I\u00fana",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6584,
      "name":"Iva\u00ed",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6583,
      "name":"Ivaipor\u00e3",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6585,
      "name":"Ivat\u00e9",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6586,
      "name":"Ivatuba",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7675,
      "name":"Ivinhema",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3985,
      "name":"Ivol\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5480,
      "name":"Ivor\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5481,
      "name":"Ivoti",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7322,
      "name":"Jaboat\u00e3o dos Guararapes",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4964,
      "name":"Jabor\u00e1",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3132,
      "name":"Jaborandi",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3847,
      "name":"Jaborandi",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6587,
      "name":"Jaboti",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5482,
      "name":"Jaboticaba",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3848,
      "name":"Jaboticabal",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8771,
      "name":"Jaboticatubas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5834,
      "name":"Ja\u00e7an\u00e3",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7903,
      "name":"Jacaraci",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8235,
      "name":"Jacara\u00edpe",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7360,
      "name":"Jacara\u00fa",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3850,
      "name":"Jacar\u00e9",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7455,
      "name":"Jacareacanga",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4569,
      "name":"Jacar\u00e9 dos Homens",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3849,
      "name":"Jacare\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6996,
      "name":"Jacarezinho",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3851,
      "name":"Jaci",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7624,
      "name":"Jaciara",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8772,
      "name":"Jacinto",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4965,
      "name":"Jacinto Machado",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7559,
      "name":"Jacobina",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7060,
      "name":"Jacobina do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8773,
      "name":"Jacu\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4570,
      "name":"Jacu\u00edpe",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5483,
      "name":"Jacuizinho",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4195,
      "name":"Jacund\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":3852,
      "name":"Jacupiranga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5372,
      "name":"Jacutinga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5484,
      "name":"Jacutinga",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6588,
      "name":"Jaguapit\u00e3",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4013,
      "name":"Jaguaquara",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8774,
      "name":"Jaguara\u00e7u",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5485,
      "name":"Jaguar\u00e3o",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6427,
      "name":"Jaguarari",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8236,
      "name":"Jaguar\u00e9",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6115,
      "name":"Jaguaremb\u00e9",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8079,
      "name":"Jaguaretama",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5387,
      "name":"Jaguari",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6589,
      "name":"Jaguaria\u00edva",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8080,
      "name":"Jaguaribara",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8081,
      "name":"Jaguaribe",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4431,
      "name":"Jaguaripe",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3854,
      "name":"Jaguari\u00fana",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8082,
      "name":"Jaguaruana",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4966,
      "name":"Jaguaruna",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8775,
      "name":"Ja\u00edba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7061,
      "name":"Jaic\u00f3s",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3856,
      "name":"Jales",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5741,
      "name":"Jamari",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":3857,
      "name":"Jambeiro",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8776,
      "name":"Jampruca",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5681,
      "name":"Jana\u00faba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8328,
      "name":"Jandaia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6590,
      "name":"Jandaia do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4311,
      "name":"Janda\u00edra",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5835,
      "name":"Janda\u00edra",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3861,
      "name":"Jandira",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5836,
      "name":"Jandu\u00eds",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7625,
      "name":"Jangada",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6591,
      "name":"Jani\u00f3polis",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8777,
      "name":"Janu\u00e1ria",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5837,
      "name":"Janu\u00e1rio Cicco",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8778,
      "name":"Japara\u00edba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4571,
      "name":"Japaratinga",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":4533,
      "name":"Japaratuba",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6116,
      "name":"Japeri",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5838,
      "name":"Japi",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6592,
      "name":"Japira",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4534,
      "name":"Japoat\u00e3",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":8779,
      "name":"Japonvar",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3989,
      "name":"Japor\u00e3",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6117,
      "name":"Japu\u00edba",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6593,
      "name":"Japur\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5908,
      "name":"Japur\u00e1",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7323,
      "name":"Jaqueira",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5496,
      "name":"Jaquirana",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5657,
      "name":"Jaragu\u00e1",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4967,
      "name":"Jaragu\u00e1 do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4129,
      "name":"Jaraguari",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4572,
      "name":"Jaramataia",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5709,
      "name":"Jardim",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8083,
      "name":"Jardim",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6594,
      "name":"Jardim Alegre",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5839,
      "name":"Jardim de Angicos",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5840,
      "name":"Jardim de Piranhas",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7062,
      "name":"Jardim do Mulato",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5841,
      "name":"Jardim do Serid\u00f3",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3241,
      "name":"Jardim Olinda",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4968,
      "name":"Jardin\u00f3polis",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3862,
      "name":"Jardin\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5497,
      "name":"Jari",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3864,
      "name":"Jarinu",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5742,
      "name":"Jaru",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":7626,
      "name":"Jarudor\u00e9",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5658,
      "name":"Jata\u00ed",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6595,
      "name":"Jataizinho",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7324,
      "name":"Jata\u00faba",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":9086,
      "name":"Jate\u00ed",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8084,
      "name":"Jati",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4712,
      "name":"Jatob\u00e1",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4188,
      "name":"Jatob\u00e1",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7063,
      "name":"Jatob\u00e1 do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3866,
      "name":"Ja\u00fa",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3389,
      "name":"Ja\u00fa do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3939,
      "name":"Jaupaci",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7627,
      "name":"Jauru",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8780,
      "name":"Jeceaba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8781,
      "name":"Jenipapo de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8422,
      "name":"Jenipapo dos Vieiras",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8782,
      "name":"Jequeri",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":83457,
      "name":"Jequi\u00e1 da Praia",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6428,
      "name":"Jequi\u00e9",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8783,
      "name":"Jequita\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8784,
      "name":"Jequitib\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8785,
      "name":"Jequitinhonha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4014,
      "name":"Jeremoabo",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7363,
      "name":"Jeric\u00f3",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8085,
      "name":"Jericoacoara",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3867,
      "name":"Jeriquara",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8237,
      "name":"Jer\u00f4nimo Monteiro",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7064,
      "name":"Jerumenha",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8786,
      "name":"Jesu\u00e2nia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6596,
      "name":"Jesu\u00edtas",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8329,
      "name":"Jes\u00fapolis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8086,
      "name":"Jijoca de Jericoacoara",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5743,
      "name":"Ji-Paran\u00e1",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":4623,
      "name":"Jiquiri\u00e7a",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4216,
      "name":"Jita\u00fana",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4969,
      "name":"Joa\u00e7aba",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8787,
      "name":"Joa\u00edma",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8788,
      "name":"Joan\u00e9sia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3869,
      "name":"Joan\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7325,
      "name":"Jo\u00e3o Alfredo",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5842,
      "name":"Jo\u00e3o C\u00e2mara",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7065,
      "name":"Jo\u00e3o Costa",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5843,
      "name":"Jo\u00e3o Dias",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7904,
      "name":"Jo\u00e3o Dourado",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8423,
      "name":"Jo\u00e3o Lisboa",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8789,
      "name":"Jo\u00e3o Monlevade",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8238,
      "name":"Jo\u00e3o Neiva",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7364,
      "name":"Jo\u00e3o Pessoa",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8790,
      "name":"Jo\u00e3o Pinheiro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3871,
      "name":"Jo\u00e3o Ramalho",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3872,
      "name":"Joaquim Eg\u00eddio",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8791,
      "name":"Joaquim Fel\u00edcio",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4573,
      "name":"Joaquim Gomes",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":7326,
      "name":"Joaquim Nabuco",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7066,
      "name":"Joaquim Pires",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3216,
      "name":"Joaquim T\u00e1vora",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7067,
      "name":"Joca Marques",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5498,
      "name":"J\u00f3ia",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4970,
      "name":"Joinville",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8792,
      "name":"Jord\u00e2nia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7713,
      "name":"Jord\u00e3o",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":4971,
      "name":"Jos\u00e9 Boiteux",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3873,
      "name":"Jos\u00e9 Bonif\u00e1cio",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5844,
      "name":"Jos\u00e9 da Penha",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7068,
      "name":"Jos\u00e9 de Freitas",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8793,
      "name":"Jos\u00e9 Gon\u00e7alves de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4189,
      "name":"Josel\u00e2ndia",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8794,
      "name":"Josen\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8795,
      "name":"Jos\u00e9 Raydan",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8330,
      "name":"Jovi\u00e2nia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5203,
      "name":"Juara",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7365,
      "name":"Juarez T\u00e1vora",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3390,
      "name":"Juarina",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8796,
      "name":"Juatuba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7366,
      "name":"Juazeirinho",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6429,
      "name":"Juazeiro",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5623,
      "name":"Juazeiro do Norte",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7069,
      "name":"Juazeiro do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6332,
      "name":"Juba\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8087,
      "name":"Juc\u00e1s",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7327,
      "name":"Jucati",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4263,
      "name":"Jucuru\u00e7u",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5845,
      "name":"Jucurutu",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3248,
      "name":"Ju\u00edna",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8797,
      "name":"Juiz de Fora",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7070,
      "name":"J\u00falio Borges",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5499,
      "name":"J\u00falio de Castilhos",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3874,
      "name":"J\u00falio Mesquita",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3876,
      "name":"Jumirim",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8424,
      "name":"Junco do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7368,
      "name":"Junco do Serid\u00f3",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7742,
      "name":"Jundi\u00e1",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3877,
      "name":"Jundia\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6597,
      "name":"Jundia\u00ed do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6410,
      "name":"Junqueiro",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3878,
      "name":"Junqueir\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7101,
      "name":"Jupi",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4972,
      "name":"Jupi\u00e1",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3879,
      "name":"Juque\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3880,
      "name":"Juqui\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3881,
      "name":"Juquiratiba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3882,
      "name":"Juquitiba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6327,
      "name":"Juraci",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8798,
      "name":"Juramento",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6598,
      "name":"Juranda",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4716,
      "name":"Jurema",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7102,
      "name":"Jurema",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7369,
      "name":"Juripiranga",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7370,
      "name":"Juru",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3564,
      "name":"Juru\u00e1",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":8799,
      "name":"Juruaia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4407,
      "name":"Juruena",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7456,
      "name":"Juruti",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7628,
      "name":"Juscimeira",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6599,
      "name":"Jussara",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5220,
      "name":"Jussara",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4094,
      "name":"Jussara",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4624,
      "name":"Jussari",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7905,
      "name":"Jussiape",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5909,
      "name":"Juta\u00ed",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7676,
      "name":"Juti",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8800,
      "name":"Juven\u00edlia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6600,
      "name":"Kalor\u00e9",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7780,
      "name":"L\u00e1brea",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":4974,
      "name":"Lacerd\u00f3polis",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8801,
      "name":"Ladainha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5982,
      "name":"Lad\u00e1rio",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4217,
      "name":"Lafaiete Coutinho",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8802,
      "name":"Lagamar",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4535,
      "name":"Lagarto",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4975,
      "name":"Lages",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7372,
      "name":"Lagoa",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7071,
      "name":"Lagoa Alegre",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":83459,
      "name":"Lagoa Bonita do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7743,
      "name":"Lagoa da Canoa",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3391,
      "name":"Lagoa da Confus\u00e3o",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5846,
      "name":"Lagoa d'Anta",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8425,
      "name":"Lagoa da Pedra",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5682,
      "name":"Lagoa da Prata",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7371,
      "name":"Lagoa de Dentro",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5847,
      "name":"Lagoa de Pedras",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7072,
      "name":"Lagoa de S\u00e3o Francisco",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5848,
      "name":"Lagoa de Velhos",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7073,
      "name":"Lagoa do Barro do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7103,
      "name":"Lagoa do Carro",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7104,
      "name":"Lagoa do Itaenga",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8426,
      "name":"Lagoa do Mato",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7105,
      "name":"Lagoa do Ouro",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7074,
      "name":"Lagoa do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7106,
      "name":"Lagoa dos Gatos",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7075,
      "name":"Lagoa do S\u00edtio",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3295,
      "name":"Lagoa dos Patos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8427,
      "name":"Lagoa dos Rodrigues",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5500,
      "name":"Lagoa dos Tr\u00eas Cantos",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3393,
      "name":"Lagoa do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8803,
      "name":"Lagoa Dourada",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8804,
      "name":"Lagoa Formosa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8805,
      "name":"Lagoa Grande",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7107,
      "name":"Lagoa Grande",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6244,
      "name":"Lagoa Grande do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5849,
      "name":"Lagoa Nova",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5501,
      "name":"Lago\u00e3o",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4264,
      "name":"Lagoa Real",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5850,
      "name":"Lagoa Salgada",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8806,
      "name":"Lagoa Santa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4221,
      "name":"Lagoa Santa",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7373,
      "name":"Lagoa Seca",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5502,
      "name":"Lagoa Vermelha",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8428,
      "name":"Lago da Pedra",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8429,
      "name":"Lago do Junco",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3898,
      "name":"Lagoinha",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6601,
      "name":"Lagoinha de Cima",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7076,
      "name":"Lagoinha do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8430,
      "name":"Lago Verde",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4976,
      "name":"Laguna",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":9087,
      "name":"Laguna Carap\u00e3",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4625,
      "name":"Laje",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3394,
      "name":"Lajeado",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5507,
      "name":"Lajeado",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5503,
      "name":"Lajeado do Bugre",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4977,
      "name":"Lajeado Grande",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8431,
      "name":"Lajeado Novo",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4265,
      "name":"Lajed\u00e3o",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4058,
      "name":"Lajedinho",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7108,
      "name":"Lajedo",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7906,
      "name":"Lajedo do Tabocal",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6118,
      "name":"Laje do Muria\u00e9",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5852,
      "name":"Lajes",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5851,
      "name":"Lajes Pintadas",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3169,
      "name":"Lajinha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4626,
      "name":"Lamar\u00e3o",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5683,
      "name":"Lambari",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4408,
      "name":"Lambari d'Oeste",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8807,
      "name":"Lamim",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7077,
      "name":"Landri Sales",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6602,
      "name":"Lapa",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7907,
      "name":"Lap\u00e3o",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8239,
      "name":"Laranja da Terra",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6119,
      "name":"Laranjais",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6603,
      "name":"Laranjal",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8808,
      "name":"Laranjal",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5911,
      "name":"Laranjal do Jari",
      "state":"AP",
      "country":"BR  "
   },
   {
      "id":3899,
      "name":"Laranjal Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4549,
      "name":"Laranjeiras",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6604,
      "name":"Laranjeiras do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8809,
      "name":"Lassance",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7375,
      "name":"Lastro",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4978,
      "name":"Laurentino",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3202,
      "name":"Lauro de Freitas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4979,
      "name":"Lauro Muller",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3395,
      "name":"Lavandeira",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3900,
      "name":"Lav\u00ednia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8810,
      "name":"Lavras",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8088,
      "name":"Lavras da Mangabeira",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5508,
      "name":"Lavras do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8811,
      "name":"Lavras Novas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3901,
      "name":"Lavrinhas",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8812,
      "name":"Leandro Ferreira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4980,
      "name":"Lebon R\u00e9gis",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3902,
      "name":"Leme",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8813,
      "name":"Leme do Prado",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7560,
      "name":"Len\u00e7\u00f3is",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3903,
      "name":"Len\u00e7\u00f3is Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4981,
      "name":"Leoberto Leal",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8814,
      "name":"Leopoldina",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4006,
      "name":"Leopoldo de Bulh\u00f5es",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6605,
      "name":"Le\u00f3polis",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5240,
      "name":"Liberato Salzano",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3254,
      "name":"Liberdade",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3175,
      "name":"Lic\u00ednio de Almeida",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6606,
      "name":"Lidian\u00f3polis",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6120,
      "name":"L\u00eddice",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8432,
      "name":"Lima Campos",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8815,
      "name":"Lima Duarte",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3904,
      "name":"Limeira",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8816,
      "name":"Limeira do Oeste",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7109,
      "name":"Limoeiro",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4426,
      "name":"Limoeiro de Anadia",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":7457,
      "name":"Limoeiro do Ajuru",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8089,
      "name":"Limoeiro do Norte",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6607,
      "name":"Lindoeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3905,
      "name":"Lind\u00f3ia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4982,
      "name":"Lind\u00f3ia do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5241,
      "name":"Lindolfo Collor",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5242,
      "name":"Linha Nova",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8240,
      "name":"Linhares",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":3906,
      "name":"Lins",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7376,
      "name":"Livramento",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3185,
      "name":"Livramento de Nossa Senhora",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3396,
      "name":"Lizarda",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":6608,
      "name":"Loanda",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6609,
      "name":"Lobato",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7377,
      "name":"Logradouro",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6997,
      "name":"Londrina",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8817,
      "name":"Lontra",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4983,
      "name":"Lontras",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3907,
      "name":"Lorena",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4190,
      "name":"Loreto",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3908,
      "name":"Lourdes",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3911,
      "name":"Louveira",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4494,
      "name":"Lua Nova",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7629,
      "name":"Lucas do Rio Verde",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3912,
      "name":"Luc\u00e9lia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7378,
      "name":"Lucena",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3914,
      "name":"Lucian\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7630,
      "name":"Luciara",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5853,
      "name":"Lucr\u00e9cia",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8818,
      "name":"Luisburgo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7078,
      "name":"Lu\u00eds Correia",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8433,
      "name":"Lu\u00eds Domingues",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6430,
      "name":"Lu\u00eds Eduardo Magalh\u00e3es",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5854,
      "name":"Lu\u00eds Gomes",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8819,
      "name":"Luisl\u00e2ndia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4984,
      "name":"Luiz Alves",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3915,
      "name":"Lu\u00edz Ant\u00f4nio",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6610,
      "name":"Luiziana",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3916,
      "name":"Luizi\u00e2nia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6121,
      "name":"Lumiar",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8820,
      "name":"Lumin\u00e1rias",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6611,
      "name":"Lunardelli",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3917,
      "name":"Lup\u00e9rcio",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6612,
      "name":"Lupion\u00f3polis",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3919,
      "name":"Lut\u00e9cia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8821,
      "name":"Luz",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4985,
      "name":"Luzerna",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7538,
      "name":"Luzi\u00e2nia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7079,
      "name":"Luzil\u00e2ndia",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3401,
      "name":"Luzin\u00f3polis",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":6122,
      "name":"Macabuzinho",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6123,
      "name":"Maca\u00e9",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5855,
      "name":"Maca\u00edba",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7561,
      "name":"Macajuba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5243,
      "name":"Ma\u00e7ambara",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4550,
      "name":"Macambira",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":3982,
      "name":"Macap\u00e1",
      "state":"AP",
      "country":"BR  "
   },
   {
      "id":7110,
      "name":"Macaparana",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7908,
      "name":"Macarani",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3920,
      "name":"Macatuba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4403,
      "name":"Macau",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3922,
      "name":"Macaubal",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6431,
      "name":"Maca\u00fabas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3923,
      "name":"Maced\u00f4nia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6809,
      "name":"Macei\u00f3",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8822,
      "name":"Machacalis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5244,
      "name":"Machadinho",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5744,
      "name":"Machadinho d'Oeste",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":8823,
      "name":"Machado",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7111,
      "name":"Machados",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4986,
      "name":"Macieira",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6124,
      "name":"Macuco",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4627,
      "name":"Macurur\u00e9",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8090,
      "name":"Madalena",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7080,
      "name":"Madeiro",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7909,
      "name":"Madre de Deus",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8824,
      "name":"Madre de Deus de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7379,
      "name":"M\u00e3e d'\u00c1gua",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7458,
      "name":"M\u00e3e do Rio",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4161,
      "name":"Maetinga",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4987,
      "name":"Mafra",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7459,
      "name":"Magalh\u00e3es Barata",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8434,
      "name":"Magalh\u00e3es de Almeida",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3924,
      "name":"Magda",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6125,
      "name":"Mag\u00e9",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4213,
      "name":"Maiquinique",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6432,
      "name":"Mairi",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3925,
      "name":"Mairinque",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3928,
      "name":"Mairipor\u00e3",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8331,
      "name":"Mairipotaba",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4988,
      "name":"Major Gercino",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7744,
      "name":"Major Isidoro",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5856,
      "name":"Major Sales",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4989,
      "name":"Major Vieira",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8825,
      "name":"Malacacheta",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7910,
      "name":"Malhada",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7911,
      "name":"Malhada de Pedras",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4551,
      "name":"Malhada dos Bois",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4552,
      "name":"Malhador",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6613,
      "name":"Mallet",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7380,
      "name":"Malta",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7381,
      "name":"Mamanguape",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4102,
      "name":"Mamba\u00ed",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6614,
      "name":"Mambor\u00ea",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6126,
      "name":"Mambucaba",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8826,
      "name":"Mamonas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5245,
      "name":"Mampituba",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7781,
      "name":"Manacapuru",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7382,
      "name":"Mana\u00edra",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7782,
      "name":"Manaquiri",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7112,
      "name":"Manari",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7544,
      "name":"Manaus",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":6806,
      "name":"M\u00e2ncio Lima",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":6615,
      "name":"Mandagua\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6616,
      "name":"Mandaguari",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3242,
      "name":"Mandiocaba",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6617,
      "name":"Mandirituba",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3931,
      "name":"Manduri",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6618,
      "name":"Manfrin\u00f3polis",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8827,
      "name":"Manga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6127,
      "name":"Mangaratiba",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6619,
      "name":"Mangueirinha",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8828,
      "name":"Manhua\u00e7u",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8829,
      "name":"Manhumirim",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7783,
      "name":"Manicor\u00e9",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":6128,
      "name":"Maniva",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7081,
      "name":"Manoel Em\u00eddio",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6620,
      "name":"Manoel Ribas",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6129,
      "name":"Manoel Ribeiro",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7714,
      "name":"Manoel Urbano",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":5246,
      "name":"Manoel Viana",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4162,
      "name":"Manoel Vitorino",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4628,
      "name":"Mansid\u00e3o",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8830,
      "name":"Mantena",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8241,
      "name":"Manten\u00f3polis",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6130,
      "name":"Manuel Duarte",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5247,
      "name":"Maquin\u00e9",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7784,
      "name":"Mara\u00e3",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7460,
      "name":"Marab\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6621,
      "name":"Marab\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3932,
      "name":"Marab\u00e1 Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4282,
      "name":"Maraca\u00e7um\u00e9",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3933,
      "name":"Maraca\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4990,
      "name":"Maracaj\u00e1",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7677,
      "name":"Maracaju",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":7461,
      "name":"Maracan\u00e3",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":5624,
      "name":"Maracana\u00fa",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6433,
      "name":"Marac\u00e1s",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6522,
      "name":"Maragogi",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5194,
      "name":"Maragogipe",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7113,
      "name":"Maraial",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8435,
      "name":"Maraj\u00e1 do Sena",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6131,
      "name":"Marambaia",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6132,
      "name":"Marangatu",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5625,
      "name":"Maranguape",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8436,
      "name":"Maranh\u00e3ozinho",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7462,
      "name":"Marapanim",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":3934,
      "name":"Marapoama",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4002,
      "name":"Mara Rosa",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5248,
      "name":"Marat\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8242,
      "name":"Marataizes",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5249,
      "name":"Marau",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7562,
      "name":"Mara\u00fa",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4991,
      "name":"Maravilha",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7745,
      "name":"Maravilha",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8831,
      "name":"Maravilhas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7383,
      "name":"Marca\u00e7\u00e3o",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4111,
      "name":"Marcel\u00e2ndia",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5250,
      "name":"Marcelino Ramos",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5857,
      "name":"Marcelino Vieira",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4542,
      "name":"Marcian\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7912,
      "name":"Marcion\u00edlio Souza",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8091,
      "name":"Marco",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7082,
      "name":"Marcol\u00e2ndia",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7083,
      "name":"Marcos Parente",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8832,
      "name":"Mar de Espanha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6622,
      "name":"Marechal C\u00e2ndido Rondon",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7746,
      "name":"Marechal Deodoro",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8243,
      "name":"Marechal Floriano",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7715,
      "name":"Marechal Thaumaturgo",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":4992,
      "name":"Marema",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3935,
      "name":"Maresias",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6623,
      "name":"Margarida",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7384,
      "name":"Mari",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8833,
      "name":"Maria da F\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6624,
      "name":"Maria Helena",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6625,
      "name":"Marialva",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8834,
      "name":"Mariana",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5251,
      "name":"Mariana Pimentel",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5252,
      "name":"Mariano Moro",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3402,
      "name":"Marian\u00f3polis do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3941,
      "name":"Mari\u00e1polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4099,
      "name":"Maribondo",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6133,
      "name":"Maric\u00e1",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8835,
      "name":"Marilac",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8244,
      "name":"Maril\u00e2ndia",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6626,
      "name":"Maril\u00e2ndia do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6627,
      "name":"Marilena",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3943,
      "name":"Mar\u00edlia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3217,
      "name":"Mariluz",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4553,
      "name":"Marimbondo",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6628,
      "name":"Maring\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6287,
      "name":"Maring\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3944,
      "name":"Marin\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8836,
      "name":"M\u00e1rio Campos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6629,
      "name":"Mari\u00f3polis",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6630,
      "name":"Marip\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8837,
      "name":"Marip\u00e1 de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7463,
      "name":"Marituba",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7385,
      "name":"Mariz\u00f3polis",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8838,
      "name":"Marli\u00e9ria",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6631,
      "name":"Marmeleiro",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6540,
      "name":"Marmel\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6632,
      "name":"Marqu\u00eas de Abrantes",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5253,
      "name":"Marques de Souza",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6633,
      "name":"Marquinho",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8839,
      "name":"Martinho Campos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8092,
      "name":"Martin\u00f3pole",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3945,
      "name":"Martin\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5858,
      "name":"Martins",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8840,
      "name":"Martins Soares",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7464,
      "name":"Marud\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4554,
      "name":"Maruim",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6634,
      "name":"Marumbi",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3116,
      "name":"Mar Vermelho",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8332,
      "name":"Marzag\u00e3o",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4629,
      "name":"Mascote",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8093,
      "name":"Massap\u00ea",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7084,
      "name":"Massap\u00ea do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4993,
      "name":"Massaranduba",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7386,
      "name":"Massaranduba",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5254,
      "name":"Mata",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7913,
      "name":"Mata de S\u00e3o Jo\u00e3o",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7747,
      "name":"Mata Grande",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3946,
      "name":"Mat\u00e3o",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7387,
      "name":"Mataraca",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4876,
      "name":"Mata Roma",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8841,
      "name":"Mata Verde",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3404,
      "name":"Mateiros",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":6635,
      "name":"Matel\u00e2ndia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8842,
      "name":"Materl\u00e2ndia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8843,
      "name":"Mateus Leme",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8844,
      "name":"Mathias Lobato",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8845,
      "name":"Matias Barbosa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8846,
      "name":"Matias Cardoso",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7085,
      "name":"Matias Ol\u00edmpio",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4015,
      "name":"Matina",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8437,
      "name":"Matinha",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7388,
      "name":"Matinhas",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6636,
      "name":"Matinhos",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8847,
      "name":"Matip\u00f3",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5255,
      "name":"Mato Castelhano",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4283,
      "name":"Mat\u00f5es",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8438,
      "name":"Mat\u00f5es do Norte",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7389,
      "name":"Mato Grosso",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5256,
      "name":"Mato Leit\u00e3o",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5257,
      "name":"Mato Queimado",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3256,
      "name":"Mato Rico",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4994,
      "name":"Matos Costa",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8848,
      "name":"Mato Verde",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8849,
      "name":"Matozinhos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4121,
      "name":"Matrinch\u00e3",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7748,
      "name":"Matriz de Camaragibe",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":7631,
      "name":"Matup\u00e1",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6050,
      "name":"Matur\u00e9ia",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8850,
      "name":"Matutina",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3954,
      "name":"Mau\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6637,
      "name":"Mau\u00e1 da Serra",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7785,
      "name":"Mau\u00e9s",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":8333,
      "name":"Mauril\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3405,
      "name":"Mauril\u00e2ndia do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8094,
      "name":"Mauriti",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5859,
      "name":"Maxaranguape",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5258,
      "name":"Maximiliano de Almeida",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4617,
      "name":"Mazag\u00e3o",
      "state":"AP",
      "country":"BR  "
   },
   {
      "id":8851,
      "name":"Medeiros",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7914,
      "name":"Medeiros Neto",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6638,
      "name":"Medianeira",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4689,
      "name":"Medicil\u00e2ndia",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8852,
      "name":"Medina",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4995,
      "name":"Meleiro",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7465,
      "name":"Melga\u00e7o",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8245,
      "name":"Melga\u00e7o",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6134,
      "name":"Mendes",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8853,
      "name":"Mendes Pimentel",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3955,
      "name":"Mendon\u00e7a",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6639,
      "name":"Mercedes",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8854,
      "name":"Merc\u00eas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4071,
      "name":"Merc\u00eas de \u00c1gua Limpa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3956,
      "name":"Meridiano",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8095,
      "name":"Meruoca",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3957,
      "name":"Mes\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8855,
      "name":"Mesquita",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6135,
      "name":"Mesquita",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5626,
      "name":"Messejana",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7749,
      "name":"Messias",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5860,
      "name":"Messias Targino",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7086,
      "name":"Miguel Alves",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7915,
      "name":"Miguel Calmon",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7087,
      "name":"Miguel Le\u00e3o",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3958,
      "name":"Miguel\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6136,
      "name":"Miguel Pereira",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8856,
      "name":"Milagre",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8096,
      "name":"Milagres",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7916,
      "name":"Milagres",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8439,
      "name":"Milagres do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8097,
      "name":"Milh\u00e3",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6231,
      "name":"Milho Verde",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7088,
      "name":"Milton Brand\u00e3o",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8334,
      "name":"Mimoso de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8246,
      "name":"Mimoso do Sul",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":86032,
      "name":"Mina",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":5355,
      "name":"Mina\u00e7u",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7750,
      "name":"Minador do Negr\u00e3o",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5259,
      "name":"Minas do Le\u00e3o",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8857,
      "name":"Minas Novas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8858,
      "name":"Minduri",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5660,
      "name":"Mineiros",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3959,
      "name":"Mineiros do Tiet\u00ea",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5745,
      "name":"Ministro Andreazza",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":8859,
      "name":"Mirabela",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3960,
      "name":"Miracatu",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6137,
      "name":"Miracema",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3406,
      "name":"Miracema do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4191,
      "name":"Mirador",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6640,
      "name":"Mirador",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8860,
      "name":"Miradouro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3961,
      "name":"Mira Estrela",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5260,
      "name":"Miragua\u00ed",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8861,
      "name":"Mira\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8098,
      "name":"Mira\u00edma",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7678,
      "name":"Miranda",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8440,
      "name":"Miranda do Norte",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7114,
      "name":"Mirandiba",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3962,
      "name":"Mirand\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7917,
      "name":"Mirangaba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3407,
      "name":"Miranorte",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7918,
      "name":"Mirante",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5746,
      "name":"Mirante da Serra",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":3963,
      "name":"Mirante do Paranapanema",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6641,
      "name":"Miraselva",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3968,
      "name":"Mirassol",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3967,
      "name":"Mirassol\u00e2ndia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4926,
      "name":"Mirassol d'Oeste",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8862,
      "name":"Mirav\u00e2nia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4996,
      "name":"Mirim Doce",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8441,
      "name":"Mirinzal",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6642,
      "name":"Missal",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5627,
      "name":"Miss\u00e3o Velha",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7466,
      "name":"Mocajuba",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4007,
      "name":"Mococa",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4997,
      "name":"Modelo",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8863,
      "name":"Moeda",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8864,
      "name":"Moema",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7390,
      "name":"Mogeiro",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4008,
      "name":"Mogi das Cruzes",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4011,
      "name":"Mogi-Gua\u00e7u",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4012,
      "name":"Mogi-Mirim",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8335,
      "name":"Moipor\u00e1",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4555,
      "name":"Moita Bonita",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":7467,
      "name":"Moju",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8099,
      "name":"Momba\u00e7a",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4018,
      "name":"Mombuca",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8442,
      "name":"Mon\u00e7\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4019,
      "name":"Mon\u00e7\u00f5es",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4998,
      "name":"Monda\u00ed",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8100,
      "name":"Mondubim",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3697,
      "name":"Mongagu\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8865,
      "name":"Monjolos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6138,
      "name":"Monnerat",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7089,
      "name":"Monsenhor Gil",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7090,
      "name":"Monsenhor Hip\u00f3lito",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8866,
      "name":"Monsenhor Paulo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8101,
      "name":"Monsenhor Tabosa",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7391,
      "name":"Montadas",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8867,
      "name":"Montalv\u00e2nia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3257,
      "name":"Montanha",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5861,
      "name":"Montanhas",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5261,
      "name":"Montauri",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7468,
      "name":"Monte Alegre",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":5862,
      "name":"Monte Alegre",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6139,
      "name":"Monte Alegre",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7539,
      "name":"Monte Alegre de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":2175,
      "name":"Monte Alegre de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4556,
      "name":"Monte Alegre de Sergipe",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":7091,
      "name":"Monte Alegre do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5262,
      "name":"Monte Alegre dos Campos",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3698,
      "name":"Monte Alegre do Sul",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3699,
      "name":"Monte Alto",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3700,
      "name":"Monte Apraz\u00edvel",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8868,
      "name":"Monte Azul",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3701,
      "name":"Monte Azul Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3146,
      "name":"Monte Belo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5263,
      "name":"Monte Belo do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4999,
      "name":"Monte Carlo",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5684,
      "name":"Monte Carmelo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5000,
      "name":"Monte Castelo",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3702,
      "name":"Monte Castelo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4544,
      "name":"Monte das Gameleiras",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3408,
      "name":"Monte do Carmo",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4323,
      "name":"Monte Dourado",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8869,
      "name":"Monte Formoso",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6194,
      "name":"Monte Gordo",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6051,
      "name":"Monte Horebe",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4200,
      "name":"Monteiro",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3703,
      "name":"Monteiro Lobato",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7751,
      "name":"Monteir\u00f3polis",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3704,
      "name":"Monte Mor",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5264,
      "name":"Montenegro",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5747,
      "name":"Monte Negro",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":8443,
      "name":"Montes Altos",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7919,
      "name":"Monte Santo",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8870,
      "name":"Monte Santo de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3409,
      "name":"Monte Santo do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8871,
      "name":"Montes Claros",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3940,
      "name":"Montes Claros de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4248,
      "name":"Monte Si\u00e3o",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4098,
      "name":"Monte Verde",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6140,
      "name":"Monte Verde",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3705,
      "name":"Monte Verde Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8872,
      "name":"Montezuma",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8336,
      "name":"Montividiu",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4003,
      "name":"Montividiu do Norte",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6141,
      "name":"Monumento",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8102,
      "name":"Morada Nova",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8873,
      "name":"Morada Nova de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6142,
      "name":"Morangaba",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6145,
      "name":"Morangas",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8103,
      "name":"Mora\u00fajo",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7115,
      "name":"Moreil\u00e2ndia",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3218,
      "name":"Moreira Sales",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7116,
      "name":"Moreno",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5265,
      "name":"Morma\u00e7o",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7920,
      "name":"Morpar\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6643,
      "name":"Morretes",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5661,
      "name":"Morrinhos",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8104,
      "name":"Morrinhos",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5266,
      "name":"Morrinhos do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3706,
      "name":"Morro Agudo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8337,
      "name":"Morro Agudo de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7092,
      "name":"Morro Cabe\u00e7a no Tempo",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5001,
      "name":"Morro da Fuma\u00e7a",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8874,
      "name":"Morro da Gar\u00e7a",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3173,
      "name":"Morro de S\u00e3o Paulo",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6825,
      "name":"Morro do Chap\u00e9u",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7093,
      "name":"Morro do Chap\u00e9u do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6143,
      "name":"Morro do Coco",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8875,
      "name":"Morro do Pilar",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6144,
      "name":"Morro Grande",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5002,
      "name":"Morro Grande",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5267,
      "name":"Morro Redondo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5268,
      "name":"Morro Reuter",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8444,
      "name":"Morros",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":2601,
      "name":"Mortugaba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6248,
      "name":"Morumbi",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3707,
      "name":"Morungaba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5269,
      "name":"Morungava",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5662,
      "name":"Moss\u00e2medes",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5863,
      "name":"Mossor\u00f3",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5270,
      "name":"Mostardas",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3708,
      "name":"Motuca",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7786,
      "name":"Moura",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":8338,
      "name":"Mozarl\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7469,
      "name":"Muan\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":5780,
      "name":"Mucaja\u00ed",
      "state":"RR",
      "country":"BR  "
   },
   {
      "id":8105,
      "name":"Mucambo",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3204,
      "name":"Mucug\u00ea",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5271,
      "name":"Mu\u00e7um",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7921,
      "name":"Mucuri",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8247,
      "name":"Mucurici",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5272,
      "name":"Muitos Cap\u00f5es",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5273,
      "name":"Muliterno",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7392,
      "name":"Mulungu",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8106,
      "name":"Mulungu",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4630,
      "name":"Mulungu do Morro",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":9088,
      "name":"Mundo Novo",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8339,
      "name":"Mundo Novo",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3127,
      "name":"Mundo Novo",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8876,
      "name":"Munhoz",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6644,
      "name":"Munhoz de Melo",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4631,
      "name":"Muniz Ferreira",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8248,
      "name":"Muniz Freire",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6180,
      "name":"Muqu\u00e9m de S\u00e3o Francisco",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8249,
      "name":"Muqui",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8877,
      "name":"Muria\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4557,
      "name":"Muribeca",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":7117,
      "name":"Muribeca dos Guararapes",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7752,
      "name":"Murici",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":7094,
      "name":"Murici dos Portelas",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3411,
      "name":"Muricil\u00e2ndia",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":6434,
      "name":"Muritiba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3709,
      "name":"Murutinga do Sul",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6146,
      "name":"Mussurepe",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4314,
      "name":"Mutu\u00edpe",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8878,
      "name":"Mutum",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4222,
      "name":"Mutun\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8879,
      "name":"Muzambinho",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8880,
      "name":"Nacip Raydan",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3710,
      "name":"Nantes",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5685,
      "name":"Nanuque",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8881,
      "name":"Naque",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3711,
      "name":"Narandiba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5864,
      "name":"Natal",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4686,
      "name":"Natal\u00e2ndia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8882,
      "name":"Nat\u00e9rcia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6147,
      "name":"Natividade",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3412,
      "name":"Natividade",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3712,
      "name":"Natividade da Serra",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7393,
      "name":"Natuba",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5003,
      "name":"Navegantes",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8340,
      "name":"Navesl\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":9089,
      "name":"Navira\u00ed",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3413,
      "name":"Nazar\u00e9",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4165,
      "name":"Nazar\u00e9",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7118,
      "name":"Nazar\u00e9 da Mata",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7095,
      "name":"Nazar\u00e9 do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8883,
      "name":"Nazareno",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3713,
      "name":"Nazar\u00e9 Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7394,
      "name":"Nazarezinho",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":83460,
      "name":"Naz\u00e1ria",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8341,
      "name":"Naz\u00e1rio",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6195,
      "name":"Neol\u00e2ndia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4558,
      "name":"Ne\u00f3polis",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":8884,
      "name":"Nepomuceno",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4103,
      "name":"Ner\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":9138,
      "name":"Neves",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3714,
      "name":"Neves Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4427,
      "name":"Nhamund\u00e1",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":3715,
      "name":"Nhandeara",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5275,
      "name":"Nicolau Vergueiro",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4166,
      "name":"Nilo Pe\u00e7anha",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6148,
      "name":"Nil\u00f3polis",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8445,
      "name":"Nina Rodrigues",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8885,
      "name":"Ninheira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3222,
      "name":"Nioaque",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3716,
      "name":"Nipo\u00e3",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8342,
      "name":"Niquel\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5865,
      "name":"N\u00edsia Floresta",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6149,
      "name":"Niter\u00f3i",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7632,
      "name":"Nobres",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5276,
      "name":"Nonoai",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4432,
      "name":"Nordestina",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5877,
      "name":"Normandia",
      "state":"RR",
      "country":"BR  "
   },
   {
      "id":7633,
      "name":"Nortel\u00e2ndia",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4559,
      "name":"Nossa Senhora Aparecida",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6150,
      "name":"Nossa Senhora da Aparecida",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4560,
      "name":"Nossa Senhora da Gl\u00f3ria",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6151,
      "name":"Nossa Senhora da Penha",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4561,
      "name":"Nossa Senhora das Dores",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6645,
      "name":"Nossa Senhora das Gra\u00e7as",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4562,
      "name":"Nossa Senhora de Lourdes",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":7096,
      "name":"Nossa Senhora de Nazar\u00e9",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6152,
      "name":"Nossa Senhora do Amparo",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6214,
      "name":"Nossa Senhora do Livramento",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4574,
      "name":"Nossa Senhora do Socorro",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":7097,
      "name":"Nossa Senhora dos Rem\u00e9dios",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3717,
      "name":"Nova Alian\u00e7a",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6646,
      "name":"Nova Alian\u00e7a do Iva\u00ed",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8250,
      "name":"Nova Almeida",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5277,
      "name":"Nova Alvorada",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":9090,
      "name":"Nova Alvorada do Sul",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8343,
      "name":"Nova Am\u00e9rica",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6647,
      "name":"Nova Am\u00e9rica da Colina",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":9091,
      "name":"Nova Andradina",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":5278,
      "name":"Nova Ara\u00e7\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8344,
      "name":"Nova Aurora",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6648,
      "name":"Nova Aurora",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4409,
      "name":"Nova Bandeirantes",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5279,
      "name":"Nova Bassano",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8886,
      "name":"Nova Bel\u00e9m",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5280,
      "name":"Nova Boa Vista",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4410,
      "name":"Nova Brasil\u00e2ndia",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5748,
      "name":"Nova Brasil\u00e2ndia d'Oeste",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":5281,
      "name":"Nova Br\u00e9scia",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3718,
      "name":"Nova Campina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4167,
      "name":"Nova Cana\u00e3",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4411,
      "name":"Nova Cana\u00e3 do Norte",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3719,
      "name":"Nova Cana\u00e3 Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5282,
      "name":"Nova Candel\u00e1ria",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6649,
      "name":"Nova Cantu",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3720,
      "name":"Nova Castilho",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4495,
      "name":"Nova Colinas",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4223,
      "name":"Nova Crix\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4700,
      "name":"Nova Cruz",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8887,
      "name":"Nova Era",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5004,
      "name":"Nova Erechim",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":9092,
      "name":"Nova Esperan\u00e7a",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6650,
      "name":"Nova Esperan\u00e7a",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7470,
      "name":"Nova Esperan\u00e7a do Piri\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4697,
      "name":"Nova Esperan\u00e7a do Sudoeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5283,
      "name":"Nova Esperan\u00e7a do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3721,
      "name":"Nova Europa",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3219,
      "name":"Nova F\u00e1tima",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6651,
      "name":"Nova F\u00e1tima",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7395,
      "name":"Nova Floresta",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6153,
      "name":"Nova Friburgo",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7634,
      "name":"Nova Galil\u00e9ia",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8345,
      "name":"Nova Gl\u00f3ria",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3722,
      "name":"Nova Granada",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3948,
      "name":"Nova Guarita",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3723,
      "name":"Nova Guataporanga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5284,
      "name":"Nova Hartz",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4059,
      "name":"Nova Ibi\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6154,
      "name":"Nova Igua\u00e7u",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8346,
      "name":"Nova Igua\u00e7u de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3724,
      "name":"Nova Independ\u00eancia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8446,
      "name":"Nova Iorque",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7471,
      "name":"Nova Ipixuna",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":3725,
      "name":"Novais",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5005,
      "name":"Nova Itaberaba",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4632,
      "name":"Nova Itarana",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6341,
      "name":"Nova Jales",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4412,
      "name":"Nova Lacerda",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6652,
      "name":"Nova Laranjeiras",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8888,
      "name":"Nova Lima",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6653,
      "name":"Nova Londrina",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3726,
      "name":"Nova Luzit\u00e2nia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5749,
      "name":"Nova Mamor\u00e9",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":7635,
      "name":"Nova Maril\u00e2ndia",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7636,
      "name":"Nova Maring\u00e1",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8889,
      "name":"Nova M\u00f3dica",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4413,
      "name":"Nova Monte Verde",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7637,
      "name":"Nova Mutum",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":83461,
      "name":"Nova Nazar\u00e9",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3727,
      "name":"Nova Odessa",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7638,
      "name":"Nova Ol\u00edmpia",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6656,
      "name":"Nova Ol\u00edmpia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8107,
      "name":"Nova Olinda",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6052,
      "name":"Nova Olinda",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3414,
      "name":"Nova Olinda",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":6245,
      "name":"Nova Olinda do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7787,
      "name":"Nova Olinda do Norte",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":5285,
      "name":"Nova P\u00e1dua",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5286,
      "name":"Nova Palma",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7396,
      "name":"Nova Palmeira",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5287,
      "name":"Nova Petr\u00f3polis",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8890,
      "name":"Nova Ponte",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8891,
      "name":"Nova Porteirinha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4543,
      "name":"Nova Porto XV",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":5288,
      "name":"Nova Prata",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6657,
      "name":"Nova Prata do Igua\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5289,
      "name":"Nova Ramada",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4060,
      "name":"Nova Reden\u00e7\u00e3o",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3243,
      "name":"Nova Resende",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8347,
      "name":"Nova Roma",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5290,
      "name":"Nova Roma do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3415,
      "name":"Nova Rosal\u00e2ndia",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8108,
      "name":"Nova Russas",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6658,
      "name":"Nova Santa B\u00e1rbara",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":83462,
      "name":"Nova Santa Helena",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7098,
      "name":"Nova Santa Rita",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5291,
      "name":"Nova Santa Rita",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6659,
      "name":"Nova Santa Rosa",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6435,
      "name":"Nova Sento S\u00e9",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8892,
      "name":"Nova Serrana",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4168,
      "name":"Nova Soure",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6660,
      "name":"Nova Tebas",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7472,
      "name":"Nova Timboteua",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":5006,
      "name":"Nova Trento",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7639,
      "name":"Nova Ubirat\u00e3",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8893,
      "name":"Nova Uni\u00e3o",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5750,
      "name":"Nova Uni\u00e3o",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":8251,
      "name":"Nova Ven\u00e9cia",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8348,
      "name":"Nova Veneza",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5007,
      "name":"Nova Veneza",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3220,
      "name":"Nova Vi\u00e7osa",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7640,
      "name":"Nova Xavantina",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3416,
      "name":"Novo Acordo",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7788,
      "name":"Novo Air\u00e3o",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":3418,
      "name":"Novo Alegre",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7789,
      "name":"Novo Aripuan\u00e3",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":5292,
      "name":"Novo Barreiro",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8349,
      "name":"Novo Brasil",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5293,
      "name":"Novo Cabrais",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8894,
      "name":"Novo Cruzeiro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5343,
      "name":"Novo Gama",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5295,
      "name":"Novo Hamburgo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4267,
      "name":"Novo Horizonte",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4678,
      "name":"Novo Horizonte",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3728,
      "name":"Novo Horizonte",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5751,
      "name":"Novo Horizonte d'Oeste",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":6247,
      "name":"Novo Horizonte do Norte",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5752,
      "name":"Novo Horizonte do Oeste",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":3990,
      "name":"Novo Horizonte do Sul",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6661,
      "name":"Novo Itacolomi",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3419,
      "name":"Novo Jardim",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7753,
      "name":"Novo Lino",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5296,
      "name":"Novo Machado",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4414,
      "name":"Novo Mundo",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8109,
      "name":"Novo Oriente",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8895,
      "name":"Novo Oriente de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7099,
      "name":"Novo Oriente do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4025,
      "name":"Novo Planalto",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4196,
      "name":"Novo Progresso",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7473,
      "name":"Novo Repartimento",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8896,
      "name":"Novorizonte",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4321,
      "name":"Novo Santo Ant\u00f4nio",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7100,
      "name":"Novo Santo Ant\u00f4nio",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7641,
      "name":"Novo S\u00e3o Joaquim",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6662,
      "name":"Novo Sarandi",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5299,
      "name":"Novo Tiradentes",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4433,
      "name":"Novo Triunfo",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5300,
      "name":"Novo Xingu",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8179,
      "name":"N\u00facleo Bandeirante",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":3729,
      "name":"Nuporanga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7474,
      "name":"\u00d3bidos",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8110,
      "name":"Ocara",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3730,
      "name":"Ocau\u00e7u",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6795,
      "name":"Oeiras",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7475,
      "name":"Oeiras do Par\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4724,
      "name":"Oiapoque",
      "state":"AP",
      "country":"BR  "
   },
   {
      "id":8897,
      "name":"Olaria",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3731,
      "name":"\u00d3leo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7397,
      "name":"Olho d'\u00c1gua",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8447,
      "name":"Olho d'\u00c1gua das Cunh\u00e3s",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4917,
      "name":"Olho d'\u00c1gua das Flores",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5866,
      "name":"Olho d'\u00c1gua do Borges",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7754,
      "name":"Olho d'\u00c1gua do Casado",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6796,
      "name":"Olho d'\u00c1gua do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7755,
      "name":"Olho d'\u00c1gua Grande",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":4911,
      "name":"Olhos d'\u00c1gua",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6451,
      "name":"Ol\u00edmpia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3297,
      "name":"Ol\u00edmpio Noronha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7119,
      "name":"Olinda",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8448,
      "name":"Olinda Nova do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4016,
      "name":"Olindina",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7398,
      "name":"Olivedos",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5221,
      "name":"Oliveira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3420,
      "name":"Oliveira de F\u00e1tima",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3926,
      "name":"Oliveira dos Brejinhos",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3296,
      "name":"Oliveira Fortes",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7756,
      "name":"Oliven\u00e7a",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6207,
      "name":"Oliven\u00e7a",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3298,
      "name":"On\u00e7a de Pitangui",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3732,
      "name":"Onda Verde",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3299,
      "name":"Orat\u00f3rios",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3733,
      "name":"Oriente",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3734,
      "name":"Orindi\u00fava",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7476,
      "name":"Oriximin\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":3300,
      "name":"Oriz\u00e2nia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8350,
      "name":"Orizona",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6452,
      "name":"Orl\u00e2ndia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4679,
      "name":"Orleans",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7120,
      "name":"Orob\u00f3",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7121,
      "name":"Oroc\u00f3",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8111,
      "name":"Or\u00f3s",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5603,
      "name":"Ortigueira",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3735,
      "name":"Osasco",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3736,
      "name":"Oscar Bressane",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5301,
      "name":"Os\u00f3rio",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3737,
      "name":"Osvaldo Cruz",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4680,
      "name":"Otac\u00edlio Costa",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6155,
      "name":"Our\u00e2nia",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7477,
      "name":"Our\u00e9m",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4169,
      "name":"Ouri\u00e7angas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7122,
      "name":"Ouricuri",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7478,
      "name":"Ouril\u00e2ndia do Norte",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":3738,
      "name":"Ourinhos",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6663,
      "name":"Ourizona",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4681,
      "name":"Ouro",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5867,
      "name":"Ouro Branco",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7757,
      "name":"Ouro Branco",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3301,
      "name":"Ouro Branco",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3739,
      "name":"Ouroeste",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5686,
      "name":"Ouro Fino",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4541,
      "name":"Ourol\u00e2ndia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6901,
      "name":"Ouro Preto",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5753,
      "name":"Ouro Preto do Oeste",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":6054,
      "name":"Ouro Velho",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4682,
      "name":"Ouro Verde",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3740,
      "name":"Ouro Verde",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8351,
      "name":"Ouro Verde de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3302,
      "name":"Ouro Verde de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6664,
      "name":"Ouro Verde do Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6665,
      "name":"Ouro Verde do Piquiri",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8352,
      "name":"Ouvidor",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3741,
      "name":"Pacaembu",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7479,
      "name":"Pacaj\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8112,
      "name":"Pacajus",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5781,
      "name":"Pacaraima",
      "state":"RR",
      "country":"BR  "
   },
   {
      "id":4575,
      "name":"Pacatuba",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":8113,
      "name":"Pacatuba",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8449,
      "name":"Pa\u00e7o do Lumiar",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8114,
      "name":"Pacoti",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8252,
      "name":"Pacotuba",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8115,
      "name":"Pacuj\u00e1",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3884,
      "name":"Padre Bernardo",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3303,
      "name":"Padre Carvalho",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6797,
      "name":"Padre Marcos",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3304,
      "name":"Padre Para\u00edso",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6798,
      "name":"Paes Landim",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6342,
      "name":"Paiagu\u00e1s",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4683,
      "name":"Paial",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6666,
      "name":"Pai\u00e7andu",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5302,
      "name":"Paim Filho",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3306,
      "name":"Paineiras",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4648,
      "name":"Painel",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3307,
      "name":"Pains",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3305,
      "name":"Pai Pedro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3308,
      "name":"Paiva",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6799,
      "name":"Paje\u00fa do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7758,
      "name":"Palestina",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3742,
      "name":"Palestina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3237,
      "name":"Palestina de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7480,
      "name":"Palestina do Par\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8116,
      "name":"Palhano",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4756,
      "name":"Palho\u00e7a",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3309,
      "name":"Palma",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8117,
      "name":"Palm\u00e1cia",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7123,
      "name":"Palmares",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5303,
      "name":"Palmares do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3743,
      "name":"Palmares Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6667,
      "name":"Palmas",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3427,
      "name":"Palmas",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3870,
      "name":"Palmas de Monte Alto",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4757,
      "name":"Palma Sola",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6375,
      "name":"Palmeira",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4758,
      "name":"Palmeira",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5304,
      "name":"Palmeira das Miss\u00f5es",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3744,
      "name":"Palmeira d'Oeste",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6800,
      "name":"Palmeira do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5486,
      "name":"Palmeira dos \u00cdndios",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6801,
      "name":"Palmeirais",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8450,
      "name":"Palmeir\u00e2ndia",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4547,
      "name":"Palmeirante",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":2470,
      "name":"Palmeiras",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8353,
      "name":"Palmeiras de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3410,
      "name":"Palmeiras do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7124,
      "name":"Palmeirina",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3428,
      "name":"Palmeir\u00f3polis",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4122,
      "name":"Palmelo",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8354,
      "name":"Palmin\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6376,
      "name":"Palmital",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3745,
      "name":"Palmital",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5305,
      "name":"Palmitinho",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6377,
      "name":"Palmitol\u00e2ndia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4759,
      "name":"Palmitos",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3310,
      "name":"Palm\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6378,
      "name":"Palotina",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8355,
      "name":"Panam\u00e1",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5306,
      "name":"Panambi",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8253,
      "name":"Pancas",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7125,
      "name":"Panelas",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3746,
      "name":"Panorama",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":9145,
      "name":"Pantanal da Nhecol\u00e2ndia",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":5307,
      "name":"Pantano Grande",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7759,
      "name":"P\u00e3o de A\u00e7\u00facar",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3125,
      "name":"Papagaios",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4760,
      "name":"Papanduva",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6156,
      "name":"Papucaia",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6802,
      "name":"Paquet\u00e1",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6157,
      "name":"Paracambi",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6902,
      "name":"Paracatu",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8118,
      "name":"Paracuru",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6903,
      "name":"Par\u00e1 de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7481,
      "name":"Paragominas",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6541,
      "name":"Paragua\u00e7u",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3747,
      "name":"Paragua\u00e7u Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5308,
      "name":"Para\u00ed",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6158,
      "name":"Para\u00edba do Sul",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4192,
      "name":"Paraibano",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3748,
      "name":"Paraibuna",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8119,
      "name":"Paraipaba",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":9093,
      "name":"Para\u00edso",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4761,
      "name":"Para\u00edso",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4973,
      "name":"Para\u00edso",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":143538,
      "name":"Para\u00edso das \u00c1guas",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6348,
      "name":"Para\u00edso do Leste",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6379,
      "name":"Para\u00edso do Norte",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5313,
      "name":"Para\u00edso do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6159,
      "name":"Para\u00edso do Tobias",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3429,
      "name":"Para\u00edso do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3179,
      "name":"Parais\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8254,
      "name":"Paraju",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8120,
      "name":"Parambu",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4434,
      "name":"Paramirim",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8121,
      "name":"Paramoti",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5868,
      "name":"Paran\u00e1",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7541,
      "name":"Paran\u00e3",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":6380,
      "name":"Paranacity",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6381,
      "name":"Paran\u00e1 d'Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5604,
      "name":"Paranagu\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7679,
      "name":"Parana\u00edba",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":5663,
      "name":"Paranaiguara",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4415,
      "name":"Parana\u00edta",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3749,
      "name":"Paranapanema",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3750,
      "name":"Paranapiacaba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6382,
      "name":"Paranapoema",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3751,
      "name":"Paranapu\u00e3",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7126,
      "name":"Paranatama",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7642,
      "name":"Paranatinga",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5607,
      "name":"Paranava\u00ed",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8122,
      "name":"Parangaba",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":9094,
      "name":"Paranhos",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8180,
      "name":"Parano\u00e1",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":3311,
      "name":"Paraopeba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3752,
      "name":"Parapu\u00e3",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6055,
      "name":"Parari",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6160,
      "name":"Parati Mirim",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6436,
      "name":"Paratinga",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6161,
      "name":"Paraty",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4701,
      "name":"Para\u00fa",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7482,
      "name":"Parauapebas",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8356,
      "name":"Para\u00fana",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5869,
      "name":"Parazinho",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3753,
      "name":"Pardinho",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5315,
      "name":"Pareci Novo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5754,
      "name":"Parecis",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":5870,
      "name":"Parelhas",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7760,
      "name":"Pariconha",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":7790,
      "name":"Parintins",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":5218,
      "name":"Paripiranga",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7761,
      "name":"Paripueira",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3754,
      "name":"Pariquera-A\u00e7u",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3755,
      "name":"Parisi",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6803,
      "name":"Parnagu\u00e1",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6823,
      "name":"Parna\u00edba",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7127,
      "name":"Parnamirim",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5871,
      "name":"Parnamirim",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8451,
      "name":"Parnarama",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5316,
      "name":"Parob\u00e9",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3314,
      "name":"Passab\u00e9m",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5872,
      "name":"Passa e Fica",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5873,
      "name":"Passagem",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6056,
      "name":"Passagem",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8452,
      "name":"Passagem Franca",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6824,
      "name":"Passagem Franca do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5687,
      "name":"Passa Quatro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5317,
      "name":"Passa Sete",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3312,
      "name":"Passa Tempo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6162,
      "name":"Passa Tr\u00eas",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3313,
      "name":"Passa Vinte",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7128,
      "name":"Passira",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7762,
      "name":"Passo de Camaragibe",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":4762,
      "name":"Passo de Torres",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5318,
      "name":"Passo do Sobrado",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5319,
      "name":"Passo Fundo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5688,
      "name":"Passos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4763,
      "name":"Passos Maia",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8453,
      "name":"Pastos Bons",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7922,
      "name":"Pata\u00edba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3315,
      "name":"Patis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6383,
      "name":"Pato Bragado",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5609,
      "name":"Pato Branco",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7399,
      "name":"Patos",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6904,
      "name":"Patos de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6828,
      "name":"Patos do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5689,
      "name":"Patroc\u00ednio",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3316,
      "name":"Patroc\u00ednio do Muria\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3756,
      "name":"Patroc\u00ednio Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5874,
      "name":"Patu",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6163,
      "name":"Paty do Alferes",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4268,
      "name":"Pau Brasil",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7129,
      "name":"Paudalho",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6384,
      "name":"Pau d'Alho do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7483,
      "name":"Pau d'Arco",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":3430,
      "name":"Pau d'Arco",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":83463,
      "name":"Pau D'Arco do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5875,
      "name":"Pau dos Ferros",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7791,
      "name":"Pauini",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":3317,
      "name":"Paula C\u00e2ndido",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6385,
      "name":"Paula Freitas",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3757,
      "name":"Paulic\u00e9ia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3758,
      "name":"Paul\u00ednia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8454,
      "name":"Paulino Neves",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7130,
      "name":"Paulista",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7400,
      "name":"Paulista",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6829,
      "name":"Paulistana",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3759,
      "name":"Paulist\u00e2nia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6386,
      "name":"Paulist\u00e2nia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3318,
      "name":"Paulistas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6826,
      "name":"Paulo Afonso",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5320,
      "name":"Paulo Bento",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3760,
      "name":"Paulo de Faria",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6164,
      "name":"Paulo de Frontin",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6387,
      "name":"Paulo Frontin",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7763,
      "name":"Paulo Jacinto",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":4764,
      "name":"Paulo Lopes",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8455,
      "name":"Paulo Ramos",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3319,
      "name":"Pav\u00e3o",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5321,
      "name":"Paverama",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6830,
      "name":"Pavussu",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6388,
      "name":"Peabiru",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3332,
      "name":"Pe\u00e7anha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8123,
      "name":"Pec\u00e9m",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3761,
      "name":"Pederneiras",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3205,
      "name":"P\u00e9 de Serra",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4208,
      "name":"Pedra",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8255,
      "name":"Pedra Azul",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6905,
      "name":"Pedra Azul",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3762,
      "name":"Pedra Bela",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3320,
      "name":"Pedra Bonita",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8124,
      "name":"Pedra Branca",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7401,
      "name":"Pedra Branca",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5912,
      "name":"Pedra Branca do Amapari",
      "state":"AP",
      "country":"BR  "
   },
   {
      "id":6165,
      "name":"Pedra de Guaratiba",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3322,
      "name":"Pedra do Anta",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3323,
      "name":"Pedra do Indai\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6301,
      "name":"Pedra do Sino",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3321,
      "name":"Pedra Dourada",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5876,
      "name":"Pedra Grande",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7402,
      "name":"Pedra Lavrada",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3324,
      "name":"Pedralva",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4576,
      "name":"Pedra Mole",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":3763,
      "name":"Pedran\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4435,
      "name":"Pedr\u00e3o",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5878,
      "name":"Pedra Preta",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7643,
      "name":"Pedra Preta",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5323,
      "name":"Pedras Altas",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7403,
      "name":"Pedras de Fogo",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3403,
      "name":"Pedras de Maria da Cruz",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6166,
      "name":"Pedra Selada",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4765,
      "name":"Pedras Grandes",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3764,
      "name":"Pedregulho",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3765,
      "name":"Pedreira",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8456,
      "name":"Pedreiras",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4577,
      "name":"Pedrinhas",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":3766,
      "name":"Pedrinhas Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3155,
      "name":"Pedrin\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3431,
      "name":"Pedro Afonso",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4633,
      "name":"Pedro Alexandre",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5879,
      "name":"Pedro Avelino",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8256,
      "name":"Pedro Can\u00e1rio",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":3767,
      "name":"Pedro de Toledo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6167,
      "name":"Pedro do Rio",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8457,
      "name":"Pedro do Ros\u00e1rio",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6343,
      "name":"Pedro Gomes",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6832,
      "name":"Pedro II",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6833,
      "name":"Pedro Laurentino",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5332,
      "name":"Pedro Leopoldo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5324,
      "name":"Pedro Os\u00f3rio",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":83464,
      "name":"Pedro R\u00e9gis",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3325,
      "name":"Pedro Teixeira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5880,
      "name":"Pedro Velho",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3432,
      "name":"Peixe",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7484,
      "name":"Peixe Boi",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7644,
      "name":"Peixoto de Azevedo",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5325,
      "name":"Peju\u00e7ara",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5326,
      "name":"Pelotas",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8125,
      "name":"Penaforte",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8458,
      "name":"Penalva",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3768,
      "name":"Pen\u00e1polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5881,
      "name":"Pend\u00eancias",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6168,
      "name":"Penedo",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7764,
      "name":"Penedo",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":4766,
      "name":"Penha",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6169,
      "name":"Pentagna",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8126,
      "name":"Pentecoste",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3326,
      "name":"Pequeri",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3327,
      "name":"Pequi",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3433,
      "name":"Pequizeiro",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3328,
      "name":"Perdig\u00e3o",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3156,
      "name":"Perdizes",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3329,
      "name":"Perd\u00f5es",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3769,
      "name":"Pereira Barreto",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3770,
      "name":"Pereiras",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8127,
      "name":"Pereiro",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8459,
      "name":"Peri Mirim",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3330,
      "name":"Periquito",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4767,
      "name":"Peritiba",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8460,
      "name":"Peritor\u00f3",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6389,
      "name":"Perobal",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6392,
      "name":"P\u00e9rola",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6390,
      "name":"P\u00e9rola d'Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6391,
      "name":"P\u00e9rola Independente",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8357,
      "name":"Perol\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3771,
      "name":"Peru\u00edbe",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3772,
      "name":"Perus",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3331,
      "name":"Pescador",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7131,
      "name":"Pesqueira",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7132,
      "name":"Petrol\u00e2ndia",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4768,
      "name":"Petrol\u00e2ndia",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7133,
      "name":"Petrolina",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4276,
      "name":"Petrolina de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6170,
      "name":"Petr\u00f3polis",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6171,
      "name":"Piabet\u00e1",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7765,
      "name":"Pia\u00e7abu\u00e7u",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":4136,
      "name":"Pia\u00e7a\u00e7uba",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3773,
      "name":"Piacatu",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4228,
      "name":"Pianc\u00f3",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6172,
      "name":"Pi\u00e3o",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3191,
      "name":"Piat\u00e3",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3333,
      "name":"Piau",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5327,
      "name":"Picada Caf\u00e9",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7485,
      "name":"Pi\u00e7arra",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":3774,
      "name":"Picinguaba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6834,
      "name":"Picos",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3993,
      "name":"Picu\u00ed",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3775,
      "name":"Piedade",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3334,
      "name":"Piedade de Caratinga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3335,
      "name":"Piedade de Ponte Nova",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6906,
      "name":"Piedade do Rio Grande",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3336,
      "name":"Piedade dos Gerais",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6393,
      "name":"Pi\u00ean",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6437,
      "name":"Pil\u00e3o Arcado",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7404,
      "name":"Pilar",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7766,
      "name":"Pilar",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8358,
      "name":"Pilar de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3776,
      "name":"Pilar do Sul",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":86034,
      "name":"Pilha de Est\u00e9ril",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":5882,
      "name":"Pil\u00f5es",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7405,
      "name":"Pil\u00f5es",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7406,
      "name":"Pil\u00f5ezinhos",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3194,
      "name":"Pimenta",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5755,
      "name":"Pimenta Bueno",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":6835,
      "name":"Pimenteiras",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5756,
      "name":"Pimenteiras do Oeste",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":4170,
      "name":"Pinda\u00ed",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6337,
      "name":"Pinda\u00edbas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3777,
      "name":"Pindamonhangaba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8461,
      "name":"Pindar\u00e9 Mirim",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4591,
      "name":"Pindoba",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6438,
      "name":"Pindoba\u00e7u",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3778,
      "name":"Pindorama",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3434,
      "name":"Pindorama do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8128,
      "name":"Pindoretama",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":83465,
      "name":"Pingo-d'\u00c1gua",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3337,
      "name":"Pingo d'\u00c1gua - DESATIVADA",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6394,
      "name":"Pinhais",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5333,
      "name":"Pinhal",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6395,
      "name":"Pinhal\u00e3o",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5328,
      "name":"Pinhal da Serra",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6396,
      "name":"Pinhal de S\u00e3o Bento",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5331,
      "name":"Pinhal Grande",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4770,
      "name":"Pinhalzinho",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3779,
      "name":"Pinhalzinho",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4578,
      "name":"Pinh\u00e3o",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":5610,
      "name":"Pinh\u00e3o",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6173,
      "name":"Pinheiral",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5334,
      "name":"Pinheirinho do Vale",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8462,
      "name":"Pinheiro",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5335,
      "name":"Pinheiro Machado",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4771,
      "name":"Pinheiro Preto",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8257,
      "name":"Pinheiros",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6313,
      "name":"Pinhotiba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3910,
      "name":"Pintadas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":83512,
      "name":"Pinto Bandeira",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3338,
      "name":"Pint\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6836,
      "name":"Pio IX",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8463,
      "name":"Pio XII",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3780,
      "name":"Piquerobi",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8129,
      "name":"Piquet Carneiro",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3781,
      "name":"Piquete",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3782,
      "name":"Piracaia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3181,
      "name":"Piracanjuba",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3339,
      "name":"Piracema",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3783,
      "name":"Piracicaba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6837,
      "name":"Piracura",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6838,
      "name":"Piracuruca",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6174,
      "name":"Pira\u00ed",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7923,
      "name":"Pira\u00ed do Norte",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6397,
      "name":"Pira\u00ed do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3785,
      "name":"Piraju",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3157,
      "name":"Pirajuba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3784,
      "name":"Piraju\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4579,
      "name":"Pirambu",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":3340,
      "name":"Piranga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3786,
      "name":"Pirangi",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8898,
      "name":"Pirangu\u00e7u",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8899,
      "name":"Piranguinho",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4137,
      "name":"Piranhas",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5664,
      "name":"Piranhas",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4284,
      "name":"Pirapemas",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8900,
      "name":"Pirapetinga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5336,
      "name":"Pirap\u00f3",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6907,
      "name":"Pirapora",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6175,
      "name":"Pirapora de Bom Jesus",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3787,
      "name":"Pirapora do Bom Jesus",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3788,
      "name":"Pirapozinho",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5613,
      "name":"Piraquara",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3435,
      "name":"Piraqu\u00ea",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3789,
      "name":"Pirassununga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5337,
      "name":"Piratini",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3790,
      "name":"Piratininga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4772,
      "name":"Piratuba",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8901,
      "name":"Pira\u00faba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5200,
      "name":"Piren\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8359,
      "name":"Pires do Rio",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8130,
      "name":"Pires Ferreira",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4269,
      "name":"Pirip\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6839,
      "name":"Piripiri",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":2836,
      "name":"Piritiba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3791,
      "name":"Pirituba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7407,
      "name":"Pirpirituba",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5614,
      "name":"Pitanga",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6398,
      "name":"Pitangueiras",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3792,
      "name":"Pitangueiras",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6908,
      "name":"Pitangui",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6246,
      "name":"Pitarana",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7408,
      "name":"Pitimbu",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5690,
      "name":"Piu\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3436,
      "name":"Pium",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8258,
      "name":"Pi\u00fama",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5389,
      "name":"Piumhi",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7486,
      "name":"Placas",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6807,
      "name":"Pl\u00e1cido de Castro",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":8181,
      "name":"Planaltina",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":5665,
      "name":"Planaltina",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6399,
      "name":"Planaltina do Paran\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3927,
      "name":"Planaltino",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6400,
      "name":"Planalto",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3355,
      "name":"Planalto",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5338,
      "name":"Planalto",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3793,
      "name":"Planalto",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4773,
      "name":"Planalto Alegre",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4416,
      "name":"Planalto da Serra",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3158,
      "name":"Planura",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3794,
      "name":"Platina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3795,
      "name":"Po\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7134,
      "name":"Po\u00e7\u00e3o",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8464,
      "name":"Po\u00e7\u00e3o de Pedras",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4229,
      "name":"Pocinhos",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5883,
      "name":"Po\u00e7o Branco",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7409,
      "name":"Po\u00e7o Dantas",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5339,
      "name":"Po\u00e7o das Antas",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4592,
      "name":"Po\u00e7o das Trincheiras",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":7410,
      "name":"Po\u00e7o de Jos\u00e9 de Moura",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6439,
      "name":"Po\u00e7\u00f5es",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6912,
      "name":"Po\u00e7o Fundo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7645,
      "name":"Pocon\u00e9",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4580,
      "name":"Po\u00e7o Redondo",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6913,
      "name":"Po\u00e7os de Caldas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4581,
      "name":"Po\u00e7o Verde",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":8902,
      "name":"Pocrane",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3172,
      "name":"Pojuca",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3796,
      "name":"Poloni",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7411,
      "name":"Pombal",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7135,
      "name":"Pombos",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4774,
      "name":"Pomerode",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3797,
      "name":"Pomp\u00e9ia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6909,
      "name":"Pomp\u00e9u",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3798,
      "name":"Ponga\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4113,
      "name":"Ponta de Pedras",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6401,
      "name":"Ponta Grossa",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3800,
      "name":"Pontal",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4417,
      "name":"Pontal do Araguaia",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6402,
      "name":"Pontal do Paran\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8360,
      "name":"Pontalina",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3799,
      "name":"Pontalinda",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6176,
      "name":"Ponta Negra",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5340,
      "name":"Pont\u00e3o",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":9095,
      "name":"Ponta Por\u00e3",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":4776,
      "name":"Ponte Alta",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3437,
      "name":"Ponte Alta do Bom Jesus",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4775,
      "name":"Ponte Alta do Norte",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3438,
      "name":"Ponte Alta do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7646,
      "name":"Ponte Branca",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7647,
      "name":"Ponte de Pedra",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6910,
      "name":"Ponte Nova",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5341,
      "name":"Ponte Preta",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7648,
      "name":"Pontes e Lacerda",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4777,
      "name":"Ponte Serrada",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3801,
      "name":"Pontes Gestal",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6197,
      "name":"Pontinha do Coxo",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8259,
      "name":"Ponto Belo",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8903,
      "name":"Ponto Chique",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8904,
      "name":"Ponto dos Volantes",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3975,
      "name":"Ponto Novo",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3802,
      "name":"Populina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8131,
      "name":"Poranga",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3803,
      "name":"Porangaba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5396,
      "name":"Porangatu",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6177,
      "name":"Porci\u00fancula",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6403,
      "name":"Porecatu",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5884,
      "name":"Portalegre",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5345,
      "name":"Port\u00e3o",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3942,
      "name":"Porteir\u00e3o",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8132,
      "name":"Porteiras",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6911,
      "name":"Porteirinha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7487,
      "name":"Portel",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6178,
      "name":"Portela",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8361,
      "name":"Portel\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6841,
      "name":"Porto",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6808,
      "name":"Porto Acre",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":5346,
      "name":"Porto Alegre",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4322,
      "name":"Porto Alegre do Norte",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6840,
      "name":"Porto Alegre do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3426,
      "name":"Porto Alegre do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":6406,
      "name":"Porto Amazonas",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6407,
      "name":"Porto Barreiro",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4778,
      "name":"Porto Belo",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3354,
      "name":"Porto Calvo",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6446,
      "name":"Porto Camargo",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4582,
      "name":"Porto da Folha",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6179,
      "name":"Porto das Caixas",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7136,
      "name":"Porto de Galinhas",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7488,
      "name":"Porto de Moz",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6411,
      "name":"Porto de Pedras",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5885,
      "name":"Porto do Mangue",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7658,
      "name":"Porto dos Ga\u00fachos",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6344,
      "name":"Porto Esperan\u00e7a",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":7659,
      "name":"Porto Esperidi\u00e3o",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4418,
      "name":"Porto Estrela",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3804,
      "name":"Porto Feliz",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3805,
      "name":"Porto Ferreira",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8905,
      "name":"Porto Firme",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8465,
      "name":"Porto Franco",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7812,
      "name":"Porto Grande",
      "state":"AP",
      "country":"BR  "
   },
   {
      "id":5347,
      "name":"Porto Lucena",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5348,
      "name":"Porto Mau\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6447,
      "name":"Porto Mendes",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4501,
      "name":"Porto Morrinho",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6345,
      "name":"Porto Murtinho",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3439,
      "name":"Porto Nacional",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4109,
      "name":"Porto Primavera",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6181,
      "name":"Porto Real",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7767,
      "name":"Porto Real do Col\u00e9gio",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6448,
      "name":"Porto Rico",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8466,
      "name":"Porto Rico do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3174,
      "name":"Porto Sau\u00edpe",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6827,
      "name":"Porto Seguro",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4114,
      "name":"Porto Trombetas",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4779,
      "name":"Porto Uni\u00e3o",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5757,
      "name":"Porto Velho",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":6183,
      "name":"Porto Velho do Cunha",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5349,
      "name":"Porto Vera Cruz",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6219,
      "name":"Porto Vilma",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6449,
      "name":"Porto Vit\u00f3ria",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7716,
      "name":"Porto Walter",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":5350,
      "name":"Porto Xavier",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8362,
      "name":"Posse",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8906,
      "name":"Pot\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8133,
      "name":"Potengi",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3806,
      "name":"Potim",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4270,
      "name":"Potiragu\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3807,
      "name":"Potirendaba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8134,
      "name":"Potiretama",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5691,
      "name":"Pouso Alegre",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6542,
      "name":"Pouso Alto",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5351,
      "name":"Pouso Novo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4780,
      "name":"Pouso Redondo",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8260,
      "name":"Povoa\u00e7\u00e3o",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7660,
      "name":"Poxor\u00e9o",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3808,
      "name":"Pracinha",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5913,
      "name":"Pracu\u00faba",
      "state":"AP",
      "country":"BR  "
   },
   {
      "id":3164,
      "name":"Prado",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6450,
      "name":"Prado Ferreira",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3809,
      "name":"Prad\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8907,
      "name":"Prados",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7137,
      "name":"Praia da Concei\u00e7\u00e3o",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5886,
      "name":"Praia da Pipa",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6328,
      "name":"Praia do Forte",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6334,
      "name":"Praia do Franc\u00eas",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":4781,
      "name":"Praia do Santinho",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4782,
      "name":"Praia Grande",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3589,
      "name":"Praia Grande",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3440,
      "name":"Praia Norte",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":6184,
      "name":"Praia Seca",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7489,
      "name":"Prainha",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6454,
      "name":"Pranchita",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3225,
      "name":"Prata",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7412,
      "name":"Prata",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6842,
      "name":"Prata do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3590,
      "name":"Prat\u00e2nia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8908,
      "name":"Prat\u00e1polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8909,
      "name":"Pratinha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3591,
      "name":"Presidente Alves",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8910,
      "name":"Presidente Bernardes",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3592,
      "name":"Presidente Bernardes",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6455,
      "name":"Presidente Castelo Branco",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4783,
      "name":"Presidente Castelo Branco",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8467,
      "name":"Presidente Dutra",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4017,
      "name":"Presidente Dutra",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3593,
      "name":"Presidente Epit\u00e1cio",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7792,
      "name":"Presidente Figueiredo",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":4784,
      "name":"Presidente Get\u00falio",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7924,
      "name":"Presidente J\u00e2nio Quadros",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8468,
      "name":"Presidente Juscelino",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8911,
      "name":"Presidente Juscelino",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5887,
      "name":"Presidente Juscelino",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8261,
      "name":"Presidente Kennedy",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":3441,
      "name":"Presidente Kennedy",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8912,
      "name":"Presidente Kubitschek",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5352,
      "name":"Presidente Lucena",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5758,
      "name":"Presidente M\u00e9dici",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":8469,
      "name":"Presidente M\u00e9dici",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4785,
      "name":"Presidente Nereu",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3147,
      "name":"Presidente Oleg\u00e1rio",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3594,
      "name":"Presidente Prudente",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8470,
      "name":"Presidente Sarney",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7925,
      "name":"Presidente Tancredo Neves",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8471,
      "name":"Presidente Vargas",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3595,
      "name":"Presidente Venceslau",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7138,
      "name":"Primavera",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7490,
      "name":"Primavera",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":3596,
      "name":"Primavera",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5759,
      "name":"Primavera de Rond\u00f4nia",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":5377,
      "name":"Primavera do Leste",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8472,
      "name":"Primeira Cruz",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6456,
      "name":"Primeiro de Maio",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4811,
      "name":"Princesa",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4324,
      "name":"Princesa Isabel",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8363,
      "name":"Professor Jamil",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5353,
      "name":"Progresso",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3597,
      "name":"Promiss\u00e3o",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4583,
      "name":"Propri\u00e1",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":5354,
      "name":"Prot\u00e1sio Alves",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8913,
      "name":"Prudente de Morais",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5615,
      "name":"Prudent\u00f3polis",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3442,
      "name":"Pugmil",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":6186,
      "name":"Pureza",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4719,
      "name":"Pureza",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6189,
      "name":"Puril\u00e2ndia",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5357,
      "name":"Putinga",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7413,
      "name":"Puxinan\u00e3",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3598,
      "name":"Quadra",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5358,
      "name":"Quara\u00ed",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8914,
      "name":"Quartel Geral",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6457,
      "name":"Quarto Centen\u00e1rio",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3599,
      "name":"Quat\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6458,
      "name":"Quatigu\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7491,
      "name":"Quatipuru",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6190,
      "name":"Quatis",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6459,
      "name":"Quatro Barras",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4702,
      "name":"Quatro Irm\u00e3os",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6460,
      "name":"Quatro Pontes",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4593,
      "name":"Quebrangulo",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6461,
      "name":"Quedas do Igua\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6843,
      "name":"Queimada Nova",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7414,
      "name":"Queimadas",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6440,
      "name":"Queimadas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5948,
      "name":"Queimados",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3600,
      "name":"Queiroz",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3601,
      "name":"Queluz",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7374,
      "name":"Queluzito",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7663,
      "name":"Quer\u00eancia",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6462,
      "name":"Quer\u00eancia do Norte",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5359,
      "name":"Quevedos",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4171,
      "name":"Quijingue",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4812,
      "name":"Quilombo",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6463,
      "name":"Quinta do Sol",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3602,
      "name":"Quintana",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5361,
      "name":"Quinze de Novembro",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4713,
      "name":"Quipap\u00e1",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6528,
      "name":"Quirin\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5949,
      "name":"Quissam\u00e3",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6464,
      "name":"Quitandinha",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8135,
      "name":"Quiterian\u00f3polis",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7415,
      "name":"Quixaba",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7139,
      "name":"Quixab\u00e1",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7926,
      "name":"Quixabeira",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8136,
      "name":"Quixad\u00e1",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8137,
      "name":"Quixel\u00f4",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8138,
      "name":"Quixeramobim",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8139,
      "name":"Quixer\u00e9",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5888,
      "name":"Rafael Fernandes",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5889,
      "name":"Rafael Godeiro",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4095,
      "name":"Rafael Jambeiro",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3603,
      "name":"Rafard",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6465,
      "name":"Ramil\u00e2ndia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3604,
      "name":"Rancharia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6467,
      "name":"Rancho Alegre",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6466,
      "name":"Rancho Alegre d'Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4813,
      "name":"Rancho Queimado",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8473,
      "name":"Raposa",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5950,
      "name":"Raposo",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8915,
      "name":"Raposos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6914,
      "name":"Raul Soares",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4687,
      "name":"Ravena",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6468,
      "name":"Realeza",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6469,
      "name":"Rebou\u00e7as",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8182,
      "name":"Recanto das Emas",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":7140,
      "name":"Recife",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8916,
      "name":"Recreio",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3443,
      "name":"Recursol\u00e2ndia",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8140,
      "name":"Reden\u00e7\u00e3o",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7492,
      "name":"Reden\u00e7\u00e3o",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":3605,
      "name":"Reden\u00e7\u00e3o da Serra",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6844,
      "name":"Reden\u00e7\u00e3o do Gurgu\u00e9ia",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5362,
      "name":"Redentora",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8917,
      "name":"Reduto",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8262,
      "name":"Reg\u00eancia",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":4694,
      "name":"Regenera\u00e7\u00e3o",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3606,
      "name":"Regente Feij\u00f3",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3607,
      "name":"Regin\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3608,
      "name":"Registro",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5364,
      "name":"Relvado",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7563,
      "name":"Remanso",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7416,
      "name":"Rem\u00edgio",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5951,
      "name":"Renascen\u00e7a",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6470,
      "name":"Renascen\u00e7a",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8141,
      "name":"Reriutaba",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5952,
      "name":"Resende",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8918,
      "name":"Resende Costa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6472,
      "name":"Reserva",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4225,
      "name":"Reserva do Caba\u00e7al",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6471,
      "name":"Reserva do Igua\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8919,
      "name":"Resplendor",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8920,
      "name":"Ressaquinha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3609,
      "name":"Restinga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5366,
      "name":"Restinga Seca",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5953,
      "name":"Retiro do Muria\u00e9",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7927,
      "name":"Retirol\u00e2ndia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":390415,
      "name":"RH26",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7417,
      "name":"Riach\u00e3o",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8474,
      "name":"Riach\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7928,
      "name":"Riach\u00e3o das Neves",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7418,
      "name":"Riach\u00e3o do Bacamarte",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4584,
      "name":"Riach\u00e3o do Dantas",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":3206,
      "name":"Riach\u00e3o do Jacu\u00edpe",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7419,
      "name":"Riach\u00e3o do Po\u00e7o",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8921,
      "name":"Riachinho",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3445,
      "name":"Riachinho",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5890,
      "name":"Riacho da Cruz",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7141,
      "name":"Riacho das Almas",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5891,
      "name":"Riacho de Santana",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6441,
      "name":"Riacho de Santana",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7420,
      "name":"Riacho de Santo Ant\u00f4nio",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7421,
      "name":"Riacho dos Cavalos",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8922,
      "name":"Riacho dos Machados",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6845,
      "name":"Riacho Frio",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3610,
      "name":"Riacho Grande",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5892,
      "name":"Riachuelo",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4585,
      "name":"Riachuelo",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4066,
      "name":"Rialma",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5954,
      "name":"Rialto",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8364,
      "name":"Rian\u00e1polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8475,
      "name":"Ribamar Fiquene",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5495,
      "name":"Ribas do Rio Pardo",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3619,
      "name":"Ribeira",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4634,
      "name":"Ribeira do Amparo",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6846,
      "name":"Ribeira do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6442,
      "name":"Ribeira do Pombal",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7142,
      "name":"Ribeir\u00e3o",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3611,
      "name":"Ribeir\u00e3o Bonito",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3612,
      "name":"Ribeir\u00e3o Branco",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3949,
      "name":"Ribeir\u00e3o Cascalheira",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6473,
      "name":"Ribeir\u00e3o Claro",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3613,
      "name":"Ribeir\u00e3o Corrente",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6915,
      "name":"Ribeir\u00e3o das Neves",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4172,
      "name":"Ribeir\u00e3o do Largo",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6474,
      "name":"Ribeir\u00e3o do Pinhal",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3614,
      "name":"Ribeir\u00e3o dos \u00cdndios",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3615,
      "name":"Ribeir\u00e3o do Sul",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3616,
      "name":"Ribeir\u00e3o Grande",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3617,
      "name":"Ribeir\u00e3o Pires",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3618,
      "name":"Ribeir\u00e3o Preto",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3894,
      "name":"Ribeir\u00e3o Vermelho",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3950,
      "name":"Ribeir\u00e3ozinho",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6847,
      "name":"Ribeiro Gon\u00e7alves",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4586,
      "name":"Ribeir\u00f3polis",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":3620,
      "name":"Rifaina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3621,
      "name":"Rinc\u00e3o",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3622,
      "name":"Rin\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8923,
      "name":"Rio Acima",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3976,
      "name":"Rio Ant\u00f4nio",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6475,
      "name":"Rio Azul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8263,
      "name":"Rio Bananal",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6476,
      "name":"Rio Bom",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5955,
      "name":"Rio Bonito",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6477,
      "name":"Rio Bonito do Igua\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4419,
      "name":"Rio Branco",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7717,
      "name":"Rio Branco",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":6478,
      "name":"Rio Branco do Iva\u00ed",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6479,
      "name":"Rio Branco do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":9096,
      "name":"Rio Brilhante",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8924,
      "name":"Rio Casca",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3623,
      "name":"Rio Claro",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5956,
      "name":"Rio Claro",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5760,
      "name":"Rio Crespo",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":3446,
      "name":"Rio da Concei\u00e7\u00e3o",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4814,
      "name":"Rio das Antas",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5957,
      "name":"Rio das Flores",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5958,
      "name":"Rio das Ostras",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3624,
      "name":"Rio das Pedras",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7929,
      "name":"Rio de Contas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5959,
      "name":"Rio de Janeiro",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":73779,
      "name":"Rio de Janeiro - centro",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7930,
      "name":"Rio do Ant\u00f4nio",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4815,
      "name":"Rio do Campo",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8925,
      "name":"Rio Doce",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4816,
      "name":"Rio d'Oeste",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5894,
      "name":"Rio do Fogo",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3977,
      "name":"Rio do Pires",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3343,
      "name":"Rio do Prado",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6480,
      "name":"Rio do Salto",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3447,
      "name":"Rio dos Bois",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4817,
      "name":"Rio dos Cedros",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5367,
      "name":"Rio dos \u00cdndios",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4818,
      "name":"Rio do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8926,
      "name":"Rio Espera",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7143,
      "name":"Rio Formoso",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4819,
      "name":"Rio Fortuna",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5368,
      "name":"Rio Grande",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3625,
      "name":"Rio Grande da Serra",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6848,
      "name":"Rio Grande do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5960,
      "name":"Riograndina",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3626,
      "name":"Riol\u00e2ndia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6412,
      "name":"Rio Largo",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8927,
      "name":"Rio Manso",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7493,
      "name":"Rio Maria",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4820,
      "name":"Rio Negrinho",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5504,
      "name":"Rio Negro",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6481,
      "name":"Rio Negro",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8928,
      "name":"Rio Novo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8264,
      "name":"Rio Novo do Sul",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8929,
      "name":"Rio Parana\u00edba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5370,
      "name":"Rio Pardo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6916,
      "name":"Rio Pardo de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8930,
      "name":"Rio Piracicaba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8931,
      "name":"Rio Pomba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3341,
      "name":"Rio Preto",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4873,
      "name":"Rio Preto da Eva",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":3203,
      "name":"Rio Quente",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3207,
      "name":"Rio Real",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4821,
      "name":"Rio Rufino",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3448,
      "name":"Rio Sono",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7422,
      "name":"Rio Tinto",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6863,
      "name":"Rio Verde",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5298,
      "name":"Rio Verde de Mato Grosso",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":5505,
      "name":"Rio Verde do Sul",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3342,
      "name":"Rio Vermelho",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5373,
      "name":"Riozinho",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4822,
      "name":"Riqueza",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3344,
      "name":"Rit\u00e1polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4498,
      "name":"Riverl\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3627,
      "name":"Riversul",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3628,
      "name":"Riviera de S\u00e3o Louren\u00e7o",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":84019,
      "name":"RJ - Barra",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":84022,
      "name":"RJ - Copacabana",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":84020,
      "name":"RJ - Deodoro",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":84021,
      "name":"RJ - Maracan\u00e3",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5374,
      "name":"Roca Sales",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5506,
      "name":"Rochedinho",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3947,
      "name":"Rochedo",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8932,
      "name":"Rochedo de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6285,
      "name":"Roda Velha",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4823,
      "name":"Rodeio",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5120,
      "name":"Rodeio Bonito",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8933,
      "name":"Rodeiro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7931,
      "name":"Rodelas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5928,
      "name":"Rodolfo Fernandes",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7718,
      "name":"Rodrigues Alves",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":5121,
      "name":"Rolador",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5616,
      "name":"Rol\u00e2ndia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5122,
      "name":"Rolante",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5761,
      "name":"Rolim de Moura",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":8934,
      "name":"Romaria",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4824,
      "name":"Romel\u00e2ndia",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6482,
      "name":"Roncador",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5123,
      "name":"Ronda Alta",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5124,
      "name":"Rondinha",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":83466,
      "name":"Rondol\u00e2ndia",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6483,
      "name":"Rondon",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7494,
      "name":"Rondon do Par\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7664,
      "name":"Rondon\u00f3polis",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5125,
      "name":"Roque Gonzales",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5782,
      "name":"Rorain\u00f3polis",
      "state":"RR",
      "country":"BR  "
   },
   {
      "id":5961,
      "name":"Rosal",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3629,
      "name":"Rosana",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8476,
      "name":"Ros\u00e1rio",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8935,
      "name":"Ros\u00e1rio da Limeira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4587,
      "name":"Ros\u00e1rio do Catete",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":6484,
      "name":"Ros\u00e1rio do Iva\u00ed",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5126,
      "name":"Ros\u00e1rio do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7665,
      "name":"Ros\u00e1rio Oeste",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3630,
      "name":"Roseira",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4594,
      "name":"Roteiro",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8936,
      "name":"Rubelita",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3631,
      "name":"Rubi\u00e1cea",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4067,
      "name":"Rubiataba",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8937,
      "name":"Rubim",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3632,
      "name":"Rubin\u00e9ia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7495,
      "name":"Rur\u00f3polis",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8142,
      "name":"Russas",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7932,
      "name":"Ruy Barbosa",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5929,
      "name":"Ruy Barbosa",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6917,
      "name":"Sabar\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6485,
      "name":"Sab\u00e1udia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3633,
      "name":"Sabino",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8938,
      "name":"Sabin\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8143,
      "name":"Saboeiro",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8939,
      "name":"Sacramento",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5127,
      "name":"Sagrada Fam\u00edlia",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3634,
      "name":"Sagres",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7144,
      "name":"Sair\u00e9",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5128,
      "name":"Saldanha Marinho",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3637,
      "name":"Sales",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3635,
      "name":"Sales Oliveira",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3636,
      "name":"Sales\u00f3polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4825,
      "name":"Salete",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7145,
      "name":"Salgadinho",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7423,
      "name":"Salgadinho",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4588,
      "name":"Salgado",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":7424,
      "name":"Salgado de S\u00e3o F\u00e9lix",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6486,
      "name":"Salgado Filho",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7146,
      "name":"Salgueiro",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6918,
      "name":"Salinas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4635,
      "name":"Salinas da Margarida",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7496,
      "name":"Salin\u00f3polis",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8144,
      "name":"Salitre",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3638,
      "name":"Salmour\u00e3o",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7147,
      "name":"Salo\u00e1",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7148,
      "name":"Salobro",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3639,
      "name":"Saltinho",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4826,
      "name":"Saltinho",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3642,
      "name":"Salto",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8940,
      "name":"Salto da Divisa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3640,
      "name":"Salto de Pirapora",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4073,
      "name":"Salto do C\u00e9u",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6487,
      "name":"Salto do Itarar\u00e9",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5129,
      "name":"Salto do Jacu\u00ed",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6488,
      "name":"Salto do Lontra",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3641,
      "name":"Salto Grande",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4827,
      "name":"Salto Veloso",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5962,
      "name":"Salutaris",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7564,
      "name":"Salvador",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5130,
      "name":"Salvador das Miss\u00f5es",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5131,
      "name":"Salvador do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7497,
      "name":"Salvaterra",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8183,
      "name":"Samambaia",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":5963,
      "name":"Sambaetiba",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8477,
      "name":"Samba\u00edba",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3449,
      "name":"Sampaio",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5965,
      "name":"Sampaio Correia",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5966,
      "name":"Sana",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5132,
      "name":"Sananduva",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3986,
      "name":"Sanclerl\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3450,
      "name":"Sandol\u00e2ndia",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3643,
      "name":"Sandovalina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4828,
      "name":"Sang\u00e3o",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":9097,
      "name":"Sanga Puit\u00e3",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3994,
      "name":"Sanhar\u00f3",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3644,
      "name":"Santa Ad\u00e9lia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3645,
      "name":"Santa Albertina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6489,
      "name":"Santa Am\u00e9lia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4637,
      "name":"Santa B\u00e1rbara",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8941,
      "name":"Santa B\u00e1rbara",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5369,
      "name":"Santa B\u00e1rbara de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3646,
      "name":"Santa B\u00e1rbara d'Oeste",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3425,
      "name":"Santa B\u00e1rbara do Leste",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3423,
      "name":"Santa B\u00e1rbara do Monte Verde",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7498,
      "name":"Santa B\u00e1rbara do Par\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":5133,
      "name":"Santa B\u00e1rbara do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3424,
      "name":"Santa B\u00e1rbara do Tug\u00fario",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3647,
      "name":"Santa Branca",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4636,
      "name":"Santa Br\u00edgida",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7666,
      "name":"Santa Carmem",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7425,
      "name":"Santa Cec\u00edlia",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4829,
      "name":"Santa Cec\u00edlia",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6490,
      "name":"Santa Cec\u00edlia do Pav\u00e3o",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5134,
      "name":"Santa Cec\u00edlia do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5967,
      "name":"Santa Clara",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3648,
      "name":"Santa Clara d'Oeste",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5135,
      "name":"Santa Clara do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4325,
      "name":"Santa Cruz",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5969,
      "name":"Santa Cruz",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7151,
      "name":"Santa Cruz",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5930,
      "name":"Santa Cruz",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8265,
      "name":"Santa Cruz",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6525,
      "name":"Santa Cruz Cabr\u00e1lia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7149,
      "name":"Santa Cruz da Baixa Verde",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3649,
      "name":"Santa Cruz da Concei\u00e7\u00e3o",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3650,
      "name":"Santa Cruz da Esperan\u00e7a",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5968,
      "name":"Santa Cruz da Serra",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3651,
      "name":"Santa Cruz das Palmeiras",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7933,
      "name":"Santa Cruz da Vit\u00f3ria",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8365,
      "name":"Santa Cruz de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8942,
      "name":"Santa Cruz de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6491,
      "name":"Santa Cruz de Monte Castelo",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8943,
      "name":"Santa Cruz de Salinas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7499,
      "name":"Santa Cruz do Arari",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7150,
      "name":"Santa Cruz do Capibaribe",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3421,
      "name":"Santa Cruz do Escalvado",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6849,
      "name":"Santa Cruz do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3652,
      "name":"Santa Cruz do Rio Pardo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6850,
      "name":"Santa Cruz dos Milagres",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5136,
      "name":"Santa Cruz do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":83467,
      "name":"Santa Cruz do Xingu",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3422,
      "name":"Santa Efig\u00eania de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3653,
      "name":"Santa Ernestina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6492,
      "name":"Santa F\u00e9",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4318,
      "name":"Santa F\u00e9 de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8944,
      "name":"Santa F\u00e9 de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4706,
      "name":"Santa F\u00e9 do Araguaia",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3654,
      "name":"Santa F\u00e9 do Sul",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6851,
      "name":"Santa Filomena",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7152,
      "name":"Santa Filomena",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8512,
      "name":"Santa Filomena do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3655,
      "name":"Santa Gertrudes",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8478,
      "name":"Santa Helena",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7426,
      "name":"Santa Helena",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4830,
      "name":"Santa Helena",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6493,
      "name":"Santa Helena",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8366,
      "name":"Santa Helena de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8945,
      "name":"Santa Helena de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6494,
      "name":"Santa In\u00eas",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7427,
      "name":"Santa In\u00eas",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8479,
      "name":"Santa In\u00eas",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3246,
      "name":"Santa In\u00eas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8367,
      "name":"Santa Isabel",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3656,
      "name":"Santa Isabel",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6495,
      "name":"Santa Isabel do Iva\u00ed",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7500,
      "name":"Santa Isabel do Par\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6226,
      "name":"Santa Isabel do Rio Negro",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":6496,
      "name":"Santa Izabel do Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3126,
      "name":"Santa Juliana",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8266,
      "name":"Santa Leopoldina",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":6497,
      "name":"Santa L\u00facia",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3657,
      "name":"Santa L\u00facia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3192,
      "name":"Santaluz",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6852,
      "name":"Santa Luz",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8481,
      "name":"Santa Luzia",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7934,
      "name":"Santa Luzia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6919,
      "name":"Santa Luzia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7428,
      "name":"Santa Luzia",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5762,
      "name":"Santa Luzia d'Oeste",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":4589,
      "name":"Santa Luzia do Itanhy",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4595,
      "name":"Santa Luzia do Norte",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":7501,
      "name":"Santa Luzia do Par\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8480,
      "name":"Santa Luzia do Paru\u00e1",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8946,
      "name":"Santa Margarida",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5137,
      "name":"Santa Margarida do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8184,
      "name":"Santa Maria",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":5931,
      "name":"Santa Maria",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5139,
      "name":"Santa Maria",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5971,
      "name":"Santa Maria",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7153,
      "name":"Santa Maria da Boa Vista",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7502,
      "name":"Santa Maria das Barreiras",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":3658,
      "name":"Santa Maria da Serra",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7935,
      "name":"Santa Maria da Vit\u00f3ria",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8947,
      "name":"Santa Maria de Itabira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8267,
      "name":"Santa Maria de Jetib\u00e1",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7154,
      "name":"Santa Maria do Cambuc\u00e1",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5138,
      "name":"Santa Maria do Herval",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4105,
      "name":"Santa Maria do Itabira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3161,
      "name":"Santa Maria do Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7503,
      "name":"Santa Maria do Par\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8948,
      "name":"Santa Maria do Salto",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8949,
      "name":"Santa Maria do Sua\u00e7u\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3451,
      "name":"Santa Maria do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5970,
      "name":"Santa Maria Madalena",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6498,
      "name":"Santa Mariana",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8268,
      "name":"Santa Marta",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":3659,
      "name":"Santa Mercedes",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6499,
      "name":"Santa M\u00f4nica",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3199,
      "name":"Santana",
      "state":"AP",
      "country":"BR  "
   },
   {
      "id":7936,
      "name":"Santana",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5140,
      "name":"Santana da Boa Vista",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3660,
      "name":"Santana da Ponte Pensa",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8950,
      "name":"Santana da Vargem",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8951,
      "name":"Santana de Cataguases",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7429,
      "name":"Santana de Mangueira",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3661,
      "name":"Santana de Parna\u00edba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8952,
      "name":"Santana de Pirapama",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8145,
      "name":"Santana do Acara\u00fa",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7504,
      "name":"Santana do Araguaia",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8953,
      "name":"Santana do Capivari",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8146,
      "name":"Santana do Cariri",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8954,
      "name":"Santana do Deserto",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8955,
      "name":"Santana do Garamb\u00e9u",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5487,
      "name":"Santana do Ipanema",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6500,
      "name":"Santana do Itarar\u00e9",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8956,
      "name":"Santana do Jacar\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5141,
      "name":"Santana do Livramento",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8957,
      "name":"Santana do Manhua\u00e7u",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8482,
      "name":"Santana do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5932,
      "name":"Santana do Matos",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4596,
      "name":"Santana do Munda\u00fa",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8958,
      "name":"Santana do Para\u00edso",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6853,
      "name":"Santana do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8959,
      "name":"Santana do Riacho",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7362,
      "name":"Santana do S\u00e3o Francisco",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":5933,
      "name":"Santana do Serid\u00f3",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7430,
      "name":"Santana dos Garrotes",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3895,
      "name":"Santana dos Montes",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4638,
      "name":"Santan\u00f3polis",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8147,
      "name":"Santa Quit\u00e9ria",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8513,
      "name":"Santa Quiteria do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7431,
      "name":"Santar\u00e9m",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7506,
      "name":"Santar\u00e9m",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7505,
      "name":"Santar\u00e9m Novo",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8483,
      "name":"Santa Rita",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7432,
      "name":"Santa Rita",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5972,
      "name":"Santa Rita da Floresta",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8960,
      "name":"Santa Rita de Caldas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7565,
      "name":"Santa Rita de C\u00e1ssia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8961,
      "name":"Santa Rita de Ibitipoca",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8962,
      "name":"Santa Rita de Jacutinga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8963,
      "name":"Santa Rita de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4123,
      "name":"Santa Rita do Araguaia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3662,
      "name":"Santa Rita d'Oeste",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6501,
      "name":"Santa Rita d'Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8964,
      "name":"Santa Rita do Itueto",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6239,
      "name":"Santa Rita do Novo Destino",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":9098,
      "name":"Santa Rita do Pardo",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3663,
      "name":"Santa Rita do Passa Quatro",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5493,
      "name":"Santa Rita do Sapuca\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3452,
      "name":"Santa Rita do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7680,
      "name":"Santa Rita do Trivelato",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5142,
      "name":"Santa Rosa",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8965,
      "name":"Santa Rosa da Serra",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8368,
      "name":"Santa Rosa de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4831,
      "name":"Santa Rosa de Lima",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4590,
      "name":"Santa Rosa de Lima",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":3664,
      "name":"Santa Rosa de Viterbo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6854,
      "name":"Santa Rosa do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7719,
      "name":"Santa Rosa do Purus",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":4832,
      "name":"Santa Rosa do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3453,
      "name":"Santa Rosa do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3665,
      "name":"Santa Salete",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8269,
      "name":"Santa Teresa",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7433,
      "name":"Santa Teresinha",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7937,
      "name":"Santa Teresinha",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5143,
      "name":"Santa Tereza",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8369,
      "name":"Santa Tereza de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6502,
      "name":"Santa Tereza do Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3454,
      "name":"Santa Tereza do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4834,
      "name":"Santa Terezinha",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4420,
      "name":"Santa Terezinha",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7155,
      "name":"Santa Terezinha",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4499,
      "name":"Santa Terezinha de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6503,
      "name":"Santa Terezinha de Itaipu",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4833,
      "name":"Santa Terezinha do Progresso",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3455,
      "name":"Santa Terezinha do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":2193,
      "name":"Santa Vit\u00f3ria",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5144,
      "name":"Santa Vit\u00f3ria do Palmar",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5145,
      "name":"Santiago",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4835,
      "name":"Santiago do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4421,
      "name":"Santo Afonso",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5973,
      "name":"Santo Aleixo",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7938,
      "name":"Santo Amaro",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4836,
      "name":"Santo Amaro da Imperatriz",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4616,
      "name":"Santo Amaro das Brotas",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":5974,
      "name":"Santo Amaro de Campos",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8484,
      "name":"Santo Amaro do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3666,
      "name":"Santo Anast\u00e1cio",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3667,
      "name":"Santo Andr\u00e9",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7434,
      "name":"Santo Andr\u00e9",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5153,
      "name":"Santo \u00c2ngelo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4545,
      "name":"Santo Ant\u00f4nio",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3668,
      "name":"Santo Ant\u00f4nio da Alegria",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8370,
      "name":"Santo Ant\u00f4nio da Barra",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5146,
      "name":"Santo Ant\u00f4nio da Patrulha",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6504,
      "name":"Santo Ant\u00f4nio da Platina",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5147,
      "name":"Santo Ant\u00f4nio das Miss\u00f5es",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3987,
      "name":"Santo Ant\u00f4nio de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7939,
      "name":"Santo Ant\u00f4nio de Jesus",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6855,
      "name":"Santo Ant\u00f4nio de Lisboa",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5975,
      "name":"Santo Ant\u00f4nio de P\u00e1dua",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3669,
      "name":"Santo Ant\u00f4nio de Posse",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8966,
      "name":"Santo Ant\u00f4nio do Amparo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3670,
      "name":"Santo Ant\u00f4nio do Aracangu\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8967,
      "name":"Santo Ant\u00f4nio do Aventureiro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6505,
      "name":"Santo Ant\u00f4nio do Caiu\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4124,
      "name":"Santo Ant\u00f4nio do Descoberto",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8968,
      "name":"Santo Ant\u00f4nio do Grama",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7793,
      "name":"Santo Ant\u00f4nio do I\u00e7\u00e1",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":5976,
      "name":"Santo Ant\u00f4nio do Imb\u00e9",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8969,
      "name":"Santo Ant\u00f4nio do Itamb\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8970,
      "name":"Santo Ant\u00f4nio do Jacinto",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3671,
      "name":"Santo Ant\u00f4nio do Jardim",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7681,
      "name":"Santo Ant\u00f4nio do Leste",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7682,
      "name":"Santo Ant\u00f4nio do Leverger",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3123,
      "name":"Santo Ant\u00f4nio do Monte",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5148,
      "name":"Santo Ant\u00f4nio do Palma",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6506,
      "name":"Santo Ant\u00f4nio do Para\u00edso",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3672,
      "name":"Santo Ant\u00f4nio do Pinhal",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5149,
      "name":"Santo Ant\u00f4nio do Planalto",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8971,
      "name":"Santo Ant\u00f4nio do Retiro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8972,
      "name":"Santo Ant\u00f4nio do Rio Abaixo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8485,
      "name":"Santo Ant\u00f4nio dos Lopes",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6856,
      "name":"Santo Ant\u00f4nio dos Milagres",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6507,
      "name":"Santo Ant\u00f4nio do Sudoeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7507,
      "name":"Santo Ant\u00f4nio do Tau\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":5150,
      "name":"Santo Augusto",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5151,
      "name":"Santo Cristo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5977,
      "name":"Santo Eduardo",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3165,
      "name":"Santo Estev\u00e3o",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3673,
      "name":"Santo Expedito",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5152,
      "name":"Santo Expedito do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8973,
      "name":"Santo Hip\u00f3lito",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6508,
      "name":"Santo In\u00e1cio",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6857,
      "name":"Santo In\u00e1cio do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3674,
      "name":"Sant\u00f3polis do Aguape\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3675,
      "name":"Santos",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5390,
      "name":"Santos Dumont",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8148,
      "name":"S\u00e3o Benedito",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8486,
      "name":"S\u00e3o Benedito do Rio Preto",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7156,
      "name":"S\u00e3o Benedito do Sul",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7436,
      "name":"S\u00e3o Bento",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8487,
      "name":"S\u00e3o Bento",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8974,
      "name":"S\u00e3o Bento Abade",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3676,
      "name":"S\u00e3o Bento das Areias",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7435,
      "name":"S\u00e3o Bento de Pombal",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5934,
      "name":"S\u00e3o Bento do Norte",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3677,
      "name":"S\u00e3o Bento do Sapuca\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4837,
      "name":"S\u00e3o Bento do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3456,
      "name":"S\u00e3o Bento do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5935,
      "name":"S\u00e3o Bento do Trairi",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7157,
      "name":"S\u00e3o Bento do Una",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4838,
      "name":"S\u00e3o Bernardino",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8488,
      "name":"S\u00e3o Bernardo",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3678,
      "name":"S\u00e3o Bernardo do Campo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4839,
      "name":"S\u00e3o Bonif\u00e1cio",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5154,
      "name":"S\u00e3o Borja",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4598,
      "name":"S\u00e3o Br\u00e1s",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8975,
      "name":"S\u00e3o Br\u00e1s do Sua\u00e7u\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6858,
      "name":"S\u00e3o Braz do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7508,
      "name":"S\u00e3o Caetano de Odivelas",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":3679,
      "name":"S\u00e3o Caetano do Sul",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7158,
      "name":"S\u00e3o Caitano",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3680,
      "name":"S\u00e3o Carlos",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4840,
      "name":"S\u00e3o Carlos",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6509,
      "name":"S\u00e3o Carlos do Iva\u00ed",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4639,
      "name":"S\u00e3o Crist\u00f3v\u00e3o",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4841,
      "name":"S\u00e3o Cristov\u00e3o do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7940,
      "name":"S\u00e3o Desid\u00e9rio",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4842,
      "name":"S\u00e3o Domingos",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4641,
      "name":"S\u00e3o Domingos",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4125,
      "name":"S\u00e3o Domingos",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3978,
      "name":"S\u00e3o Domingos",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8976,
      "name":"S\u00e3o Domingos das Dores",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7437,
      "name":"S\u00e3o Domingos de Pombal",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7509,
      "name":"S\u00e3o Domingos do Araguaia",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8489,
      "name":"S\u00e3o Domingos do Azeit\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7510,
      "name":"S\u00e3o Domingos do Capim",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7438,
      "name":"S\u00e3o Domingos do Cariri",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8490,
      "name":"S\u00e3o Domingos do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8270,
      "name":"S\u00e3o Domingos do Norte",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8977,
      "name":"S\u00e3o Domingos do Prata",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5155,
      "name":"S\u00e3o Domingos do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7941,
      "name":"S\u00e3o Felipe",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5763,
      "name":"S\u00e3o Felipe d'Oeste",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":4640,
      "name":"S\u00e3o F\u00e9lix",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8491,
      "name":"S\u00e3o F\u00e9lix de Balsas",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8978,
      "name":"S\u00e3o F\u00e9lix de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7683,
      "name":"S\u00e3o F\u00e9lix do Araguaia",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3929,
      "name":"S\u00e3o F\u00e9lix do Coribe",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6859,
      "name":"S\u00e3o F\u00e9lix do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3457,
      "name":"S\u00e3o F\u00e9lix do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7511,
      "name":"S\u00e3o F\u00e9lix do Xingu",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":5936,
      "name":"S\u00e3o Fernando",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5978,
      "name":"S\u00e3o Fid\u00e9lis",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4642,
      "name":"S\u00e3o Francisco",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4201,
      "name":"S\u00e3o Francisco",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6922,
      "name":"S\u00e3o Francisco",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3682,
      "name":"S\u00e3o Francisco",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5156,
      "name":"S\u00e3o Francisco de Assis",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6860,
      "name":"S\u00e3o Francisco de Assis do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8371,
      "name":"S\u00e3o Francisco de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5979,
      "name":"S\u00e3o Francisco de Itabapoana",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5157,
      "name":"S\u00e3o Francisco de Paula",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8979,
      "name":"S\u00e3o Francisco de Paula",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8980,
      "name":"S\u00e3o Francisco de Sales",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8492,
      "name":"S\u00e3o Francisco do Brej\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3913,
      "name":"S\u00e3o Francisco do Conde",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8981,
      "name":"S\u00e3o Francisco do Gl\u00f3ria",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5764,
      "name":"S\u00e3o Francisco do Guapor\u00e9",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":8493,
      "name":"S\u00e3o Francisco do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5937,
      "name":"S\u00e3o Francisco do Oeste",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7512,
      "name":"S\u00e3o Francisco do Par\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6878,
      "name":"S\u00e3o Francisco do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4843,
      "name":"S\u00e3o Francisco do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4722,
      "name":"S\u00e3o Francisco Xavier",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7942,
      "name":"S\u00e3o Gabriel",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5158,
      "name":"S\u00e3o Gabriel",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7794,
      "name":"S\u00e3o Gabriel da Cachoeira",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":8271,
      "name":"S\u00e3o Gabriel da Palha",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8372,
      "name":"S\u00e3o Gabriel de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":9099,
      "name":"S\u00e3o Gabriel do Oeste",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8984,
      "name":"S\u00e3o Geraldo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8982,
      "name":"S\u00e3o Geraldo da Piedade",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7513,
      "name":"S\u00e3o Geraldo do Araguaia",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8983,
      "name":"S\u00e3o Geraldo do Baixio",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5980,
      "name":"S\u00e3o Gon\u00e7alo",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7439,
      "name":"S\u00e3o Gon\u00e7alo",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8985,
      "name":"S\u00e3o Gon\u00e7alo do Abaet\u00e9",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5938,
      "name":"S\u00e3o Gon\u00e7alo do Amarante",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8149,
      "name":"S\u00e3o Gon\u00e7alo do Amarante",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6886,
      "name":"S\u00e3o Gon\u00e7alo do Gurgu\u00e9ia",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8986,
      "name":"S\u00e3o Gon\u00e7alo do Par\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6925,
      "name":"S\u00e3o Gon\u00e7alo do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8987,
      "name":"S\u00e3o Gon\u00e7alo do Rio Abaixo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4437,
      "name":"S\u00e3o Gon\u00e7alo do Rio das Pedras",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8988,
      "name":"S\u00e3o Gon\u00e7alo do Rio Preto",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8989,
      "name":"S\u00e3o Gon\u00e7alo do Sapuca\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3930,
      "name":"S\u00e3o Gon\u00e7alo dos Campos",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5692,
      "name":"S\u00e3o Gotardo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5159,
      "name":"S\u00e3o Jer\u00f4nimo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6510,
      "name":"S\u00e3o Jer\u00f4nimo da Serra",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7159,
      "name":"S\u00e3o Jo\u00e3o",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3162,
      "name":"S\u00e3o Jo\u00e3o",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4844,
      "name":"S\u00e3o Jo\u00e3o Batista",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8494,
      "name":"S\u00e3o Jo\u00e3o Batista",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3233,
      "name":"S\u00e3o Jo\u00e3o Batista do Gl\u00f3ria",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5783,
      "name":"S\u00e3o Jo\u00e3o da Baliza",
      "state":"RR",
      "country":"BR  "
   },
   {
      "id":5981,
      "name":"S\u00e3o Jo\u00e3o da Barra",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3684,
      "name":"S\u00e3o Jo\u00e3o da Boa Vista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6926,
      "name":"S\u00e3o Jo\u00e3o da Canabrava",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7943,
      "name":"S\u00e3o Jo\u00e3o da Fortaleza",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6927,
      "name":"S\u00e3o Jo\u00e3o da Fronteira",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8990,
      "name":"S\u00e3o Jo\u00e3o da Lagoa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8373,
      "name":"S\u00e3o Jo\u00e3o d'Alian\u00e7a",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8991,
      "name":"S\u00e3o Jo\u00e3o da Mata",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8374,
      "name":"S\u00e3o Jo\u00e3o da Para\u00fana",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6046,
      "name":"S\u00e3o Jo\u00e3o da Ponta",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6923,
      "name":"S\u00e3o Jo\u00e3o da Ponte",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3685,
      "name":"S\u00e3o Jo\u00e3o das Duas Pontes",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6928,
      "name":"S\u00e3o Jo\u00e3o da Serra",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8992,
      "name":"S\u00e3o Jo\u00e3o das Miss\u00f5es",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5160,
      "name":"S\u00e3o Jo\u00e3o da Urtiga",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6929,
      "name":"S\u00e3o Jo\u00e3o da Varjota",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3686,
      "name":"S\u00e3o Jo\u00e3o de Iracema",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6924,
      "name":"S\u00e3o Jo\u00e3o del Rei",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5983,
      "name":"S\u00e3o Jo\u00e3o de Meriti",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6047,
      "name":"S\u00e3o Jo\u00e3o de Pirabas",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7514,
      "name":"S\u00e3o Jo\u00e3o do Araguaia",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6930,
      "name":"S\u00e3o Jo\u00e3o do Arraial",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6511,
      "name":"S\u00e3o Jo\u00e3o do Caiu\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4692,
      "name":"S\u00e3o Jo\u00e3o do Cariri",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8495,
      "name":"S\u00e3o Jo\u00e3o do Car\u00fa",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6512,
      "name":"S\u00e3o Jo\u00e3o d'Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4845,
      "name":"S\u00e3o Jo\u00e3o do Itaperi\u00fa",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6513,
      "name":"S\u00e3o Jo\u00e3o do Iva\u00ed",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3887,
      "name":"S\u00e3o Jo\u00e3o do Jacutinga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8150,
      "name":"S\u00e3o Jo\u00e3o do Jaguaribe",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":8993,
      "name":"S\u00e3o Jo\u00e3o do Manhua\u00e7u",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8994,
      "name":"S\u00e3o Jo\u00e3o do Manteninha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4846,
      "name":"S\u00e3o Jo\u00e3o do Oeste",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8995,
      "name":"S\u00e3o Jo\u00e3o do Oriente",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8996,
      "name":"S\u00e3o Jo\u00e3o do Pacu\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8997,
      "name":"S\u00e3o Jo\u00e3o do Para\u00edso",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5984,
      "name":"S\u00e3o Jo\u00e3o do Para\u00edso",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8496,
      "name":"S\u00e3o Jo\u00e3o do Para\u00edso",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3687,
      "name":"S\u00e3o Jo\u00e3o do Pau d'Alho",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6931,
      "name":"S\u00e3o Jo\u00e3o do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5161,
      "name":"S\u00e3o Jo\u00e3o do Pol\u00easine",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7440,
      "name":"S\u00e3o Jo\u00e3o do Rio do Peixe",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5939,
      "name":"S\u00e3o Jo\u00e3o do Sabugi",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8497,
      "name":"S\u00e3o Jo\u00e3o do Soter",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8498,
      "name":"S\u00e3o Jo\u00e3o dos Patos",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4847,
      "name":"S\u00e3o Jo\u00e3o do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7441,
      "name":"S\u00e3o Jo\u00e3o do Tigre",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6514,
      "name":"S\u00e3o Jo\u00e3o do Triunfo",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3897,
      "name":"S\u00e3o Jo\u00e3o Evangelista",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5985,
      "name":"S\u00e3o Jo\u00e3o Marcos",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3855,
      "name":"S\u00e3o Jo\u00e3o Nepomuceno",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4848,
      "name":"S\u00e3o Joaquim",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3688,
      "name":"S\u00e3o Joaquim da Barra",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8998,
      "name":"S\u00e3o Joaquim de Bicas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7160,
      "name":"S\u00e3o Joaquim do Monte",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6515,
      "name":"S\u00e3o Joaquim do Pontal",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5162,
      "name":"S\u00e3o Jorge",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6516,
      "name":"S\u00e3o Jorge d'Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6517,
      "name":"S\u00e3o Jorge do Iva\u00ed",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6518,
      "name":"S\u00e3o Jorge do Patroc\u00ednio",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4698,
      "name":"S\u00e3o Jos\u00e9",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4851,
      "name":"S\u00e3o Jos\u00e9",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8999,
      "name":"S\u00e3o Jos\u00e9 da Barra",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3689,
      "name":"S\u00e3o Jos\u00e9 da Bela Vista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6519,
      "name":"S\u00e3o Jos\u00e9 da Boa Vista",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7161,
      "name":"S\u00e3o Jos\u00e9 da Coroa Grande",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7442,
      "name":"S\u00e3o Jos\u00e9 da Lagoa Tapada",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4599,
      "name":"S\u00e3o Jos\u00e9 da Laje",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":9000,
      "name":"S\u00e3o Jos\u00e9 da Lapa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9001,
      "name":"S\u00e3o Jos\u00e9 da Safira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3690,
      "name":"S\u00e3o Jos\u00e9 das Laranjeiras",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5163,
      "name":"S\u00e3o Jos\u00e9 das Miss\u00f5es",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6550,
      "name":"S\u00e3o Jos\u00e9 das Palmeiras",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5488,
      "name":"S\u00e3o Jos\u00e9 da Tapera",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":9002,
      "name":"S\u00e3o Jos\u00e9 da Varginha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7944,
      "name":"S\u00e3o Jos\u00e9 da Vit\u00f3ria",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7443,
      "name":"S\u00e3o Jos\u00e9 de Caiana",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7214,
      "name":"S\u00e3o Jos\u00e9 de Espinharas",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5940,
      "name":"S\u00e3o Jos\u00e9 de Mipibu",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4287,
      "name":"S\u00e3o Jos\u00e9 de Piranhas",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7215,
      "name":"S\u00e3o Jos\u00e9 de Princesa",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8499,
      "name":"S\u00e3o Jos\u00e9 de Ribamar",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5986,
      "name":"S\u00e3o Jos\u00e9 de Ub\u00e1",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":9003,
      "name":"S\u00e3o Jos\u00e9 do Alegre",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4106,
      "name":"S\u00e3o Jos\u00e9 do Barreiro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3691,
      "name":"S\u00e3o Jos\u00e9 do Barreiro",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7162,
      "name":"S\u00e3o Jos\u00e9 do Belmonte",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7216,
      "name":"S\u00e3o Jos\u00e9 do Bonfim",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7359,
      "name":"S\u00e3o Jos\u00e9 do Brejo do Cruz",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6302,
      "name":"S\u00e3o Jos\u00e9 do Buriti",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8272,
      "name":"S\u00e3o Jos\u00e9 do Cal\u00e7ado",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5941,
      "name":"S\u00e3o Jos\u00e9 do Campestre",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4849,
      "name":"S\u00e3o Jos\u00e9 do Cedro",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4850,
      "name":"S\u00e3o Jos\u00e9 do Cerrito",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":9004,
      "name":"S\u00e3o Jos\u00e9 do Divino",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6932,
      "name":"S\u00e3o Jos\u00e9 do Divino",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7163,
      "name":"S\u00e3o Jos\u00e9 do Egito",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5164,
      "name":"S\u00e3o Jos\u00e9 do Erval",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":9005,
      "name":"S\u00e3o Jos\u00e9 do Goiabal",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":83468,
      "name":"S\u00e3o Jos\u00e9 do Herval",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5165,
      "name":"S\u00e3o Jos\u00e9 do Hort\u00eancio",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5166,
      "name":"S\u00e3o Jos\u00e9 do Inhacor\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7945,
      "name":"S\u00e3o Jos\u00e9 do Jacu\u00edpe",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":9006,
      "name":"S\u00e3o Jos\u00e9 do Jacuri",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9007,
      "name":"S\u00e3o Jos\u00e9 do Mantimento",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5167,
      "name":"S\u00e3o Jos\u00e9 do Norte",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5168,
      "name":"S\u00e3o Jos\u00e9 do Ouro",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6933,
      "name":"S\u00e3o Jos\u00e9 do Peixe",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6934,
      "name":"S\u00e3o Jos\u00e9 do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4422,
      "name":"S\u00e3o Jos\u00e9 do Povo",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5987,
      "name":"S\u00e3o Jos\u00e9 do Ribeir\u00e3o",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7684,
      "name":"S\u00e3o Jos\u00e9 do Rio Claro",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3692,
      "name":"S\u00e3o Jos\u00e9 do Rio Pardo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3693,
      "name":"S\u00e3o Jos\u00e9 do Rio Preto",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7217,
      "name":"S\u00e3o Jos\u00e9 do Sabugi",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5169,
      "name":"S\u00e3o Jos\u00e9 dos Ausentes",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8500,
      "name":"S\u00e3o Jos\u00e9 dos Bas\u00edlios",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3694,
      "name":"S\u00e3o Jos\u00e9 dos Campos",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7218,
      "name":"S\u00e3o Jos\u00e9 dos Cordeiros",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5942,
      "name":"S\u00e3o Jos\u00e9 do Serid\u00f3",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6551,
      "name":"S\u00e3o Jos\u00e9 dos Pinhais",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3196,
      "name":"S\u00e3o Jos\u00e9 dos Quatro Marcos",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":7219,
      "name":"S\u00e3o Jos\u00e9 dos Ramos",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":83469,
      "name":"S\u00e3o Jos\u00e9 do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5988,
      "name":"S\u00e3o Jos\u00e9 do Turvo",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5989,
      "name":"S\u00e3o Jos\u00e9 do Vale do Rio Preto",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7685,
      "name":"S\u00e3o Jos\u00e9 do Xingu",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6935,
      "name":"S\u00e3o Juli\u00e3o",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5170,
      "name":"S\u00e3o Leopoldo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6543,
      "name":"S\u00e3o Louren\u00e7o",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6552,
      "name":"S\u00e3o Louren\u00e7o",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7164,
      "name":"S\u00e3o Louren\u00e7o da Mata",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3695,
      "name":"S\u00e3o Louren\u00e7o da Serra",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4852,
      "name":"S\u00e3o Louren\u00e7o d'Oeste",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6936,
      "name":"S\u00e3o Louren\u00e7o do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5171,
      "name":"S\u00e3o Louren\u00e7o do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4853,
      "name":"S\u00e3o Ludgero",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6867,
      "name":"S\u00e3o Lu\u00eds",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5294,
      "name":"S\u00e3o Lu\u00eds de Montes Belos",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8151,
      "name":"S\u00e3o Lu\u00eds do Curu",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3696,
      "name":"S\u00e3o Lu\u00eds do Paraitinga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6937,
      "name":"S\u00e3o Luis do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7768,
      "name":"S\u00e3o Lu\u00eds do Quitunde",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8501,
      "name":"S\u00e3o Lu\u00eds Gonzaga do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5784,
      "name":"S\u00e3o Luiz",
      "state":"RR",
      "country":"BR  "
   },
   {
      "id":8375,
      "name":"S\u00e3o Luiz do Norte",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6191,
      "name":"S\u00e3o Luiz do Purun\u00e3",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5172,
      "name":"S\u00e3o Luiz Gonzaga",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7220,
      "name":"S\u00e3o Mamede",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6192,
      "name":"S\u00e3o Manoel do Paran\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3475,
      "name":"S\u00e3o Manuel",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5173,
      "name":"S\u00e3o Marcos",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4854,
      "name":"S\u00e3o Martinho",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5175,
      "name":"S\u00e3o Martinho",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6193,
      "name":"S\u00e3o Martinho",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5174,
      "name":"S\u00e3o Martinho da Serra",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5990,
      "name":"S\u00e3o Mateus",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8273,
      "name":"S\u00e3o Mateus",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":9008,
      "name":"S\u00e3o Mateus de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8502,
      "name":"S\u00e3o Mateus do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6198,
      "name":"S\u00e3o Mateus do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5944,
      "name":"S\u00e3o Miguel",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3476,
      "name":"S\u00e3o Miguel Arcanjo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6946,
      "name":"S\u00e3o Miguel da Baixa Grande",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":4855,
      "name":"S\u00e3o Miguel da Boa Vista",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7946,
      "name":"S\u00e3o Miguel das Matas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5176,
      "name":"S\u00e3o Miguel das Miss\u00f5es",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7221,
      "name":"S\u00e3o Miguel de Taipu",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4643,
      "name":"S\u00e3o Miguel do Aleixo",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":9009,
      "name":"S\u00e3o Miguel do Anta",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4126,
      "name":"S\u00e3o Miguel do Araguaia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6938,
      "name":"S\u00e3o Miguel do Fidalgo",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5943,
      "name":"S\u00e3o Miguel do Gostoso",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7515,
      "name":"S\u00e3o Miguel do Guam\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":5765,
      "name":"S\u00e3o Miguel do Guapor\u00e9",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":6199,
      "name":"S\u00e3o Miguel do Igua\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4856,
      "name":"S\u00e3o Miguel do Oeste",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7367,
      "name":"S\u00e3o Miguel do Passa Quatro",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5489,
      "name":"S\u00e3o Miguel dos Campos",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":9142,
      "name":"S\u00e3o Miguel dos Milagres",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":4695,
      "name":"S\u00e3o Miguel do Tapuio",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3458,
      "name":"S\u00e3o Miguel do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5177,
      "name":"S\u00e3o Nicolau",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8376,
      "name":"S\u00e3o Patr\u00edcio",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3477,
      "name":"S\u00e3o Paulo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5178,
      "name":"S\u00e3o Paulo das Miss\u00f5es",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7795,
      "name":"S\u00e3o Paulo de Oliven\u00e7a",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":5945,
      "name":"S\u00e3o Paulo do Potengi",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5946,
      "name":"S\u00e3o Pedro",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3479,
      "name":"S\u00e3o Pedro",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8503,
      "name":"S\u00e3o Pedro da \u00c1gua Branca",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5991,
      "name":"S\u00e3o Pedro da Aldeia",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7686,
      "name":"S\u00e3o Pedro da Cipa",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5992,
      "name":"S\u00e3o Pedro da Serra",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5179,
      "name":"S\u00e3o Pedro da Serra",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5180,
      "name":"S\u00e3o Pedro das Miss\u00f5es",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3209,
      "name":"S\u00e3o Pedro da Uni\u00e3o",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4857,
      "name":"S\u00e3o Pedro de Alc\u00e2ntara",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5181,
      "name":"S\u00e3o Pedro do Buti\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6200,
      "name":"S\u00e3o Pedro do Igua\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6201,
      "name":"S\u00e3o Pedro do Iva\u00ed",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6202,
      "name":"S\u00e3o Pedro do Paran\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6939,
      "name":"S\u00e3o Pedro do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8504,
      "name":"S\u00e3o Pedro dos Crentes",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3234,
      "name":"S\u00e3o Pedro dos Ferros",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9010,
      "name":"S\u00e3o Pedro do Sua\u00e7u\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5182,
      "name":"S\u00e3o Pedro do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3478,
      "name":"S\u00e3o Pedro do Turvo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5947,
      "name":"S\u00e3o Rafael",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8505,
      "name":"S\u00e3o Raimundo das Mangabeiras",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8506,
      "name":"S\u00e3o Raimundo do Doca Bezerra",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6940,
      "name":"S\u00e3o Raimundo Nonato",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8507,
      "name":"S\u00e3o Roberto",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5314,
      "name":"S\u00e3o Rom\u00e3o",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3480,
      "name":"S\u00e3o Roque",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":9011,
      "name":"S\u00e3o Roque de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8274,
      "name":"S\u00e3o Roque do Cana\u00e3",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":3459,
      "name":"S\u00e3o Salvador do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4600,
      "name":"S\u00e3o Sebasti\u00e3o",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":3482,
      "name":"S\u00e3o Sebasti\u00e3o",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8185,
      "name":"S\u00e3o Sebasti\u00e3o",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":6203,
      "name":"S\u00e3o Sebasti\u00e3o da Amoreira",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":2837,
      "name":"S\u00e3o Sebasti\u00e3o da Bela Vista",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7516,
      "name":"S\u00e3o Sebasti\u00e3o da Boa Vista",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":3481,
      "name":"S\u00e3o Sebasti\u00e3o da Grama",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6196,
      "name":"S\u00e3o Sebasti\u00e3o das \u00c1guas Claras",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9012,
      "name":"S\u00e3o Sebasti\u00e3o da Vargem Alegre",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5993,
      "name":"S\u00e3o Sebasti\u00e3o de Campos",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5621,
      "name":"S\u00e3o Sebasti\u00e3o de Lagoa de Ro\u00e7a",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5994,
      "name":"S\u00e3o Sebasti\u00e3o do Alto",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":9013,
      "name":"S\u00e3o Sebasti\u00e3o do Anta",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5183,
      "name":"S\u00e3o Sebasti\u00e3o do Ca\u00ed",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":9014,
      "name":"S\u00e3o Sebasti\u00e3o do Maranh\u00e3o",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9015,
      "name":"S\u00e3o Sebasti\u00e3o do Oeste",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5297,
      "name":"S\u00e3o Sebasti\u00e3o do Para\u00edso",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7947,
      "name":"S\u00e3o Sebasti\u00e3o do Pass\u00e9",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6333,
      "name":"S\u00e3o Sebasti\u00e3o do Pontal",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9016,
      "name":"S\u00e3o Sebasti\u00e3o do Rio Preto",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6544,
      "name":"S\u00e3o Sebasti\u00e3o do Rio Verde",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5995,
      "name":"S\u00e3o Sebasti\u00e3o dos Ferreiros",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3460,
      "name":"S\u00e3o Sebasti\u00e3o do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7361,
      "name":"S\u00e3o Sebasti\u00e3o do Uatum\u00e3",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7222,
      "name":"S\u00e3o Sebasti\u00e3o do Umbuzeiro",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5184,
      "name":"S\u00e3o Sep\u00e9",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8377,
      "name":"S\u00e3o Sim\u00e3o",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3483,
      "name":"S\u00e3o Sim\u00e3o",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":9017,
      "name":"S\u00e3o Tiago",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9018,
      "name":"S\u00e3o Tom\u00e1s de Aquino",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6204,
      "name":"S\u00e3o Tom\u00e9",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5642,
      "name":"S\u00e3o Tom\u00e9",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":9019,
      "name":"S\u00e3o Tom\u00e9 das Letras",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5188,
      "name":"S\u00e3o Valentim",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5187,
      "name":"S\u00e3o Valentim do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3461,
      "name":"S\u00e3o Val\u00e9rio da Natividade",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5189,
      "name":"S\u00e3o Valerio do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5191,
      "name":"S\u00e3o Vendelino",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3484,
      "name":"S\u00e3o Vicente",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5643,
      "name":"S\u00e3o Vicente",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":9020,
      "name":"S\u00e3o Vicente de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5996,
      "name":"S\u00e3o Vicente de Paula",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4230,
      "name":"S\u00e3o Vicente do Serid\u00f3",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5192,
      "name":"S\u00e3o Vicente do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7165,
      "name":"S\u00e3o Vicente Ferrer",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4285,
      "name":"S\u00e3o Vicente Ferrer",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7223,
      "name":"Sap\u00e9",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7948,
      "name":"Sapea\u00e7u",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3294,
      "name":"Sapezal",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5193,
      "name":"Sapiranga",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6205,
      "name":"Sapopema",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7517,
      "name":"Sapucaia",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":5997,
      "name":"Sapucaia",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5195,
      "name":"Sapucaia do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":9021,
      "name":"Sapuca\u00ed-Mirim",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5998,
      "name":"Saquarema",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5196,
      "name":"Sarandi",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6206,
      "name":"Sarandi",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3485,
      "name":"Sarapu\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":9022,
      "name":"Sardo\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3486,
      "name":"Sarutai\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":9023,
      "name":"Sarzedo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7949,
      "name":"S\u00e1tiro Dias",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4086,
      "name":"Satuba",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8508,
      "name":"Satubinha",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7950,
      "name":"Saubara",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6208,
      "name":"Saudade do Igua\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4858,
      "name":"Saudades",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7951,
      "name":"Sa\u00fade",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":92429,
      "name":"SBAU",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":74792,
      "name":"SBBE",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":74770,
      "name":"SBBR",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":74780,
      "name":"SBCF",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":86059,
      "name":"SBCG",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":85793,
      "name":"SBCH",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":74808,
      "name":"SBCT",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":85794,
      "name":"SBCX",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":85286,
      "name":"SBCY",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":74754,
      "name":"SBEG",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":85279,
      "name":"SBFI",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":74832,
      "name":"SBFL",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":85276,
      "name":"SBFZ",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":74816,
      "name":"SBGL",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":85282,
      "name":"SBGO",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":74839,
      "name":"SBGR",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":85287,
      "name":"SBJP",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":74833,
      "name":"SBJV",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":85288,
      "name":"SBKP",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":74810,
      "name":"SBLO",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":74811,
      "name":"SBMG",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":85280,
      "name":"SBMO",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":85285,
      "name":"SBNF",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":85278,
      "name":"SBNT",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":74827,
      "name":"SBPA",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":85284,
      "name":"SBPS",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":86060,
      "name":"SBPV",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":85277,
      "name":"SBRF",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":74817,
      "name":"SBRJ",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":85333,
      "name":"SBSG",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":85283,
      "name":"SBSL",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":74845,
      "name":"SBSP",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":85281,
      "name":"SBSV",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":92428,
      "name":"SBVC",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":74771,
      "name":"SBVT",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":4859,
      "name":"Schroeder",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":2504,
      "name":"Seabra",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4860,
      "name":"Seara",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3487,
      "name":"Sebastian\u00f3polis do Sul",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6941,
      "name":"Sebasti\u00e3o Barros",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5999,
      "name":"Sebasti\u00e3o de Lacerda",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4514,
      "name":"Sebasti\u00e3o Laranjeiras",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6942,
      "name":"Sebasti\u00e3o Leal",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5197,
      "name":"Seberi",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6000,
      "name":"Secret\u00e1rio",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6209,
      "name":"Sede Alvorada",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5198,
      "name":"Sede Nova",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5201,
      "name":"Segredo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5202,
      "name":"Selbach",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4319,
      "name":"Selv\u00edria",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":9024,
      "name":"Sem-Peixe",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8511,
      "name":"Senador Alexandre Costa",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":9025,
      "name":"Senador Amaral",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8378,
      "name":"Senador Canedo",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":9026,
      "name":"Senador Cortes",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5644,
      "name":"Senador El\u00f3i de Souza",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":9027,
      "name":"Senador Firmino",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5645,
      "name":"Senador Georgino Avelino",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7720,
      "name":"Senador Guiomard",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":9028,
      "name":"Senador Jos\u00e9 Bento",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7518,
      "name":"Senador Jos\u00e9 Porf\u00edrio",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8509,
      "name":"Senador La Rocque",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":9029,
      "name":"Senador Modestino Gon\u00e7alves",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8152,
      "name":"Senador Pompeu",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4597,
      "name":"Senador Rui Palmeira",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":8153,
      "name":"Senador S\u00e1",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5204,
      "name":"Senador Salgado Filho",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4538,
      "name":"Sena Madureira",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":6210,
      "name":"Seng\u00e9s",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":9030,
      "name":"Senhora de Oliveira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9031,
      "name":"Senhora do Porto",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9032,
      "name":"Senhora dos Rem\u00e9dios",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7566,
      "name":"Senhor do Bonfim",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5205,
      "name":"Sentinela do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7952,
      "name":"Sento S\u00e9",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5206,
      "name":"Serafina Correa",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":9033,
      "name":"Sericita",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7224,
      "name":"Serid\u00f3",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5766,
      "name":"Seringueiras",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":5207,
      "name":"S\u00e9rio",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":9034,
      "name":"Seritinga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6001,
      "name":"Serop\u00e9dica",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8275,
      "name":"Serra",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":4861,
      "name":"Serra Alta",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3488,
      "name":"Serra Azul",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":9035,
      "name":"Serra Azul de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7225,
      "name":"Serra Branca",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7226,
      "name":"Serra da Raiz",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":9036,
      "name":"Serra da Saudade",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5646,
      "name":"Serra de S\u00e3o Bento",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3171,
      "name":"Serra do Cip\u00f3",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5647,
      "name":"Serra do Mel",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5914,
      "name":"Serra do Navio",
      "state":"AP",
      "country":"BR  "
   },
   {
      "id":7953,
      "name":"Serra do Ramalho",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":9037,
      "name":"Serra dos Aimor\u00e9s",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9038,
      "name":"Serra do Salitre",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7954,
      "name":"Serra Dourada",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7227,
      "name":"Serra Grande",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3489,
      "name":"Serrana",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3490,
      "name":"Serra Negra",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5648,
      "name":"Serra Negra do Norte",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":9039,
      "name":"Serrania",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8510,
      "name":"Serrano do Maranh\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8379,
      "name":"Serran\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":9040,
      "name":"Serran\u00f3polis de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6211,
      "name":"Serran\u00f3polis do Igua\u00e7u",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":9041,
      "name":"Serranos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":83470,
      "name":"Serra Nova Dourada",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":8276,
      "name":"Serra Pelada",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":7955,
      "name":"Serra Preta",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7228,
      "name":"Serra Redonda",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7229,
      "name":"Serraria",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7166,
      "name":"Serra Talhada",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5659,
      "name":"Serrinha",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7956,
      "name":"Serrinha",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6003,
      "name":"Serrinha",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6002,
      "name":"Serrinha do Alambari",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5649,
      "name":"Serrinha dos Pintos",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":7167,
      "name":"Serrita",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":9042,
      "name":"Serro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7957,
      "name":"Serrol\u00e2ndia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6212,
      "name":"Sertaneja",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7168,
      "name":"Sert\u00e2nia",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6215,
      "name":"Sertan\u00f3polis",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5208,
      "name":"Sert\u00e3o",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5209,
      "name":"Sert\u00e3o Santana",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3491,
      "name":"Sert\u00e3ozinho",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7230,
      "name":"Sert\u00e3ozinho",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3492,
      "name":"Sete Barras",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5210,
      "name":"Sete de Setembro",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6920,
      "name":"Sete Lagoas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6004,
      "name":"Sete Pontes",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":9100,
      "name":"Sete Quedas",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3896,
      "name":"Setubinha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5211,
      "name":"Severiano de Almeida",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5670,
      "name":"Severiano Melo",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3493,
      "name":"Sever\u00ednia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4862,
      "name":"Sider\u00f3polis",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":9101,
      "name":"Sidrol\u00e2ndia",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6943,
      "name":"Sigefredo Pacheco",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6005,
      "name":"Silva Jardim",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5666,
      "name":"Silv\u00e2nia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3462,
      "name":"Silvan\u00f3polis",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5212,
      "name":"Silveira Martins",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":9043,
      "name":"Silveir\u00e2nia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3494,
      "name":"Silveiras",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4049,
      "name":"Silves",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":6921,
      "name":"Silvian\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4644,
      "name":"Sim\u00e3o Dias",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":9044,
      "name":"Sim\u00e3o Pereira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6944,
      "name":"Sim\u00f5es",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7958,
      "name":"Sim\u00f5es Filho",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8380,
      "name":"Simol\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":9045,
      "name":"Simon\u00e9sia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6945,
      "name":"Simpl\u00edcio Mendes",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5213,
      "name":"Sinimbu",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6349,
      "name":"Sinop",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6216,
      "name":"Siqueira Campos",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7169,
      "name":"Sirinha\u00e9m",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4645,
      "name":"Siriri",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":4104,
      "name":"S\u00edtio d'Abadia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7959,
      "name":"S\u00edtio do Mato",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7960,
      "name":"S\u00edtio do Quinto",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4525,
      "name":"S\u00edtio Novo",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5671,
      "name":"S\u00edtio Novo",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3464,
      "name":"S\u00edtio Novo do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8186,
      "name":"Sobradinho",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":7961,
      "name":"Sobradinho",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5214,
      "name":"Sobradinho",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7231,
      "name":"Sobrado",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8154,
      "name":"Sobral",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":9046,
      "name":"Sobr\u00e1lia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3495,
      "name":"Socorro",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6947,
      "name":"Socorro do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6006,
      "name":"Sodrel\u00e2ndia",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7232,
      "name":"Sol\u00e2nea",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5217,
      "name":"Soledade",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7233,
      "name":"Soledade",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":9047,
      "name":"Soledade de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7170,
      "name":"Solid\u00e3o",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8155,
      "name":"Solon\u00f3pole",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4863,
      "name":"Sombrio",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5376,
      "name":"Sonora",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8277,
      "name":"Sooretama",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":3496,
      "name":"Sorocaba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7687,
      "name":"Sorriso",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6007,
      "name":"Sossego",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7234,
      "name":"Soss\u00eago",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7519,
      "name":"Soure",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7235,
      "name":"Sousa",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3497,
      "name":"Sousas",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7962,
      "name":"Souto Soares",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":84016,
      "name":"SP - CENTRO",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":84018,
      "name":"SP - LESTE",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":84014,
      "name":"SP - NORTE",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":84017,
      "name":"SP - OESTE",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":84015,
      "name":"SP - SUL",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6008,
      "name":"Subaio",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8156,
      "name":"Sucesso",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3465,
      "name":"Sucupira",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":4193,
      "name":"Sucupira do Norte",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8514,
      "name":"Sucupira do Riach\u00e3o",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3498,
      "name":"Sud Mennucci",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4864,
      "name":"Sul Brasil",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6217,
      "name":"Sulina",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3499,
      "name":"Sumar\u00e9",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7236,
      "name":"Sum\u00e9",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6009,
      "name":"Sumidouro",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7171,
      "name":"Surubim",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6010,
      "name":"Suru\u00ed",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6948,
      "name":"Sussuapara",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3500,
      "name":"Suzan\u00e1polis",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3501,
      "name":"Suzano",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5222,
      "name":"Taba\u00ed",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6330,
      "name":"Tabajara",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4423,
      "name":"Tabapor\u00e3",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3502,
      "name":"Tabapu\u00e3",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3503,
      "name":"Tabatinga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5309,
      "name":"Tabatinga",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":3995,
      "name":"Tabira",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3504,
      "name":"Tabo\u00e3o da Serra",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6011,
      "name":"Taboas",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7963,
      "name":"Tabocas do Brejo Velho",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5673,
      "name":"Taboleiro Grande",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":9048,
      "name":"Tabuleiro",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8157,
      "name":"Tabuleiro do Norte",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7172,
      "name":"Tacaimb\u00f3",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7173,
      "name":"Tacaratu",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3505,
      "name":"Taciba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7237,
      "name":"Tacima",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":9102,
      "name":"Tacuru",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3506,
      "name":"Tagua\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3466,
      "name":"Taguatinga",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":8187,
      "name":"Taguatinga",
      "state":"DF",
      "country":"BR  "
   },
   {
      "id":3507,
      "name":"Taia\u00e7u",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4004,
      "name":"Tail\u00e2ndia",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4865,
      "name":"Tai\u00f3",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5360,
      "name":"Taiobeiras",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3467,
      "name":"Taipas do Tocantins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":5674,
      "name":"Taipu",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3508,
      "name":"Tai\u00fava",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3468,
      "name":"Talism\u00e3",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7174,
      "name":"Tamandar\u00e9",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6218,
      "name":"Tamarana",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3509,
      "name":"Tamba\u00fa",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6220,
      "name":"Tamboara",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3510,
      "name":"Tambor\u00e9",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8158,
      "name":"Tamboril",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6949,
      "name":"Tamboril do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":6012,
      "name":"Tamoios",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3511,
      "name":"Tanabi",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5675,
      "name":"Tangar\u00e1",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4866,
      "name":"Tangar\u00e1",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7688,
      "name":"Tangar\u00e1 da Serra",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6013,
      "name":"Tangu\u00e1",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7964,
      "name":"Tanha\u00e7u",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4601,
      "name":"Tanque d'Arca",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":6950,
      "name":"Tanque do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7965,
      "name":"Tanque Novo",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7966,
      "name":"Tanquinho",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5611,
      "name":"Taparuba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7796,
      "name":"Tapau\u00e1",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":5223,
      "name":"Tapejara",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6221,
      "name":"Tapejara",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5224,
      "name":"Tapera",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7967,
      "name":"Tapero\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7238,
      "name":"Tapero\u00e1",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5225,
      "name":"Tapes",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":9049,
      "name":"Tapira",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6222,
      "name":"Tapira",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6545,
      "name":"Tapira\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3512,
      "name":"Tapira\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3860,
      "name":"Tapiramut\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3513,
      "name":"Tapiratiba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7689,
      "name":"Tapurah",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5226,
      "name":"Taquara",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":9050,
      "name":"Taquara\u00e7u de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3514,
      "name":"Taquaral",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8381,
      "name":"Taquaral de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4602,
      "name":"Taquarana",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5227,
      "name":"Taquari",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7968,
      "name":"Taquarinha",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3515,
      "name":"Taquaritinga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7175,
      "name":"Taquaritinga do Norte",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":3516,
      "name":"Taquarituba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3517,
      "name":"Taquariva\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5228,
      "name":"Taquaru\u00e7u do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":9103,
      "name":"Taquarussu",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":3518,
      "name":"Tarabai",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7721,
      "name":"Tarauac\u00e1",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":6014,
      "name":"Tarituba",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8159,
      "name":"Tarrafas",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":7813,
      "name":"Tartarugalzinho",
      "state":"AP",
      "country":"BR  "
   },
   {
      "id":3519,
      "name":"Tarum\u00e3",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":9051,
      "name":"Tarumirim",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8515,
      "name":"Tasso Fragoso",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3520,
      "name":"Tatu\u00ed",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8160,
      "name":"Tau\u00e1",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3521,
      "name":"Taubat\u00e9",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":9104,
      "name":"Taunay",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":7239,
      "name":"Tavares",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5229,
      "name":"Tavares",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":86033,
      "name":"TCLD",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6232,
      "name":"Tebas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3522,
      "name":"Te\u00e7aind\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7797,
      "name":"Tef\u00e9",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7240,
      "name":"Teixeira",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":7969,
      "name":"Teixeira de Freitas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":9052,
      "name":"Teixeiras",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6223,
      "name":"Teixeira Soares",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5767,
      "name":"Teixeir\u00f3polis",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":8161,
      "name":"Teju\u00e7uoca",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":3523,
      "name":"Tejup\u00e1",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6224,
      "name":"Tel\u00eamaco Borba",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":4646,
      "name":"Telha",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":5676,
      "name":"Tenente Ananias",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5677,
      "name":"Tenente Laurentino Cruz",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5230,
      "name":"Tenente Portela",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7241,
      "name":"Ten\u00f3rio",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3524,
      "name":"Teodoro Sampaio",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7970,
      "name":"Teodoro Sampaio",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7971,
      "name":"Teofil\u00e2ndia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7661,
      "name":"Te\u00f3filo Otoni",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7972,
      "name":"Teol\u00e2ndia",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":4536,
      "name":"Teot\u00f4nio Vilela",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":9105,
      "name":"Terenos",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6951,
      "name":"Teresina",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8382,
      "name":"Teresina de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6015,
      "name":"Teres\u00f3polis",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7176,
      "name":"Terezinha",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":8383,
      "name":"Terez\u00f3polis de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6048,
      "name":"Terra Alta",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6225,
      "name":"Terra Boa",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5231,
      "name":"Terra de Areia",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7973,
      "name":"Terra Nova",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7177,
      "name":"Terra Nova",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7690,
      "name":"Terra Nova do Norte",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3525,
      "name":"Terra Preta",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6227,
      "name":"Terra Rica",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6228,
      "name":"Terra Roxa",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3526,
      "name":"Terra Roxa",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7520,
      "name":"Terra Santa",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7691,
      "name":"Tesouro",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5232,
      "name":"Teut\u00f4nia",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5768,
      "name":"Theobroma",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":8162,
      "name":"Tiangu\u00e1",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6249,
      "name":"Tibagi",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5612,
      "name":"Tibau",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5710,
      "name":"Tibau do Sul",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3527,
      "name":"Tiet\u00ea",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4867,
      "name":"Tigrinhos",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4868,
      "name":"Tijucas",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6250,
      "name":"Tijucas do Sul",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7178,
      "name":"Timba\u00faba",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":4546,
      "name":"Timba\u00faba dos Batistas",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4869,
      "name":"Timb\u00e9 do Sul",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8516,
      "name":"Timbiras",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4871,
      "name":"Timb\u00f3",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4870,
      "name":"Timb\u00f3 Grande",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3528,
      "name":"Timburi",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8517,
      "name":"Timon",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7662,
      "name":"Tim\u00f3teo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6016,
      "name":"Tingu\u00e1",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5233,
      "name":"Tio Hugo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6736,
      "name":"Tiradentes",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5234,
      "name":"Tiradentes do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":9053,
      "name":"Tiros",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4647,
      "name":"Tobias Barreto",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":3469,
      "name":"Tocant\u00ednia",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3470,
      "name":"Tocantin\u00f3polis",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":9054,
      "name":"Tocantins",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6017,
      "name":"Tocos",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3886,
      "name":"Tocos do Moji",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6251,
      "name":"Toledo",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":9055,
      "name":"Toledo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4651,
      "name":"Tomar do Geru",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":9056,
      "name":"Tom\u00e1s Gonzaga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6252,
      "name":"Tomazina",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":9057,
      "name":"Tombos",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7521,
      "name":"Tom\u00e9-A\u00e7u",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7798,
      "name":"Tonantins",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":4714,
      "name":"Toritama",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7692,
      "name":"Torixor\u00e9u",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5235,
      "name":"Toropi",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3529,
      "name":"Torre de Pedra",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5236,
      "name":"Torres",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3530,
      "name":"Torrinha",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5711,
      "name":"Touros",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":3531,
      "name":"Trabiju",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7522,
      "name":"Tracuateua",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7179,
      "name":"Tracunha\u00e9m",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7769,
      "name":"Traipu",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":4197,
      "name":"Trair\u00e3o",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8163,
      "name":"Trairi",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6018,
      "name":"Trajano de Morais",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5237,
      "name":"Tramanda\u00ed",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6831,
      "name":"Trancoso",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6019,
      "name":"Travess\u00e3o",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5238,
      "name":"Travesseiro",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7974,
      "name":"Tremedal",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3532,
      "name":"Trememb\u00e9",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5239,
      "name":"Trentin",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5008,
      "name":"Tr\u00eas Arroios",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4872,
      "name":"Tr\u00eas Barras",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6253,
      "name":"Tr\u00eas Barras do Paran\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5009,
      "name":"Tr\u00eas Cachoeiras",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6737,
      "name":"Tr\u00eas Cora\u00e7\u00f5es",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5010,
      "name":"Tr\u00eas Coroas",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5011,
      "name":"Tr\u00eas de Maio",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5012,
      "name":"Tr\u00eas Forquilhas",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3533,
      "name":"Tr\u00eas Fronteiras",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6020,
      "name":"Tr\u00eas Irm\u00e3os",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":9106,
      "name":"Tr\u00eas Lagoas",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":6738,
      "name":"Tr\u00eas Marias",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5013,
      "name":"Tr\u00eas Palmeiras",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5014,
      "name":"Tr\u00eas Passos",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6739,
      "name":"Tr\u00eas Pontas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3252,
      "name":"Tr\u00eas Ranchos",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6021,
      "name":"Tr\u00eas Rios",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":4875,
      "name":"Treviso",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4878,
      "name":"Treze de Maio",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4879,
      "name":"Treze T\u00edlias",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3198,
      "name":"Trindade",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6022,
      "name":"Trindade",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5667,
      "name":"Trindade",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5015,
      "name":"Trindade do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3952,
      "name":"Triunfo",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7242,
      "name":"Triunfo",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5016,
      "name":"Triunfo",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6023,
      "name":"Triunfo",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5712,
      "name":"Triunfo Potiguar",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8518,
      "name":"Trizidela do Vale",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8384,
      "name":"Trombas",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5329,
      "name":"Trombetas",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4880,
      "name":"Trombudo Central",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4881,
      "name":"Tubar\u00e3o",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6296,
      "name":"Tucano",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7523,
      "name":"Tucum\u00e3",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7693,
      "name":"Tucum\u00e3",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5017,
      "name":"Tucunduva",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7524,
      "name":"Tucuru\u00ed",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8519,
      "name":"Tufil\u00e2ndia",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3534,
      "name":"Tuiuti",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":9058,
      "name":"Tumiritinga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4882,
      "name":"Tun\u00e1polis",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":5018,
      "name":"Tunas",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6254,
      "name":"Tunas do Paran\u00e1",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6255,
      "name":"Tuneiras do Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8520,
      "name":"Tuntum",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3535,
      "name":"Tup\u00e3",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":2195,
      "name":"Tupaciguara",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7180,
      "name":"Tupanatinga",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5019,
      "name":"Tupanci do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5020,
      "name":"Tupanciret\u00e3",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5021,
      "name":"Tupandi",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5022,
      "name":"Tuparendi",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7181,
      "name":"Tuparetama",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6256,
      "name":"Tup\u00e3ssi",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":3536,
      "name":"Tupi Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3471,
      "name":"Tupirama",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":3472,
      "name":"Tupiratins",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7799,
      "name":"Tupuruquara",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7670,
      "name":"Turia\u00e7u",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8521,
      "name":"Turil\u00e2ndia",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3537,
      "name":"Turi\u00faba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6749,
      "name":"Turmalina",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3538,
      "name":"Turmalina",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5023,
      "name":"Turu\u00e7u",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8164,
      "name":"Tururu",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4026,
      "name":"Turv\u00e2nia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8385,
      "name":"Turvel\u00e2ndia",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4883,
      "name":"Turvo",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6257,
      "name":"Turvo",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":9059,
      "name":"Turvol\u00e2ndia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8522,
      "name":"Tut\u00f3ia",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7800,
      "name":"Uarini",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7567,
      "name":"Uau\u00e1",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6752,
      "name":"Ub\u00e1",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9060,
      "name":"Uba\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7975,
      "name":"Uba\u00edra",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7976,
      "name":"Ubaitaba",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":8165,
      "name":"Ubajara",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":9061,
      "name":"Ubaporanga",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3539,
      "name":"Ubarana",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7977,
      "name":"Ubat\u00e3",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3540,
      "name":"Ubatuba",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6750,
      "name":"Uberaba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6751,
      "name":"Uberl\u00e2ndia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3541,
      "name":"Ubirajara",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6258,
      "name":"Ubirat\u00e3",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5024,
      "name":"Ubiretama",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3542,
      "name":"Uchoa",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7978,
      "name":"Uiba\u00ed",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5785,
      "name":"Uiramut\u00e3",
      "state":"RR",
      "country":"BR  "
   },
   {
      "id":8386,
      "name":"Uirapuru",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4112,
      "name":"Uirapuru",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":4202,
      "name":"Uira\u00fana",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":4005,
      "name":"Ulian\u00f3polis",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":8166,
      "name":"Umari",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5713,
      "name":"Umarizal",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":4652,
      "name":"Umba\u00faba",
      "state":"SE",
      "country":"BR  "
   },
   {
      "id":7979,
      "name":"Umburanas",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":9062,
      "name":"Umburatiba",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7243,
      "name":"Umbuzeiro",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8167,
      "name":"Umirim",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6259,
      "name":"Umuarama",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7980,
      "name":"Una",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6753,
      "name":"Una\u00ed",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6952,
      "name":"Uni\u00e3o",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5025,
      "name":"Uni\u00e3o da Serra",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6260,
      "name":"Uni\u00e3o da Vit\u00f3ria",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":2377,
      "name":"Uni\u00e3o de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4884,
      "name":"Uni\u00e3o do Oeste",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":7770,
      "name":"Uni\u00e3o dos Palmares",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":4424,
      "name":"Uni\u00e3o do Sul",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3543,
      "name":"Uni\u00e3o Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6261,
      "name":"Uniflor",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5026,
      "name":"Unistalda",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5714,
      "name":"Upanema",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6262,
      "name":"Ura\u00ed",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7981,
      "name":"Urandi",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3544,
      "name":"Ur\u00e2nia",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":8523,
      "name":"Urbano Santos",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":3546,
      "name":"Uru",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3167,
      "name":"Urua\u00e7u",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":8387,
      "name":"Uruana",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":9063,
      "name":"Uruana de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3197,
      "name":"Uruar\u00e1",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":4885,
      "name":"Urubici",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8168,
      "name":"Uruburetama",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":9064,
      "name":"Uruc\u00e2nia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4685,
      "name":"Urucar\u00e1",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":7982,
      "name":"Uru\u00e7uca",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6953,
      "name":"Uru\u00e7u\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":9065,
      "name":"Urucuia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7801,
      "name":"Urucurituba",
      "state":"AM",
      "country":"BR  "
   },
   {
      "id":5027,
      "name":"Uruguaiana",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8169,
      "name":"Uruoca",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5769,
      "name":"Urup\u00e1",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":4886,
      "name":"Urupema",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3545,
      "name":"Urup\u00eas",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4887,
      "name":"Urussanga",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8388,
      "name":"Uruta\u00ed",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":86035,
      "name":"Usina",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7983,
      "name":"Utinga",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5028,
      "name":"Vacaria",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6024,
      "name":"Val\u00e3o do Barro",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":83471,
      "name":"Vale de S\u00e3o Domingos",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5770,
      "name":"Vale do Anari",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":5771,
      "name":"Vale do Para\u00edso",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":3683,
      "name":"Vale do Sol",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3547,
      "name":"Vale Formoso",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7984,
      "name":"Valen\u00e7a",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6025,
      "name":"Valen\u00e7a",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6954,
      "name":"Valen\u00e7a do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7985,
      "name":"Valente",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3548,
      "name":"Valentim Gentil",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3681,
      "name":"Vale Real",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5029,
      "name":"Vale Verde",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3549,
      "name":"Valinhos",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3550,
      "name":"Valpara\u00edso",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5344,
      "name":"Valpara\u00edso de Goi\u00e1s",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":5030,
      "name":"Vanini",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4482,
      "name":"Varge\u00e3o",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3553,
      "name":"Vargem",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4484,
      "name":"Vargem",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4717,
      "name":"Vargem Alegre",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":9066,
      "name":"Vargem Alegre",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8278,
      "name":"Vargem Alta",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":9067,
      "name":"Vargem Bonita",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":4483,
      "name":"Vargem Bonita",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":8524,
      "name":"Vargem Grande",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":6026,
      "name":"Vargem Grande",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":9068,
      "name":"Vargem Grande do Rio Pardo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":3551,
      "name":"Vargem Grande do Sul",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3552,
      "name":"Vargem Grande Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6754,
      "name":"Varginha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8389,
      "name":"Varj\u00e3o",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":9069,
      "name":"Varj\u00e3o de Minas",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8170,
      "name":"Varjota",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":6027,
      "name":"Varre Sai",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7244,
      "name":"V\u00e1rzea",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":5715,
      "name":"V\u00e1rzea",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":8171,
      "name":"V\u00e1rzea Alegre",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":4696,
      "name":"V\u00e1rzea Branca",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":9070,
      "name":"V\u00e1rzea da Palma",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7986,
      "name":"V\u00e1rzea da Ro\u00e7a",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7987,
      "name":"V\u00e1rzea do Po\u00e7o",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7694,
      "name":"V\u00e1rzea Grande",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6955,
      "name":"V\u00e1rzea Grande",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":7988,
      "name":"V\u00e1rzea Nova",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3554,
      "name":"V\u00e1rzea Paulista",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7989,
      "name":"Varzedo",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":9071,
      "name":"Varzel\u00e2ndia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6028,
      "name":"Vassouras",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3121,
      "name":"Vazante",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9107,
      "name":"Velhacaria",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":5031,
      "name":"Ven\u00e2ncio Aires",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6029,
      "name":"Venda das Flores",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":8279,
      "name":"Venda Nova do Imigrante",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5716,
      "name":"Venha-Ver",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6263,
      "name":"Ventania",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7182,
      "name":"Venturosa",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7695,
      "name":"Vera",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":5717,
      "name":"Vera Cruz",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5032,
      "name":"Vera Cruz",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7990,
      "name":"Vera Cruz",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":3555,
      "name":"Vera Cruz",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6264,
      "name":"Vera Cruz do Oeste",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6956,
      "name":"Vera Mendes",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":5033,
      "name":"Veran\u00f3polis",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3210,
      "name":"Verdejante",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":9072,
      "name":"Verdel\u00e2ndia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6265,
      "name":"Ver\u00ea",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":7991,
      "name":"Vereda",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":9073,
      "name":"Veredinha",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9074,
      "name":"Ver\u00edssimo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9075,
      "name":"Vermelho Novo",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7183,
      "name":"Vertente do L\u00e9rio",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7184,
      "name":"Vertentes",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":6755,
      "name":"Vespasiano",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":5034,
      "name":"Vespasiano Correa",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5035,
      "name":"Viadutos",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5036,
      "name":"Viam\u00e3o",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8525,
      "name":"Viana",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":8280,
      "name":"Viana",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5668,
      "name":"Vian\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":3996,
      "name":"Vic\u00eancia",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5037,
      "name":"Vicente Dutra",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":9108,
      "name":"Vicentina",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8390,
      "name":"Vicentin\u00f3polis",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":7771,
      "name":"Vi\u00e7osa",
      "state":"AL",
      "country":"BR  "
   },
   {
      "id":5718,
      "name":"Vi\u00e7osa",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":6758,
      "name":"Vi\u00e7osa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":8172,
      "name":"Vi\u00e7osa do Cear\u00e1",
      "state":"CE",
      "country":"BR  "
   },
   {
      "id":5038,
      "name":"Victor Graeff",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4485,
      "name":"Vidal Ramos",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4486,
      "name":"Videira",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":9076,
      "name":"Vieiras",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7246,
      "name":"Vieir\u00f3polis",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":6049,
      "name":"Vigia",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6266,
      "name":"Vila Alta",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6350,
      "name":"Vila Bela da Sant\u00edssima Trindade",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":3255,
      "name":"Vila Boa",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":6030,
      "name":"Vila da Grama",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5719,
      "name":"Vila Flor",
      "state":"RN",
      "country":"BR  "
   },
   {
      "id":5039,
      "name":"Vila Flores",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5040,
      "name":"Vila L\u00e2ngaro",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5041,
      "name":"Vila Maria",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":6035,
      "name":"Vila Nova de Campos",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6957,
      "name":"Vila Nova do Piau\u00ed",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":8526,
      "name":"Vila Nova dos Mart\u00edrios",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":5042,
      "name":"Vila Nova do Sul",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":8281,
      "name":"Vila Pav\u00e3o",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":8391,
      "name":"Vila Prop\u00edcio",
      "state":"GO",
      "country":"BR  "
   },
   {
      "id":4130,
      "name":"Vila Rica",
      "state":"MT",
      "country":"BR  "
   },
   {
      "id":6237,
      "name":"Vila Uni\u00e3o",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8282,
      "name":"Vila Val\u00e9rio",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":4688,
      "name":"Vila Vargas",
      "state":"MS",
      "country":"BR  "
   },
   {
      "id":8283,
      "name":"Vila Velha",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":5772,
      "name":"Vilhena",
      "state":"RO",
      "country":"BR  "
   },
   {
      "id":3556,
      "name":"Vinhedo",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3557,
      "name":"Viradouro",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":6756,
      "name":"Virgem da Lapa",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6546,
      "name":"Virg\u00ednia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9077,
      "name":"Virgin\u00f3polis",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":9078,
      "name":"Virgol\u00e2ndia",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6268,
      "name":"Virmond",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6036,
      "name":"Visconde de Imb\u00e9",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":9139,
      "name":"Visconde de Mau\u00e1",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":6757,
      "name":"Visconde do Rio Branco",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7525,
      "name":"Viseu",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":5044,
      "name":"Vista Alegre",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":3558,
      "name":"Vista Alegre do Alto",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":5043,
      "name":"Vista Alegre do Prata",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":5045,
      "name":"Vista Ga\u00facha",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7247,
      "name":"Vista Serrana",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":8284,
      "name":"Vit\u00f3ria",
      "state":"ES",
      "country":"BR  "
   },
   {
      "id":3559,
      "name":"Vit\u00f3ria Brasil",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7568,
      "name":"Vit\u00f3ria da Conquista",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":5046,
      "name":"Vit\u00f3ria das Miss\u00f5es",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":7185,
      "name":"Vit\u00f3ria de Santo Ant\u00e3o",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":5915,
      "name":"Vit\u00f3ria do Jari",
      "state":"AP",
      "country":"BR  "
   },
   {
      "id":8527,
      "name":"Vit\u00f3ria do Mearim",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":7526,
      "name":"Vit\u00f3ria do Xingu",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":6269,
      "name":"Vitorino",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":8528,
      "name":"Vitorino Freire",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4487,
      "name":"Vitor Meireles",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":9079,
      "name":"Volta Grande",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":6037,
      "name":"Volta Redonda",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":3560,
      "name":"Votorantim",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":3561,
      "name":"Votuporanga",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":7992,
      "name":"Wagner",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6958,
      "name":"Wall Ferraz",
      "state":"PI",
      "country":"BR  "
   },
   {
      "id":3473,
      "name":"Wanderl\u00e2ndia",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":7993,
      "name":"Wanderley",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6270,
      "name":"Warta",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":6271,
      "name":"Wenceslau Braz",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":9080,
      "name":"Wenceslau Braz",
      "state":"MG",
      "country":"BR  "
   },
   {
      "id":7994,
      "name":"Wenceslau Guimar\u00e3es",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":6038,
      "name":"Werneck",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":5047,
      "name":"Westf\u00e1lia",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4488,
      "name":"Witmarsum",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":3474,
      "name":"Xambio\u00e1",
      "state":"TO",
      "country":"BR  "
   },
   {
      "id":6272,
      "name":"Xambr\u00ea",
      "state":"PR",
      "country":"BR  "
   },
   {
      "id":5048,
      "name":"Xangri-l\u00e1",
      "state":"RS",
      "country":"BR  "
   },
   {
      "id":4489,
      "name":"Xanxer\u00ea",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4707,
      "name":"Xapuri",
      "state":"AC",
      "country":"BR  "
   },
   {
      "id":4490,
      "name":"Xavantina",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":4491,
      "name":"Xaxim",
      "state":"SC",
      "country":"BR  "
   },
   {
      "id":6039,
      "name":"Xer\u00e9m",
      "state":"RJ",
      "country":"BR  "
   },
   {
      "id":7186,
      "name":"Xex\u00e9u",
      "state":"PE",
      "country":"BR  "
   },
   {
      "id":7527,
      "name":"Xinguara",
      "state":"PA",
      "country":"BR  "
   },
   {
      "id":7995,
      "name":"Xique-Xique",
      "state":"BA",
      "country":"BR  "
   },
   {
      "id":7248,
      "name":"Zabel\u00ea",
      "state":"PB",
      "country":"BR  "
   },
   {
      "id":3562,
      "name":"Zacarias",
      "state":"SP",
      "country":"BR  "
   },
   {
      "id":4496,
      "name":"Z\u00e9 Doca",
      "state":"MA",
      "country":"BR  "
   },
   {
      "id":4492,
      "name":"Zort\u00e9a",
      "state":"SC",
      "country":"BR  "
   }
]