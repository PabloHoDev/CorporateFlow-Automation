# DEVELOPMENT.md

# Guia de Desenvolvimento

## Objetivo

Este documento descreve as diretrizes para desenvolvimento do CorporateFlow Automation, garantindo consistência arquitetural, legibilidade e facilidade de manutenção.

---

# Estrutura Geral

Todo novo código deve respeitar a organização definida em `ARCHITECTURE.md`.

Cada módulo deve possuir uma única responsabilidade.

Sempre que possível, componentes devem ser desacoplados por meio de abstrações.

---

# Convenções de Código

## Idioma

* Código em inglês.
* Comentários apenas quando realmente necessários.
* Documentação em português.

---

## Nomenclatura

### Classes

Utilizar PascalCase.

Exemplo:

```text
ExcelService
ReportService
ConfigurationManager
```

### Funções e métodos

Utilizar snake_case.

Exemplo:

```text
load_configuration()
create_backup()
generate_report()
```

### Variáveis

Utilizar nomes descritivos.

Evitar abreviações.

---

# Organização das Responsabilidades

## main.py

Responsável apenas por iniciar a aplicação.

Não deve conter lógica de negócio.

---

## Orchestrator

Responsável por coordenar o pipeline.

Não deve implementar regras específicas.

---

## Services

Executam operações concretas.

Exemplo:

* leitura;
* escrita;
* backup;
* logs.

---

## Validators

Responsáveis exclusivamente por validação.

Não devem modificar dados.

---

## Normalizers

Responsáveis exclusivamente pela transformação e padronização.

---

## Models

Representam entidades do domínio.

---

# Logging

Todo evento relevante deve ser registrado.

Priorizar mensagens claras e objetivas.

---

# Tratamento de Exceções

Nunca utilizar:

```python
except:
    pass
```

As exceções devem ser específicas e fornecer contexto suficiente para diagnóstico.

---

# Testes

Toda funcionalidade nova deve possuir testes automatizados sempre que viável.

Preferencialmente:

* testes unitários;
* testes de integração;
* cenários de erro.

---

# Boas Práticas

* Evitar duplicação de código.
* Priorizar funções pequenas.
* Manter baixo acoplamento.
* Manter alta coesão.
* Favorecer composição em vez de lógica excessivamente centralizada.
* Documentar decisões arquiteturais relevantes por meio de ADRs.
