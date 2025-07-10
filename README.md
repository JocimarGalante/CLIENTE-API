# Desafio Python - API de Clientes

## 📌 1.1 Objetivo

Este desafio tem por objetivo medir as capacidades técnicas para requisitos de back-end utilizando Python com FastAPI e SQLAlchemy.

---

## ⚙️ 1.2 Stack Tecnológica

- **FastAPI** (framework web)
- **SQLAlchemy** (ORM)
- **Pydantic** (validação e DTOs)
- **Requests** (integração com API externa)
- **Banco de dados**: SQLite, PostgreSQL ou outro relacional

---

## 🧠 1.3 Nível

**Intermediário** – Capacidade de interpretar os requisitos do cliente e implementar uma API RESTful utilizando Python com boas práticas de código, DTOs e integração com serviços externos.

---

## 📋 1.4 Problema

Criar uma solução em Python para permitir o **cadastramento, consulta, exclusão, listagem, pesquisa e alteração de Clientes**, seguindo a modelagem abaixo:

### 📦 Modelagem sugerida

#### 🧍 Cliente
- `Id`: int
- `Nome`: string
- `DataCadastro`: string

#### 🏠 Endereço
- `Cep`: string
- `Logradouro`: string
- `Cidade`: string
- `Numero`: string
- `Complemento`: string

#### ☎️ Contato
- `Id`: int
- `Tipo`: string (ex: celular, email)
- `Texto`: string (ex: número ou email)

### 🔗 Relacionamento

- Cliente tem **um endereço**
- Cliente pode ter **vários contatos**

---

## 📌 Regras de Negócio

- 🔄 **Consulta automática do endereço pelo CEP**:  
  Ao receber o CEP do cliente, deve-se consultar a API do **ViaCEP** (ou similar) para adquirir os dados de `logradouro` e `cidade`, salvando automaticamente no banco.

---

## 🛠️ Requisitos Técnicos

É necessário implementar:

- [x] API RESTful
- [x] Uso de DTOs com **Pydantic**
- [x] Conversão entre DTO e model com **Mapper**
- [x] ORM utilizando **SQLAlchemy**

---

## 🧪 Testes

A API pode ser testada com ferramentas como:

- [Postman](https://www.postman.com/)
- [Insomnia](https://insomnia.rest/)
- Ou diretamente pela **Swagger UI**:  
  Acesse [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

