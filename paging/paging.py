# paging_menu.py
from paging.paging import PagingSystem

def run_paging():
    mem_size = int(input("Tamanho Total da Memoria: "))
    page_size = int(input("Tamanho da pagina: "))
    ps = PagingSystem(mem_size, page_size)

    while True:
        print("\n--- Paginacao ---")
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
            ps.show_pagetable(name)

        elif op == "0":
            break
        else: 
            print("Opcao Invalida!")
