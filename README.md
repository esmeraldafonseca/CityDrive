# CityDrive — Trabalho Prático 4

**Professor:** Engº Sebilson Cristóvão  
**Função:** Project Manager

Aplicação de reserva de viaturas desenvolvida em Python, Flet e MySQL.

## Cenário

Um utilizador encontra-se numa cidade, por exemplo Castelo Branco, e pretende reservar uma viatura para um determinado período. A aplicação deverá apresentar as viaturas disponíveis, a estação onde cada uma se encontra e o horário de funcionamento da estação.

Exemplo:

```text
Reserva existente: 06:30 → 12:00
Nova reserva:       12:00 → 15:00  ✓ permitida
Nova reserva:       11:00 → 13:00  ✗ conflito
```

## Arquitetura

```text
Flet View
   ↓
Service
   ↓
Repository
   ↓
Database
   ↓
MySQL
```

A estrutura está fornecida e não deve ser substituída sem justificação técnica.

## Estado inicial

A interface e a navegação estão parcialmente construídas. Algumas operações possuem exemplos completos.

Os métodos marcados com `TODO` são propositadamente incompletos e constituem o núcleo do Trabalho Prático 4.

## Instalação no Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Base de dados

Executar:

```text
database/citydrive.sql
```

O script cria apenas a estrutura da base de dados e não contém dados de negócio.

## Execução

```powershell
python main.py
```

## Documentação

- `docs/REGRAS_NEGOCIO.md`
- `docs/MAPA_TODOS.md`
- `docs/GUIA_PROFESSOR.md`


## Versão de Flet usada no projeto

Este projeto foi atualizado para a API do Flet 0.86.5.

Depois de ativar o ambiente virtual, recomenda-se:

```powershell
python -m pip install -r requirements.txt
python main.py
```

Na API atual do Flet são utilizadas classes como:

```python
ft.Border.all(...)
ft.Padding.symmetric(...)
ft.Alignment.CENTER
```

em vez das antigas formas em minúsculas.
