import csv
import pysolr

# Initialize a connection to Solr
solr_url = 'http://localhost:8983/solr/geonames_en'  # Replace 'YOUR_CORE_NAME' with the name of your Solr core
solr = pysolr.Solr(solr_url, timeout=10)

# Path to the GeoNames en.txt file
geonames_file_path = 'data/US.txt'  # Replace with your actual path

# Read the file and index to Solr
with open(geonames_file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='\t')

    # For batch processing and efficient indexing
    batch = []

    for row in reader:
        # Construct a document for Solr based on your schema
        # This is a basic mapping and might need adjustments based on your exact schema
        doc = {
            'id': row[0],
            'name': row[1],
            # 'asciiname': row[2],
            # 'alternatenames': row[3].split(','),
            'latitude': float(row[4]),
            'longitude': float(row[5]),
            # 'featureClass': row[6],
            # 'featureCode': row[7],
            # 'countryCode': row[8],
            # 'population': int(row[14]),
            # 'elevation': int(row[15]) if row[15] else None,
            # 'admin1Code': row[10],
            # 'admin2Code': row[11],
            # 'admin3Code': row[12],
            # 'admin4Code': row[13],
            'location': f"{row[4]},{row[5]}"
        }

        print(doc)

        batch.append(doc)

        # Send data to Solr in batches (e.g., every 1000 documents)
        if len(batch) >= 1000:
            solr.add(batch)
            batch = []

    # Index the remaining documents
    if batch:
        solr.add(batch)

print("Finished indexing to Solr!")
