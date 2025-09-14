# **memsim - Simulador de Gerenciamento de Memória**

## Visão Geral
Este projeto implementa um simulador interativo de **Gerenciamento de Memória** em Sistemas Operacionais.
Ele permite explorar os conceitos de **Alocação Contígua Dinâmica** e **Paginação Pura**, com diferentes algoritmos e métricas de fragmentação.

## Linguagem e Interface
- **Linguagem**: Python 3.8+
- **Interface**: Linha de comando (CLI) interativa

## Dependências
- Apenas bibliotecas padrão do Python.

## **Como executar**

### **Pré-requisitos**
- Python 3.8+
- Git (para clonar o repositório)

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

## Decisões de Projeto e Arquitetura
- Estrutura modular: `main.py` centraliza o menu e a lógica de interface de linha de comando.
- Módulos separados para **alocação contígua** e **paginação**, facilitando manutenção e extensão.
- Uso de **classes** para representar processos e páginas, permitindo simulações independentes.

## 🖼️ Exemplos de Uso
![Menu Principal](<img width="549" height="500" alt="image" src="https://github.com/user-attachments/assets/195ed0bd-46af-470a-9040-361ee6cc8a57" />)
![Exemplo de Alocação]()

## Integrantes 
- Brenda Braga de Lima
- Érica Pilati Sartoreto


>  Projeto acadêmico - Sistemas Operacionais II
