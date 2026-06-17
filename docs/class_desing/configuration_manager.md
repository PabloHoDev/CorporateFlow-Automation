# ConfigurationManager

* **Status:** 🟡 Em elaboração
* **Módulo:** `src/config/configuration_manager.py`
* **Categoria:** Configuration

---

# Objetivo

A classe `ConfigurationManager` é responsável por carregar, interpretar e validar as configurações da aplicação a partir de fontes externas.

Sua principal função é transformar os dados de configuração em um objeto `AppConfig`, que será utilizado pelo restante do sistema.

---

# Responsabilidade

O `ConfigurationManager` atua exclusivamente durante a fase de inicialização da aplicação.

Após concluir o carregamento das configurações, sua responsabilidade termina e o objeto `AppConfig` passa a ser a única representação das configurações em memória.

---

# Responsabilidades dentro do escopo

* Localizar o arquivo de configuração.
* Ler o conteúdo do arquivo.
* Interpretar os dados.
* Validar a estrutura básica da configuração.
* Construir uma instância de `AppConfig`.
* Retornar o objeto configurado para o `main.py`.

---

# Responsabilidades fora do escopo

O `ConfigurationManager` **não deve**:

* Armazenar estado da execução.
* Compartilhar configurações entre componentes.
* Processar regras de negócio.
* Gerenciar arquivos de entrada.
* Criar backups.
* Executar validações de domínio.
* Coordenar o fluxo da aplicação.

Após produzir o `AppConfig`, sua responsabilidade é considerada concluída.

---

# Atributos previstos

A implementação idealmente não deve manter atributos permanentes.

Caso necessário, apenas:

| Atributo    | Tipo | Descrição                                                           |
| ----------- | ---- | ------------------------------------------------------------------- |
| config_path | Path | Caminho do arquivo de configuração utilizado durante o carregamento |

---

# Métodos públicos previstos

## load()

Realiza o carregamento completo das configurações da aplicação e retorna um objeto `AppConfig`.

Retorno esperado:

```text
AppConfig
```

---

## validate_configuration()

Valida a estrutura mínima do conteúdo carregado antes da criação do objeto `AppConfig`.

---

## build_app_config()

Converte os dados carregados para uma instância tipada de `AppConfig`.

---

# Dependências

O `ConfigurationManager` poderá depender apenas de componentes relacionados ao carregamento da configuração, como:

* AppConfig
* bibliotecas de leitura YAML
* utilitários de sistema de arquivos

Não deve depender de serviços de negócio da aplicação.

---

# Classes consumidoras

Espera-se que apenas o `main.py` utilize diretamente esta classe.

Nenhum outro componente deve depender do `ConfigurationManager`.

Após sua utilização, apenas o objeto `AppConfig` deverá ser compartilhado com o restante do sistema.

---

# Fluxo simplificado

```text
main.py

│

▼

ConfigurationManager

│

├── localiza config.yaml

├── lê arquivo

├── valida estrutura

├── cria AppConfig

│

▼

retorna AppConfig

│

▼

main.py

│

▼

Orchestrator
```

---

# Ciclo de vida

O `ConfigurationManager` possui ciclo de vida temporário.

Ele existe apenas durante a inicialização da aplicação e pode ser descartado imediatamente após retornar o objeto `AppConfig`.

---

# Princípios SOLID aplicados

## Single Responsibility Principle (SRP)

Possui uma única responsabilidade: carregar e construir a configuração da aplicação.

---

## Open/Closed Principle (OCP)

Novos campos podem ser adicionados ao `AppConfig` sem alterar a responsabilidade principal da classe.

---

## Dependency Inversion Principle (DIP)

Os demais componentes dependem do objeto `AppConfig`, e não do mecanismo utilizado para carregá-lo.

---

# Possíveis evoluções futuras

A arquitetura permite adicionar facilmente suporte para:

* múltiplos arquivos de configuração;
* variáveis de ambiente;
* arquivos JSON;
* arquivos TOML;
* banco de dados;
* serviços remotos de configuração;
* provedores secretos (*Secrets Manager*);
* configuração por linha de comando.

Todas essas mudanças podem ser implementadas sem impactar o restante da aplicação.

---

# Observações arquiteturais

O `ConfigurationManager` não representa a configuração da aplicação.

Sua única função é produzir um objeto `AppConfig` consistente e validado.

Após essa etapa, todos os componentes do sistema devem utilizar exclusivamente o `AppConfig`, evitando dependência direta do mecanismo de carregamento e preservando baixo acoplamento entre as camadas da aplicação.
