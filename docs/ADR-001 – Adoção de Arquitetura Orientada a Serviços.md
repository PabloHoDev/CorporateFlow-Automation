# ADR-001 – Adoção de Arquitetura Orientada a Serviços

* **Status:** Aceito
* **Data:** 16/06/2026

## Contexto

O CorporateFlow Automation foi concebido para automatizar diferentes processos corporativos baseados em arquivos estruturados, como planilhas Excel e arquivos CSV.

A solução deverá ser facilmente reutilizável em novos cenários de negócio, permitindo a inclusão de novas funcionalidades sem comprometer a estabilidade das implementações existentes.

Uma arquitetura excessivamente centralizada tenderia a concentrar responsabilidades, dificultando manutenção, testes automatizados e evolução do sistema.

## Decisão

Foi adotada uma arquitetura orientada a serviços (*Service-Oriented Design*), na qual cada componente possui responsabilidade bem definida e atua de forma independente.

Cada serviço executa apenas uma função específica, como:

* leitura de planilhas;
* criação de backups;
* geração de relatórios;
* manipulação de arquivos;
* registro de logs.

A coordenação desses serviços é realizada pelo `Orchestrator`, responsável apenas por organizar o fluxo de execução, sem conter regras de negócio.

## Consequências

### Benefícios

* Maior separação de responsabilidades.
* Redução do acoplamento entre módulos.
* Facilidade para manutenção.
* Facilidade para criação de testes unitários.
* Maior reutilização de componentes.
* Inclusão simplificada de novas funcionalidades.

### Trade-offs

* Aumento inicial na quantidade de arquivos e classes.
* Necessidade de maior disciplina arquitetural.
* Curva de aprendizado ligeiramente maior para novos colaboradores.

## Alternativas consideradas

### Arquitetura Monolítica com lógica centralizada

Rejeitada por concentrar múltiplas responsabilidades em poucos componentes, aumentando o acoplamento e dificultando evolução.

### Arquitetura baseada apenas em funções utilitárias

Rejeitada por limitar a escalabilidade do projeto e reduzir a clareza sobre responsabilidades de cada módulo.

## Justificativa

A arquitetura orientada a serviços oferece um equilíbrio entre simplicidade, modularidade e escalabilidade, sendo adequada para aplicações corporativas que precisam evoluir continuamente sem comprometer a qualidade do código.

Essa decisão está alinhada com princípios como:

* Single Responsibility Principle (SRP);
* Separation of Concerns;
* Modularidade;
* Reutilização;
* Testabilidade.
