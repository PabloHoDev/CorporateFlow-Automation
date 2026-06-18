# AppConfig

* **Status:** 🟡 Em elaboração
* **Módulo:** `src/models/app_config.py`
* **Categoria:** Model

---

# Objetivo

A classe `AppConfig` representa a configuração efetiva da aplicação após o carregamento e validação realizados pelo `ConfigurationManager`.

Ela funciona como um objeto centralizado e tipado, permitindo que todos os componentes do sistema acessem configurações de forma consistente, segura e desacoplada do mecanismo de carregamento.

---

# Responsabilidade

O `AppConfig` é responsável exclusivamente por armazenar os valores de configuração utilizados durante uma execução da aplicação.

Ele não realiza leitura de arquivos, validações ou qualquer tipo de processamento.

---

# Responsabilidades dentro do escopo

* Representar as configurações carregadas da aplicação.
* Disponibilizar propriedades tipadas para acesso aos parâmetros.
* Servir como fonte única de configuração durante toda a execução.
* Facilitar compartilhamento seguro entre os componentes.

---

# Responsabilidades fora do escopo

O `AppConfig` **não deve**:

* Ler arquivos YAML.
* Interpretar configurações.
* Validar regras de configuração.
* Carregar variáveis de ambiente.
* Persistir informações.
* Modificar valores dinamicamente durante a execução.

Essas responsabilidades pertencem ao `ConfigurationManager`.

---

# Atributos previstos

## Diretórios

| Atributo         | Tipo | Descrição                       |
| ---------------- | ---- | ------------------------------- |
| input_directory  | Path | Diretório de entrada            |
| output_directory | Path | Diretório de saída              |
| backup_directory | Path | Diretório destinado aos backups |
| log_directory    | Path | Diretório destinado aos logs    |

---

## Configurações de processamento

| Atributo           | Tipo | Descrição                                                  |
| ------------------ | ---- | ---------------------------------------------------------- |
| create_backup      | bool | Define se backups devem ser criados                        |
| overwrite_existing | bool | Permite sobrescrever arquivos existentes                   |
| continue_on_error  | bool | Indica se o processamento continua após erros recuperáveis |

---

## Configurações de log

| Atributo      | Tipo | Descrição                                          |
| ------------- | ---- | -------------------------------------------------- |
| log_level     | str  | Nível de detalhamento dos logs                     |
| save_log_file | bool | Indica se os logs devem ser persistidos em arquivo |

---

## Configurações futuras

A estrutura permite expansão para novos grupos, como:

* notificações;
* integração com APIs;
* banco de dados;
* autenticação;
* processamento paralelo;
* filas de mensagens.

---

# Métodos públicos previstos

Por ser um modelo de dados, o `AppConfig` idealmente não deve possuir lógica operacional.

Caso necessário, apenas métodos utilitários simples poderão existir.

## to_dict()

Retorna uma representação serializável da configuração.

---

## **repr**()

Retorna uma representação resumida para depuração.

---

# Dependências

O `AppConfig` não depende de serviços da aplicação.

Pode utilizar apenas tipos básicos e estruturas auxiliares como:

* `Path`
* `bool`
* `str`
* `int`
* `float`
* `list`
* `dict`

---

# Classes consumidoras

O objeto poderá ser utilizado por:

* `Orchestrator`
* `ExecutionContext`
* `BackupService`
* `FileService`
* `ExcelService`
* `LogService`
* `ReportService`
* `SchemaValidator`
* `BusinessValidator`
* `TextNormalizer`
* `CityNormalizer`

Sempre em modo somente leitura.

---

# Fluxo simplificado

```text
config.yaml

│

▼

ConfigurationManager

│

▼

AppConfig

│

▼

main.py

│

▼

Orchestrator

│

▼

ExecutionContext

│

▼

Serviços e demais componentes
```

---

# Ciclo de vida

O `AppConfig` é criado durante a inicialização da aplicação pelo `ConfigurationManager`.

Após sua criação, ele deve permanecer inalterado durante toda a execução, sendo compartilhado entre os componentes por meio do `ExecutionContext`.

---

# Imutabilidade

Sempre que possível, recomenda-se implementar `AppConfig` como um objeto imutável.

Exemplo conceitual:

```python
@dataclass(frozen=True)
class AppConfig:
    ...
```

Essa abordagem evita modificações acidentais durante o processamento e aumenta a previsibilidade do sistema.

---

# Princípios SOLID aplicados

## Single Responsibility Principle (SRP)

Possui apenas uma responsabilidade: representar as configurações da aplicação.

---

## Open/Closed Principle (OCP)

Novos parâmetros podem ser adicionados sem alterar o comportamento existente.

---

# Possíveis evoluções futuras

O modelo permite incorporar facilmente:

* configurações específicas por ambiente;
* configuração de múltiplos perfis;
* parâmetros de cache;
* configurações de segurança;
* limites de processamento;
* políticas de retry;
* configuração de integrações externas.

---

# Observações arquiteturais

O `AppConfig` é um objeto de domínio e não um serviço.

Ele representa exclusivamente os dados de configuração carregados pelo `ConfigurationManager` e compartilhados durante a execução.

Nenhum componente da aplicação deve acessar diretamente arquivos de configuração após sua criação.

Todo acesso às configurações deve ocorrer exclusivamente através da instância de `AppConfig`, garantindo baixo acoplamento e uma arquitetura consistente.
