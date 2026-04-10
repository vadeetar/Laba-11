FROM python:3.12-slim
WORKDIR /app
COPY write.py .
CMD ["python", "write.py"]
# ... существующий код (FROM, WORKDIR, COPY, CMD) ...
# Добавить в самом конце:

HEALTHCHECK --interval=5s --timeout=3s --retries=3 \
    CMD test -f /data/shared.txt || exit 1