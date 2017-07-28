#!/usr/bin/env python

from torrequest import TorRequest
from fake_useragent import UserAgent
import json

# TODO Usar brew para instalar tor?
# TODO Settings para el setup de la pass en el primer arranque de la aplicacion
# TODO automatizarlo


def cw_balancer(request=None, proxy_port=None, ctrl_port=None, password=None):
    # TODO clase que lo que hace es, tener un contador que cada X peticiones rota el proxy por el que sales de forma
    # TODO transparente.
    return


def cw_check_identity():
    try:
        with TorRequest(proxy_port=9050, ctrl_port=9051, password='ultramegachachi') as tr:
            print tr.get('https://check.torproject.org/').text
            origin_ip = str(json.loads(tr.get('http://httpbin.org/ip').text).get('origin'))
    except Exception as e:
        print 'Unable to retrieve identity'
        print 'Exception: ' + str(e)
    else:
        return origin_ip


def cw_request(url):
    headers = {'UserAgent': str(UserAgent().random)}
    with TorRequest(proxy_port=9050, ctrl_port=9051, password='ultramegachachi') as tr:
        try:
            r = tr.get(url, verify=True, headers=headers)
        except Exception as e:
            print 'Unable to stablish connection'
            print 'Exception: ' + str(e)
        else:
            if r.status_code == 200:
                print '[STATUS CODE]: 200 OK'
                return r


def cw_reset_identity():
    with TorRequest(proxy_port=9050, ctrl_port=9051, password='ultramegachachi') as tr:
        try:
            tr.reset_identity()
        except Exception as e:
            print 'Unable to reset identity'
            print 'Exception: ' + str(e)
        else:
            return 'Succesfull'



# def main():
#    print '[ACTUAL IP]:' + cw_check_identity()
#    print '***'*20
#    print '[STATUS CODE]: ' + cw_request(url='https://www.crummy.com/software/BeautifulSoup/')
#    print '***'*20
#    print '[RENEW IP]: ' + cw_reset_identity()
#    print '***' * 20
#    print '[NEW IP]: ' + cw_check_identity()

# if __name__ == '__main__':
#     main()
