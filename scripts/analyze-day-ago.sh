#!/bin/bash

# PURPOSE:
#   Analyze the scraped irozhlas.cz content (`*.txt`).
#
# PREREQUISITIES:
#   - Set the environment variable GENEEA_API_KEY on system
# or
#   - Set the environment variable in `.env` file in current directory.

# Activate the existing virtual environment.
source /root/irozhlas/cro-geneea-sdk/.venv/bin/activate

# Executes the NLP analysis gor all TXT files.
for i in $(find /root/irozhlas/irozhlas-scraper/output/*.txt -newermt $(date +%Y-%m-%d -d '1 day ago') -type f -print); do
	cro.geneea --input "$i" --type analysis --format xml;
	sleep 1;
done

# Deactivate the current virtual environment.
deactivate

# Move all XML files to dedicated folder.
mv /root/irozhlas/irozhlas-scraper/output/*.xml /root/irozhlas/irozhlas-scraper/output/xml
