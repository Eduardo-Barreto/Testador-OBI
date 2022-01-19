# Desafio disponível em: https://olimpiada.ic.unicamp.br/pratique/p2/2007/f1/mobile/

quant_pecas = int(input())

input_pecas = []

for i in range(quant_pecas):
  peca_atual = input()
  peca_atual = peca_atual.split(' ')
  peca_atual[0] = int(peca_atual[0])
  peca_atual[1] = int(peca_atual[1])
  input_pecas.append(peca_atual)

# print(quant_pecas)
# print(input_pecas)

pais_filhos = {}

for sub in input_pecas:
  filhos_atuais = pais_filhos.get(sub[1])

  if filhos_atuais is None:
    pais_filhos.update({sub[1]: [sub[0]]})

  else:
    filhos_atuais.append(sub[0])
    pais_filhos.update({sub[1]: filhos_atuais})

# print(pais_filhos)

# percorrer pais
# para cada filho atual, contar quantos filhos cada um tem
# se diferente, mal equilibrado

result = 'bem'
for pai, filhos in pais_filhos.items():
  conta_filhos = None
  # print(pai, filhos)

  for filho in filhos:
    try:
      filhos_atuais = len(pais_filhos.get(filho))
    except TypeError:
      filhos_atuais = 0


    if (conta_filhos is not None) and (filhos_atuais != conta_filhos):
      result = 'mal'
    
    conta_filhos = filhos_atuais

print(result)