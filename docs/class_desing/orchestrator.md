# Orchestrator

* **Status:** 🟡 Em elaboração
* **Módulo:** `src/core/orchestrator.py`
* **Categoria:** Core

---

# Objetivo

A classe `Orchestrator` é responsável por coordenar todo o fluxo de execução da aplicação.

Ela atua como ponto central de controle, definindo a sequência de chamadas entre os diferentes componentes do sistema e garantindo que cada etapa seja executada na ordem correta.

---

# Responsabilidade

O `Orchestrator` deve controlar o ciclo de vida completo de uma execução, utilizando o `ExecutionContext` para compartilhar informações entre os componentes.

Sua função é exclusivamente de coordenação.

---

# Responsabilidades dentro do escopo

* Inicializar o fluxo de processamento.
* Coordenar a criação e utilização do `ExecutionContext`.
* Invocar os serviços na ordem correta.
* Controlar a sequência das etapas do processamento.
* Encerrar corretamente a execução.
* Garantir que erros sejam registrados antes da finalização.
* Solicitar a geração do relatório final.

---

# Responsabilidades fora do escopo

O `Orchestrator` **não deve**:

* Implementar regras de negócio.
* Ler arquivos diretamente.
* Manipular planilhas.
* Executar validações.
* Normalizar dados.
* Criar backups diretamente.
* Gerar relatórios.
* Escrever logs manualmente quando houver um serviço dedicado.

Toda lógica específica deve ser delegada ao componente responsável.

---

# Atributos previstos

| Atributo | Tipo             | Descrição                          |
| -------- | ---------------- | ---------------------------------- |
| context  | ExecutionContext | Contexto compartilhado da execução |

---

# Métodos públicos previstos

## run()

Inicia e coordena todo o fluxo principal da aplicação.

É o principal ponto de entrada da classe.

---

## initialize()

Prepara o ambiente necessário antes do início do processamento.

---

## finalize()

Executa as operações de encerramento da execução.

---

## handle_exception()

Centraliza o tratamento de exceções inesperadas durante o fluxo.

---

# Fluxo esperado

```text
run()

│

├── initialize()

│

├── BackupService

│

├── FileService

│

├── ExcelService

│

├── SchemaValidator

│

├── BusinessValidator

│

├── TextNormalizer

│

├── CityNormalizer

│

├── ReportService

│

└── finalize()
```

---

# Dependências

O `Orchestrator` poderá utilizar:

* ExecutionContext
* BackupService
* FileService
* ExcelService
* LogService
* ReportService
* SchemaValidator
* BusinessValidator
* TextNormalizer
* CityNormalizer

As dependências deverão ser recebidas por injeção de dependência sempre que possível.

---

# Classes consumidoras

Espera-se que apenas:

* `main.py`

instancie diretamente o `Orchestrator`.

As demais classes não devem depender dele.

---

# Fluxo simplificado de utilização

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

ExcelService

↓

SchemaValidator

↓

BusinessValidator

↓

TextNormalizer

↓

CityNormalizer

↓

ReportService
```

---

# Princípios SOLID aplicados

## Single Responsibility Principle (SRP)

O `Orchestrator` possui apenas uma responsabilidade: coordenar a execução da aplicação.

---

## Open/Closed Principle (OCP)

Novas etapas podem ser incorporadas ao fluxo sem alterar o comportamento das etapas já existentes.

---

## Dependency Inversion Principle (DIP)

Sempre que possível, o `Orchestrator` deve depender de abstrações (protocolos/interfaces) em vez de implementações concretas.

---

# Possíveis evoluções futuras

A arquitetura permite adicionar facilmente:

* execução paralela de etapas independentes;
* monitoramento de progresso;
* cancelamento controlado da execução;
* retomada após falhas;
* execução distribuída;
* integração com filas de processamento.

---

# Observações arquiteturais

O `Orchestrator` representa o ponto central de coordenação do sistema.

Ele não deve acumular responsabilidades técnicas ou regras de negócio, atuando apenas como controlador do fluxo de execução.

Toda operação especializada deve ser delegada aos respectivos serviços, validadores ou normalizadores, preservando baixo acoplamento e alta coesão entre os componentes da aplicação.
