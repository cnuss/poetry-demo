# Poetry Demo

This demonstrates a Poetry Project as a CLI

## Installing the CLI

```
python -mvenv .venv
source .venv/bin/activate
pip install git+git@github.com:cnuss/poetry-demo.git
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

Then, select the right Intrepeter on the bottom right in the blue bar.

## Changing Dependencies

```
poetry add cryptography
poetry remove cryptography
```
