# Builder stage
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt ./
RUN pip install --user --no-cache-dir -r requirements.txt

COPY . /app

# Final minimal image
FROM python:3.11-alpine

WORKDIR /app

# Install runtime dependencies
RUN apk add --no-cache libstdc++ gcc musl-dev

# Create non-root user
RUN adduser -D -u 10001 kopfuser

# Copy installed Python packages from builder
COPY --from=builder /root/.local /home/kopfuser/.local
ENV PATH=/home/kopfuser/.local/bin:$PATH

# Copy only necessary files
COPY --from=builder /app /app

USER kopfuser

EXPOSE 9090

CMD ["sh", "-c", "kopf run memory_exporter.py ${KOPF_ARGS} --verbose"]
