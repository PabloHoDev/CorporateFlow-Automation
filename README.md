# CorporateFlow Automation

Framework modular em Python para automação de processos corporativos baseados em planilhas e arquivos, com foco em rastreabilidade, padronização de dados, auditoria e redução de tarefas manuais.


Breve descrição

## 📋 Índice

- Visão Geral
- Problema de Negócio
- Objetivos
- Funcionalidades
- Arquitetura
- Estrutura do Projeto
- Tecnologias
- Fluxo de Execução
- Instalação
- Configuração
- Como Utilizar
- Exemplo Prático
- Logs e Auditoria
- Testes
- Melhorias Futuras
- Contribuição
- Licença



## 📖 Visão Geral

CorporateFlow Automation é um projeto desenvolvido para automatizar fluxos operacionais que envolvem processamento de grandes volumes de dados provenientes de arquivos Excel, CSV ou outras fontes estruturadas.

A solução foi projetada utilizando princípios de arquitetura modular, separação de responsabilidades e boas práticas de engenharia de software, permitindo reutilização em diferentes cenários corporativos.


## 🎯 Problema de Negócio

Muitas operações corporativas dependem de atividades repetitivas como:

- Atualização manual de planilhas;
- Consolidação de bases;
- Validação de informações;
- Padronização de registros;
- Distribuição de arquivos;
- Controle operacional.

Essas tarefas aumentam o risco de erros humanos, elevam o retrabalho e dificultam auditorias.

O CorporateFlow Automation foi criado para reduzir esses riscos por meio da automação estruturada desses processos.

## 🚀 Objetivos

- Automatizar processos repetitivos;
- Garantir rastreabilidade das operações;
- Padronizar dados de entrada;
- Gerar logs completos;
- Facilitar auditorias;
- Minimizar erros humanos;
- Produzir relatórios automáticos;
- Servir como base reutilizável para novos projetos.

## ⚙️ Funcionalidades

- Backup automático antes das alterações
- Leitura de arquivos Excel
- Validação de dados
- Normalização de textos
- Aplicação de regras de negócio
- Atualização automatizada
- Geração de logs
- Relatórios de execução
- Tratamento de exceções
- Configuração externa via arquivo

## 🏗️ Arquitetura

O projeto segue uma arquitetura modular baseada em responsabilidades independentes.

                Entrada

                    │

                    ▼

            Validação Inicial

                    │

                    ▼

             Backup Automático

                    │

                    ▼

          Leitura dos Arquivos

                    │

                    ▼

         Normalização dos Dados

                    │

                    ▼

      Aplicação das Regras de Negócio

                    │

                    ▼

        Atualização das Informações

                    │

                    ▼

            Geração de Logs

                    │

                    ▼

          Relatório de Execução


## 📁 Estrutura do Projeto

CorporateFlow/

├── config/

├── docs/

├── input/

├── output/

├── backups/

├── logs/

├── src/

│   ├── core/

│   ├── services/

│   ├── validators/

│   ├── normalizers/

│   ├── models/

│   └── utils/

├── tests/

├── requirements.txt

└── README.md


## 🛠️ Tecnologias

- Python 3.13+
- pandas
- openpyxl
- pathlib
- logging
- pytest
- pydantic
- PyYAML
- typing
- dataclasses

## 🔄 Fluxo de Execução

1. Recebimento dos arquivos
2. Validação estrutural
3. Backup automático
4. Leitura das planilhas
5. Padronização dos dados
6. Aplicação das regras de negócio
7. Atualização das informações
8. Registro em log
9. Geração do relatório final

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/PabloHoDev/corporateflow.git
```

Entre na pasta:

```bash
cd corporateflow
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## ⚙️ Configuração

As configurações são centralizadas em um arquivo YAML.

Exemplo:

```yaml
input_folder: input

output_folder: output

backup_folder: backups

log_folder: logs
```

## ▶️ Execução

Execute:

```bash
python main.py
```

Ao final do processamento serão gerados:

- arquivos atualizados;
- logs completos;
- backups;
- relatório resumido.

## 📄 Exemplo de Log

```text

20:10:01 - Backup iniciado

20:10:04 - Backup concluído

20:10:05 - Arquivo carregado

20:10:12 - 1258 registros processados

20:10:15 - Execução finalizada
```

## ✅ Testes

O projeto possui testes automatizados utilizando pytest.

Para executar:

```bash
pytest
```

## 🔮 Roadmap

- Interface Web
- API REST
- Processamento paralelo
- Banco de dados
- Dashboard de monitoramento
- Docker
- Integração com filas de mensagens

## 📜 Licença

Projeto desenvolvido para fins educacionais e demonstração de arquitetura de software e automação corporativa.