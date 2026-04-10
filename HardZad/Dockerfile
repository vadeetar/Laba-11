# ========== Этап 1: Сборка Rust-расширения ==========
FROM rust:1.75-slim AS builder

WORKDIR /app

# Устанавливаем Python и maturin
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install maturin

# Копируем файлы для кэширования зависимостей
COPY Cargo.toml pyproject.toml ./
RUN mkdir src && echo "fn main() {}" > src/lib.rs
RUN maturin build --release

# Копируем реальный исходный код и пересобираем
COPY src ./src
RUN maturin build --release

# ========== Этап 2: Финальный образ ==========
FROM python:3.12-slim

# Устанавливаем curl для healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем собранное расширение из builder
COPY --from=builder /app/target/release/libmyapp.so /app/myapp.so
COPY app.py requirements.txt /app/

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Настройка non-root пользователя
RUN useradd -m -s /bin/bash appuser && chown -R appuser /app
USER appuser

# Переменные окружения
ENV PORT=8000
ENV APP_ENV=production

# Healthcheck
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT}/health || exit 1

EXPOSE 8000

CMD ["python", "app.py"]