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

printf "P1585\n" | ./999999999/0/1603_3_12.py \
  --actionem-sparql --de=P --query --ex-interlinguis \
  | ./999999999/0/1603_3_12.py --actionem-sparql --csv --hxltm \
  > 999999/0/P1585.tm.hxl.csv

printf "P1585\n" | ./999999999/0/1603_3_12.py \
  --actionem-sparql --de=P --query --lingua-divisioni=20 --lingua-paginae=1 \
  | ./999999999/0/1603_3_12.py --actionem-sparql --csv --hxltm \
  > 999999/0/P1585.wikiq~1-20.hxl.csv

printf "P1585\n" | ./999999999/0/1603_3_12.py \
  --actionem-sparql --de=P --query --lingua-divisioni=20 --lingua-paginae=2 \
  | ./999999999/0/1603_3_12.py --actionem-sparql --csv --hxltm \
  > 999999/0/P1585.wikiq~2-20.hxl.csv

printf "P1585\n" | ./999999999/0/1603_3_12.py \
  --actionem-sparql --de=P --query --lingua-divisioni=20 --lingua-paginae=3 \
  | ./999999999/0/1603_3_12.py --actionem-sparql --csv --hxltm \
  > 999999/0/P1585.wikiq~3-20.hxl.csv

hxlmerge --keys='#item+conceptum+codicem' \
  --tags='#item+rem' \
  --merge="999999/0/P1585.wikiq~1-20.hxl.csv" \
  "999999/0/P1585.wikiq~2-20.hxl.csv" \
  >"999999/0/P1585.wikiq~1+2-20.hxl.csv"

sed -i '1d' "999999/0/P1585.wikiq~1+2-20.hxl.csv"

hxlmerge --keys='#item+conceptum+codicem' \
  --tags='#item+rem' \
  --merge="999999/0/P1585.wikiq~1+2-20.hxl.csv" \
  "999999/0/P1585.wikiq~3-20.hxl.csv" \
  >"999999/0/P1585.wikiq~1+2+3-20.hxl.csv"

sed -i '1d' "999999/0/P1585.wikiq~1+2-20.hxl.csv"
