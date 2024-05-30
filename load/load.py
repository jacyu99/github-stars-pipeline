import gzip
import shutil
import os
import tempfile
import duckdb
import json

# create a temporary folder
with tempfile.TemporaryDirectory() as temp_folder:

    # define paths
    src_gz_path = 'data/gharchive_sample'
    dest_json_dir = temp_folder

    # create function to unzip .json.gz file into temp folder
    def unzip_json_file(src_gz_path, dest_json_dir, json_file_name):
        with gzip.open(os.path.join(src_gz_path, f"{json_file_name}.gz"), 'rb') as f_in:
            with open(os.path.join(dest_json_dir, json_file_name), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    # list all the files ending in .json.gz in gharchive_sample
    json_files = [pos_json for pos_json in os.listdir(src_gz_path) if pos_json.endswith('.json.gz')]

    # loop over all files and apply unzip_json_file to each
    for file in json_files:
        unzip_json_file(src_gz_path, dest_json_dir, os.path.splitext(file)[0])

    # checking the contents of the temporary directory
    # for item in os.listdir(temp_folder.name):
    #     print(item)

    # create a persistent duckdb connection
    con = duckdb.connect("repos.db")

    # create a schema
    con.execute("CREATE SCHEMA IF NOT EXISTS source")

    # create table source.gharchive and insert jsons
    con.execute(f"""
            CREATE OR REPLACE TABLE source.gharchive AS
            SELECT *
            FROM '{dest_json_dir}/*.json'
    """)

    # close the connection
    con.close()