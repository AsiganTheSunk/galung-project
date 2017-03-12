#!/usr/bin/env python

import sys
from time import sleep

from main import libtorrent as lt


def m2t_create(magnet, output_name=None):

    print("\nMagnet2Torrent Service (starting)")
    # Paths
    # Tener un fichero de configuracion
    tempdir = "/home/asigan/Escritorio/test-library/"
    temptorrent = "/home/asigan/Escritorio/test-library/" + output_name + ".torrent"

    # Inicio de Session
    session = lt.session()
    session.listen_on(6881, 6891) #todo use 0??

    # Parametros de Descarga del Torrent
    magnet_uri = str(magnet)
    params = {
        'paused': False,
        'auto_manage': False,
        'save_path': tempdir,
        'duplicate_is_error': True
    }

    # Validacion del Handle
    handle = lt.add_magnet_uri(session, magnet_uri, params)
    if(handle.is_valid()):
        print "[Checking Handle]: Valid"
    else:
        print("[Checking Handle]: Invalid")
        session.pause()
        exit(0)

    print("Downloading Metadata (this may take a while)")
    while (not handle.has_metadata()):
        try:
            s = handle.status()
            if (s.active_time > 120):
                print "Donwloading Metadata Error (timeout)"
                session.pause()
                sys.exit(0)
            else:
                sleep(1)
        except KeyboardInterrupt:
            print("Aborting...")
            session.pause()
            sys.exit(0)


    session.pause()
    print("Complete")

    # Guardando el Torrent
    print("Saving Torrent File here:\n"+"[PATH]: "+temptorrent)
    torinfo = handle.get_torrent_info()
    torfile = lt.create_torrent (torinfo)
    f = open(temptorrent, "wb")
    torcontent = lt.bencode(torfile.generate())
    f.write(torcontent)
    f.close()

    session.remove_torrent(handle)
    print("Magnet2Torrent Service (closing)\n")
    return (temptorrent)
