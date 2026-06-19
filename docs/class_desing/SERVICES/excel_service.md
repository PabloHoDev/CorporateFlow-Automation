# ExcelService

* **Status:** 🟡 Em elaboração
* **Módulo:** `src/services/excel_service.py`
* **Categoria:** Service

---

# Objetivo

A classe `ExcelService` é responsável por encapsular todas as operações relacionadas à leitura, escrita e manipulação de arquivos Excel utilizados pela aplicação.

Seu objetivo é fornecer uma camada única e padronizada para interação com planilhas, isolando bibliotecas externas e complexidade técnica.

---

# Responsabilidade

O `ExcelService` deve executar exclusivamente operações técnicas relacionadas a arquivos Excel.

Ele não deve interpretar dados, aplicar regras de negócio ou decidir quais alterações devem ser realizadas.

---

# Responsabilidades dentro do escopo

* Abrir arquivos Excel.
* Ler dados de planilhas.
* Escrever dados em planilhas.
* Atualizar células específicas.
* Atualizar múltiplas abas.
* Preservar formatação básica quando possível.
* Converter dados entre estruturas Python e Excel.
* Garantir salvamento seguro dos arquivos.

---

# Responsabilidades fora do escopo

A classe **não deve**:

* Decidir quais dados serão alterados.
* Aplicar regras de validação de negócio.
* Executar normalização de dados.
* Controlar fluxo de execução.
* Gerar relatórios.
* Interpretar regras de domínio.

Essas responsabilidades pertencem ao `Orchestrator`, `Validators` e `Normalizers`.

---

# Métodos públicos previstos

## open_workbook()

Abre um arquivo Excel e retorna uma representação manipulável.

---

## read_sheet()

Lê dados de uma aba específica e retorna estrutura Python (ex: dict, DataFrame ou list).

---

## write_sheet()

Escreve dados em uma aba específica do arquivo Excel.

---

## update_cell()

Atualiza uma célula específica com base em coordenadas ou chave de referência.

---

## update_multiple_sheets()

Executa atualizações em múltiplas abas de forma controlada.

---

## save()

Persiste alterações realizadas no arquivo Excel.

---

## close()

Finaliza a manipulação do arquivo e libera recursos.

---

# Dependências

O `ExcelService` poderá depender de bibliotecas como:

* `openpyxl`
* `pandas`
* `pathlib.Path`

E opcionalmente de:

* `AppConfig` (para caminhos e configurações de comportamento)

Não deve depender de componentes de regra de negócio.

---

# Classes consumidoras

Espera-se que os seguintes componentes utilizem o `ExcelService`:

* `Orchestrator`
* `ReportService`
* `BusinessValidator` (somente leitura, se necessário)
* `FileService` (apoio indireto em alguns fluxos)

---

# Fluxo simplificado

```text id="p4w2sk"
InputFile
   │
   ▼
Orchestrator
   │
   ▼
ExcelService
   │
   ├── leitura
   ├── atualização
   ├── escrita
   ▼
Arquivo Excel atualizado
```

---

# Ciclo de vida

O `ExcelService` é instanciado no `main.py` (Composition Root) e injetado no `Orchestrator`.

Ele pode ser reutilizado durante toda a execução, desde que operações sejam controladas para evitar conflitos de acesso.

---

# Tratamento de erros

Erros relacionados a leitura ou escrita de Excel devem ser propagados utilizando exceções apropriadas da aplicação.

O serviço não deve suprimir erros silenciosamente.

---

# Princípios SOLID aplicados

## Single Responsibility Principle (SRP)

Possui apenas uma responsabilidade: manipular arquivos Excel.

---

## Dependency Inversion Principle (DIP)

Depende de bibliotecas externas, mas não de regras de negócio internas da aplicação.

---

## Open/Closed Principle (OCP)

Novas operações de manipulação de Excel podem ser adicionadas sem alterar a responsabilidade central do serviço.

---

# Possíveis evoluções futuras

A estrutura permite incorporar facilmente:

* suporte a arquivos Excel grandes (streaming);
* processamento assíncrono;
* cache de leitura de planilhas;
* suporte a múltiplos formatos (CSV, XLSX híbrido);
* validação estrutural de planilhas;
* integração com Google Sheets ou APIs externas;
* otimização de performance para grandes volumes.

---

# Observações arquiteturais

O `ExcelService` atua como uma camada de abstração entre a aplicação e bibliotecas de manipulação de Excel.

Nenhum outro componente deve acessar diretamente bibliotecas como `openpyxl` ou `pandas` para operações de escrita ou leitura de planilhas.

Essa responsabilidade deve permanecer centralizada neste serviço, garantindo consistência, reusabilidade e facilidade de manutenção.
