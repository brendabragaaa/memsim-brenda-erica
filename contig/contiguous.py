class MemoryManager:
    def __init__(self, size):
        self.size = size    #tamanho total da memoria
        self.memory = [None] * size         #lista com espaço livre ou ocupado
        self.processes = {}    #para guardar os processos alocados
        self.last_alloc = 0 #para utilizar no circular-fit

    def create_process(self, name, size, algorithm="first"):
        if name in self.processes:
            print(f"Erro: processo {name} ja existe!")
            return
        
        pos = None
        if algorithm == "first":
            pos = self.first_fit(size)
        elif algorithm == "best":
            pos = self.best_fit(size)
        elif algorithm == "worst":
            pos = self.worst_fit(size)
        elif algorithm == "circular":
            pos = self.circular_fit(size)
        
        if pos is not None:
            for i in range(pos, pos + size):
                self.memory[i] = name
            self.processes[name] = (pos, size)
            print(f"Processo {name} alocado de {pos} ate {pos+size+i}.")
        else:
            print("Erro: Memoria Insuficiente!")

    def remove_process(self, name):
        if name not in self.processes:
            print("Erro: Processo não encontrado!")
            return
        pos, size = self.processes.pop(name)

        for i in range(pos, pos+size):
            self.memory[i]= None
        print (f"Processo {name} removido.")

    def first_fit(self, size):
        # esta procurando o primeiro espaço livre que tenha tamanho suficiente
        free = 0
        start = 0 
        for i in range(self.size):
            if self.memory[i] is None:    #para o espaço livre
                if free == 0:
                    start = i
                free += 1
                if free == size:
                    return start     #quando achar o espaço livre
            else:
                free = 0     #reinicia a contagem se encontrar espaço ocupado
        return None