FROM registry.fedoraproject.org/fedora-minimal:28

# Updates and pipenv
RUN microdnf update -y && \
    microdnf -y install pipenv which make && \
    microdnf clean all

# Set Openshift label
ARG BUILDID=unknown
ARG REPO_URL=unknown/unknown
LABEL io.openshift.build.source-location=$REPO_URL/-/jobs/$BUILDID

# Set LANG for pipenv
ENV LANG en_US.UTF-8

# Expose port
EXPOSE 8080

# Code and install pipenv
ADD . /code
WORKDIR /code

# Install dependencies
RUN pipenv install --system --deploy

# Use makefile for jobs
ENTRYPOINT ["make"]
CMD ["run"]
