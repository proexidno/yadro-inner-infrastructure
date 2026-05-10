import requests
from requests.exceptions import ConnectionError, Timeout, RequestException
import sys


def handle_response(response: requests.Response):
    code = response.status_code
    body = response.text

    if code // 100 in (1, 2, 3):
        print(f"{code}: {body}")
    else:
        raise Exception(f"HTTP Error {code}: {body}")


def main():
    if len(sys.argv) < 2:
        print("Url of the service in first argument")
        return
    url = sys.argv[1]

    urls = [
        url + "200",
        url + "301",
        url + "404",
        url + "501",
        url + "201",
    ]

    for url in urls:
        try:
            resp = requests.get(url, timeout=10, allow_redirects=False)
            handle_response(resp)
        except ConnectionError as e:
            print(f"Error: Connection failed")
            exit(1)
        except Timeout:
            print(f"Error: Request timed out")
        except RequestException as e:
            print(f"Error: Request failed - {e}")
        except Exception as e:
            print(f"{e}")


if __name__ == "__main__":
    main()
