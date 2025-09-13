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

    def best_fit(self,size):
        best_start, best_size = None, self.size + 1
        free, start = 0, 0
        for i in range(self.size+1):
            if i < self.size and self.memory[i] is None:
                if free == 0: start = i
                free += 1
            else:
                if size <= free < best_size:
                    best_start, best_size = start, free
                free = 0
        return best_start

    def worst_fit(self,size):
        worst_start, worst_size = None, -1
        free, start = 0,0 
        for i in range(self.size+1):
            if i < self.size and self.memory[i] is None:
                if free == 0: start = i
                free+=1
            else:
                if free >= size and free > worst_size:
                    worst_start, worst_size = start, free
                free = 0
        return worst_start 
    
    def circular_fit(self, size):
        start = self.last_alloc    #varre a memoria a partir da ultima alocação feita 
        n = self.size
        free, pos = 0, None
        for i in range(n):
            idx = (start + i) % n     #para indice circular
            if self.memory[idx] is None:
                if free == 0:
                    pos = idx
                free += 1
                if free == size:
                    self.last_alloc = (pos + size) % n       #atualiza onde parou para próxima busca
                    return pos
            else:
                free, pos = 0, None
        return None
    
    def show_memory(self):
        print("Memoria: ", "".join([m if m else "-" for m in self.memory]))   #traço - para o espaço livre

    def show_processtable(self):
        print("Tabela de Processos: ")
        for p, (pos, size) in self.processes.items():
            print(f"{p}: base = {pos}, limite = {pos + size - 1}")   #mostra a tabela com endereço base e limite