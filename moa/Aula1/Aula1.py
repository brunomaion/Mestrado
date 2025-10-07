import math 
import random


def fun_obj(x, y):
  sol = 0.97 * math.exp(-(((x + 3) ** 2 + (y + 3) ** 2) / 5)) \
      + 0.98 * math.exp(-(((x - 3) ** 2 + (y + 3) ** 2) / 5)) \
      + 0.99 * math.exp(-(((x + 3) ** 2 + (y - 3) ** 2) / 5)) \
      + 1.00 * math.exp(-(((x - 3) ** 2 + (y - 3) ** 2) / 5))
  return sol

def rand():
  return random.uniform(0, 1)


def sol_init(tp):
  x = rand() * tp - (tp/2)
  y = rand() * tp - (tp/2)
  return [x,y]

def explotacao_min(x, y, sol, delta):
  valores = []
  vetor = []
  
  valor1 = fun_obj(x+delta, y)
  valores.append(valor1)
  vetor.append([x+delta, y])
  
  valor2 = fun_obj(x-delta, y)
  valores.append(valor2)
  vetor.append([x-delta, y])
  
  valor3 = fun_obj(x, y+delta)
  valores.append(valor3)
  vetor.append([x, y+delta])
  
  valor4 = fun_obj(x, y-delta)
  valores.append(valor4)
  vetor.append([x, y-delta])
  
  min_valor = min(valores)
  if min_valor < sol:
    index = valores.index(min_valor)
    return vetor[index]
  else:
    return [x, y]


#Busca Iterativa Rapida
def busca_iterativa_rapida(range_0, range_1, parada):
  tp = range_1 - range_0
  sol_inicial = sol_init(tp)

  sol = sol_inicial
  sol_corrente = sol_inicial
  sol_valor = fun_obj(sol[0], sol[1])
  
  i=0
  while i<parada:
    i+=1
    #Explotação
    sol_corrente=explotacao_min(sol_corrente[0], sol_corrente[1], sol_valor, 0.01)
    if fun_obj(sol_corrente[0], sol_corrente[1]) < sol_valor:
      sol = sol_corrente
      sol_valor = fun_obj(sol[0], sol[1])
    
    #Exploração
    sol_corrente = sol_init(tp)

  print("Solução: ", sol)
  print("Valor: ", sol_valor)

def busca_iterativa_local_rapida(range_0, range_1, parada):
  tp = range_1 - range_0
  sol_inicial = sol_init(tp)

  sol = sol_inicial
  sol_corrente = sol_inicial
  sol_valor = fun_obj(sol[0], sol[1])
  
  i=0
  while i<parada:
    i+=1
    #Explotação
    j=1
    while (j!=0):
      t = explotacao_min(sol_corrente[0], sol_corrente[1], sol_valor, 0.1)
      if fun_obj(t[0], t[1]) < fun_obj(sol_corrente[0], sol_corrente[1]):
        sol_corrente = t
        if fun_obj(t[0], t[1]) < fun_obj(sol[0], sol[1]):
          sol=t
          sol_valor=fun_obj(t[0], t[1])
      else:
        j=0
    #Exploração
    sol_corrente = sol_init(tp)

  print("Solução: ", sol)
  print("Valor: ", sol_valor)
  print("t:", t)



busca_iterativa_rapida(-4, 4, 100000)
busca_iterativa_local_rapida(-4, 4, 1000)



teste = fun_obj(3, 3)
print(teste)

teste = fun_obj(4, 4)
print(teste)

teste = fun_obj(3, -3)
print(teste)

teste = fun_obj(4, 4)
print(teste)


