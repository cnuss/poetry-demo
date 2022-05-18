# Poetry Demo

This demonstrates a Poetry Project installed ad a script, with a local library for modularity.

Secret Sauce:

- `packages = [...]` defined in [pyproject.toml](./pyproject.toml)
  - so modular libraries can be defined
- a [requirements.txt](./requirements.txt) that references `./`
  - so a `pip install` works
- `[tool.poetry.scripts]` in [pyproject.toml](./pyproject.toml)
  - creates a `poetry-demo` bin-link on `pip install`

## Requires

- Python 3.9+
  - Enforced by `python = "^3.9"` in [pyproject.toml](./pyproject.toml)
- Poetry
  - Auto-installed using `install_requires` in [setup.cfg](./setup.cfg)

## Installing the script

```
python -mvenv .venv
source .venv/bin/activate
pip install git+https://github.com/cnuss/poetry-demo
./.venv/bin/poetry-demo
```

Secret sauce:

- a [requirements.txt](./requirements.txt) that references `./`
- `[tool.poetry.scripts]` in [pyproject.toml](./pyproject.toml)

### Without venvs, in docker...

```
docker run -it python:3.9-slim bash
apt-get update && apt-get install -y git
pip install git+https://github.com/cnuss/poetry-demo
```

Then run the installed script globally:

```
poetry-demo
```

## Developing

First, install poetry:

```
pip install poetry
```

### Running

```
poetry install
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
