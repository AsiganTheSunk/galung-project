#!/usr/bin/python

import os
import sys

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
path = os.path.dirname(os.path.abspath('china_wall.py'))
sys.path.append(path)
import china_wall as cw


SHOW_FLAG = '6'
FILM_FLAG = '14'
ANIME_FLAG = '10'


rarbg_default_url =  'https://www.rarbg.to/torrents.php?search='

# No esta fucando el tema este. No me acuerdo porque
# TODO Devuelve None because reasons!!!
def rarbg_request_builder(title='', year='', season='', episode='', subber='', fflag='0'):
    if int(fflag) == SHOW_FLAG:
        print rarbg_show_request_builder(title=title, season=season, episode=episode)
    if int(fflag) == FILM_FLAG:
        print rarbg_film_request_builder(title=title, year=year)
    if int(fflag) == ANIME_FLAG:
        print rarbg_anime_request_builder(title=title, episode=episode, subber=subber)


def rarbg_film_request_builder(title='', year=''):
    return (rarbg_default_url +  (title.replace(" ", "%20") + '%20' + str(year)))


def rarbg_show_request_builder(title='', season='', episode=''):
    return (rarbg_default_url + (title.replace(" ", "%20") + '%20S' + str(season) + 'E' + str(episode)) + '&category%5B%5D=18&category%5B%5D=41&category%5B%5D=49' )


def rarbg_anime_request_builder(title='', episode='', subber=''):
    return (rarbg_default_url + (str(subber) + '%20' + title.replace(" ", "%20") + '%20' + 'E' + str(episode)))


def rarbg_search (url):
    headers = {'UserAgent':str(UserAgent().random)}
    try:
        r = requests.get (url, verify=True, headers=headers)
    except Exception as e:
        print 'Unable to stablish connection'
    finally:
        if r.status_code == 200:
            print '200 OK'
            return r

def rarbg_parser (content=None):
    soup = BeautifulSoup (content.text, 'html.parser')
    # print soup.prettify()
    ttable = soup.findAll('tr', {'class': 'lista2'})
    # print ttable
    raw_input('Press [ENTER] To Continue...')

    if ttable != []:
    # TODO anadir un callback o algo si no lo encuentra de la primera forma.
        print 'Retrieving individual values from the table'
        for items in ttable:
            title = (items.findAll('a')[1])['title']
            tamano = items.findAll('td', {'class': 'lista'})[3].text
            # leechs = tamano = items.findAll('td', {'class': 'lista'})[5].text
            # print title, tamano
            # print '****' * 20

        for items in ttable:
            # href =  items.findAll('td', {'class': 'lista'})[1]
            href = (items.findAll('a')[1])['href']
            print '+++HREF 1: ' + str(href)
            #href1 = items.findAll('td', {'class': 'lista'})[2]['href']
            #print '+++HREF 2: ' + str(href1)
            seeds = items.findAll('td', {'class': 'lista'})[4].text
            print '***SEEDS: ' + str(seeds)
            leechs = items.findAll('td', {'class': 'lista'})[5].text
            print '***LEECHS: ' + str(leechs)

    else:
        print 'rarbg.to seems to not be working at the moment, please try again later'

    content = cw.cw_request('https://www.rarbg.to/torrent/49b7tml')
    soup = BeautifulSoup(content.text, 'html.parser')
    magnet = soup.findAll('a', href=True)
    #magnet2 = (soup.findAll('a', href=True)[21])['href']

    print '____' * 20
    #print magnet2
    print '____' * 20

    contador = 1
    for item in magnet:

        #print contador, item
        contador = contador + 1

        #print '____'*3
        #print magnet




def main():
    print '[ACTUAL IP]: ' + str(cw.cw_check_identity())
    print '[RESET IP]: ' + str(cw.cw_reset_identity())
    print '[NEW IP]: ' + str(cw.cw_check_identity())

    show = rarbg_show_request_builder(title='Game Of Thrones', season='02', episode='01')
    #film =  rarbg_film_request_builder(title='Why Him', year='2016')
    #anime = rarbg_anime_request_builder(title='One Punch Man', episode='01', subber='HorribleSubs')

    print show
    #print film
    #print anime
    raw_input('Press [ENTER] To Launch WebScrapping...')

    rarbg_parser(content=cw.cw_request(show))
    # rarbg_parser(content=rarbg_search(film))
    # rarbg_parser(content=rarbg_search(anime))

if __name__ == '__main__':
    main()


su