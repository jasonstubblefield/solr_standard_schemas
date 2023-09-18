# Solr Schema Manager

This is part of my attempt to make Solr less difficult to use.

This package includes solr schemas for common data tables.

* Nutch and compatible crawlers I have created
* Wordpress API
* Geonames Data

It also includes mapping tables for several different languages to map common data tables to solr wildcard fields.

This example is for homebrew on Mac OS, other *nix systems should be similar.  

Make sure homebrew uis up to date.

`brew update && brew upgrade`

Install Solr with homebrew

`brew install solr`

Create a solr collection.

`/opt/homebrew/bin/solr create -c testCollection"`

Disable automatic field creation.

`/opt/homebrew/bin/solr config -c testCollection -p 8983 -action set-user-property -property update.autoCreateFields -value false`

Back up the managed schema.

`mv /opt/homebrew/var/lib/solr/testCollection/conf/managed-schema.xml \
/opt/homebrew/var/lib/solr/testCollection/conf/managed-schema.backup`

Copy the schema file to the core conf folder. 

`cp nutch.schema.xml /opt/homebrew/var/lib/solr/testCollection/conf/schema.xml`

EASY: upload the solrconfig.xml

`cp solrconfig.xml /opt/homebrew/var/lib/solr/testCollection/conf/`

OR:

Make the changes to your solrconfig.xml file as described here:

https://solr.apache.org/guide/solr/latest/configuration-guide/schema-factory.html#switching-from-schema-xml-to-managed-schema

`nano /opt/homebrew/var/lib/solr/testCollection/conf/solrconfig.xml`

Change this:

`<schemaFactory class="ManagedIndexSchemaFactory">
<bool name="mutable">true</bool>
<str name="managedSchemaResourceName">managed-schema</str>
</schemaFactory>`

To this:

`<schemaFactory class="ClassicIndexSchemaFactory"/>`

Restart the solr core:

`curl 'http://localhost:8983/solr/admin/cores?action=RELOAD&core=YOUR_CORE_NAME'`
