
FROM python:3.7

ENV INSTALL_PATH /personal-tracker
RUN mkdir -p ${INSTALL_PATH}
WORKDIR ${INSTALL_PATH}

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
RUN mkdir -p data/db
