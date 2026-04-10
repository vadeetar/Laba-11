# ========== ЭТАП 1: СБОРКА RUST-РАСШИРЕНИЯ ==========
FROM rust:1.75-slim AS builder

WORKDIR /app

# Устанавливаем Python и maturin
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install maturin

# Копируем только файлы с зависимостями (для кэширования)
COPY Cargo.toml pyproject.toml ./

# Создаём фиктивный src/lib.rs, чтобы cargo собрал зависимости
RUN mkdir src && echo "fn main() {}" > src/lib.rs && \
    maturin build --release && \
    rm -rf src

# Теперь копируем реальный исходный код и пересобираем только его
COPY src ./src
RUN maturin build --release

# ========== ЭТАП 2: ФИНАЛЬНЫЙ ОБРАЗ ==========
FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем собранное расширение из builder
COPY --from=builder /app/target/release/libmyapp.so /app/myapp.so
COPY app.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Добавляем PYTHONPATH, чтобы Python видел модули
ENV PYTHONPATH=/app

# Non-root пользователь
RUN useradd -m -s /bin/bash appuser && chown -R appuser /app
USER appuser

ENV PORT=8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT}/health || exit 1

EXPOSE 8000

CMD ["python", "app.py"]