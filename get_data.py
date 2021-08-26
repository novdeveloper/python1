import argparse
import pathlib
import requests
from bs4 import BeautifulSoup
import time

if __name__ == '__main__':
    # Args
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='start page', type=str)
    parser.add_argument('--output', help='output_directory', type=str, default='output')
    parser.add_argument('--skip', help='skip downloaded files', action='store_true')
    args = parser.parse_args()

    if not pathlib.Path(args.output).is_dir():
        pathlib.Path(args.output).mkdir()

    page_link = args.input
    proceed = True

    session = requests.session()

    while proceed:
        print('New page')
        page_html = session.get(page_link).text
        page_soup = BeautifulSoup(page_html, 'html.parser')

        winery_post_headers = page_soup.find_all('h4', {'class': 'blog-archive-title'})     
        wineries = []
        for header in winery_post_headers:
            wineries.append({
                'url': header.findChild('a').attrs['href'],
                'name': ''.join(i for i in header.text if i not in '/\:*?<>|"')
            })

        for winery in wineries:
            if args.skip and pathlib.Path('{}/{}.html'.format(args.output, winery['name'])).exists():
                print('File already exists, continue')
                continue

            resp = session.get(winery['url'])
            with open('{}/{}.html'.format(args.output, winery['name']), "w", encoding="utf-8") as f:
                f.write(resp.text)
                f.close()
            print('Saved info for {}'.format(winery['name']))
            time.sleep(0.5)

        proceed = page_soup.find('a', {'class': 'next page-numbers'})
        if proceed:
            page_link = page_soup.find('a', {'class': 'next page-numbers'}).attrs['href']
            print('Next page exists')

        time.sleep(1)
