# SchemaValidator

* **Status:** 🟡 Em elaboração
* **Módulo:** `src/validators/schema_validator.py`
* **Categoria:** Validator

---

# Objetivo

A classe `SchemaValidator` é responsável por validar a estrutura dos dados recebidos pela aplicação antes que qualquer processamento seja iniciado.

Seu objetivo é garantir que os arquivos e informações possuam o formato mínimo esperado para que as demais etapas possam ser executadas com segurança.

---

# Responsabilidade

O `SchemaValidator` deve validar exclusivamente aspectos estruturais dos dados.

Ele não deve validar regras de negócio ou tomar decisões relacionadas ao domínio da aplicação.

---

# Responsabilidades dentro do escopo

* Verificar existência de colunas obrigatórias.
* Validar estrutura de planilhas.
* Verificar existência de abas obrigatórias.
* Validar tipos de dados esperados.
* Validar presença de campos obrigatórios.
* Detectar inconsistências estruturais.
* Garantir compatibilidade mínima para processamento.

---

# Responsabilidades fora do escopo

A classe **não deve**:

* Aplicar regras de negócio.
* Corrigir dados inválidos.
* Normalizar informações.
* Atualizar planilhas.
* Processar arquivos.
* Gerar relatórios.
* Tomar decisões de fluxo.

Essas responsabilidades pertencem a outros componentes da arquitetura.

---

# Cenários de validação previstos

## Estrutura de planilha

Exemplos:

* aba obrigatória inexistente;
* nome de aba incorreto;
* planilha vazia;
* estrutura incompatível.

---

## Colunas obrigatórias

Exemplos:

* coluna ausente;
* coluna renomeada incorretamente;
* ordem inesperada (quando aplicável).

---

## Tipagem

Exemplos:

* valor textual onde deveria existir número;
* data inválida;
* campo obrigatório nulo.

---

# Métodos públicos previstos

## validate()

Executa o processo completo de validação estrutural.

Retorna sucesso ou lança exceções específicas da aplicação.

---

## validate_required_columns()

Verifica a existência das colunas obrigatórias.

---

## validate_sheet_structure()

Valida a estrutura geral da planilha.

---

## validate_data_types()

Valida tipos de dados esperados.

---

## validate_required_fields()

Verifica preenchimento de campos obrigatórios.

---

# Dependências

O `SchemaValidator` poderá depender de:

* Validator Protocol
* InputFile
* AppConfig
* pandas
* openpyxl

Não deve depender de regras de negócio ou componentes de domínio.

---

# Classes consumidoras

Espera-se que os seguintes componentes utilizem o `SchemaValidator`:

* Orchestrator
* ExcelService (indiretamente, em alguns fluxos)

---

# Fluxo simplificado

```text
InputFile
     │
     ▼
SchemaValidator
     │
     ├── colunas
     ├── abas
     ├── tipos
     └── campos obrigatórios
     │
     ▼
Estrutura válida
```

---

# Ciclo de vida

O `SchemaValidator` é instanciado no Composition Root (`main.py`) e injetado no `Orchestrator`.

Ele deve ser executado antes de qualquer processamento ou validação de negócio.

---

# Tratamento de erros

Falhas estruturais devem gerar exceções específicas da aplicação.

Exemplos:

```text
FileValidationError
SchemaValidationError
```

A validação não deve corrigir automaticamente inconsistências.

---

# Princípios SOLID aplicados

## Single Responsibility Principle (SRP)

Possui apenas uma responsabilidade: validar a estrutura dos dados.

---

## Liskov Substitution Principle (LSP)

Pode ser utilizado através do contrato definido em `Validator Protocol`.

---

## Dependency Inversion Principle (DIP)

Consumidores dependem da abstração de validação e não da implementação concreta.

---

# Possíveis evoluções futuras

A estrutura permite incorporar facilmente:

* validações configuráveis por arquivo;
* schemas dinâmicos;
* suporte a múltiplos formatos;
* validação baseada em JSON Schema;
* integração com frameworks de validação;
* relatórios detalhados de inconsistências.

---

# Observações arquiteturais

O `SchemaValidator` representa a primeira barreira de proteção da aplicação.

Seu objetivo é impedir que dados estruturalmente inválidos avancem para etapas posteriores do processamento.

Ele deve permanecer focado exclusivamente na validação estrutural, deixando validações relacionadas ao domínio para o `BusinessValidator`.

Essa separação reduz acoplamento, facilita manutenção e melhora a legibilidade da arquitetura.
