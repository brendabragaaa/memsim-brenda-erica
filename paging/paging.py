class PagingSystem:
    def __init__(self, mem_size, page_size):
        if page_size <= 0:
            raise ValueError("Erro: o tamanho da página deve ser maior que zero.")
        if mem_size <= 0:
            raise ValueError("Erro: o tamanho da memória deve ser maior que zero.")
        if mem_size < page_size:
            raise ValueError("Erro: o tamanho da memória deve ser maior ou igual ao tamanho da página.")
        
        self.mem_size = mem_size
        self.page_size = page_size
        self.frames = [None] * (mem_size // page_size)
        self.processes = {}

    def create_process(self, name, size):
        num_pages = (size + self.page_size - 1) // self.page_size
        free_frames = [i for i, f in enumerate(self.frames) if f is None]

        if len(free_frames) < num_pages:
            print(f"Memoria insuficiente para o processo {name}.")
            return
        
        allocated = free_frames[:num_pages]
        for f in allocated:
            self.frames[f] = name

        self.processes[name] = allocated
        print(f"Processo {name} criado com {num_pages} paginas nos frames {allocated}.")

    def show_frames(self):
        print("Frames de Memoria: ")
        for i, frame in enumerate(self.frames):
            print(f"Frame {i}: {frame}")

    def show_pagetable(self, name):
        if name not in self.processes:
            print(f"Processo {name} nao encontrado.")
            return
        print(f"Tabela de paginas do processo {name}: ")
        for i, frame in enumerate(self.processes[name]):
            print(f"Pagina {i} -> Frame {frame}")