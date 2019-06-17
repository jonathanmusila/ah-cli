import sys
import requests
import click

from halo import Halo

spinner = Halo(text='Loading', spinner='dots', text_color='magenta')
url = "https://ah-django-staging.herokuapp.com/api"


@click.group()
def main():
    """
        Simple CLI for consuming Authors Haven App
    """
    pass


@main.command()
@click.argument("slug")
def get(slug):
    """
        This return a particular article from the given slug on Authors Haven API
    """
    url_format = url + "/articles/{}/"
    click.echo(slug)

    spinner.start()
    response = requests.get(url_format.format(slug))
    spinner.stop()
    spinner.clear()
    if response.status_code == 404:
        spinner.warn("Not found ❎")
        click.echo("Status code: {}".format(response.status_code))
    elif response.status_code == 200:
        spinner.succeed("Article found ✅")
        click.echo("Status code: {}".format(response.status_code))
        click.echo(response.json())


if __name__ == "__main__":
    main()
