
import random


def sorteio( j):
	i = 0
	while i < j :
		x = random.randint(1, 100)

		if x == 33:
			print(x, "Existe ganhador")
		
		else:
			print(x, "Não ha ganhadores")

		i += 1


qtd = int(input("Digite a quantidade de sorteios a serem realizados"))

sorteio(qtd)

