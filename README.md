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

| name | description | type | Required |
|---|---|----|---|
| name |Define o nome do bucket| string | True |
| project_id |Define em que projeto o bucket será criado| string |True|
| region |Define em que região o bucket será criado| string | True |
| force_destroy |Se configurada como false ela não permite que o terraform delete um bucket que possuam objetos | boolean | false |
| storage_class |Define a classe de armazenamento dos objetos desse bucket| string | false |
| Versoning |Define se os objetos armazenados no bucket serão versionados| boolean | false|
| labels |Define as labels que serão aplicadas no bucket | map(string) | false |


