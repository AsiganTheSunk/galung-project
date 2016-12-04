#!/usr/bin/env python

from __future__ import print_function
import sys
import time
from trunk import libtorrent as lt


def st_client (torrent):

    ses = lt.session()
    ses.listen_on(6881, 6891)

    print('Simple Torrent Client (starting)')

    # Configuracion Torrent
    #path = raw_input ("Seleccion el Path")
    # Validar el path, si no volver a formular la pregunta
    # Si el path existe pero la carpeta no esta creada, la crea
    # Generar un Fichero de Configuracion, para el path
    torrentFilePath = "/home/asigan/Escritorio/torrent/"
    info = lt.torrent_info(torrent)

    # Validacion Torrent
    handle = ses.add_torrent({'ti': info,'storage_mode':lt.storage_mode_t.storage_mode_sparse,'auto_managed': True, 'save_path': torrentFilePath})
    if (handle.is_valid()): 
        print ("[Checking Handle]: Valid")
    else :
        print ("[Checking Handle]: Invalid")
        print('[TORRENT]: '+ handle.name())

    # Bucle de Descarga
    while (not handle.is_seed()):
        try:
            s = handle.status()
            state_str = ['queued', 'checking', 'downloading metadata', \
                'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']
            print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % \
                (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
                s.num_peers, state_str[s.state]), end=' ')

            alerts = ses.pop_alerts()
            for a in alerts:
                if a.category() & lt.alert.category_t.error_notification:
                    print(a)

            sys.stdout.flush()
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nAborting...\n")
            sys.exit(0)

    print('Complete')
    print("Simple Torrent Client (closing)\n")
