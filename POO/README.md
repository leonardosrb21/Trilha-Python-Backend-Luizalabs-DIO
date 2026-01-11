

# Refatoração do Sistema Bancário em Python (POO)

Este documento descreve as alterações realizadas no código do sistema bancário para alinhá-lo às práticas modernas de desenvolvimento em Python, mantendo a lógica de negócio e a estrutura original solicitada.

## 1. Atualização de Métodos Abstratos (Módulo `abc`)

No código original, foram utilizados os decoradores `abstractclassmethod` e `abstractproperty`. Estes decoradores estão **obsoletos (deprecated)** desde o Python 3.3.

**O que foi feito:**
Atualizamos para a sintaxe moderna, onde empilhamos os decoradores. Isso garante compatibilidade com versões recentes do Python e melhor suporte de ferramentas de análise de código (linters).

* **Propriedade Abstrata:**
```python
@property
@abstractmethod
def valor(self):
    pass

```


* **Método de Classe Abstrato:**
```python
@classmethod
@abstractmethod
def registrar(cls, conta):
    pass

```



---

## 2. Aplicação de Pilares de POO

O código reforça os quatro pilares da Programação Orientada a Objetos:

### A. Herança

As classes `PessoaFisica` herda de `Cliente`, e `ContaCorrente` herda de `Conta`. Isso permite o reuso de código e a especialização de comportamentos.

### B. Encapsulamento

Atributos sensíveis como `_saldo`, `_numero` e `_historico` foram mantidos com o prefixo `_`, indicando que são protegidos. O acesso a eles é feito de forma controlada através de `@property` (Getters).

### C. Polimorfismo

A função `realizar_transacao` do `Cliente` demonstra polimorfismo, pois aceita qualquer objeto que seja uma subclasse de `Transacao` (seja `Saque` ou `Deposito`), chamando o método `.registrar()` de forma genérica.

### D. Abstração

A classe `Transacao` foi definida como uma **ABC (Abstract Base Class)**, funcionando como uma interface (contrato) que obriga qualquer nova transação a implementar os métodos `valor` e `registrar`.

---

## 3. Boas Práticas e Estilo (PEP 8)

Foram aplicadas melhorias na organização visual para seguir o guia de estilo oficial do Python:

* **Espaçamento:** Adição de duas linhas em branco entre classes e uma linha entre métodos, facilitando a leitura.
* **Bloco `main`:** Inclusão do `if __name__ == "__main__":` para garantir que o script só seja executado quando chamado diretamente, uma prática essencial para modularização.
* **Correção de Nomenclatura:** Na função `menu`, alteramos a variável interna de `menu` para `menu_text` para evitar conflito de nomes com a própria função.

---

## 4. Ajustes de Data e Hora

No método `adicionar_transacao` da classe `Historico`, o formato de data foi ajustado:

* De: `%d-%m-%Y %H:%M:%s` (o `%s` é frequentemente inconsistente entre sistemas operacionais).
* Para: `%d-%m-%Y %H:%M:%S` (Segundos em formato padrão).

---

## Como Executar

1. Certifique-se de ter o Python 3.8 ou superior instalado.
2. Salve o código em um arquivo `.py`.
3. Execute via terminal: `python nome_do_arquivo.py`.

