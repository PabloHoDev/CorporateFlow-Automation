# Validator Protocol

* **Status:** 🟡 Em elaboração
* **Módulo:** `src/interfaces/validator.py`
* **Categoria:** Interface

---

# Objetivo

O `Validator Protocol` define o contrato comum para componentes responsáveis por validar estruturas, dados ou regras de negócio.

---

# Responsabilidade

Padronizar a forma como validações são executadas na aplicação, garantindo comportamento consistente entre diferentes validadores.

---

# Responsabilidades dentro do escopo

* Definir um contrato único para validadores.
* Permitir substituição de implementações.
* Facilitar composição de múltiplas validações.
* Favorecer testes automatizados.

---

# Responsabilidades fora do escopo

A interface **não deve**:

* Implementar validações concretas.
* Persistir informações.
* Produzir efeitos colaterais.

---

# Métodos previstos

## validate()

Recebe um objeto de entrada e executa sua validação.

O método poderá:

* retornar sucesso;
* retornar um resultado estruturado;
* lançar exceções específicas quando aplicável.

---

# Classes implementadoras previstas

* SchemaValidator
* BusinessValidator

---

# Princípios SOLID aplicados

## Dependency Inversion Principle (DIP)

Os consumidores dependem do contrato de validação e não das implementações concretas.

---

## Liskov Substitution Principle (LSP)

Qualquer implementação deverá poder substituir outra sem alterar o comportamento esperado pelo consumidor.

---

# Observações arquiteturais

A interface deve permanecer simples e focada apenas na definição do comportamento esperado para componentes de validação.
