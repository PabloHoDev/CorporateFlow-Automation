# Component Diagram

* **Status:** 🟡 Em elaboração
* **Documento:** `docs/diagrams/component_diagram.md`
* **Categoria:** UML - Component Diagram

---

# Objetivo

Este diagrama apresenta a visão de alto nível dos principais componentes do sistema CorporateFlow e seus relacionamentos.

Seu objetivo é demonstrar como os módulos da aplicação colaboram entre si durante uma execução completa.

O foco deste diagrama não está em métodos ou atributos, mas sim na comunicação entre os grandes blocos arquiteturais da solução.

---

# Visão Geral da Arquitetura

```text
                    +------------------+
                    |     main.py      |
                    +---------+--------+
                              |
                              v
                    +------------------+
                    |   Orchestrator   |
                    +---------+--------+
                              |
        -------------------------------------------------
        |           |            |           |          |
        v           v            v           v          v

+-----------+ +-----------+ +-----------+ +-----------+ +------------------+
| AppConfig | | Validators| |Normalizers| | Services  | | ExecutionContext |
+-----------+ +-----------+ +-----------+ +-----------+ +------------------+

                 |                |
                 |                |
                 v                v

      +----------------+   +----------------+
      | SchemaValidator|   | TextNormalizer |
      +----------------+   +----------------+

      +----------------+   +----------------+
      |BusinessValidator|  | CityNormalizer |
      +----------------+   +----------------+

                              |
                              |
                              v

                    +------------------+
                    |    Services      |
                    +------------------+
                    | BackupService    |
                    | FileService      |
                    | ExcelService     |
                    | LogService       |
                    | ReportService    |
                    +------------------+
```

---

# Componentes Principais

## main.py

Representa o ponto de entrada da aplicação.

Responsável por:

* Inicializar componentes.
* Montar dependências.
* Criar o ExecutionContext.
* Instanciar o Orchestrator.
* Iniciar a execução.

---

## Orchestrator

Representa o núcleo da aplicação.

Responsável por:

* Coordenar o fluxo completo.
* Acionar serviços.
* Acionar validadores.
* Acionar normalizadores.
* Consolidar resultados.
* Encerrar a execução.

O Orchestrator não implementa regras específicas de processamento.

Seu papel é exclusivamente coordenar os componentes.

---

## AppConfig

Representa as configurações carregadas da aplicação.

Fornece:

* diretórios;
* parâmetros;
* caminhos;
* configurações globais.

É compartilhado entre diversos componentes.

---

## ExecutionContext

Representa o estado compartilhado da execução.

Armazena:

* configuração;
* logger;
* arquivos processados;
* resultados;
* relatório final;
* metadados da execução.

---

# Validators

Camada responsável pela validação dos dados.

## SchemaValidator

Valida:

* estrutura dos arquivos;
* colunas obrigatórias;
* tipos de dados;
* layout esperado.

---

## BusinessValidator

Valida:

* regras de negócio;
* consistência operacional;
* restrições corporativas;
* SLA.

---

# Normalizers

Camada responsável pela padronização dos dados.

## TextNormalizer

Executa:

* remoção de acentos;
* limpeza textual;
* padronização de caixa;
* tratamento de caracteres especiais.

---

## CityNormalizer

Especialização para padronização de cidades.

Utiliza o TextNormalizer como base.

---

# Services

Camada responsável pelas operações técnicas da aplicação.

---

## BackupService

Responsável por:

* criar backups;
* preservar arquivos originais;
* versionar artefatos.

---

## FileService

Responsável por:

* localizar arquivos;
* validar existência;
* manipular diretórios.

---

## ExcelService

Responsável por:

* leitura de planilhas;
* escrita de planilhas;
* atualização de arquivos Excel.

---

## LogService

Responsável por:

* registrar eventos;
* registrar erros;
* manter rastreabilidade.

---

## ReportService

Responsável por:

* exportar relatórios;
* persistir resultados;
* gerar saídas finais.

---

# Fluxo Arquitetural

Fluxo simplificado:

```text
main.py

↓

Orchestrator

↓

ExecutionContext

↓

BackupService

↓

FileService

↓

SchemaValidator

↓

BusinessValidator

↓

TextNormalizer

↓

CityNormalizer

↓

ExcelService

↓

ProcessingResult

↓

Report

↓

ReportService
```

---

# Dependências Entre Componentes

```text
main.py
    |
    v
Orchestrator
    |
    +--> AppConfig
    |
    +--> ExecutionContext
    |
    +--> Validators
    |
    +--> Normalizers
    |
    +--> Services
```

Os componentes não devem depender diretamente uns dos outros quando a comunicação puder ser intermediada pelo Orchestrator.

Essa abordagem reduz acoplamento e facilita manutenção.

---

# Princípios Arquiteturais Aplicados

## Separation of Concerns

Cada componente possui uma responsabilidade claramente definida.

---

## Dependency Injection

Dependências são criadas no Composition Root (`main.py`) e injetadas nos componentes consumidores.

---

## Single Responsibility Principle

Cada componente possui uma única responsabilidade principal.

---

## Dependency Inversion Principle

Componentes dependem de contratos e abstrações sempre que possível.

---

# Observações Arquiteturais

O Component Diagram representa a visão macro da aplicação.

Ele deve permanecer estável mesmo quando novas classes forem adicionadas ao sistema.

Mudanças frequentes devem ocorrer no nível de implementação (Classes), não no nível de Componentes.

Por esse motivo, este diagrama é considerado uma das representações mais importantes da arquitetura do CorporateFlow.
