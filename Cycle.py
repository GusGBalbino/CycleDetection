class No:
    def __init__(self, valorNo):
        self.valorNo = valorNo #Armazenar o valor do nó
        self.next = None #Ponteiro para o próximo nó(Inicializado como None)



def has_cycle(head):
    
    percorridos = set() #Conjunto para armazenar todos os nós percorridos
    noAtual = head #Ponteiro que começa apontando para o nó atual(parâmetro)

    while noAtual: #Percorre a lista encadeada

        if  noAtual in percorridos: #Verificar se o nó atual já foi percorrido
            return True
        
        percorridos.add( noAtual) #Armazena o nó percorrido no laço do while
        noAtual =  noAtual.next #Avança para o próximo nó (Evita a duplicada de laço)

    return False #Laço finalizado = False

#Criação de uma lista encadeada simples (Sem ciclos) 

no1 = No(1)
no2 = No(2)
no3 = No(3)


no1.next = no2 # Nó 01 -> Nó 02
no2.next = no3 # Nó 02 -> Nó 03
# 1 -> 2 -> 3

#Criação de uma lista encadeada simples (Com ciclos)

no4 = No(4)
no5 = No(5)
no6 = No(6)

no4.next = no5 # Nó 04 -> Nó 05
no5.next = no6 # Nó 05 -> Nó 06
no6.next = no4 # Nó 06 -> Nó 04

#4 -> 5 -> 6 -> 4(CICLO)

print(has_cycle(no1)) #False
print(has_cycle(no4)) #True

