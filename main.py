from contig import MemoryManager
from paging import PagingSystem

def menu():
    while True:
        print("\n=== Simulador de Gerenciamento de Memoria ===")
        print("1. Alocacao Contigua Dinamica")
        print("2. Paginacao Pura")
        print("0. Sair")

        option = input("Escolha uma opcao: ")

        if option == "1":
            run_contiguous()
        elif option == "2":
            run_paging()
        elif option == "0":
            print ("Saindo...")
            break
        else:
            print("Opcao Invalida!")

def run_contiguous():
    mm = MemoryManager(100)  #define a memoria com 100 unidades
    while True:
        print("\n---- Alocacao Contigua ----")
        print("1. Criar Processo")
        print("2. Remover Processo")
        print("3. Mostrar Memoria")
        print("4. Mostrar Tabela de Processos")
        print("0. Voltar")

        op = input("Escolha: ")

        if op == "1":
            name = input("Nomde do Processo: ")
            size = int(input("Tamanho: "))
            algorithm = input("Algoritmo (First, Best, Worst e Circular): ").lower() #lower para converter todos os caracteres
            mm.create_process(name, size, algorithm)
        elif op == "2":
            name = input("Nome do processo a ser removido: ")
            mm.remove_process(name)
        elif op == "3":
            mm.show_memory()
        elif op == "4":
            mm.show_processtable()
        elif op == "0":
            break
        else:
            print("Opcao Invalida!")

def run_paging():
    mem_size = int(input("Tamanho Total da Memoria: "))
    page_size = int(input("Tamanho da pagina: "))
    ps = PagingSystem(mem_size, page_size)

    while True:
        print("\n---- Paginacao ----")
        print("1. Criar Processo")
        print("2. Mostrar Frames")
        print("3. Mostrar Tabela de Paginas de um Processo")
        print("0. Voltar")

        op = input("Escolha: ")

        if op == "1":
            name = input("Nome do Processo: ")
            size = int(input("Tamanho: "))
            ps.create_process(name, size)
        elif op == "2":
            ps.show_frames()
        elif op == "3":
            name = input("Nome do Processo: ")
            ps.show_pagetable()
        elif op == "0":
            break
        else: 
            print("Opcao Invalida!")

if __name__ == "__main__":
    menu()