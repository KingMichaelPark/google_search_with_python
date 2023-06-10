# Search Google with Python

A quick example of how to search Google using
their API.

## Requirements

Httpx for http and typer for the CLI for convenience.

```bash
pip install -r requirements.txt
```

You will need a search engine id and an API key.

- [API Key](https://developers.google.com/custom-search/v1/introduction)
- [Search Engine ID](https://programmablesearchengine.google.com/controlpanel/all)

Add those to your environment.

```bash
export API_KEY=YOUR_API_KEY
export SEARCH_ENGINE_ID=YOUR_SEARCH_ENGINE_ID
```

## Running

```bash
python main.py "your search"
```
