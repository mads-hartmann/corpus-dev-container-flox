# Flox Devcontainer Corpus

This tiny repository is a corpus case for devcontainer setup evaluation. It already
uses Flox to describe the development environment, but it does not include a
devcontainer.

## Flox workflow

```sh
flox activate
make check
make run
```

The Flox environment also defines a `web` service:

```sh
flox services start web
```

The service listens on `0.0.0.0:8000` by default and exposes `/healthz` for
health checks.
