# Лабораторная работа №11 – Контейнеризация мультиязычных приложений

**Студент:** Тарасов Вадим Романович  
**Группа:** 221131  
**Вариант:** 8  

## Цель
Освоить multi-stage сборку, healthcheck, named volumes, кэширование зависимостей, автоматическое обновление (watchtower).

## Быстрый запуск
```bash
# MidZad – обмен данными через том
cd MidZad && docker compose up --build

# HardZad – Rust+Python
cd HardZad && docker build -t hardzad . && docker run -p 8000:8000 hardzad

# Watchtower – автообновление (отдельно)
cd watchtower && docker compose up -d