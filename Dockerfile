FROM nginx/unit:1.22.0-python3.9

ENV PYTHONDONTWRITEBYTECODE 1

COPY Pipfile .
COPY Pipfile.lock .
RUN add-apt-repository ppa:pypa/ppa                                           \
    && apt-get update                                                         \
    && apt install -y pipenv                                                  \
    && PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy                       \
    && apt remove -y pipenv                                                   \
    && apt autoremove --purge -y                                              \
    && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list

