# TEST STRATEGY

## Objetivo

Definir a estratégia oficial de testes do projeto CorporateFlow, estabelecendo padrões, responsabilidades, níveis de cobertura e critérios de qualidade para todas as camadas da aplicação.

O objetivo é garantir:

* previsibilidade do comportamento do sistema;
* redução de regressões;
* facilidade de manutenção;
* segurança para futuras evoluções;
* confiabilidade operacional.

---

# Princípios da Estratégia de Testes

A estratégia de testes do projeto será baseada nos seguintes princípios:

* testes rápidos;
* testes determinísticos;
* isolamento entre componentes;
* baixo acoplamento com infraestrutura externa;
* alta cobertura das regras de negócio;
* facilidade de manutenção dos testes.

---

# Pirâmide de Testes

O projeto seguirá a estratégia clássica da Pirâmide de Testes.

```text
                End-to-End
                     ▲
                     │
            Integration Tests
                     ▲
                     │
               Unit Tests
```

Distribuição esperada:

| Tipo              | Percentual aproximado |
| ----------------- | --------------------- |
| Unit Tests        | 70%                   |
| Integration Tests | 25%                   |
| End-to-End Tests  | 5%                    |

---

# Testes Unitários

## Objetivo

Validar o comportamento de uma única unidade da aplicação de forma isolada.

## Características

* execução rápida;
* sem acesso ao sistema de arquivos;
* sem dependência de planilhas reais;
* sem dependência de APIs externas;
* uso de mocks sempre que necessário.

## Exemplos

* validação de regras do `BusinessValidator`;
* normalização de texto;
* normalização de cidades;
* comportamento dos modelos;
* tratamento de exceções.

---

# Testes de Integração

## Objetivo

Garantir que múltiplos componentes funcionem corretamente em conjunto.

## Exemplos

* `FileService` + `SchemaValidator`;
* `ExcelService` + `ProcessingResult`;
* `Orchestrator` + `ExecutionContext`;
* geração de relatórios.

---

# Testes End-to-End

## Objetivo

Validar o fluxo completo da aplicação utilizando arquivos reais de entrada e saída.

## Cenários previstos

* execução totalmente bem-sucedida;
* arquivo inválido;
* erro de configuração;
* erro de regra de negócio;
* múltiplos arquivos simultâneos.

---

# Cobertura Mínima Esperada

| Camada      | Cobertura mínima |
| ----------- | ---------------- |
| Core        | 95%              |
| Services    | 90%              |
| Validators  | 95%              |
| Normalizers | 95%              |
| Models      | 80%              |
| Global      | 90%              |

---

# Estratégia de Mocks

## Devem ser mockados

* sistema de arquivos;
* leitura e escrita de Excel;
* timestamps;
* geração de logs;
* configurações externas.

## Não devem ser mockados

* regras de negócio;
* validadores;
* normalizadores;
* modelos de domínio.

---

# Estratégia de Fixtures

As fixtures deverão representar cenários reais do ambiente produtivo.

Exemplos:

* arquivos válidos;
* arquivos inválidos;
* arquivos vazios;
* arquivos com estrutura incompleta;
* arquivos com regras de negócio inválidas.

---

# Critérios para aprovação de Pull Requests

Um Pull Request somente poderá ser aprovado quando:

* todos os testes passarem;
* cobertura mínima for mantida;
* não houver regressões identificadas;
* análise estática não identificar problemas críticos.

---

# Ferramentas previstas

| Ferramenta    | Finalidade                    |
| ------------- | ----------------------------- |
| pytest        | Framework principal de testes |
| pytest-cov    | Cobertura                     |
| unittest.mock | Mocking                       |
| pytest-mock   | Auxílio para mocks            |
| faker         | Geração de dados              |
| coverage.py   | Métricas de cobertura         |

---

# Objetivo de Qualidade

O projeto busca atingir um nível de qualidade compatível com aplicações corporativas, permitindo evolução contínua com baixo risco operacional e alta confiabilidade.
