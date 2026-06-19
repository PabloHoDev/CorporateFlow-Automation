# ProcessingResult

* **Status:** 🟡 Em elaboração
* **Módulo:** `src/models/processing_result.py`
* **Categoria:** Model

---

# Objetivo

A classe `ProcessingResult` representa o resultado produzido pelo processamento de um único arquivo durante a execução da aplicação.

Ela consolida informações sobre sucesso, falha, duração, mensagens e demais dados relevantes gerados ao longo do processamento.

---

# Responsabilidade

O `ProcessingResult` é responsável exclusivamente por representar o resultado de uma operação de processamento associada a um `InputFile`.

Ele não executa processamento, validações ou geração de relatórios.

---

# Responsabilidades dentro do escopo

* Representar o resultado do processamento de um arquivo.
* Associar o resultado ao respectivo `InputFile`.
* Registrar o status final da operação.
* Armazenar mensagens informativas ou de erro.
* Registrar tempos de início e término do processamento.
* Disponibilizar informações para geração de relatórios e auditoria.

---

# Responsabilidades fora do escopo

O `ProcessingResult` **não deve**:

* Processar arquivos.
* Executar regras de negócio.
* Validar informações.
* Criar logs.
* Gerar relatórios.
* Persistir dados.
* Manipular arquivos físicos.

Essas responsabilidades pertencem aos componentes especializados da arquitetura.

---

# Atributos previstos

## Associação

| Atributo   | Tipo      | Descrição                                     |
| ---------- | --------- | --------------------------------------------- |
| input_file | InputFile | Arquivo ao qual este resultado está associado |

---

## Resultado da operação

| Atributo | Tipo             | Descrição                                           |
| -------- | ---------------- | --------------------------------------------------- |
| success  | bool             | Indica se o processamento foi concluído com sucesso |
| status   | str              | Estado final do processamento                       |
| message  | str | None       | Mensagem resumida sobre o resultado                 |
| error    | Exception | None | Exceção capturada, quando aplicável                 |

---

## Informações temporais

| Atributo    | Tipo      | Descrição                           |
| ----------- | --------- | ----------------------------------- |
| started_at  | datetime  | Momento de início do processamento  |
| finished_at | datetime  | Momento de término do processamento |
| duration    | timedelta | Tempo total gasto na operação       |

---

## Informações adicionais

| Atributo | Tipo           | Descrição                                           |
| -------- | -------------- | --------------------------------------------------- |
| metadata | dict[str, Any] | Dados auxiliares produzidos durante o processamento |

---

# Estados previstos (`status`)

O atributo `status` poderá assumir valores como:

* `SUCCESS`
* `FAILED`
* `SKIPPED`
* `PARTIAL_SUCCESS`

Novos estados poderão ser incorporados conforme evolução da aplicação.

---

# Métodos públicos previstos

Por se tratar de um modelo de domínio, recomenda-se limitar seus métodos a operações utilitárias.

## finish()

Marca o encerramento do processamento e calcula sua duração.

---

## to_dict()

Retorna uma representação serializável do resultado.

---

## **repr**()

Retorna uma representação resumida para fins de depuração.

---

# Dependências

O `ProcessingResult` poderá depender apenas de estruturas simples e modelos da aplicação, como:

* `InputFile`
* `datetime`
* `timedelta`
* `dict`
* `Exception`

Não deve depender de serviços ou componentes responsáveis pelo processamento.

---

# Classes consumidoras

O objeto poderá ser utilizado por:

* `ExecutionContext`
* `Report`
* `ReportService`
* `LogService`
* `Orchestrator`

---

# Fluxo simplificado

```text
InputFile

│

▼

Processamento

│

▼

ProcessingResult

│

▼

ExecutionContext

│

▼

Report

│

▼

ReportService
```

---

# Ciclo de vida

Um novo `ProcessingResult` deverá ser criado para cada `InputFile` processado.

Após concluído, o objeto será armazenado no `ExecutionContext` e posteriormente utilizado para composição do relatório consolidado da execução.

---

# Imutabilidade

Após o encerramento do processamento (`finish()`), recomenda-se que o objeto não sofra novas alterações, preservando a integridade das informações registradas.

Caso seja necessário adicionar dados complementares, recomenda-se utilizar o campo `metadata`.

---

# Princípios SOLID aplicados

## Single Responsibility Principle (SRP)

Possui apenas uma responsabilidade: representar o resultado do processamento de um único arquivo.

---

## Open/Closed Principle (OCP)

Novos atributos ou estados poderão ser adicionados sem modificar sua responsabilidade principal.

---

# Possíveis evoluções futuras

A estrutura permite incorporar facilmente:

* códigos padronizados de erro;
* níveis de severidade;
* métricas detalhadas de desempenho;
* identificadores de correlação;
* informações de auditoria;
* resultados parciais por etapa;
* indicadores de retry.

---

# Observações arquiteturais

O `ProcessingResult` é um objeto de domínio destinado exclusivamente à representação do resultado de processamento de um único arquivo.

Ele não deve conter lógica de negócio ou comportamento responsável pela execução do processamento.

Sua principal finalidade é fornecer uma estrutura consistente para armazenamento, rastreamento, auditoria e posterior consolidação das informações pelo `Report` e pelo `ReportService`.
