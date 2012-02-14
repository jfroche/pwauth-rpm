#!/bin/sh
version="2.3.10"
rm -rf BUILD RPMS SRPMS tmp || true
mkdir -p BUILD RPMS SRPMS SOURCES

if [ ! -f SOURCES/pwauth-$version.tar.gz ];
then
    wget "http://pwauth.googlecode.com/files/pwauth-$version.tar.gz" -O SOURCES/pwauth-$version.tar.gz
fi

rpmbuild -ba --define="_topdir $PWD" --define="_tmppath $PWD/tmp" --define="ver $version" pwauth.spec
