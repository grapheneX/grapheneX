FROM alpine:latest
LABEL maintainer="graphenex.project@protonmail.com"

ENV LC_ALL=C.UTF-8

RUN echo "**** Installing Python ****" && \
    apk add --no-cache python3 python3-dev  && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** Installing pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
	if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi
RUN apk add --no-cache curl \
	tar \
	gcc \
	libc-dev

# Fetching repository
RUN VERSION=$(curl --silent "https://api.github.com/repos/graphenex/grapheneX/releases/latest" | \
    grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/') && \
    curl -LO https://github.com/grapheneX/grapheneX/archive/$VERSION.tar.gz && \
	tar -xzf $VERSION.tar.gz && \
	cd "grapheneX-$VERSION" && \
	python3 setup.py install

CMD ["/bin/sh", "-c", "grapheneX"]

# For two
# FROM alpine:latest

# WORKDIR /root/
# COPY --from=builder /usr/bin/grapheneX .

# CMD ["./grapheneX"]
