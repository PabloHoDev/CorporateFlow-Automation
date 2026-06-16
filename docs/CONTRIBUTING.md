# CONTRIBUTING.md

# Guia de Contribuição

Obrigado pelo interesse em contribuir com o CorporateFlow Automation.

Este projeto busca manter um padrão consistente de qualidade e organização.

---

# Fluxo de Trabalho

1. Criar uma branch para a funcionalidade.
2. Implementar as alterações.
3. Adicionar ou atualizar testes.
4. Atualizar a documentação quando necessário.
5. Abrir um Pull Request.

---

# Padrão de Commits

Utilizar mensagens claras seguindo uma convenção consistente.

Exemplos:

```text
feat: adiciona BackupService

fix: corrige leitura de arquivos Excel

refactor: reorganiza estrutura do pipeline

docs: atualiza documentação da arquitetura

test: adiciona testes para normalizadores
```

---

# Regras Gerais

* Respeitar a arquitetura definida em `ARCHITECTURE.md`.
* Evitar código duplicado.
* Manter responsabilidade única por classe.
* Não introduzir dependências sem justificativa técnica.
* Registrar decisões arquiteturais relevantes por meio de ADRs.

---

# Pull Requests

Antes de abrir um Pull Request, verificar:

* [ ] O código compila corretamente.
* [ ] Os testes existentes continuam passando.
* [ ] Novas funcionalidades possuem testes quando aplicável.
* [ ] A documentação foi atualizada.
* [ ] Não existem arquivos temporários ou artefatos desnecessários.

---

# Filosofia do Projeto

O objetivo do CorporateFlow Automation é servir como uma base reutilizável para automação corporativa, priorizando clareza, modularidade, manutenibilidade e escalabilidade.

Toda contribuição deve preservar esses princípios.
