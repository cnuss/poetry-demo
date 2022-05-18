# Poetry Demo

This demonstrates a Poetry Project as a CLI, with a local library for modularity.

## Requires

- Python 3.9+
  - Enforced by `python = "^3.9"` in [pyproject.toml](./pyproject.toml)
- Poetry
  - Auto-installed using `install_requires` in [setup.cfg](./setup.cfg)

## Installing the CLI

```
python -mvenv .venv
source .venv/bin/activate
pip install git+https://github.com/cnuss/poetry-demo
./.venv/bin/poetry-demo
```

Secret sauce:

- a [requirements.txt](./requirements.txt) that references `./`
- `[tool.poetry.scripts]` in [pyproject.toml](./pyproject.toml)

## Developing the CLI

### Running

```
poetry run poetry-demo
```

Secret sauce:

- `[tool.poetry.scripts]` in [pyproject.toml](./pyproject.toml)

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
