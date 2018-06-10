FROM registry.fedoraproject.org/fedora-minimal:28

ARG BUILDID=unknown
ARG REPO_SLUG=unknown/unknown

# Updates and pipenv
RUN microdnf update -y && \
    microdnf -y install pipenv which make && \
    microdnf clean all

LABEL io.openshift.build.source-location=https://travis-ci.org/$REPO_SLUG/builds/$BUILDID
ENV LANG en_US.UTF-8
EXPOSE 8080

# Code and install pipenv
ADD . /code
WORKDIR /code

# Install dependencies
RUN pipenv install --system --deploy

ENTRYPOINT ["make"]
CMD ["run"]
