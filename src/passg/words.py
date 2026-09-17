import pathlib
import urllib.request

WORD_LIST_PATH = pathlib.Path.home() / ".cache" / "passg" / "word_list"
URL_PATH = pathlib.Path.home() / ".cache" / "passg" / "url"


def fetch_word_list(url: str) -> None:
    """
    Fetch and cache the EFF Large Word List.
    """
    request = urllib.request.Request(
        url, headers={"User-Agent": "Passg-Diceware-Generator"}
    )

    WORD_LIST_PATH.parent.mkdir(parents=True, exist_ok=True)
    URL_PATH.parent.mkdir(parents=True, exist_ok=True)

    try:
        with (
            urllib.request.urlopen(request) as response,
            WORD_LIST_PATH.open("wb") as file,
        ):
            file.write(response.read())

        with URL_PATH.open("w") as file:
            file.write(url)
    except Exception:
        print(f"Failed to fetch word list from '{url}'.")
        raise


def get_word_list(url: str) -> list[str]:
    """
    Get the word list from the cache or fetch it if it doesn't exist.
    """
    if not URL_PATH.is_file():
        fetch_word_list(url)
    else:
        with URL_PATH.open("r") as file:
            cached_url = file.read()
        if cached_url != url:
            fetch_word_list(url)

    with WORD_LIST_PATH.open("r") as file:
        list = file.read().splitlines()

    result: list[str] = []
    for item in list:
        _, word = item.split(sep="\t", maxsplit=1)
        result.append(word)

    return result
