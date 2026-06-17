# PROJECT_STRUCTURE.md

# Estrutura Física do Projeto

## Objetivo

Definir a organização oficial do repositório do **CorporateFlow Automation**, estabelecendo responsabilidades claras para cada diretório e preparando o projeto para crescimento sustentável.

---

# Estrutura Final do Projeto - CorporateFlow Automation

```text
CorporateFlow/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── assets/
│   ├── diagrams/
│   ├── images/
│   └── gifs/
│
├── config/
│   ├── config.yaml
│   └── logging.yaml
│
├── data/
│   ├── input/
│   ├── output/
│   ├── backups/
│   └── logs/
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── ARCHITECTURAL_CONVENTIONS.md
│   ├── PROJECT_STRUCTURE.md
│   ├── CLASS_DESIGN.md
│   ├── UML.md
│   ├── INTERFACES.md
│   ├── PIPELINE.md
│   ├── TEST_STRATEGY.md
│   ├── DEVELOPMENT.md
│   ├── ROADMAP.md
│   ├── CONTRIBUTING.md
│   └── adr/
│       ├── ADR-001-arquitetura-orientada-a-servicos.md
│       ├── ADR-002-estrutura-de-diretorios.md
│       └── ADR-003-estrategia-de-testes.md
│
├── examples/
│   ├── sample.xlsx
│   ├── sample.csv
│   └── sample_config.yaml
│
├── scripts/
│   ├── create_demo_data.py
│   └── clean_output.py
│
├── src/
│   │
│   ├── core/
│   │   ├── orchestrator.py
│   │   ├── pipeline.py
│   │   └── execution_context.py
│   │
│   ├── config/
│   │   └── configuration_manager.py
│   │
│   ├── services/
│   │   ├── backup_service.py
│   │   ├── excel_service.py
│   │   ├── file_service.py
│   │   ├── log_service.py
│   │   └── report_service.py
│   │
│   ├── validators/
│   │   ├── schema_validator.py
│   │   └── business_validator.py
│   │
│   ├── normalizers/
│   │   ├── text_normalizer.py
│   │   └── city_normalizer.py
│   │
│   ├── models/
│   │   ├── input_file.py
│   │   ├── processing_result.py
│   │   └── report.py
│   │
│   ├── interfaces/
│   │   ├── service_protocol.py
│   │   ├── validator_protocol.py
│   │   └── normalizer_protocol.py
│   │
│   ├── exceptions/
│   │   ├── configuration_error.py
│   │   ├── business_rule_error.py
│   │   └── file_validation_error.py
│   │
│   ├── enums/
│   │   ├── execution_status.py
│   │   └── log_level.py
│   │
│   ├── constants/
│   │   ├── file_types.py
│   │   ├── messages.py
│   │   
│   │
│   └── utils/
│       ├── filesystem.py
│       ├── helpers.py
│       └── paths.py
│
├── tests/
│   │
│   ├── unit/
│   │   ├── core/
│   │   ├── services/
│   │   ├── validators/
│   │   ├── normalizers/
│   │   ├── models/
│   │   └── utils/
│   │
│   ├── integration/
│   │
│   └── fixtures/
│       ├── sample.xlsx
│       ├── sample.csv
│       ├── invalid.xlsx
│       └── config.yaml
│
├── .editorconfig
├── .gitignore
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── main.py
└── README.md
```


# Responsabilidades

## `.github/`

Armazena fluxos de integração contínua (CI), validações automáticas e futuras rotinas de deploy.

---

## `config/`

Contém apenas arquivos de configuração externos.

Nenhuma regra de negócio deve ser implementada nesse diretório.

---

## `docs/`

Centraliza toda a documentação funcional e técnica do projeto.

---

## `input/`

Ponto de entrada dos arquivos que serão processados.

---

## `output/`

Destino padrão dos arquivos produzidos pelo sistema.

---

## `backups/`

Armazena cópias de segurança criadas automaticamente antes de qualquer alteração.

---

## `logs/`

Contém os arquivos de auditoria gerados durante as execuções.

---

## `src/core/`

Implementa a coordenação do fluxo principal da aplicação.

Não deve conter regras específicas do domínio.

---

## `src/config/`

Responsável pelo carregamento e validação das configurações da aplicação.

---

## `src/services/`

Implementa operações técnicas reutilizáveis, como leitura de arquivos, backup e geração de relatórios.

---

## `src/validators/`

Executa verificações estruturais e de regras de negócio antes do processamento.

---

## `src/normalizers/`

Realiza padronizações necessárias para garantir consistência dos dados.

---

## `src/models/`

Representa objetos do domínio utilizados durante o processamento.

---

## `src/interfaces/`

Define contratos que permitem desacoplamento entre implementações concretas.

---

## `src/exceptions/`

Centraliza exceções personalizadas utilizadas pela aplicação.

---

## `src/utils/`

Disponibiliza funções auxiliares reutilizáveis, evitando duplicação de código.

---

## `tests/`

Agrupa testes unitários e de integração organizados conforme a estrutura do projeto.

---

# Regras Arquiteturais

* O `main.py` apenas inicia a aplicação.
* O `Orchestrator` coordena o fluxo, mas não implementa regras de negócio.
* Serviços não devem depender diretamente entre si quando isso puder ser evitado.
* Validadores não modificam dados.
* Normalizadores não validam regras.
* Models representam estado, não processamento complexo.
* Configurações devem permanecer externas ao código.
* Toda nova decisão arquitetural relevante deve ser registrada em um ADR.
