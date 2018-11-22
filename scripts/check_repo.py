"""
pip install git+https://github.com/brennerm/python-apt-repo.git@master
pip install apt-repo

Python2

ImportError: No module named lzma

import urllib.error
ImportError: No module named error

Sources listed at
https://github.com/OSGeo/OSGeoLive/blob/master/sources.list.d/ubuntugis.list

deb http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu bionic main

"""

from apt_repo import APTSources, APTRepository

def get_package():
    url = 'http://archive.ubuntu.com/ubuntu'
    # url = 'https://launchpad.net/~ubuntugis/+archive/ubuntu/ubuntugis-experimental'
    components = ['main', 'universe', 'multiverse', 'restricted']
    #components = ['main']

    sources = APTSources([
        APTRepository(url, 'bionic', components),
        #APTRepository(url, 'bionic-updates', components),
        #APTRepository(url, 'bionic-backports', components),
        #APTRepository(url, 'bionic-proposed', components)
    ])

    pkg = "python-mapscript"
    print([(package.package, package.version) for package in sources.get_packages_by_name(pkg)])

    repo = APTRepository(url, 'bionic', components)

    for pkg in ["python-mapscript"]:
        print([(package.package, package.version) for package in repo.get_packages_by_name(pkg)])
        #package = repo.get_packages_by_name(pkg_name)
        #print((package.package, package.version))

get_package()
print("Done!")