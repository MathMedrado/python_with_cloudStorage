from google.cloud import storage

bucket_name = "nome do bucket"
destination_file_name="Caminho onde o arquivo será salvo"
project_name="nome do projeto"
blob_file = "Sample-Spreadsheet-10-rows.csv" #nome do arquivo no bucket

storage_client = storage.Client(project_name)
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob(blob_file)
blob.download_to_filename(destination_file_name)