# CityNormalizer

- **Status:** 🟡 Em elaboração
- **Módulo:** `src/normalizers/city_normalizer.py`
- **Categoria:** Normalizer

---

# Objetivo

A classe `CityNormalizer` é responsável por padronizar nomes de cidades utilizados pela aplicação.

Seu objetivo é reduzir inconsistências provocadas por diferenças de escrita, acentuação, abreviações, caracteres especiais e variações cadastrais.

---

# Responsabilidade

O `CityNormalizer` deve executar exclusivamente operações relacionadas à normalização de nomes de cidades.

Ele não deve validar regras de negócio nem determinar se uma cidade existe ou é válida.

---

# Responsabilidades dentro do escopo

- Padronizar nomes de cidades.
- Remover acentuação.
- Padronizar caixa de texto.
- Corrigir espaços excedentes.
- Tratar caracteres especiais.
- Uniformizar variações comuns de escrita.
- Preparar nomes de cidades para comparação e cruzamento de dados.

---

# Responsabilidades fora do escopo

A classe **não deve**:

- Validar existência da cidade.
- Validar códigos IBGE.
- Aplicar regras de negócio.
- Atualizar arquivos.
- Persistir informações.
- Corrigir dados cadastrais incorretos.
- Executar processamento operacional.

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
SAO PAULO
```

---

## Padronização de caixa

Entrada:

```text
rio de janeiro
```

Saída:

```text
RIO DE JANEIRO
```

---

## Remoção de espaços excedentes

Entrada:

```text
  BELO   HORIZONTE
```

Saída:

```text
BELO HORIZONTE
```

---

## Tratamento de caracteres especiais

Entrada:

```text
SÃO-PAULO
```

Saída:

```text
SAO PAULO
```

---

## Comparação padronizada

Entrada:

```text
São Paulo
SAO PAULO
são paulo
```

Resultado normalizado:

```text
SAO PAULO
```

---

# Estratégia de normalização

O processo de normalização deverá seguir a sequência:

```text
Cidade original

↓

TextNormalizer

↓

Regras específicas de cidade

↓

Cidade normalizada
```

O componente deverá reutilizar o `TextNormalizer` sempre que possível, evitando duplicação de lógica.

---

# Métodos públicos previstos

## normalize()

Executa o fluxo completo de normalização de cidades.

Representa o principal ponto de entrada da classe.

---

## normalize_city_name()

Aplica regras específicas de padronização para nomes de cidades.

---

## remove_city_variations()

Trata variações conhecidas de escrita.

---

## standardize_city_format()

Aplica o formato padrão definido pela aplicação.

---

# Dependências

O `CityNormalizer` poderá depender de:

- Normalizer Protocol
- TextNormalizer
- re
- unicodedata

Não deve depender de componentes de validação ou regras de negócio.

---

# Classes consumidoras

Espera-se que os seguintes componentes utilizem o `CityNormalizer`:

- Orchestrator
- BusinessValidator
- Processos de cruzamento de dados
- Serviços de integração

---

# Fluxo simplificado

```text
Nome da Cidade

│

▼

TextNormalizer

│

▼

CityNormalizer

│

▼

Nome Padronizado
```

---

# Ciclo de vida

O `CityNormalizer` é instanciado no Composition Root (`main.py`) e injetado nos componentes que necessitam de normalização de cidades.

Sua utilização é stateless, permitindo reutilização durante toda a execução da aplicação.

---

# Tratamento de erros

O componente deve ser resiliente a entradas inesperadas.

Exemplos:

```text
None
String vazia
Caracteres especiais
Texto inválido
```

Quando aplicável, exceções específicas poderão ser lançadas.

---

# Princípios SOLID aplicados

## Single Responsibility Principle (SRP)

Possui apenas uma responsabilidade: normalizar nomes de cidades.

---

## Liskov Substitution Principle (LSP)

Pode ser utilizado através do contrato definido em `Normalizer Protocol`.

---

## Dependency Inversion Principle (DIP)

Consumidores dependem da abstração de normalização e não da implementação concreta.

---

# Possíveis evoluções futuras

A estrutura permite incorporar facilmente:

- integração com base IBGE;
- dicionários oficiais de municípios;
- fuzzy matching;
- aliases de cidades;
- correção automática de grafias conhecidas;
- suporte internacional;
- enriquecimento de dados geográficos.

---

# Observações arquiteturais

O `CityNormalizer` representa um normalizador especializado para o domínio de cidades.

Ele deve reutilizar o `TextNormalizer` para operações textuais genéricas e concentrar apenas as regras específicas relacionadas à padronização de municípios.

Essa abordagem evita duplicação de código, aumenta reutilização e mantém a arquitetura alinhada aos princípios de responsabilidade única e composição de componentes.

O componente não deve validar se uma cidade existe ou pertence a uma determinada UF. Seu papel é exclusivamente produzir uma representação textual padronizada do nome informado.