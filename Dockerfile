FROM registry.fedoraproject.org/fedora:28

ARG BUILDID=unknown
ARG REPO_SLUG=unknown/unknown

LABEL io.openshift.build.source-location=https://travis-ci.org/$REPO_SLUG/builds/$BUILDID

# Updates and pipenv
RUN dnf update -y && \
    dnf -y install pipenv which && \
    dnf clean all


ENV LANG en_US.UTF-8
EXPOSE 8080

# Code and install pipenv
ADD . /code
WORKDIR /code

# Make tests executable
RUN chmod +x tests/run.sh
# Install dependencies
RUN pipenv install --system --deploy

CMD ["python3", "server.py"]
