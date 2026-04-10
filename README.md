# Лабораторная работа №11 – Контейнеризация мультиязычных приложений

**Студент:** Тарасов Вадим Романович  
**Группа:** 221131  
**Вариант:** 8  

## Описание
Проект демонстрирует:
- Многоэтапную сборку Rust-расширения для Python с кэшированием зависимостей.
- Взаимодействие контейнеров через named volume с `depends_on` + `healthcheck`.
- Автоматическое обновление контейнеров через Watchtower.

## Быстрый запуск
```bash
# MidZad – обмен данными через том
cd MidZad && docker compose up --build

# HardZad – Rust + Python
cd HardZad && docker build -t hardzad . && docker run -p 8000:8000 hardzad

# Watchtower – автообновление
cd watchtower && docker compose up -d
