FROM python:3.9

RUN mkdir -p /service
WORKDIR /service

COPY . /service

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN  ln -s /root/.poetry/bin/poetry /usr/bin/poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 5010

CMD ["python", "main.py"]