# BusinessValidator

- **Status:** 🟡 Em elaboração
- **Módulo:** `src/validators/business_validator.py`
- **Categoria:** Validator

---

# Objetivo

A classe `BusinessValidator` é responsável por validar regras de negócio aplicáveis aos dados processados pela aplicação.

Seu objetivo é garantir que os dados sejam não apenas estruturalmente válidos, mas também consistentes com as regras operacionais e requisitos do domínio.

---

# Responsabilidade

O `BusinessValidator` deve validar exclusivamente regras de negócio.

Ele não deve validar estrutura de arquivos, formatos de planilhas ou aspectos técnicos dos dados.

---

# Responsabilidades dentro do escopo

- Validar regras de negócio.
- Verificar consistência entre campos relacionados.
- Validar restrições operacionais.
- Garantir conformidade com regras corporativas.
- Detectar situações incompatíveis com o domínio da aplicação.
- Impedir processamento de dados inválidos sob a ótica do negócio.

---

# Responsabilidades fora do escopo

A classe **não deve**:

- Validar estrutura de arquivos.
- Verificar existência de colunas.
- Validar tipos de dados.
- Corrigir informações.
- Atualizar planilhas.
- Processar arquivos.
- Gerar relatórios.
- Coordenar fluxo de execução.

Essas responsabilidades pertencem a outros componentes da arquitetura.

---

# Cenários de validação previstos

Os exemplos abaixo representam cenários típicos de validação de negócio.

A implementação final dependerá dos requisitos específicos do sistema.

---

## Consistência de status

Exemplos:

- status incompatível com etapa do processo;
- status inexistente na lista permitida;
- transição inválida entre estados.

---

## Consistência operacional

Exemplos:

- obrigação incompatível com a UF;
- categoria incompatível com o tipo de registro;
- relacionamento inválido entre campos.

---

## Regras corporativas

Exemplos:

- valores obrigatórios sob determinadas condições;
- restrições específicas do processo;
- bloqueios operacionais.

---

## Regras de SLA

Exemplos:

- prazo vencido;
- data inconsistente;
- cálculo incompatível com política definida.

---

# Métodos públicos previstos

## validate()

Executa o processo completo de validação de negócio.

Retorna sucesso ou lança exceções específicas da aplicação.

---

## validate_status()

Valida regras relacionadas a status.

---

## validate_relationships()

Valida consistência entre campos relacionados.

---

## validate_business_rules()

Executa regras corporativas específicas.

---

## validate_sla()

Valida regras relacionadas a prazos e SLA.

---

# Dependências

O `BusinessValidator` poderá depender de:

- Validator Protocol
- AppConfig
- InputFile
- pandas

Poderá utilizar configurações da aplicação para parametrizar regras.

Não deve depender de serviços responsáveis por processamento ou persistência.

---

# Classes consumidoras

Espera-se que os seguintes componentes utilizem o `BusinessValidator`:

- Orchestrator

Outros consumidores poderão surgir conforme evolução da arquitetura.

---

# Fluxo simplificado

```text
InputFile
     │
     ▼
BusinessValidator
     │
     ├── regras operacionais
     ├── consistência
     ├── SLA
     └── domínio
     │
     ▼
Dados válidos para processamento
```

---

# Ciclo de vida

O `BusinessValidator` é instanciado no Composition Root (`main.py`) e injetado no `Orchestrator`.

Sua execução ocorre após a validação estrutural realizada pelo `SchemaValidator`.

Fluxo esperado:

```text
SchemaValidator

↓

BusinessValidator

↓

Normalizers

↓

Processamento
```

---

# Tratamento de erros

Falhas de negócio devem gerar exceções específicas da aplicação.

Exemplos:

```text
BusinessRuleError
ValidationError
```

As validações não devem corrigir automaticamente inconsistências identificadas.

---

# Princípios SOLID aplicados

## Single Responsibility Principle (SRP)

Possui apenas uma responsabilidade: validar regras de negócio.

---

## Liskov Substitution Principle (LSP)

Pode ser utilizado através do contrato definido em `Validator Protocol`.

---

## Dependency Inversion Principle (DIP)

Consumidores dependem da abstração de validação e não da implementação concreta.

---

# Possíveis evoluções futuras

A estrutura permite incorporar facilmente:

- regras configuráveis via arquivo;
- motor de regras (Rule Engine);
- validações parametrizadas;
- integração com APIs corporativas;
- validações condicionais;
- catálogos externos de regras;
- auditoria detalhada de inconsistências.

---

# Observações arquiteturais

O `BusinessValidator` representa a camada responsável por proteger as regras e restrições do domínio da aplicação.

Ele deve assumir que a estrutura dos dados já foi validada previamente pelo `SchemaValidator`.

Essa separação entre validação estrutural e validação de negócio reduz complexidade, facilita manutenção e melhora significativamente a testabilidade da aplicação.

O componente deve permanecer focado exclusivamente em regras de domínio, evitando acoplamento com aspectos técnicos de arquivos, planilhas ou infraestrutura.