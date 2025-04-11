import requests as rq
from bs4 import BeautifulSoup
import argparse as arg
from rich import print
from rich.table import Table
import pandas as pd


def weather_scaping(city):
    page = rq.get(f"https://www.timeanddate.com/weather/india/{city}")

    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(class_="headline-banner__title").text.strip()

    details_div = soup.find(id="qlook")
    temp = details_div.find(class_="h2").text.strip()

    p = details_div.find("p").next_sibling.next_sibling
    feels = p.contents[0].strip().split(": ")[1]
    wind = p.contents[4].strip().split(": ")[1]

    table_div = soup.find(class_="table table--left table--inner-borders-rows")
    t_body = table_div.find("tbody").children

    table_div_details = {}
    for tr in t_body:
        content = tr.contents
        key = content[0].text.strip().rstrip(":")
        value = content[1].text.strip()
        table_div_details[key] = value

    weather_data = {
        "Place": title,
        "Temperature": temp,
        "Feels Like": feels,
        "Wind": wind,
        **table_div_details,
    }

    return weather_data


def display_weather(weather):
    table = Table(title="🌦 Weather Report")

    for key in weather:
        table.add_row(f"[cyan]{key}[/cyan]", f"[white]{weather[key]}[/white]")

    print(table)


def export_to_file(weather, filename):
    filetype = filename.split(".")[1]
    df = pd.DataFrame([weather])  # converting the normal dictionary into a list

    if filetype == "json":
        df.to_json(filename, indent=2, orient="records")
    elif filetype == "csv":
        df.to_csv(filename, index=False)


def main():
    parser = arg.ArgumentParser(description="🌀 Weather CLI for Indian cities")
    parser.add_argument(
        "-c",
        "--city",
        required=True,
        help="City name in lowercase (e.g. delhi, mumbai, dehradun)",
    )
    parser.add_argument(
        "-o", "--output", help="Filname to export (e.g. weather.json or weather.csv)"
    )

    args = parser.parse_args()

    print(f"[bold blue]📡 Fetching weather for {args.city.title()}...[/bold blue]\n")
    weather = weather_scaping(args.city)
    display_weather(weather)

    if args.output:
        export_to_file(weather, args.output)


if __name__ == "__main__":
    main()
