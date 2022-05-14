#!/bin/bash
#===============================================================================
#
#          FILE:  1603_3_12_16_5305.sh
#
#         USAGE:  ./999999999/1603_3_12_16_5305.sh
#                 time ./999999999/1603_3_12_16_5305.sh
#   DESCRIPTION:  Drills related to manage a spark SPARQL endpoint
#                 https://www.wikidata.org/wiki/Property:P5305
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - hxltmcli
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.0
#       CREATED:  2022-05-14 15:45 UTC started. based on 999999_1679.sh
#      REVISION:  ---
#===============================================================================
set -e

# time HTTPS_PROXY="socks5://127.0.0.1:9050" ./999999999/1603_3_12_16_5305.sh

ROOTDIR="$(pwd)"

# shellcheck source=999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh


# @TODO eventualmente talvez anotar as propriedades de campos que tem aqui
#       Cadastro Nacional de Endereços para Fins Estatísticos
#       https://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Cadastro_Nacional_de_Enderecos_Fins_Estatisticos/

# @TODO https://geoftp.ibge.gov.br/

# @TODO https://geoftp.ibge.gov.br/organizacao_do_territorio/estrutura_territorial/divisao_territorial/2021/
# @TODO https://geoftp.ibge.gov.br/cartas_e_mapas/bases_cartograficas_continuas/bc250/versao2021/geopackage/

# https://github.com/conjecto/docker-blazegraph
# docker run --name some-blazegraph -d conjecto/blazegraph:2.1.6
# https://github.com/lyrasis/docker-blazegraph

# docker run --name blazegraph -d -p 8889:8080 lyrasis/blazegraph:2.1.5
# docker logs -f blazegraph
# http://localhost:8889/bigdata/

# https://wiki.uib.no/info216/index.php/Lab:_SPARQL_Programming

# See https://github.com/blazegraph/database/wiki/Quick_Start
# wget https://raw.githubusercontent.com/blazegraph/blazegraph-samples/53f615248f33f767d2b259472d84f19452d39aa5/sample-sesame-embedded/src/main/resources/data.n3 -o /tmp/data.n3
# xdg-open http://localhost:8889/bigdata/
# Run
#    load <file:///tmp/data.n3>

# https://github.com/apache/jena/blob/main/jena-fuseki2/jena-fuseki-docker/README.md
# https://www.youtube.com/watch?v=5-UfFV5XmTI
# https://jena.apache.org/documentation/io/
# https://github.com/stain/jena-docker
# https://ontola.io/blog/rdf-serialization-formats/
