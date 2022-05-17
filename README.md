# Poetry Demo

This demonstrates a Poetry Project as a CLI, with a local library for modularity.

## Installing the CLI

```
python -mvenv .venv
source .venv/bin/activate
pip install git+https://github.com:cnuss/poetry-demo.git
./.venv/bin/poetry-demo
```

## Developing the CLI

### Running

```
poetry run poetry-demo
```

### In VSCode

```
poetry config virtualenvs.in-project true
poetry shell
code .
```

### Testing

```
poetry install
poetry run pytest
```

Then, select the right Intrepeter on the bottom right in the blue bar.

## Changing Dependencies

```
poetry add cryptography
poetry remove cryptography
```
