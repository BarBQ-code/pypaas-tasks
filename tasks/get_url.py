import requests
from pypaas import task


@task
def get_url(url: str):
    print(f'I am get requesting this url: {url}')
    requests.get(url)
