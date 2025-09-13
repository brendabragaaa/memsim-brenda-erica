from contig.contiguous import MemoryManager
from paging.paging import PagingSystem

def run_presets():
    print("\n=== Executando Preset Scenarios ===")

    # ---------- Cenário 1: Alocação Contígua ----------
    print("\n[ Cenário 1 - Alocação Contígua ]")
    mm = MemoryManager(50)
    mm.create_process("P1", 10, "first")
    mm.create_process("P2", 15, "best")
    mm.create_process("P3", 5, "worst")
    mm.show_memory()
    mm.remove_process("P2")
    mm.show_memory()
    mm.create_process("P4", 12, "circular")
    mm.show_memory()
    mm.show_processtable()

    # ---------- Cenário 2: Paginação ----------
    print("\n[ Cenário 2 - Paginação ]")
    ps = PagingSystem(32, 4)
    ps.create_process("A", 10)
    ps.create_process("B", 8)
    ps.create_process("C", 12)
    ps.show_frames()
    ps.show_pagetable("A")
    ps.show_pagetable("B")