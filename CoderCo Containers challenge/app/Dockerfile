FROM python:3.8-slim
WORKDIR /app
# Install runtime Python dependencies
RUN pip install flask redis
# Copy application code
COPY . .
EXPOSE 5002
CMD ["python", "count.py"]
