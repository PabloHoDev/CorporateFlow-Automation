# InputFile

* **Status:** 🟡 Em elaboração
* **Módulo:** `src/models/input_file.py`
* **Categoria:** Model

---

# Objetivo

A classe `InputFile` representa um arquivo identificado pela aplicação para participar do fluxo de processamento.

Ela encapsula os metadados necessários para que serviços, validadores e demais componentes possam manipular o arquivo de forma consistente, sem depender diretamente do sistema de arquivos.

---

# Responsabilidade

O `InputFile` é responsável exclusivamente por representar um arquivo de entrada e seus respectivos atributos.

Ele não executa operações de leitura, escrita, movimentação ou exclusão.

---

# Responsabilidades dentro do escopo

* Representar um arquivo localizado pela aplicação.
* Armazenar informações relevantes para o processamento.
* Disponibilizar metadados de forma estruturada.
* Facilitar o compartilhamento dessas informações entre os componentes do sistema.

---

# Responsabilidades fora do escopo

O `InputFile` **não deve**:

* Abrir arquivos.
* Ler conteúdo.
* Escrever dados.
* Copiar arquivos.
* Mover arquivos.
* Excluir arquivos.
* Validar regras de negócio.
* Normalizar informações.

Essas responsabilidades pertencem aos respectivos serviços especializados.

---

# Atributos previstos

## Identificação

| Atributo  | Tipo | Descrição                    |
| --------- | ---- | ---------------------------- |
| file_name | str  | Nome completo do arquivo     |
| stem      | str  | Nome do arquivo sem extensão |
| extension | str  | Extensão do arquivo          |
| path      | Path | Caminho absoluto do arquivo  |

---

## Informações físicas

| Atributo    | Tipo     | Descrição                   |
| ----------- | -------- | --------------------------- |
| size_bytes  | int      | Tamanho do arquivo em bytes |
| created_at  | datetime | Data de criação             |
| modified_at | datetime | Data da última modificação  |

---

## Informações de processamento

| Atributo      | Tipo           | Descrição                                                |
| ------------- | -------------- | -------------------------------------------------------- |
| discovered_at | datetime       | Momento em que o arquivo foi identificado pela aplicação |
| status        | str            | Estado atual durante o processamento                     |
| metadata      | dict[str, Any] | Informações adicionais associadas ao arquivo             |

---

# Estados previstos (`status`)

O atributo `status` poderá assumir valores como:

* `DISCOVERED`
* `VALIDATED`
* `PROCESSING`
* `PROCESSED`
* `FAILED`
* `SKIPPED`

Outros estados poderão ser adicionados conforme evolução do projeto.

---

# Métodos públicos previstos

Por se tratar de um modelo de domínio, recomenda-se minimizar lógica operacional.

## to_dict()

Retorna uma representação serializável do objeto.

---

## **repr**()

Retorna uma representação resumida para fins de depuração.

---

# Dependências

O `InputFile` deve depender apenas de estruturas simples, como:

* `Path`
* `datetime`
* `dict`
* `str`
* `int`

Não deve depender de serviços da aplicação.

---

# Classes consumidoras

O objeto poderá ser utilizado por:

* `FileService`
* `BackupService`
* `ExcelService`
* `SchemaValidator`
* `BusinessValidator`
* `TextNormalizer`
* `CityNormalizer`
* `ProcessingResult`
* `ExecutionContext`

---

# Fluxo simplificado

```text
Sistema de Arquivos

│

▼

FileService

│

▼

InputFile

│

▼

Validators

│

▼

Normalizers

│

▼

ExcelService

│

▼

ProcessingResult
```

---

# Ciclo de vida

O `InputFile` é criado quando o `FileService` identifica um arquivo elegível para processamento.

Após sua criação, ele acompanha o fluxo completo da aplicação até a geração do resultado final.

---

# Imutabilidade

Os atributos que representam características físicas do arquivo (nome, caminho, extensão e tamanho) devem permanecer inalterados após a criação do objeto.

Caso seja necessário registrar informações adicionais durante a execução, recomenda-se utilizar os campos `status` e `metadata`.

---

# Princípios SOLID aplicados

## Single Responsibility Principle (SRP)

Possui apenas uma responsabilidade: representar um arquivo de entrada da aplicação.

---

## Open/Closed Principle (OCP)

Novos atributos podem ser adicionados sem alterar a responsabilidade fundamental da classe.

---

# Possíveis evoluções futuras

A estrutura permite incorporar facilmente:

* hash SHA-256;
* hash MD5;
* MIME Type;
* proprietário do arquivo;
* permissões do sistema operacional;
* identificadores únicos;
* classificação por categoria;
* tags de processamento.

Essas evoluções podem ser adicionadas sem impacto significativo na arquitetura existente.

---

# Observações arquiteturais

O `InputFile` é um objeto de domínio e não deve conter lógica operacional.

Toda interação com o sistema de arquivos deve ocorrer exclusivamente por meio do `FileService`.

Essa separação garante baixo acoplamento, alta coesão e facilita a manutenção, os testes automatizados e futuras evoluções da aplicação.
