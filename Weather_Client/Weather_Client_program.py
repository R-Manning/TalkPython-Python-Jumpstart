import requests  # for http requests
import bs4  # beautifulsoup4
import collections  # allows naming variables in tuples for easier access

WeatherReport = collections.namedtuple('WeatherReport',
                                       'loc, cond, temp, scale', )


def main():
    print_the_header()
    zipcode = ''
    while True:
        zipcode = input('What zip-code do you want the weather for [90210]?')

        if not zipcode.isnumeric():
            print('Please enter only integer values for the zip-code')
        elif len(zipcode) != 5:
            print('Please enter a 5 digit zip-code')
        else:
            break  # had a cast to int here and it dropped the leading zero causing issues

    html = get_html_from_web(zipcode)
    report = get_weather_from_html(html)

    print('The weather in {} is {} {} and {}.'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))


def print_the_header():
    print('----------------------')
    print('      Weather App     ')
    print('----------------------')
    print()


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)

    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find('h1').get_text()
    cond = soup.find(class_='condition-icon').get_text()
    temp = soup.find('span', attrs={'_ngcontent-c17': '', 'class': 'wu-value wu-value-to', 'style': ''}).get_text()
    scale = soup.find('span', class_='wu-label').get_text()

    # cleaning up text
    loc = cleanup_text(loc)
    cond = cleanup_text(cond)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    return WeatherReport(loc=loc, cond=cond, temp=temp, scale=scale)


def cleanup_text(text: str):
    if not text:  # if empty just return it so that the program doesn't error out
        return text

    text = text.strip()  # remove whitespace
    if "\n" in text:  # if multiple lines
        text = text.splitlines()[0]  # keep only the first line
    return text


if __name__ == '__main__':
    main()


# TODO: could add stuff like daily or extended forecast, if there are any advisories
