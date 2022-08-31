Para utilizar o código substitua os parametros abaixo:

bucket_name = "nome do bucket"

destination_file_name="Caminho onde o arquivo será salvo"

project_name="nome do projeto"

blob_file = "Sample-Spreadsheet-10-rows.csv" #nome do arquivo no bucket

Caso o arquivo esteja dentro de uma pasta:
blob_file = "csv/Sample-Spreadsheet-10-rows.csv"

Para authenticação com a google utilize a variavel de ambiente GOOGLE_APPLICATION_CREDENTIALS passando
como parametro o caminho de onde está armazenado a sua chave json da sua service account.

Exemplo para linux/MacOS
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

|name|description | type | Required|
|---|---|----|---|
|name|Define o nome do bucket|string|True|
