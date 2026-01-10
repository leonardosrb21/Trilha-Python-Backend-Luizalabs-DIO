
# 🏦 Sistema Bancário Simples em Python

Este é um sistema bancário desenvolvido em Python com interface via linha de comando (CLI). O projeto simula operações essenciais de um banco, como depósitos, saques, emissão de extratos e gerenciamento de usuários e contas correntes.

## 🚀 Funcionalidades

O sistema está dividido em módulos lógicos para facilitar a manutenção e leitura:

* **Operações Financeiras:**
* `Depositar`: Adiciona valores ao saldo da conta.
* `Sacar`: Permite retiradas respeitando o saldo disponível, o limite por saque e a quantidade máxima de saques diários.
* `Extrato`: Exibe todas as movimentações e o saldo atual formatado.


* **Gestão de Clientes:**
* `Novo Usuário`: Cadastra clientes com nome, data de nascimento, CPF e endereço.
* `Nova Conta`: Vincula uma conta corrente (agência e número) a um usuário cadastrado via CPF.
* `Listar Contas`: Exibe todas as contas criadas no sistema.



---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Bibliotecas:** `textwrap` (para formatação de menus e textos).

---

## 📋 Regras de Negócio

Para garantir o funcionamento correto, o sistema segue algumas diretrizes:

| Regra | Descrição |
| --- | --- |
| **Limite de Saques** | O usuário pode realizar no máximo 3 saques por sessão/dia. |
| **Valor Máximo** | Cada saque individual não pode exceder R$ 500,00. |
| **Identificação** | Não é permitido cadastrar dois usuários com o mesmo CPF. |
| **Vínculo** | Uma conta só pode ser criada se o CPF informado pertencer a um usuário já cadastrado. |

---

## ⚙️ Como Executar

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Clone este repositório ou copie o arquivo `.py`.
3. Abra o terminal na pasta do arquivo e execute:
```bash
python nome_do_arquivo.py

```



---

## 🧩 Estrutura do Código

O código utiliza conceitos avançados de funções em Python:

* **Argumentos Keyword-Only:** Utilizados na função de saque para maior segurança.
* **Argumentos Positional-Only:** Utilizados na função de depósito e extrato.
* **Tratamento de Exceções:** Proteção contra entradas de dados inválidas (letras em campos numéricos).

---

> **Nota:** Este projeto foi desenvolvido para fins didáticos, explorando estruturas de dados como listas e dicionários.

