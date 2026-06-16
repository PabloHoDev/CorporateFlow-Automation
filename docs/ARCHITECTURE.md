# ARCHITECTURE.md

# CorporateFlow Automation - Documento de Arquitetura

## 1. Objetivo do Sistema

O **CorporateFlow Automation** é um framework desenvolvido para automatizar processos corporativos baseados em arquivos estruturados (Excel, CSV e similares), reduzindo atividades manuais, aumentando a rastreabilidade das operações e promovendo padronização de dados.

A solução foi concebida para ser reutilizável em diferentes cenários de negócio, permitindo que novos fluxos sejam implementados com o mínimo de alterações na estrutura principal do sistema.

---

# 2. Objetivos Técnicos

O projeto busca atender aos seguintes objetivos:

* Separação clara de responsabilidades;
* Alta coesão entre componentes;
* Baixo acoplamento entre módulos;
* Facilidade de manutenção;
* Facilidade de extensão;
* Facilidade para criação de testes automatizados;
* Código legível e reutilizável;
* Arquitetura orientada a serviços.

---

# 3. Arquitetura Geral

O sistema é organizado em camadas independentes.

```
                main.py
                    │
                    ▼
            Orchestrator
                    │
        ┌───────────┼───────────┐
        │           │           │
        ▼           ▼           ▼
   Services    Validators   Normalizers
        │           │           │
        └───────────┼───────────┘
                    ▼
              Business Rules
                    │
                    ▼
              Report Service
                    │
                    ▼
               Output Files
```

O `Orchestrator` é responsável apenas por coordenar a execução do fluxo.

Toda lógica específica permanece encapsulada em componentes especializados.

---

# 4. Estrutura de Diretórios

```
CorporateFlow/

├── config/
├── docs/
├── input/
├── output/
├── backups/
├── logs/
├── src/
│
│   ├── core/
│   ├── services/
│   ├── validators/
│   ├── normalizers/
│   ├── models/
│   ├── exceptions/
│   ├── interfaces/
│   └── utils/
│
├── tests/
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

# 5. Responsabilidade de Cada Pasta

## config/

Centraliza todas as configurações do sistema.

Exemplos:

* caminhos;
* parâmetros;
* configurações YAML;
* variáveis de ambiente.

Nenhum caminho deverá ficar fixo no código.

---

## docs/

Contém toda documentação técnica do projeto.

Exemplos:

* arquitetura;
* diagramas;
* decisões técnicas;
* fluxogramas.

---

## input/

Diretório utilizado para entrada dos arquivos processados.

Nenhuma regra de negócio deve depender diretamente dessa pasta.

---

## output/

Armazena arquivos produzidos pelo processamento.

---

## backups/

Recebe automaticamente cópias dos arquivos antes de qualquer alteração.

---

## logs/

Contém registros detalhados da execução.

Permite auditoria completa.

---

## src/core/

Contém os componentes responsáveis por coordenar o fluxo principal.

Não implementa regras de negócio.

Seu papel é apenas orquestrar chamadas.

---

## src/services/

Implementa operações específicas.

Exemplos:

* leitura de Excel;
* backup;
* escrita;
* geração de relatórios.

Cada serviço deve possuir responsabilidade única.

---

## src/validators/

Responsável por validar dados de entrada.

Exemplos:

* colunas obrigatórias;
* formatos;
* consistência.

Nenhuma transformação deve ocorrer nesta camada.

---

## src/normalizers/

Responsável exclusivamente pela padronização dos dados.

Exemplos:

* remoção de acentos;
* tratamento de espaços;
* normalização textual;
* padronização de cidades.

---

## src/models/

Representa as entidades do domínio.

Modelos não executam processamento complexo.

São utilizados para representar informações do negócio.

---

## src/exceptions/

Define exceções customizadas utilizadas pelo sistema.

Exemplo:

```
FileValidationError

ConfigurationError

BusinessRuleError
```

---

## src/interfaces/

Contém contratos (Protocol ou ABC) utilizados para desacoplamento entre implementações.

Permite substituir implementações sem alterar consumidores.

---

## src/utils/

Funções auxiliares reutilizáveis.

Deve evitar conter regras de negócio.

---

## tests/

Armazena todos os testes automatizados.

Cada módulo principal deve possuir sua própria suíte de testes.

---

# 6. Responsabilidade das Classes Principais

## Orchestrator

Coordena toda a execução do pipeline.

Não implementa regras.

---

## ConfigurationManager

Carrega configurações do sistema.

---

## BackupService

Cria backups automáticos.

---

## ExcelService

Realiza leitura e escrita de planilhas.

---

## FileService

Manipula arquivos e diretórios.

---

## LogService

Gerencia registros de auditoria.

---

## ReportService

Produz relatórios finais da execução.

---

## SchemaValidator

Valida estrutura dos arquivos.

---

## BusinessValidator

Valida regras específicas do negócio.

---

## TextNormalizer

Padroniza textos.

---

## CityNormalizer

Padroniza nomes de municípios.

---

# 7. Comunicação Entre os Componentes

O fluxo ocorre sempre de forma sequencial.

```
main.py

↓

Orchestrator

↓

ConfigurationManager

↓

BackupService

↓

ExcelService

↓

Validators

↓

Normalizers

↓

Business Processing

↓

ReportService

↓

LogService

↓

Output
```

Nenhum componente deve acessar diretamente outro sem passar pelo fluxo definido.

---

# 8. Princípios Arquiteturais

O projeto adota os seguintes princípios:

## Single Responsibility Principle (SRP)

Cada classe possui apenas uma responsabilidade.

---

## Open/Closed Principle (OCP)

Novas funcionalidades devem ser adicionadas por extensão e não por modificação.

---

## Dependency Inversion Principle (DIP)

Componentes dependem de abstrações e não de implementações concretas.

---

## Separation of Concerns

Cada camada possui responsabilidades claramente definidas.

---

## Modularidade

Cada módulo pode evoluir independentemente.

---

## Reutilização

Componentes devem poder ser utilizados em outros projetos.

---

## Testabilidade

Toda lógica deve ser facilmente testável.

---

## Configuração Externa

Parâmetros devem ficar fora do código sempre que possível.

---

# 9. Estratégia de Logging

Toda operação relevante deve ser registrada.

Eventos mínimos:

* início da execução;
* backup realizado;
* arquivo carregado;
* validações;
* normalizações;
* quantidade de registros;
* erros encontrados;
* finalização.

---

# 10. Estratégia de Tratamento de Exceções

Exceções devem ser específicas.

Evitar:

```
except:
    pass
```

Cada erro deve possuir contexto suficiente para facilitar diagnóstico.

---

# 11. Estratégia de Testes

O projeto utilizará testes automatizados para:

* serviços;
* validadores;
* normalizadores;
* regras de negócio;
* integração entre módulos.

O objetivo é garantir previsibilidade e facilitar futuras evoluções.

---

# 12. Evolução Planejada

Futuras versões poderão incluir:

* API REST;
* interface web;
* processamento paralelo;
* banco de dados;
* filas de mensagens;
* execução agendada;
* monitoramento em tempo real;
* containerização com Docker.
