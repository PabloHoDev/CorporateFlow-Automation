# FileService

* **Status:** 🟡 Em elaboração
* **Módulo:** `src/services/file_service.py`
* **Categoria:** Service

---

# Objetivo

A classe `FileService` é responsável por centralizar todas as operações relacionadas ao sistema de arquivos utilizadas pela aplicação.

Seu objetivo é fornecer uma interface única e padronizada para descoberta, leitura de metadados, manipulação e gerenciamento de arquivos e diretórios.

---

# Responsabilidade

O `FileService` deve executar exclusivamente operações relacionadas ao sistema de arquivos.

Ele não deve conter regras de negócio nem tomar decisões sobre o fluxo de processamento.

---

# Responsabilidades dentro do escopo

* Localizar arquivos em diretórios configurados.
* Criar objetos `InputFile` a partir dos arquivos encontrados.
* Verificar existência de arquivos e diretórios.
* Criar diretórios quando necessário.
* Obter metadados de arquivos.
* Mover arquivos.
* Copiar arquivos.
* Remover arquivos quando autorizado.
* Disponibilizar operações auxiliares relacionadas ao sistema de arquivos.

---

# Responsabilidades fora do escopo

A classe **não deve**:

* Processar planilhas.
* Executar regras de negócio.
* Criar backups (responsabilidade do `BackupService`).
* Validar estruturas.
* Normalizar dados.
* Gerar relatórios.
* Coordenar o fluxo da aplicação.

Essas responsabilidades pertencem aos componentes especializados.

---

# Métodos públicos previstos

## discover_files()

Localiza arquivos elegíveis para processamento no diretório configurado.

Retorna uma coleção de objetos `InputFile`.

---

## build_input_file()

Constrói um objeto `InputFile` a partir de um arquivo localizado no sistema.

---

## exists()

Verifica se um arquivo ou diretório existe.

---

## ensure_directory()

Garante que um diretório exista, criando-o quando necessário.

---

## copy()

Realiza a cópia de um arquivo.

---

## move()

Move um arquivo para outro local.

---

## delete()

Remove um arquivo do sistema, quando permitido pela configuração da aplicação.

---

## get_metadata()

Obtém informações físicas e temporais sobre um arquivo.

---

# Dependências

O `FileService` poderá depender apenas de bibliotecas relacionadas ao sistema de arquivos, como:

* `pathlib.Path`
* `shutil`
* `os`
* `datetime`

Quando necessário, poderá utilizar parâmetros provenientes do `AppConfig`.

Não deve depender de componentes responsáveis por regras de negócio.

---

# Classes consumidoras

Espera-se que os seguintes componentes utilizem o `FileService`:

* `Orchestrator`
* `BackupService` (quando necessário)
* `ExcelService` (para obtenção de caminhos ou recursos auxiliares)

Outros consumidores poderão surgir conforme evolução da arquitetura.

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

Orchestrator

│

▼

Demais componentes
```

---

# Ciclo de vida

O `FileService` deverá ser instanciado durante a inicialização da aplicação pelo `main.py` (Composition Root).

Sua instância será compartilhada com o `Orchestrator` por meio de injeção de dependência.

---

# Tratamento de erros

Falhas relacionadas ao acesso ao sistema de arquivos deverão ser propagadas utilizando as exceções apropriadas da aplicação.

O serviço não deve ocultar erros silenciosamente.

---

# Princípios SOLID aplicados

## Single Responsibility Principle (SRP)

Possui apenas uma responsabilidade: executar operações relacionadas ao sistema de arquivos.

---

## Dependency Inversion Principle (DIP)

Os consumidores dependem do contrato do serviço e não das APIs específicas do sistema operacional.

---

## Open/Closed Principle (OCP)

Novas operações de manipulação de arquivos poderão ser adicionadas sem alterar sua responsabilidade principal.

---

# Possíveis evoluções futuras

A estrutura permite incorporar facilmente:

* suporte a múltiplos sistemas de armazenamento;
* integração com armazenamento em nuvem;
* monitoramento de diretórios (*watchers*);
* operações assíncronas;
* cache de metadados;
* controle de permissões;
* versionamento de arquivos.

---

# Observações arquiteturais

O `FileService` representa a camada oficial de acesso ao sistema de arquivos da aplicação.

Nenhum outro componente deve interagir diretamente com APIs como `os`, `pathlib` ou `shutil` para operações de manipulação de arquivos.

Toda comunicação com o sistema de arquivos deve ocorrer exclusivamente por meio deste serviço, preservando baixo acoplamento, alta coesão e facilitando testes automatizados e futuras evoluções da arquitetura.
