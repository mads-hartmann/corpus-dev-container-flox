FROM mcr.microsoft.com/devcontainers/base:2.0.4-noble

# Install Flox. This repository describes its dev environment in .flox, so Flox
# must be present for environments to build, install dependencies, and run the
# `web` service reproducibly. Installing the package bakes the /nix store it
# ships into the image, so prebuilt environments start without downloading Nix.
RUN wget -qO - https://downloads.flox.dev/by-env/stable/deb/flox-archive-keyring.gpg \
      | tee /usr/share/keyrings/flox-archive-keyring.gpg >/dev/null \
    && echo "deb [signed-by=/usr/share/keyrings/flox-archive-keyring.gpg] https://downloads.flox.dev/by-env/stable/deb/ stable/" \
      > /etc/apt/sources.list.d/flox.list \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" flox \
    && rm -rf /var/lib/apt/lists/*
