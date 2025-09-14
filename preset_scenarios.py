from paging.paging import PagingSystem
from contig.contiguous import MemoryManager

def scenario1():
    
    ps = PagingSystem(mem_size=100, page_size=10)

    print("\n=== Cenário 1: Criando processos ===")
    ps.create_process("P1", 25)  # ocupa 3 páginas
    ps.create_process("P2", 40)  # ocupa 4 páginas
    ps.create_process("P3", 15)  # ocupa 2 páginas

    print("\n--- Frames após criação ---")
    ps.show_frames()

    print("\n--- Tabela de páginas do processo P2 ---")
    ps.show_pagetable("P2")

    return ps  

def scenario2():

    ps = PagingSystem(mem_size=120, page_size=10)

    print("\n=== Cenário 2: Criando e removendo processos ===")
    ps.create_process("A", 30)
    ps.create_process("B", 50)
    ps.show_frames()

    print("\nRemovendo processo A")
    ps.remove_process("A")
    ps.show_frames()

    print("\nCriando processo C")
    ps.create_process("C", 40)
    ps.show_frames()

    return ps

def scenario3():

    mm = MemoryManager(100)

    print("\n=== Cenário 3 contiguo: demonstrando fragmentacao externa ===")
    mm.create_process("A", 20, "first")
    mm.create_process("B", 35, "best")
    mm.create_process("C", 10, "worst")
    mm.create_process("D", 15, "circular")

    print("\nRemovendo processo B")
    mm.remove_process("B")
    mm.show_memory()

    print("\nTabela final")
    mm.show_processtable()

    return mm