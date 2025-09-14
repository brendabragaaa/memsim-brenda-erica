# **memsim - Simulador de Gerenciamento de Memória**

## Visão Geral
Este projeto implementa um simulador interativo de **Gerenciamento de Memória** em Sistemas Operacionais.
Ele permite explorar os conceitos de **Alocação Contígua Dinâmica** e **Paginação Pura**, com diferentes algoritmos e métricas de fragmentação.

## **Como executar**

### **Pré-requisitos**
- Python 3.8+
- Git (para clonar o repositório)

## Linguagem e Interface
- **Linguagem**: Python 3.8+
- **Interface**: Linha de comando (CLI) interativa

## Dependências
- Apenas bibliotecas padrão do Python. 

### **Executando**
Na pasta raiz do repositório, execute:

```bash
python main.py
```

Isso abrirá o menu principal do simulador, com as seguintes opções:
- Alocação Contígua Dinâmica
- Paginação Pura
- Sair

## **Funcionalidades**
- Modo Alocação Contígua Dinâmica:
    - Criar e remover processos de tamanhos variados;
    - Algoritmos implementados:
        1. First-Fit
        2. Best-Fit
        3. Worst-Fit
        4. Circular-Fit
    - Exibir memória e fragmentação externa claramente;
    - Mostrar tabela de processos com endereço base e limite.

- Modo Paginação Pura:
    - Configuração de **tamanho da página** e **número de frames**;
    - Visualização da alocação não contígua de páginas em frames;
    - Exibição da **tabela de páginas** de um processo selecionado;
    - Cálculo de **fragmentação interna**.

- Métricas:
    - Percentual de **fragmentação externa** (modo contíguo);
    - Percentual de **fragmentação interna** (modo paginação);
    - Comparação entre os dois 

## Integrantes 
- Brenda Braga de Lima
- Érica Pilati Sartoreto


>  Projeto acadêmico - Sistemas Operacionais II
