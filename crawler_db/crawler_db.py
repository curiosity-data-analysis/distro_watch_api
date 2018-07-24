import requests
from bs4 import BeautifulSoup


BASE_URL = 'https://distrowatch.com'


def get_dom(url: str) -> BeautifulSoup:
    '''Makes HTTP request for provided URL
    and returns BeautifulSoup object with its content.'''

    response = requests.get(url)
    return BeautifulSoup(response.content, 'lxml')


def save_to_csv(title: str, content: list):
    '''Save content in folder data_csv/'''

    with open('data_csv/file_{}.csv'.format(title), 'w') as file:
        file.write('position,distribution,hit_ranking\n')
        for line in content:
            file.write(line + '\n')


def get_tables(dom: BeautifulSoup) -> list:
    '''Returns the tables that contains ranking info.'''
    return dom.select('.NewsText table tr td table')


def get_table_title_and_content(table: BeautifulSoup) -> tuple:
    '''Returns the table title (first line, in this case)
    and the rows content in CSV format (comma separated).'''

    strings = list(table.stripped_strings)
    title, content = strings[0], strings[1:]

    title = '_'.join(title.lower().split()[1:])
    content = [','.join(content[i: i + 3])
               for i in range(0, len(content), 3)]

    return title, content


def crawl_ranking(save_csv: bool = False) -> dict:
    '''Collects the popularity data from DistroWatch website.
    It is also responsible for generating .csv files for data analysis.

    Returns a dictionary with ranking tables content.'''

    dom = get_dom(BASE_URL + '/dwres.php?resource=popularity')
    tables = get_tables(dom)

    ranking = {}

    for table in tables:
        title, content = get_table_title_and_content(table)
        ranking[title] = content
        if save_csv:
            save_to_csv(title, content)

    return ranking


def get_distro_names() -> set:
    '''Returns a set of distro names present in ranking.'''

    distros_name = set()
    ranking = crawl_ranking()

    for content in ranking.values():
        _distros_name = content[1::3]
        distros_name.update(_distros_name)

    return distros_name


def crawler_distribution():
    '''Collects data from existing distributions on DistroWatch
    WIP (Work In Progress).'''

    distro_names = crawl_ranking()


if __name__ == '__main__':
    crawl_ranking(save_csv=True)
