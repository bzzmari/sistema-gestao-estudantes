# 🎓 Sistema de Gestão de Estudantes

Projeto desenvolvido em **Python**, com o objetivo de implementar um sistema de gerenciamento de estudantes utilizando programação orientada a objetos, modularização, manipulação de arquivos e armazenamento de dados.

O sistema funciona por meio de um menu interativo no terminal, permitindo cadastrar, consultar, remover, importar e exportar estudantes.

## 🚀 Funcionalidades

- **Cadastrar estudantes:** permite registrar ID, nome, nota e turma.
- **Listar estudantes:** apresenta todos os estudantes cadastrados.
- **Remover estudantes:** permite excluir um estudante utilizando seu ID.
- **Registrar operações:** armazena temporariamente as ações realizadas em um buffer.
- **Salvar histórico:** grava as operações em um arquivo `operations.log`, incluindo data e hora.
- **Exportar estudantes:** salva os dados em um arquivo binário `students.pkl`.
- **Importar estudantes:** recupera os dados previamente exportados.
- **Menu interativo:** permite navegar pelas funcionalidades diretamente no terminal.

## 🛠️ Tecnologias utilizadas

- Python 3
- Programação Orientada a Objetos (POO)
- Biblioteca `pickle`
- Biblioteca `datetime`
- Manipulação de arquivos TXT e PKL
- Git e GitHub
- Visual Studio Code

## 📁 Estrutura do projeto

```text
sistema-gestao-estudantes/
│
├── student.py
├── student_service.py
├── student_register.py
└── README.md
```

### Descrição dos arquivos

**student.py**

Contém a classe `Student`, responsável por representar os estudantes e seus atributos.

**student_service.py**

Contém as funções responsáveis pelo cadastro, listagem, remoção, armazenamento, importação e exportação dos estudantes.

**student_register.py**

Contém o menu principal e realiza a integração com as funções do sistema.

## ▶️ Como executar

**1. Clone o repositório:**

```bash
git clone https://github.com/bzzmari/sistema-gestao-estudantes.git
```

**2. Entre na pasta do projeto:**

```bash
cd sistema-gestao-estudantes
```

**3. Execute o programa:**

No Windows:

```bash
py student_register.py
```

Ou, em ambientes que utilizam o comando `python3`:

```bash
python3 student_register.py
```

## 💻 Menu do sistema

```text
--- Sistema de Gestão de Estudantes ---

1: Registar Estudante
2: Listar Estudantes
3: Remover Estudante
4: Guardar Histórico (Buffer)
5: Exportar Estudantes (.pkl)
6: Importar Estudantes (.pkl)
0: Sair

Escolha uma opção:
```

## 💾 Armazenamento dos dados

O sistema utiliza dois mecanismos de armazenamento.

**Histórico de operações (`operations.log`)**

Registra as operações realizadas, incluindo data e hora.

Exemplo:

```text
[2026-10-26 14:30:00] Student registered: Maria
[2026-10-26 14:35:00] Student removed: João
```

**Dados dos estudantes (`students.pkl`)**

Armazena os objetos dos estudantes por meio da biblioteca `pickle`, permitindo recuperar os registros posteriormente.

O arquivo deve ser importado apenas de fontes confiáveis.

## 📚 Conceitos aplicados

Este projeto permite praticar:

- Classes e objetos
- Funções e modularização
- Listas e estruturas de repetição
- Estruturas condicionais
- Entrada e saída de dados
- Tratamento de exceções
- Persistência de dados
- Serialização e desserialização
- Controle de versão com Git

## 👩‍💻 Repositório

[GitHub — Sistema de Gestão de Estudantes](https://github.com/bzzmari/sistema-gestao-estudantes)

---

**Projeto acadêmico desenvolvido para fins de aprendizagem e prática de programação em Python.**
