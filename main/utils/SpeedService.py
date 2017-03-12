#!/usr/bin/env python

import pyspeedtest


def check_status():
    try:
        st = pyspeedtest.SpeedTest()
        status = st.ping()
        print status
        print "ALIVE\n"
    except:
        print "ERROR+\n"


def run_test ():
    try:
        st = pyspeedtest.SpeedTest()
        #download = st.download()
        uplink = st.upload()
        #print download + '/'
        print uplink + '\n'
        print "SUCCESS\n"
    except:
        print "ERROR\n"


def main ():
#    check_status()
    run_test()

if __name__ == "__main__":
    main()
