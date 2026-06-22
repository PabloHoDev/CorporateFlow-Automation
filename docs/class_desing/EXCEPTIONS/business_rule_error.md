# BusinessRuleError

- **Status:** 🟡 Em elaboração
- **Módulo:** `src/exceptions/business_rule_error.py`
- **Categoria:** Exception

---

# Objetivo

A exceção `BusinessRuleError` representa violações de regras de negócio identificadas durante o processamento da aplicação.

Seu objetivo é impedir que dados estruturalmente válidos, porém incompatíveis com as regras do domínio, avancem para etapas posteriores do processamento.

---

# Responsabilidade

A `BusinessRuleError` deve ser utilizada exclusivamente para representar falhas relacionadas às regras de negócio da aplicação.

Ela não deve ser utilizada para problemas estruturais dos arquivos nem para erros de configuração do sistema.

---

# Cenários de utilização

A exceção poderá ser utilizada em situações como:

- Status inválido.
- Transição de status não permitida.
- SLA violado.
- Incompatibilidade entre campos relacionados.
- Obrigação incompatível com a UF.
- Regra operacional descumprida.
- Violação de restrições corporativas.
- Dados inconsistentes com o domínio da aplicação.

---

# Exemplos

## Status inválido

```python
raise BusinessRuleError(
    "O status informado não é permitido."
)
```

---

## SLA vencido

```python
raise BusinessRuleError(
    "O prazo definido para a operação foi ultrapassado."
)
```

---

## Incompatibilidade entre campos

```python
raise BusinessRuleError(
    "A obrigação informada não é compatível com a UF selecionada."
)
```

---

## Regra corporativa violada

```python
raise BusinessRuleError(
    "O registro não atende aos critérios operacionais definidos."
)
```

---

# Classes que podem lançar esta exceção

Espera-se que esta exceção seja utilizada por:

- BusinessValidator
- Orchestrator (quando necessário)

Outros componentes poderão utilizá-la caso implementem regras de domínio específicas.

---

# Fluxo simplificado

```text
Dados Estruturalmente Válidos

│

▼

BusinessValidator

│

├── regra atendida
│       │
│       ▼
│   continua processamento
│
└── regra violada
        │
        ▼

BusinessRuleError
```

---

# Hierarquia sugerida

```text
Exception

└── BusinessRuleError
```

---

# Tratamento esperado

A aplicação deve considerar esta exceção como uma falha de negócio.

Fluxo esperado:

```text
BusinessRuleError

↓

Registrar log

↓

Registrar ProcessingResult

↓

Continuar ou interromper execução
(conforme estratégia definida)
```

A decisão sobre continuar ou interromper o fluxo pertence ao `Orchestrator`.

---

# Dependências

A exceção não deve depender de serviços, modelos ou componentes da aplicação.

Sua implementação deve permanecer simples, desacoplada e reutilizável.

---

# Princípios aplicados

## Single Responsibility Principle (SRP)

Representa exclusivamente violações de regras de negócio.

---

## Separation of Concerns

Separa claramente problemas de domínio de:

- problemas estruturais dos arquivos;
- problemas de configuração;
- falhas técnicas da infraestrutura.

---

# Possíveis evoluções futuras

A estrutura permite incorporar facilmente:

- códigos padronizados de regra;
- categorias de erro de negócio;
- contexto detalhado da violação;
- múltiplas violações em uma única exceção;
- internacionalização de mensagens;
- integração com motores de regras.

---

# Observações arquiteturais

A `BusinessRuleError` representa a principal exceção da camada de validação de negócio.

Ela deve ser utilizada sempre que os dados forem estruturalmente válidos, mas incompatíveis com as regras e restrições do domínio da aplicação.

Seu uso permite separar claramente falhas de negócio de problemas estruturais ou técnicos, tornando a arquitetura mais previsível, testável e fácil de manter.

Ela é a exceção naturalmente associada ao `BusinessValidator` dentro da arquitetura do sistema.