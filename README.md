# nshm-api

Root project for all NSHM APIs (Korora, Toshi, Solvis).
Includes the shared API Gateway configuration.
contains core features like NSHM logic tree.

Using Flask with Serverless framework to operate as a AWS Lambda API.

The API documentation is served by default from the service root.

## Getting started

```
poetry install
npm install --save-dev serverless
npm install --save-dev serverless-domain-manager
npm install --save-dev serverless-python-requirements
npm install --save-dev serverless-wsgi
```

### Run full stack locally
```
SLS_OFFLINE=1 npx serverless wsgi serve
```

### Unit tests

`poetry run pytest`

**TESTING** overrides **SLS_OFFLINE** to keep moto mockling happy
