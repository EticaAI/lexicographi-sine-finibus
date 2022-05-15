#!/bin/bash
#===============================================================================
#
#          FILE:  999999_1679.sh
#
#         USAGE:  ./999999999/999999_1679.sh
#                 FORCE_REDOWNLOAD=1 ./999999999/999999_1679.sh
#                 FORCE_CHANGED=1 ./999999999/999999_1679.sh
#                 FORCE_REDOWNLOAD_REM="1603_1_51" ./999999999/999999_1679.sh
#                 time ./999999999/999999_1679.sh
#   DESCRIPTION:  Temporary tests related to Brazilian namespace. Use case from
#                 https://github.com/EticaAI/lexicographi-sine-finibus/issues/39
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
#       CREATED:  2022-05-12 14:18 UTC started. based on 1603_99.sh
#      REVISION:  ---
#===============================================================================
set -e

# time HTTPS_PROXY="socks5://127.0.0.1:9050" ./999999999/999999_1679.sh

# ./999999999/0/1603_1.py --methodus='codex' --codex-de 1603_45_31 --codex-in-tabulam-json | jq
# ./999999999/0/1603_1.py --methodus='codex' --codex-de 1603_45_31 --codex-in-tabulam-json > 1603/45/31/1603_45_31.mul-Latn.tab.json
# https://commons.wikimedia.org/wiki/Data:Sandbox/EmericusPetro/Example.tab

# @TODO: implement download entire sheet
DATA_1603="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/export?format=xlsx"

ROOTDIR="$(pwd)"

# shellcheck source=999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh


#### Manual action, TEST locally, one per time, START --------------------------
# Download entire XLSX to local temp
# file_download_1603_xlsx "1"
# actiones_completis_locali "1603_1_1"
# actiones_completis_locali "1603_1_7"
# actiones_completis_locali "1603_1_51"

# actiones_completis_locali "1679_1_1"


#### Manual action, TEST locally, one per time, END ----------------------------

## Full drill (remote, specific item)
# actiones_completis_publicis "1603_63_101"
# actiones_completis_publicis "1603_25_1"
# actiones_completis_publicis "1603_99_123"
# actiones_completis_publicis "1603_1_8000"
# actiones_completis_locali "1679_1_1"
# deploy_0_9_markdown


#### tests _____________________________________________________________________

# TODO: deal with timeouts. Some links
#       - https://phabricator.wikimedia.org/T179879
#       - https://phabricator.wikimedia.org/T166139
#       - https://github.com/blazegraph/database/wiki/QueryHints

# wikidata_p_ex_interlinguis "1679_45_16_76_2" "1" "1" "P1585" "P402,P1566,P1937,P6555,P8119"

# sleep 10
# wikidata_p_ex_linguis "1679_45_16_76_2" "1" "1" "P1585" "1" "20"

# sleep 10
# wikidata_p_ex_linguis "1679_45_16_76_2" "1" "1" "P1585" "2" "20"

# sleep 10
# wikidata_p_ex_linguis "1679_45_16_76_2" "1" "1" "P1585" "3" "20"

# sleep 10
# wikidata_p_ex_linguis "1679_45_16_76_2" "1" "1" "P1585" "4" "20"

wikidata_p_ex_totalibus "1679_45_16_76_2" "1" "1" "P1585" "P402,P1566,P1937,P6555,P8119"

# @see https://servicodados.ibge.gov.br/api/docs/localidades
# @see https://github.com/search?o=desc&q=ibge&s=stars&type=Repositories
# @see CNAE
#      - https://servicodados.ibge.gov.br/api/docs/CNAE?versao=2#api-_
#      - https://cnae.ibge.gov.br/images/concla/documentacao/CNAE20_Introducao.pdf
# @see https://sidra.ibge.gov.br/home/pnadct/brasil
# @see https://servicodados.ibge.gov.br/api/docs
# @see - https://servicodados.ibge.gov.br/api/docs/produtos?versao=1
#        - https://servicodados.ibge.gov.br/api/v1/produtos/estatisticas
#        - https://servicodados.ibge.gov.br/api/v1/produtos/geociencias
#        - https://biblioteca.ibge.gov.br/visualizacao/livros/liv100600.pdf

