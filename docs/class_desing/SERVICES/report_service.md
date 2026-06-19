# ReportService

* **Status:** 🟡 Em elaboração
* **Módulo:** `src/services/report_service.py`
* **Categoria:** Service

---

# Objetivo

A classe `ReportService` é responsável por transformar o objeto `Report` em saídas utilizáveis, como arquivos, logs estruturados ou exportações externas.

Seu objetivo é fornecer mecanismos padronizados para persistir, exportar ou apresentar o resultado consolidado da execução da aplicação.

---

# Responsabilidade

O `ReportService` deve lidar exclusivamente com a saída e persistência do relatório final.

Ele não deve calcular métricas, interpretar resultados ou aplicar regras de negócio.

---

# Responsabilidades dentro do escopo

* Exportar o `Report` para arquivos (ex: JSON, TXT, Excel).
* Gerar representações estruturadas do relatório.
* Persistir o relatório em diretórios configurados.
* Formatá-lo para consumo externo.
* Integrar com sistema de logs quando necessário.
* Garantir versionamento ou nomeação consistente de arquivos de saída.

---

# Responsabilidades fora do escopo

A classe **não deve**:

* Criar regras de consolidação de dados.
* Processar arquivos de entrada.
* Executar validações de negócio.
* Determinar quais dados entram no relatório.
* Manipular `InputFile` ou `ProcessingResult`.
* Executar lógica de pipeline.

Essas responsabilidades pertencem ao `Orchestrator` e ao modelo `Report`.

---

# Métodos públicos previstos

## export_to_json()

Exporta o relatório para formato JSON.

---

## export_to_excel()

Exporta o relatório para um arquivo Excel estruturado.

---

## export_to_text()

Gera uma versão textual do relatório para logs ou auditoria.

---

## save()

Salva o relatório em um diretório configurado na aplicação.

---

## build_filename()

Gera um nome padronizado para o arquivo de saída do relatório.

---

## format_report()

Converte o objeto `Report` em uma estrutura serializável ou formatada.

---

# Dependências

O `ReportService` poderá depender de:

* `AppConfig`
* `Report`
* `pathlib.Path`
* `json`
* `datetime`
* `pandas` (opcional, para exportação Excel)

Não deve depender de regras de negócio ou componentes de validação.

---

# Classes consumidoras

Espera-se que os seguintes componentes utilizem o `ReportService`:

* `Orchestrator`
* `ExecutionContext`
* `LogService`

---

# Fluxo simplificado

```text id="b3x8qp"
ExecutionContext
        │
        ▼
      Report
        │
        ▼
  ReportService
        │
 ┌──────┼────────┐
 ▼      ▼        ▼
JSON   Excel    TXT
arquivo logs   exportações
```

---

# Ciclo de vida

O `ReportService` é instanciado no `main.py` (Composition Root) e injetado no `Orchestrator`.

Ele é utilizado geralmente ao final da execução, quando o `Report` já está consolidado.

---

# Tratamento de erros

Erros de exportação ou persistência devem ser tratados com exceções apropriadas da aplicação.

O serviço não deve falhar silenciosamente nem substituir o `Report`.

---

# Princípios SOLID aplicados

## Single Responsibility Principle (SRP)

Responsável apenas por exportar e persistir relatórios.

---

## Dependency Inversion Principle (DIP)

Depende do modelo `Report`, não da lógica de geração de dados.

---

## Open/Closed Principle (OCP)

Novos formatos de exportação podem ser adicionados sem alterar a responsabilidade central do serviço.

---

# Possíveis evoluções futuras

A estrutura permite incorporar facilmente:

* exportação para PDF;
* integração com APIs externas;
* envio automático de relatórios por e-mail;
* upload para cloud storage (S3, Azure, GCP);
* dashboards analíticos;
* templates customizáveis de relatórios;
* compressão e versionamento de outputs.

---

# Observações arquiteturais

O `ReportService` atua como camada de saída da aplicação, responsável por materializar o resultado final do processamento.

Ele não deve participar da construção do relatório nem interferir no fluxo de dados.

Essa separação garante clareza arquitetural entre:

* **Modelagem de dados (`Report`)**
* **Processamento (`Orchestrator`)**
* **Saída e persistência (`ReportService`)**
