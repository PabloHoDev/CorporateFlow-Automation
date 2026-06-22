# FileValidationError

- **Status:** 🟡 Em elaboração
- **Módulo:** `src/exceptions/file_validation_error.py`
- **Categoria:** Exception

---

# Objetivo

A exceção `FileValidationError` representa falhas encontradas durante a validação estrutural de arquivos e dados de entrada da aplicação.

Seu objetivo é impedir que informações incompatíveis avancem para etapas posteriores do processamento.

---

# Responsabilidade

A `FileValidationError` deve ser utilizada exclusivamente para representar erros relacionados à estrutura, formato ou integridade dos dados recebidos.

Ela não deve ser utilizada para problemas de configuração da aplicação ou violações de regras de negócio.

---

# Cenários de utilização

A exceção poderá ser utilizada em situações como:

- Coluna obrigatória inexistente.
- Aba obrigatória ausente.
- Arquivo vazio.
- Estrutura incompatível com o esperado.
- Tipo de dado inválido.
- Campo obrigatório não preenchido.
- Arquivo corrompido.
- Layout incompatível com o schema definido.

---

# Exemplos

## Coluna obrigatória ausente

```python
raise FileValidationError(
    "A coluna 'OBRIGACAO' não foi encontrada."
)
```

---

## Aba inexistente

```python
raise FileValidationError(
    "A aba 'BASE_GERAL' não existe no arquivo."
)
```

---

## Arquivo vazio

```python
raise FileValidationError(
    "O arquivo não possui registros para processamento."
)
```

---

## Estrutura inválida

```python
raise FileValidationError(
    "A estrutura do arquivo é incompatível com o layout esperado."
)
```

---

# Classes que podem lançar esta exceção

Espera-se que esta exceção seja utilizada por:

- SchemaValidator
- FileService
- ExcelService

Outros componentes poderão utilizá-la quando necessário.

---

# Fluxo simplificado

```text
InputFile

│

▼

SchemaValidator

│

├── estrutura válida
│       │
│       ▼
│   continua processamento
│
└── estrutura inválida
        │
        ▼

FileValidationError
```

---

# Hierarquia sugerida

```text
Exception

└── FileValidationError
```

---

# Tratamento esperado

A aplicação deve considerar esta exceção como uma falha de entrada de dados.

Fluxo esperado:

```text
FileValidationError

↓

Registrar log

↓

Registrar ProcessingResult

↓

Continuar ou interromper execução
(conforme estratégia definida)
```

A decisão de interromper ou continuar o processamento deve pertencer ao `Orchestrator`.

---

# Dependências

A exceção não deve depender de serviços, modelos ou componentes da aplicação.

Deve permanecer simples, desacoplada e reutilizável.

---

# Princípios aplicados

## Single Responsibility Principle (SRP)

Representa exclusivamente erros relacionados à validação estrutural de arquivos e dados de entrada.

---

## Separation of Concerns

Separa claramente problemas estruturais dos dados de:

- configuração da aplicação;
- regras de negócio;
- processamento operacional.

---

# Possíveis evoluções futuras

A estrutura permite incorporar facilmente:

- códigos padronizados de erro;
- identificação da coluna ou aba afetada;
- contexto adicional para auditoria;
- múltiplas inconsistências em uma única exceção;
- internacionalização de mensagens.

---

# Observações arquiteturais

A `FileValidationError` representa a principal exceção da camada de validação estrutural.

Ela deve ser utilizada sempre que os dados recebidos não atenderem aos requisitos mínimos necessários para o processamento seguro da aplicação.

Seu uso permite identificar rapidamente problemas de layout, schema e integridade dos arquivos de entrada, mantendo separação clara entre falhas estruturais e falhas de negócio.

Ela é a exceção naturalmente associada ao `SchemaValidator` dentro da arquitetura do sistema.