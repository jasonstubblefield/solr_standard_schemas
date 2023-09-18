# Geonames Data Importer

Create the Solr Core

`/opt/homebrew/bin/solr create -c defaultCollection`

Copy the solrconfig file.

`cp solrconfig.xml /opt/homebrew/var/lib/solr/geonames_en/conf/solrconfig.xml`

Copy the schema.

`cp geonames.schema.xml /opt/homebrew/var/lib/solr/geonames_en/conf/schema.xml`

Update the core.

`curl 'http://localhost:8983/solr/admin/cores?action=RELOAD&core=geonames_en'`

Run the importer.

Make sure the data exists at `data/US.txt`.

`python3 importer/geonames.py`

Query

`http://localhost:8983/solr/geonames_en/select?q=*:*&fq={!geofilt}&sfield=location&pt=39.0997,-94.5786&d=50&sort=geodist()%20asc`