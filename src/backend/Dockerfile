FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


RUN echo '#!/bin/bash\n\
set -m\n\
python run.py &\n\
sleep 5\n\
python db_init.py || true\n\
fg %1\n\
' > /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]