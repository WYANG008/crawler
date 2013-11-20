all: bootstrap buildout

bootstrap:
	python bootstrap.py -v 2.1.1

buildout:
	REDISSRV_LOCATION=`which redis-server` ./bin/buildout
	mkdir ./bin/temp
	mkdir ./bin/temp/data

distclean: clean

clean:
	rm -rf .installed.cfg bin develop-eggs eggs parts
	find . -name '*.pyc' | xargs rm -f
