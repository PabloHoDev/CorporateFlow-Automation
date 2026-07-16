# Dashboard Operacional — CorporateFlow

## Objetivo

O Dashboard Operacional do CorporateFlow foi desenvolvido para fornecer visibilidade completa sobre a execução dos processos automatizados, permitindo acompanhamento operacional, auditoria e identificação rápida de anomalias.

O dashboard consome dados produzidos automaticamente pelos componentes de monitoramento e observabilidade do sistema.

---

## Objetivos do Dashboard

* Monitorar execuções do processo;
* Acompanhar indicadores operacionais;
* Identificar gargalos de desempenho;
* Detectar falhas rapidamente;
* Facilitar auditorias;
* Apoiar decisões operacionais.

---

## Arquitetura

```text
ExecutionMetrics
        ↓
MonitoringService
        ↓
MonitoringSnapshot
        ↓
Exports CSV
        ↓
Dashboard Power BI
```

Fluxo de alertas:

```text
HealthValidator
        ↓
AlertService
        ↓
alerts_history.csv
        ↓
Dashboard Power BI
```

---

## Estrutura da Pasta

```text
dashboard/

├── dashboard.pbix
├── README.md
└── exports/
    ├── executions_history.csv
    ├── monitoring_history.csv
    └── alerts_history.csv
```

---

## Fontes de Dados

### executions_history.csv

Contém informações sobre cada execução realizada pelo sistema.

Campos sugeridos:

| Campo                  | Descrição                          |
| ---------------------- | ---------------------------------- |
| timestamp              | Data e hora da execução            |
| execution_time_seconds | Tempo total da execução            |
| files_processed        | Quantidade de arquivos processados |
| records_read           | Registros lidos                    |
| records_created        | Registros inseridos                |
| records_updated        | Registros atualizados              |
| records_skipped        | Registros ignorados                |
| errors_count           | Quantidade de erros                |

---

### monitoring_history.csv

Contém métricas consolidadas para análise operacional.

Campos sugeridos:

| Campo                  | Descrição                         |
| ---------------------- | --------------------------------- |
| timestamp              | Momento da captura                |
| throughput             | Registros processados por segundo |
| success_rate           | Taxa de sucesso                   |
| average_execution_time | Tempo médio                       |
| total_executions       | Total de execuções                |

---

### alerts_history.csv

Contém todos os alertas gerados pelo sistema.

Campos sugeridos:

| Campo     | Descrição              |
| --------- | ---------------------- |
| timestamp | Data do alerta         |
| severity  | Severidade             |
| title     | Título do alerta       |
| message   | Mensagem               |
| source    | Componente responsável |

---

## Indicadores Recomendados

### Execução

* Última execução;
* Tempo médio de processamento;
* Quantidade de execuções;
* Taxa de sucesso;
* Throughput médio.

---

### Processamento

* Arquivos processados;
* Registros lidos;
* Registros inseridos;
* Registros atualizados;
* Registros ignorados.

---

### Alertas

* Alertas ativos;
* Alertas críticos;
* Alertas por severidade;
* Histórico de falhas.

---

### Tendência

* Evolução do volume processado;
* Evolução dos erros;
* Evolução do throughput;
* Evolução do tempo médio de execução.

---

## Atualização dos Dados

Os arquivos localizados em `dashboard/exports/` são atualizados automaticamente ao final de cada execução do CorporateFlow.

Não é necessária intervenção manual para atualização dos indicadores.

---

## Tecnologias Utilizadas

* Power BI;
* CSV;
* Python;
* Pandas;
* CorporateFlow Monitoring Service;
* CorporateFlow Alert Service.

---

## Evoluções Futuras

As próximas versões poderão incluir:

* integração com banco de dados;
* atualização em tempo real;
* API REST;
* notificações automáticas;
* integração com Microsoft Teams;
* integração com Slack;
* dashboard web;
* monitoramento distribuído.

---

## Responsabilidade Arquitetural

O Dashboard possui responsabilidade exclusivamente de visualização e análise.

Nenhuma regra de negócio ou processamento operacional deve ser implementado nesta camada.

Toda lógica deve permanecer encapsulada nos componentes do domínio e serviços do CorporateFlow.
