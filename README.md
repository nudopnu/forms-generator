# Forms Generator 📝

- This project is in a very early stage -

The idea is to dynamically generate nice looking forms from [Pydantic BaseModels](https://docs.pydantic.dev/latest/api/base_model/).

## Setup

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

## Usage

The `main.py` contains a sample to experiment with.

```
python main.py
```

# Roadmap

- [ ] front-end validation (probably with [jsonschema](https://www.jsdelivr.com/package/npm/jsonschema))
- [ ] add ability to add restful API endpoints (probably via [FastAPI](https://fastapi.tiangolo.com/))
- [ ] communicate back exceptions from server