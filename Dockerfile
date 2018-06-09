FROM registry.fedoraproject.org/fedora:28

# Updates and PIP
RUN dnf update -y && \
    dnf -y install pipenv which && \
    dnf clean all

# Code and install pipenv
ADD . /code
WORKDIR /code

# Install dependencies
ENV LANG en_US.UTF-8
RUN pipenv install --system --deploy

EXPOSE 8080

CMD ["python3", "server.py"]
