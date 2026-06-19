# BackupService

- **Status:** 🟡 Em elaboração
- **Módulo:** `src/services/backup_service.py`
- **Categoria:** Service

---

# Objetivo

A classe `BackupService` é responsável por criar e gerenciar cópias de segurança dos arquivos utilizados pela aplicação.

Seu objetivo é garantir que informações importantes possam ser preservadas antes de operações potencialmente destrutivas ou de atualização.

---

# Responsabilidade

O `BackupService` deve executar exclusivamente operações relacionadas à criação e gerenciamento de backups.

Ele não deve participar das decisões de negócio que determinam quando ou por que um backup será realizado.

---

# Responsabilidades dentro do escopo

- Criar backups de arquivos.
- Criar backups de diretórios quando necessário.
- Gerar nomes únicos para os backups.
- Garantir que o diretório de destino exista.
- Retornar informações sobre o backup criado.
- Registrar falhas por meio das exceções apropriadas.

---

# Responsabilidades fora do escopo

A classe **não deve**:

- Decidir quando criar backups.
- Processar planilhas.
- Validar arquivos.
- Normalizar dados.
- Gerar relatórios.
- Executar regras de negócio.
- Coordenar o fluxo da aplicação.

Essas responsabilidades pertencem ao `Orchestrator` ou aos demais componentes especializados.

---

# Métodos públicos previstos

## create_backup()

Cria uma cópia de segurança de um arquivo.

Retorna informações sobre o backup realizado.

---

## create_directory_backup()

Cria uma cópia de segurança completa de um diretório.

Sua utilização dependerá das necessidades futuras da aplicação.

---

## generate_backup_name()

Gera um nome padronizado para o arquivo de backup.

Poderá utilizar timestamp ou outro identificador único.

---

## ensure_backup_directory()

Verifica se o diretório de backups existe e o cria quando necessário.

---

# Dependências

O `BackupService` poderá depender apenas de componentes relacionados ao sistema de arquivos, como:

- `Path`
- `shutil`
- `datetime`

Quando necessário, poderá utilizar informações provenientes do `AppConfig`.

Não deve depender de componentes responsáveis por regras de negócio.

---

# Classes consumidoras

Espera-se que os seguintes componentes utilizem o `BackupService`:

- `Orchestrator`

Outros consumidores poderão surgir conforme evolução da arquitetura.

---

# Fluxo simplificado

```text
Orchestrator

│

▼

BackupService

│

▼

Sistema de Arquivos

│

▼

Diretório de Backup
```

---

# Ciclo de vida

O `BackupService` deverá ser instanciado durante a inicialização da aplicação pelo `main.py` (Composition Root).

Sua instância será injetada no `Orchestrator`, permanecendo disponível durante toda a execução.

---

# Tratamento de erros

Falhas relacionadas à criação de backups deverão ser comunicadas por meio das exceções apropriadas da aplicação.

O serviço não deve ocultar erros silenciosamente.

---

# Princípios SOLID aplicados

## Single Responsibility Principle (SRP)

Possui apenas uma responsabilidade: realizar operações relacionadas a backups.

---

## Dependency Inversion Principle (DIP)

Depende apenas de abstrações ou componentes básicos da infraestrutura necessários para sua operação.

---

## Open/Closed Principle (OCP)

Novas estratégias de backup poderão ser incorporadas sem alterar a responsabilidade principal da classe.

---

# Possíveis evoluções futuras

A estrutura permite incorporar facilmente:

- versionamento automático;
- compressão de backups;
- retenção configurável;
- backups incrementais;
- backups em armazenamento remoto;
- criptografia dos arquivos;
- políticas automáticas de limpeza.

---

# Observações arquiteturais

O `BackupService` representa um serviço de infraestrutura especializado na criação de cópias de segurança.

Ele não deve conter regras de negócio relacionadas ao fluxo da aplicação.

A decisão sobre quando executar um backup pertence exclusivamente ao `Orchestrator`, que atua como coordenador do processamento.

Essa separação reduz o acoplamento entre componentes e preserva a responsabilidade única do serviço.