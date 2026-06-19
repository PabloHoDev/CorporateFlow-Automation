# Normalizer Protocol

* **Status:** 🟡 Em elaboração
* **Módulo:** `src/interfaces/normalizer.py`
* **Categoria:** Interface

---

# Objetivo

O `Normalizer Protocol` define o contrato comum para componentes responsáveis por padronizar ou transformar dados antes de seu processamento.

---

# Responsabilidade

Garantir que diferentes normalizadores compartilhem uma estrutura consistente de utilização e possam ser utilizados de forma intercambiável.

---

# Responsabilidades dentro do escopo

* Definir um contrato comum para normalizadores.
* Padronizar o processo de transformação de dados.
* Facilitar reutilização e testes.
* Reduzir acoplamento entre consumidores e implementações.

---

# Responsabilidades fora do escopo

A interface **não deve**:

* Implementar algoritmos de normalização.
* Persistir dados.
* Executar regras de negócio.

---

# Métodos previstos

## normalize()

Recebe um valor ou objeto de entrada e retorna sua representação normalizada.

O método não deve produzir efeitos colaterais externos.

---

# Classes implementadoras previstas

* TextNormalizer
* CityNormalizer

---

# Princípios SOLID aplicados

## Dependency Inversion Principle (DIP)

Os consumidores dependem da abstração e não das implementações concretas.

---

## Liskov Substitution Principle (LSP)

Qualquer normalizador deverá poder substituir outro que implemente o mesmo contrato.

---

# Observações arquiteturais

Implementações concretas devem concentrar exclusivamente a lógica de normalização correspondente ao seu domínio, mantendo a interface enxuta e estável ao longo da evolução da aplicação.
