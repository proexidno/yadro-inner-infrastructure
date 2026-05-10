FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-venv

WORKDIR /app

RUN python3 -m venv .venv
ENV PATH="/app/.venv/bin:$PATH"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY status.py .

ENTRYPOINT ["python3", "status.py"]
CMD ["https://httpstat.us/"]
