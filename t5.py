# import os
# import os.path
import requests


def download(url):
    req = requests.get(url)
    if req.status_code == 404:
        print('No such file found at {}'.format(url))
        return
    filename = url.split('/')[-1]
    with open(filename, 'wb') as fobj:
        fobj.write(req.content)
    print('Download over.')


if __name__ == '__main__':
    url = input('Enter a URL: ')
    download(url)
