#!/bin/bash
#===============================================================================
#
#          FILE:  1603_0_1603.sh
#
#         USAGE:  ./999999999/1603_0_1603.sh
#                 DE_FACTUM=1 ./999999999/1603_0_1603.sh
#
#   DESCRIPTION:  1603_0_1603.sh is a manual purge of files. Is not intented
#                 to be run automatically
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.0
#       CREATED:  2022-01-28 20:18 UTC started
#      REVISION:  ---
#===============================================================================
set -e

ROOTDIR="$(pwd)"

echo "TODO $0"

# tutorial https://opensource.com/article/18/5/you-dont-know-bash-intro-bash-arrays
PURGATORIA_CONCEPTUM=()
PURGATORIA_EXTENSIONEM=( "no1.tm.hxl.csv" "tm.hxl.csv" )

PURGATORIA_CONCEPTUM+=( "1603_1_1" )
PURGATORIA_CONCEPTUM+=( "1603_1_51" )
PURGATORIA_CONCEPTUM+=( "1603_25_1" )

DE_FACTUM="${DE_FACTUM:-''}"
# DRYRUM="0"



#######################################
# numerordiatio_caput extract from no1.tm.hxl.csv some quick metadata.
# Mostly focused on patters of the headings.
#
# Globals:
#   ROOTDIR
#   PURGATORIA
#   PURGATORIA_EXTENSIONEM
#   DE_FACTUM
# Arguments:
#   basim
# Outputs:
#   HXLated tabular output (not HXLTM neither Numeroordinatio)
#######################################
purgatoria() {
  basim="$1"
  shopt -s nullglob globstar
  # for i in "$basim/"**/*no1.tm.hxl.csv; do
  echo "PURGATORIA_CONCEPTUM (${PURGATORIA_CONCEPTUM[*]})"

  for i in "$basim/"**/**."${PURGATORIA_EXTENSIONEM[@]}"; do
    archivum=$(basename "$i")
    conceptum="${archivum%%.*}"
    echo "Candidate [$i] [$conceptum]"

    for item in "${PURGATORIA_CONCEPTUM[@]}"; do
      if [[ "$conceptum" == "$item" ]]; then
        # echo "    needs purge $i"
        # echo "    DE_FACTUM [${DE_FACTUM}]"
        if [ -n "$DE_FACTUM" ]; then
          echo "    $conceptum"
          echo "        rm $i"
        else
          echo "    needs purge (DE_FACTUM=1) $i"
        fi
        # rm "$i"
      fi
    done
  done
}


echo "${PURGATORIA[@]}"

# Production directory
purgatoria "1603"

# Temporary directory
purgatoria "999999/1603"
