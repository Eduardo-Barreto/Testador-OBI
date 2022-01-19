import pexpect

from files import *
import os

def testar(path_codigo: str, path_entrada: str, path_saida: str, linhas_saida: int = 1) -> dict:
  aprovado = False

  arquivo_entrada = open(path_entrada, 'r')
  arquivo_saida = open(path_saida, 'r')

  entrada = arquivo_entrada.read().strip('\n')
  saida = arquivo_saida.read().strip('\n')

  child = pexpect.spawn(f'python3 {path_codigo}', encoding='utf-8')
  child.sendline(entrada)

  retorno = child.read().strip('\r\n')
  retorno = retorno.split('\r\n')
  retorno = retorno[-linhas_saida:]
  retorno = ''.join(retorno)

  child.close()
  arquivo_entrada.close()
  arquivo_saida.close()

  if(retorno == saida):
    status = 'OK'
  else:
    status = 'FAIL'

  return {'status': status, 'esperado': saida, 'encontrado': retorno}


def testar_gabarito(path_codigo: str, linhas_saida: int, ano: int, fase: int, nivel: int, nome: str, silent: bool = False) -> float:
  nome = 'mobile'
  gabarito = download_gabarito(ano, fase, nivel, nome)

  directory = os.listdir(nome)

  contador_testes = 1
  contador_erros = 0
  for conjunto in directory:
    pasta_conjunto = os.listdir(f'./{nome}/{conjunto}')
    entradas = []
    saidas = []
    for teste in pasta_conjunto:
      if 'in' in teste:
        entradas.append(teste)
      else:
        saidas.append(teste)

    for i in range(len(entradas)):
      if(not silent and i != 0):
        print('------------------------')
      teste = testar(
        path_codigo=path_codigo,
        path_entrada=f'./{nome}/{conjunto}/{entradas[i]}',
        path_saida=f'./{nome}/{conjunto}/{saidas[i]}',
        linhas_saida=linhas_saida
      )
      status = teste['status']

      if(not silent):
        print(f'Teste {contador_testes}: {teste["status"]}')

      if(status == 'FAIL'):
        contador_erros += 1
        if(not silent):
          print(f'Esperado: {teste["esperado"]}, encontrado: {teste["encontrado"]}')

      contador_testes += 1

    if(not silent):
      print('------------------------------------------------------------------------')

  taxa_sucesso = 100-(contador_erros*100/contador_testes):.2f
  return taxa_sucesso

  print(f'Fim dos testes, você passou em {100-(contador_erros*100/contador_testes):.2f}%')

testar_gabarito(
  path_codigo='./code.py',
  linhas_saida=1,
  ano=2007,
  fase=1,
  nivel=2,
  nome='mobile',
  silent=False
)
