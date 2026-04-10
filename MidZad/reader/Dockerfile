FROM python:3.12-slim
WORKDIR /app
COPY read.py .
CMD ["python", "read.py"]
# ... существующий код (FROM, WORKDIR, COPY, CMD) ...
# Добавить в самом конце:

HEALTHCHECK --interval=5s --timeout=3s --retries=3 \
    CMD test -f /data/shared.txt || exit 1