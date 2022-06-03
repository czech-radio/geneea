#!/bin/bash
source /root/irozhlas/cro-geneea-sdk/.venv/bin/activate
source /root/irozhlas/cro-geneea-sdk/secret

for i in `find /root/irozhlas/irozhlas-scraper/output/*.txt -newermt $(date +%Y-%m-%d -d '1 day ago') -type f -print`; do
	cro.geneea -i $i -t analysis -f xml;
	sleep 1;
done
deactivate
mv /root/irozhlas/irozhlas-scraper/output/*.xml /root/irozhlas/irozhlas-scraper/output/xml

TODAY=$(date +%Y-%m-%d)

mkdir /root/irozhlas-scraper-geneea-output/txt/$TODAY
mkdir /root/irozhlas-scraper-geneea-output/xml/$TODAY
mkdir /root/irozhlas-scraper-geneea-output/html/$TODAY

for i in `find /root/irozhlas/irozhlas-scraper/output/*.txt -newermt $(date +%Y-%m-%d -d '1 day ago') -type f -print`; do
    cp -ar $i /root/irozhlas-scraper-geneea-output/txt/$TODAY 
done

for i in `find /root/irozhlas/irozhlas-scraper/output/xml/*.xml -newermt $(date +%Y-%m-%d -d '1 day ago') -type f -print`; do
    cp -ar $i /root/irozhlas-scraper-geneea-output/xml/$TODAY 
done

for i in `find /root/irozhlas/irozhlas-scraper/*.html -newermt $(date +%Y-%m-%d -d '1 day ago') -type f -print`; do
    cp -ar $i /root/irozhlas-scraper-geneea-output/html/$TODAY 
done

cd /root/irozhlas-scraper-geneea-output
git add .
git commit -am "Automatic data update `date`"
git pull
git push
