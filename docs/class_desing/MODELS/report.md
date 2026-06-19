# Report

* **Status:** 🟡 Em elaboração
* **Módulo:** `src/models/report.py`
* **Categoria:** Model

---

# Objetivo

A classe `Report` representa o relatório consolidado de uma execução completa da aplicação.

Ela reúne estatísticas, indicadores e a coleção de resultados individuais (`ProcessingResult`), servindo como fonte oficial para auditoria, monitoramento e geração de relatórios finais.

---

# Responsabilidade

O `Report` é responsável exclusivamente por representar o resumo de uma execução da aplicação.

Ele não executa processamento, cálculos complexos ou persistência de dados.

---

# Responsabilidades dentro do escopo

* Consolidar os resultados produzidos durante a execução.
* Armazenar estatísticas gerais do processamento.
* Manter informações temporais da execução.
* Disponibilizar os resultados individuais para consulta.
* Servir como base para geração de relatórios finais.

---

# Responsabilidades fora do escopo

O `Report` **não deve**:

* Processar arquivos.
* Executar regras de negócio.
* Gerar arquivos de relatório.
* Persistir informações.
* Criar logs.
* Manipular planilhas.
* Realizar validações.

Essas responsabilidades pertencem aos componentes especializados.

---

# Atributos previstos

## Identificação da execução

| Atributo     | Tipo      | Descrição                       |
| ------------ | --------- | ------------------------------- |
| execution_id | str       | Identificador único da execução |
| started_at   | datetime  | Momento de início da execução   |
| finished_at  | datetime  | Momento de término da execução  |
| duration     | timedelta | Tempo total da execução         |

---

## Estatísticas gerais

| Atributo        | Tipo | Descrição                                      |
| --------------- | ---- | ---------------------------------------------- |
| total_files     | int  | Quantidade total de arquivos identificados     |
| processed_files | int  | Quantidade de arquivos processados com sucesso |
| failed_files    | int  | Quantidade de arquivos com falha               |
| skipped_files   | int  | Quantidade de arquivos ignorados               |

---

## Resultados detalhados

| Atributo           | Tipo                   | Descrição                                    |
| ------------------ | ---------------------- | -------------------------------------------- |
| processing_results | list[ProcessingResult] | Lista consolidada dos resultados individuais |

---

## Informações adicionais

| Atributo | Tipo           | Descrição                              |
| -------- | -------------- | -------------------------------------- |
| metadata | dict[str, Any] | Informações complementares da execução |

---

# Métodos públicos previstos

Por ser um modelo de domínio, recomenda-se limitar seus métodos a operações auxiliares.

## add_result()

Adiciona um novo `ProcessingResult` ao relatório.

---

## calculate_statistics()

Atualiza os indicadores consolidados com base nos resultados registrados.

---

## finish()

Marca o encerramento da execução e calcula sua duração.

---

## to_dict()

Retorna uma representação serializável do relatório.

---

## **repr**()

Retorna uma representação resumida para fins de depuração.

---

# Dependências

O `Report` poderá depender apenas de:

* `ProcessingResult`
* `datetime`
* `timedelta`
* `dict`
* `list`

Não deve depender de serviços responsáveis pela geração ou persistência do relatório.

---

# Classes consumidoras

O objeto poderá ser utilizado por:

* `ExecutionContext`
* `ReportService`
* `Orchestrator`
* `LogService`

Outros consumidores poderão ser adicionados conforme evolução da arquitetura.

---

# Fluxo simplificado

```text
ProcessingResult

│

├── Resultado 1

├── Resultado 2

├── Resultado 3

├── ...

│

▼

Report

│

▼

ReportService

│

▼

Saída final (console, arquivo, API ou outro destino)
```

---

# Ciclo de vida

O `Report` deverá ser criado durante a execução da aplicação e alimentado progressivamente com objetos `ProcessingResult`.

Após o encerramento do processamento, ele representará o estado final consolidado da execução e poderá ser utilizado para exportação ou auditoria.

---

# Imutabilidade

Após a conclusão da execução (`finish()`), recomenda-se que o relatório não seja mais modificado.

Caso informações adicionais sejam necessárias, recomenda-se registrá-las no campo `metadata`.

---

# Princípios SOLID aplicados

## Single Responsibility Principle (SRP)

Possui apenas uma responsabilidade: representar o relatório consolidado de uma execução.

---

## Open/Closed Principle (OCP)

Novos indicadores estatísticos ou atributos poderão ser adicionados sem alterar sua responsabilidade principal.

---

# Possíveis evoluções futuras

A estrutura permite incorporar facilmente:

* métricas de desempenho detalhadas;
* estatísticas por etapa do processamento;
* agrupamentos por categoria;
* indicadores de qualidade;
* gráficos e dashboards;
* exportação para múltiplos formatos;
* integração com ferramentas de observabilidade.

---

# Observações arquiteturais

O `Report` é um objeto de domínio responsável apenas pela representação dos dados consolidados da execução.

A geração efetiva de arquivos, exibição em tela ou envio para sistemas externos deve ser responsabilidade do `ReportService`.

Essa separação mantém a arquitetura desacoplada, facilita testes automatizados e preserva a responsabilidade única de cada componente.
