# TextNormalizer

- **Status:** 🟡 Em elaboração
- **Módulo:** `src/normalizers/text_normalizer.py`
- **Categoria:** Normalizer

---

# Objetivo

A classe `TextNormalizer` é responsável por padronizar informações textuais utilizadas pela aplicação.

Seu objetivo é reduzir inconsistências causadas por diferenças de formatação, acentuação, capitalização, espaçamento e caracteres especiais.

---

# Responsabilidade

O `TextNormalizer` deve executar exclusivamente operações de normalização textual.

Ele não deve validar dados, aplicar regras de negócio ou realizar transformações específicas de domínio.

---

# Responsabilidades dentro do escopo

- Remover acentuação.
- Padronizar caixa de texto (maiúsculas/minúsculas).
- Remover espaços excedentes.
- Padronizar caracteres especiais.
- Remover caracteres invisíveis.
- Uniformizar formatos textuais.
- Preparar dados para comparação ou processamento posterior.

---

# Responsabilidades fora do escopo

A classe **não deve**:

- Validar dados.
- Corrigir regras de negócio.
- Interpretar significado das informações.
- Atualizar arquivos.
- Persistir dados.
- Executar processamento de domínio.
- Tomar decisões operacionais.

Essas responsabilidades pertencem a outros componentes da arquitetura.

---

# Casos de uso previstos

## Remoção de acentuação

Entrada:

```text
São Paulo
```

Saída:

```text
Sao Paulo
```

---

## Padronização de caixa

Entrada:

```text
são paulo
```

Saída:

```text
SAO PAULO
```

---

## Remoção de espaços extras

Entrada:

```text
  SAO    PAULO
```

Saída:

```text
SAO PAULO
```

---

## Limpeza de caracteres especiais

Entrada:

```text
São-Paulo_
```

Saída:

```text
SAO PAULO
```

(Dependendo da estratégia adotada.)

---

# Métodos públicos previstos

## normalize()

Executa o fluxo completo de normalização textual.

Representa o principal ponto de entrada da classe.

---

## remove_accents()

Remove caracteres acentuados.

---

## normalize_case()

Padroniza caixa de texto.

---

## normalize_whitespace()

Remove espaços excedentes.

---

## normalize_special_characters()

Padroniza caracteres especiais.

---

## clean()

Executa limpeza geral do conteúdo textual.

---

# Dependências

O `TextNormalizer` poderá depender apenas de bibliotecas auxiliares para manipulação textual, como:

- `unicodedata`
- `re`
- `string`

Não deve depender de componentes de negócio.

---

# Classes consumidoras

Espera-se que os seguintes componentes utilizem o `TextNormalizer`:

- Orchestrator
- CityNormalizer
- BusinessValidator (quando necessário)
- Outros normalizadores especializados

---

# Fluxo simplificado

```text
Texto Original

│

▼

TextNormalizer

│

├── acentos
├── espaços
├── caixa
├── caracteres especiais

▼

Texto Padronizado
```

---

# Ciclo de vida

O `TextNormalizer` é instanciado no Composition Root (`main.py`) e injetado nos componentes que necessitam de normalização textual.

Sua utilização é tipicamente stateless, permitindo reutilização durante toda a execução da aplicação.

---

# Tratamento de erros

O normalizador deve ser resiliente a entradas inesperadas sempre que possível.

Exemplos:

```text
None
String vazia
Caracteres especiais
Unicode inválido
```

Quando aplicável, exceções específicas poderão ser lançadas.

---

# Princípios SOLID aplicados

## Single Responsibility Principle (SRP)

Possui apenas uma responsabilidade: normalizar informações textuais.

---

## Liskov Substitution Principle (LSP)

Pode ser utilizado através do contrato definido em `Normalizer Protocol`.

---

## Dependency Inversion Principle (DIP)

Consumidores dependem da abstração de normalização e não da implementação concreta.

---

# Possíveis evoluções futuras

A estrutura permite incorporar facilmente:

- suporte multilíngue;
- transliteração avançada;
- normalização configurável;
- dicionários customizados;
- remoção inteligente de caracteres;
- integração com bibliotecas linguísticas especializadas.

---

# Observações arquiteturais

O `TextNormalizer` representa o componente base de normalização textual da aplicação.

Ele deve permanecer completamente independente de regras de negócio e de conhecimento específico do domínio.

Sua função é exclusivamente transformar diferentes representações textuais em uma forma padronizada e consistente.

Normalizadores especializados, como o `CityNormalizer`, poderão utilizar este componente como base para suas próprias estratégias de normalização.