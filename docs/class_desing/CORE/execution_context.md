# ExecutionContext

* **Status:** 🟡 Em elaboração
* **Módulo:** `src/core/execution_context.py`
* **Categoria:** Core

---

# Objetivo

A classe `ExecutionContext` é responsável por centralizar e compartilhar o estado da execução da aplicação durante todo o ciclo de processamento.

Ela atua como um objeto de contexto único, disponibilizando informações necessárias para os diversos componentes do sistema sem a necessidade de propagação excessiva de parâmetros entre métodos.

---

# Responsabilidade

A `ExecutionContext` deve armazenar informações relacionadas exclusivamente à execução corrente da aplicação.

Seu objetivo é fornecer um ponto centralizado de acesso aos recursos compartilhados utilizados pelo `Orchestrator` e pelos demais componentes.

---

# Responsabilidades dentro do escopo

* Armazenar configurações carregadas.
* Disponibilizar o logger da execução.
* Armazenar informações sobre arquivos de entrada.
* Disponibilizar caminhos utilizados durante a execução.
* Registrar resultados intermediários.
* Armazenar estatísticas da execução.
* Registrar horário de início e término do processamento.
* Compartilhar objetos necessários entre componentes.

---

# Responsabilidades fora do escopo

A classe **não deve**:

* Executar regras de negócio.
* Processar arquivos.
* Validar informações.
* Normalizar dados.
* Gerar relatórios.
* Criar backups.
* Controlar fluxo de execução.

Ela deve atuar apenas como um contêiner de estado.

---

# Atributos previstos

| Atributo           | Tipo                   | Descrição                                 |
| ------------------ | ---------------------- | ----------------------------------------- |
| configuration      | ConfigurationManager   | Configuração carregada da aplicação       |
| logger             | LogService             | Instância utilizada para registro de logs |
| input_files        | list[InputFile]        | Arquivos identificados para processamento |
| processing_results | list[ProcessingResult] | Resultados produzidos durante a execução  |
| report             | Report | None          | Relatório consolidado da execução         |
| execution_id       | str                    | Identificador único da execução           |
| started_at         | datetime               | Momento de início                         |
| finished_at        | datetime | None        | Momento de término                        |
| metadata           | dict[str, Any]         | Informações adicionais compartilhadas     |

---

# Métodos públicos previstos

## initialize()

Inicializa estruturas necessárias para uma nova execução.

---

## finish()

Marca oficialmente o encerramento da execução.

---

## add_input_file()

Adiciona um novo arquivo ao contexto.

---

## add_processing_result()

Registra um resultado produzido durante o processamento.

---

## set_report()

Associa o relatório final da execução.

---

## set_metadata()

Armazena informações auxiliares utilizando chave e valor.

---

## get_metadata()

Obtém um valor previamente armazenado na coleção de metadados.

---

# Dependências

A classe poderá manter referências para:

* ConfigurationManager
* LogService
* InputFile
* ProcessingResult
* Report

Entretanto, ela não deve depender da implementação interna dessas classes.

---

# Classes consumidoras

Espera-se que os seguintes componentes utilizem o `ExecutionContext`:

* Orchestrator
* BackupService
* ExcelService
* FileService
* ReportService
* SchemaValidator
* BusinessValidator
* TextNormalizer
* CityNormalizer

---

# Fluxo simplificado de utilização

```text
main.py

↓

ExecutionContext

↓

Orchestrator

↓

Services

↓

Validators

↓

Normalizers

↓

ReportService
```

O mesmo objeto de contexto acompanha toda a execução da aplicação.

---

# Princípios SOLID aplicados

## Single Responsibility Principle (SRP)

A classe possui apenas uma responsabilidade: representar o contexto da execução.

---

## Open/Closed Principle (OCP)

Novos atributos podem ser adicionados sem alterar o comportamento dos consumidores existentes.

---

## Dependency Inversion Principle (DIP)

Os consumidores dependem do contexto compartilhado, reduzindo a necessidade de múltiplos parâmetros e minimizando acoplamentos diretos.

---

# Possíveis evoluções futuras

A estrutura permite incorporar facilmente:

* métricas de desempenho;
* monitoramento em tempo real;
* rastreamento distribuído (*distributed tracing*);
* informações de usuário executor;
* contexto de autenticação;
* estatísticas avançadas;
* identificadores de correlação (*correlation IDs*).

---

# Observações arquiteturais

A utilização de um `ExecutionContext` reduz significativamente a quantidade de parâmetros trafegando entre componentes e facilita a evolução da arquitetura.

Por representar apenas o estado compartilhado da execução, esta classe não deve conter qualquer regra de negócio ou lógica operacional.

Sua implementação deverá permanecer simples, previsível e facilmente serializável sempre que possível.
