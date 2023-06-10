import json
import os
from pathlib import Path

import httpx
import typer


def main(search: str):
    api_key = os.environ.get("API_KEY")
    cx = os.environ.get("SEARCH_ENGINE_ID")
    if any(x is None for x in [search, api_key, cx]):
        print("You need an API_KEY and SEARCH_ENGINE_ID in your environment vars")
        exit()

    url = "https://customsearch.googleapis.com/customsearch/v1"
    response: httpx.Response = httpx.get(
        url,
        headers={"Accept": "application/json"},
        params={
            "key": api_key,
            "q": search,
            "cx": cx,
        },
    )
    print(f"Request for '{search}' returned {response.status_code}")
    if response.status_code <= 204:
        with Path("results.json").open("w") as f_out:
            json.dump(response.json(), f_out, indent=4)


if __name__ == "__main__":
    typer.run(main)
