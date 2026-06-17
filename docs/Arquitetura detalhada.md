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
│   │   └── paths.py
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
