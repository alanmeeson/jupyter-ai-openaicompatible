# jupyter_ai_openaicompatible

`jupyter_ai_openaicompatible` is a Jupyter AI module, a package
that registers additional model providers for the Jupyter AI
extension.

## Requirements

- Python 3.8 - 3.12
- JupyterLab 4

## Install

To install the extension, execute:

```bash
pip install jupyter_ai_openaicompatible
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall jupyter_ai_openaicompatible
```

## Contributing

### Development install

```bash
cd jupyter-ai-openaicompatible
pip install -e "."
```

### Development uninstall

```bash
pip uninstall jupyter_ai_openaicompatible
```

#### Backend tests

This package uses [Pytest](https://docs.pytest.org/) for Python testing.

Install test dependencies (needed only once):

```sh
cd jupyter-ai-openaicompatible
pip install -e ".[test]"
```

To execute them, run:

```sh
pytest -vv -r ap --cov jupyter_ai_openaicompatible
```
