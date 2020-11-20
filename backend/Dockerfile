FROM python:3.9.0-buster

RUN apt update
RUN apt install postgresql libpq-dev python3-dev -y

RUN printf "I am running on ${BUILDPLATFORM:-linux/amd64}, building for ${TARGETPLATFORM:-linux/amd64}\n$(uname -a)\n"

COPY . ./

ENV PUB_KEY_PATH=server.pub PRIV_KEY_PATH=server.pem

RUN pip install -r requirements.txt && python utils/rsa.py server

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
