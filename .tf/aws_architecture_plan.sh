#!/usr/bin/env bash

# Run this script pointing to all libraries required to package them for the Lambda.

terraform init

cp -r /Users/sameershaik/Projects/ETL_Project/venv/lib/python3.11/site-packages/* ../lambda_payloads/lambda_handler_payload/


cp /Users/sameershaik/Projects/ETL_Project/playlist_generator.py ../lambda_payloads/lambda_handler_payload/
cp /Users/sameershaik/Projects/ETL_Project/config/playlists.py ../lambda_payloads/lambda_handler_payload/config/

cp /Users/sameershaik/Projects/ETL_Project/tools/calculate_similarity.py ../lambda_payloads/lambda_handler_payload/tools/
cp /Users/sameershaik/Projects/ETL_Project/tools/get_artist_from_playlist.py ../lambda_payloads/lambda_handler_payload/tools/
cp /Users/sameershaik/Projects/ETL_Project/tools/recommend_similar_songs.py ../lambda_payloads/lambda_handler_payload/tools/

cd ../lambda_payloads/lambda_handler_payload/

zip -r ../../payload.zip *

cd ../../.tf/

terraform plan
