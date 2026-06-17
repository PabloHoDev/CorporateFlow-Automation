# Class Design

## Objetivo

Esta pasta contém a documentação de modelagem de todas as classes do projeto **CorporateFlow Automation**.

Cada documento descreve uma única classe, detalhando sua responsabilidade, atributos, métodos públicos, dependências, relacionamentos e justificativa arquitetural.

O objetivo é definir completamente a estrutura da aplicação antes da implementação, garantindo consistência, manutenibilidade e alinhamento com os princípios arquiteturais adotados pelo projeto.

---

# Organização

A documentação está dividida por responsabilidade funcional.

## Core

Componentes responsáveis por coordenar o fluxo principal da aplicação.

| Classe           | Documento              |
| ---------------- | ---------------------- |
| ExecutionContext | `execution_context.md` |
| Orchestrator     | `orchestrator.md`      |

---

## Configuration

Componentes responsáveis pelo gerenciamento das configurações do sistema.

| Classe               | Documento                  |
| -------------------- | -------------------------- |
| ConfigurationManager | `configuration_manager.md` |

---

## Services

Serviços reutilizáveis utilizados durante o processamento.

| Classe        | Documento           |
| ------------- | ------------------- |
| BackupService | `backup_service.md` |
| ExcelService  | `excel_service.md`  |
| FileService   | `file_service.md`   |
| LogService    | `log_service.md`    |
| ReportService | `report_service.md` |

---

## Validators

Componentes responsáveis pela validação estrutural e pelas regras de negócio.

| Classe            | Documento               |
| ----------------- | ----------------------- |
| SchemaValidator   | `schema_validator.md`   |
| BusinessValidator | `business_validator.md` |

---

## Normalizers

Componentes responsáveis pela padronização dos dados antes do processamento.

| Classe         | Documento            |
| -------------- | -------------------- |
| TextNormalizer | `text_normalizer.md` |
| CityNormalizer | `city_normalizer.md` |

---

## Models

Objetos que representam entidades do domínio da aplicação.

| Classe           | Documento              |
| ---------------- | ---------------------- |
| InputFile        | `input_file.md`        |
| ProcessingResult | `processing_result.md` |
| Report           | `report.md`            |

---

## Exceptions

Exceções customizadas utilizadas pelo sistema.

| Classe              | Documento                  |
| ------------------- | -------------------------- |
| ConfigurationError  | `configuration_error.md`   |
| FileValidationError | `file_validation_error.md` |
| BusinessRuleError   | `business_rule_error.md`   |

---

# Estrutura Padrão de Cada Documento

Cada especificação de classe segue o mesmo modelo para manter consistência durante o desenvolvimento.

* Objetivo
* Responsabilidade
* Responsabilidades fora do escopo
* Atributos
* Métodos públicos
* Dependências
* Classes consumidoras
* Fluxo de utilização
* Princípios SOLID aplicados
* Possíveis evoluções futuras
* Observações arquiteturais

---

# Convenções

* Cada arquivo documenta apenas uma única classe.
* A implementação deve seguir fielmente a especificação definida neste diretório.
* Alterações estruturais relevantes devem ser refletidas nesta documentação antes da implementação do código.
* Sempre que uma mudança impactar decisões arquiteturais do projeto, um novo ADR deverá ser criado na pasta `docs/adr/`.

---

# Status Atual

A documentação será construída incrementalmente, iniciando pelos componentes centrais (`Core`) e avançando para os demais módulos até cobrir toda a arquitetura do sistema.
