FROM python:3.11-slim

# environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set working directory
WORKDIR /app

# install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    git \
    nano \
    curl \
    && rm -rf /var/lib/apt/lists/*

# copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy code
COPY . .

# expose port
EXPOSE 8000

# start app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