exit 1


# echo "--actionem-sparql --de=P --query --ex-interlinguis --cum-interlinguis=P402,P1566,P1937,P6555,P8119"
# printf "P1585\n" | ./999999999/0/1603_3_12.py \
#   --actionem-sparql --de=P --query --ex-interlinguis --cum-interlinguis=P402,P1566,P1937,P6555,P8119 \
#   | ./999999999/0/1603_3_12.py --actionem-sparql --csv --hxltm \
#   > 999999/0/P1585.tm.hxl.csv

# sleep 5
# echo "--actionem-sparql --de=P --query --lingua-divisioni=20 --lingua-paginae=1"
# printf "P1585\n" | ./999999999/0/1603_3_12.py \
#   --actionem-sparql --de=P --query --lingua-divisioni=20 --lingua-paginae=1 \
#   | ./999999999/0/1603_3_12.py --actionem-sparql --csv --hxltm \
#   > 999999/0/P1585.wikiq~1-20.hxl.csv

# sleep 5
# echo "--actionem-sparql --de=P --query --lingua-divisioni=20 --lingua-paginae=2"
# printf "P1585\n" | ./999999999/0/1603_3_12.py \
#   --actionem-sparql --de=P --query --lingua-divisioni=20 --lingua-paginae=2 \
#   | ./999999999/0/1603_3_12.py --actionem-sparql --csv --hxltm \
#   > 999999/0/P1585.wikiq~2-20.hxl.csv

# sleep 5
# echo "--actionem-sparql --de=P --query --lingua-divisioni=20 --lingua-paginae=3"
# printf "P1585\n" | ./999999999/0/1603_3_12.py \
#   --actionem-sparql --de=P --query --lingua-divisioni=20 --lingua-paginae=3 \
#   | ./999999999/0/1603_3_12.py --actionem-sparql --csv --hxltm \
#   > 999999/0/P1585.wikiq~3-20.hxl.csv

# echo "hxlmerge..."
# hxlmerge --keys='#item+conceptum+codicem' \
#   --tags='#item+rem' \
#   --merge="999999/0/P1585.wikiq~2-20.hxl.csv" \
#   "999999/0/P1585.wikiq~1-20.hxl.csv" \
#   >"999999/0/P1585.wikiq~1+2-20.hxl.csv"

# sed -i '1d' "999999/0/P1585.wikiq~1+2-20.hxl.csv"

# hxlmerge --keys='#item+conceptum+codicem' \
#   --tags='#item+rem' \
#   --merge="999999/0/P1585.wikiq~3-20.hxl.csv" \
#   "999999/0/P1585.wikiq~1+2-20.hxl.csv" \
#   >"999999/0/P1585.wikiq~1+2+3-20.hxl.csv"

# sed -i '1d' "999999/0/P1585.wikiq~1+2+3-20.hxl.csv"

# hxlrename \
#   --rename='item+conceptum+codicem:#item+rem+i_qcc+is_zxxx+ix_wikiq' \
#   "999999/0/P1585.wikiq~1+2+3-20.hxl.csv" \
#   >"999999/0/P1585.wikiq~1+2+3-20~TEMP.hxl.csv"

# sed -i '1d' "999999/0/P1585.wikiq~1+2+3-20~TEMP.hxl.csv"

# hxlmerge --keys='#item+rem+i_qcc+is_zxxx+ix_wikiq' \
#   --tags='#item+rem' \
#   --merge="999999/0/P1585.wikiq~1+2+3-20~TEMP.hxl.csv" \
#   "999999/0/P1585.tm.hxl.csv" \
#   >"999999/0/1679_45_16_76_2.no11.hxl.csv"

# sed -i '1d' "999999/0/1679_45_16_76_2.no11.hxl.csv"

# file_hotfix_duplicated_merge_key "999999/0/1679_45_16_76_2.no11.hxl.csv" '#item+rem+i_qcc+is_zxxx+ix_wikiq'