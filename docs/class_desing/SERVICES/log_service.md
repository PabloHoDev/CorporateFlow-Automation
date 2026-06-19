# LogService

* **Status:** 🟡 Em elaboração
* **Módulo:** `src/services/log_service.py`
* **Categoria:** Service

---

# Objetivo

A classe `LogService` é responsável por centralizar, padronizar e gerenciar todos os registros de logs gerados pela aplicação durante sua execução.

Seu objetivo é garantir rastreabilidade, observabilidade e suporte à depuração do sistema.

---

# Responsabilidade

O `LogService` deve ser o único ponto responsável por gerar logs estruturados da aplicação.

Ele não deve conter regras de negócio nem influenciar o fluxo de execução.

---

# Responsabilidades dentro do escopo

* Registrar eventos da aplicação.
* Registrar erros e exceções.
* Registrar informações de debug.
* Registrar eventos de execução do pipeline.
* Padronizar formato de logs.
* Gerenciar níveis de log (INFO, WARNING, ERROR, DEBUG).
* Escrever logs em console e/ou arquivos.
* Integrar com diretório de logs definido no `AppConfig`.

---

# Responsabilidades fora do escopo

A classe **não deve**:

* Tomar decisões de fluxo.
* Executar regras de negócio.
* Processar arquivos.
* Validar dados.
* Normalizar informações.
* Manipular Excel ou sistema de arquivos diretamente.
* Substituir exceções da aplicação.

---

# Métodos públicos previstos

## info()

Registra um log informativo sobre o andamento da aplicação.

---

## warning()

Registra um aviso sobre comportamento não crítico.

---

## error()

Registra erros ocorridos durante a execução.

---

## debug()

Registra informações detalhadas para diagnóstico técnico.

---

## critical()

Registra falhas críticas que podem interromper a execução.

---

## set_execution_context()

Associa o logger ao `ExecutionContext`, permitindo rastreamento da execução atual.

---

## log_event()

Registra eventos estruturados da aplicação (ex: início de processamento, finalização de etapas).

---

# Dependências

O `LogService` poderá depender de:

* `AppConfig`
* `ExecutionContext`
* `datetime`
* `logging` (biblioteca padrão do Python)
* `pathlib.Path`

Não deve depender de regras de negócio ou serviços de domínio.

---

# Classes consumidoras

Espera-se que os seguintes componentes utilizem o `LogService`:

* `Orchestrator`
* `ExecutionContext`
* `FileService`
* `ExcelService`
* `BackupService`
* `ReportService`
* Validators e Normalizers (em casos específicos)

---

# Fluxo simplificado

```text id="wq9x2a"
Qualquer componente

│

▼

LogService

│

├── console

├── arquivo

└── contexto de execução

▼

Logs estruturados
```

---

# Ciclo de vida

O `LogService` deve ser instanciado no `main.py` (Composition Root) e injetado nos demais componentes da aplicação.

Ele pode permanecer ativo durante toda a execução da aplicação.

---

# Estrutura sugerida de log

Os logs devem seguir um padrão estruturado, por exemplo:

```text id="q8k2lm"
[timestamp] [level] [execution_id] message
```

Exemplo:

```text id="p4l9sn"
2026-06-19 15:42:10 | INFO | 8f3a-... | Processing started
```

---

# Princípios SOLID aplicados

## Single Responsibility Principle (SRP)

Responsável apenas por logging estruturado da aplicação.

---

## Dependency Inversion Principle (DIP)

Consumidores dependem da abstração do serviço de logging, não de implementações concretas.

---

## Open/Closed Principle (OCP)

Novos destinos de log (ex: arquivos, APIs, observabilidade externa) podem ser adicionados sem alterar consumidores.

---

# Possíveis evoluções futuras

A estrutura permite incorporar facilmente:

* integração com sistemas como ELK Stack;
* envio de logs para APIs externas;
* logging assíncrono;
* correlação distribuída de logs;
* exportação estruturada em JSON;
* dashboards de observabilidade;
* alertas automáticos baseados em eventos críticos.

---

# Observações arquiteturais

O `LogService` é um componente transversal da arquitetura, responsável por garantir visibilidade e rastreabilidade da aplicação.

Ele não deve influenciar decisões de negócio nem interferir no fluxo de execução.

Seu papel é exclusivamente registrar eventos de forma estruturada, consistente e rastreável ao longo de toda a execução.
