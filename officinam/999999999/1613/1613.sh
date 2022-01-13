#!/bin/bash
#===============================================================================
#
#          FILE:  1613.sh
#
#         USAGE:  ./999999999/1613/1613.sh
#
#   DESCRIPTION:  ---
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
#       CREATED:  2022-01-13 16:43 UTC started, based on EticaAI/
#                                      HXL-CPLP/Auxilium-Humanitarium-API
#                                      /_systema/programma/download-hxl-datum.sh
#      REVISION: ---
#===============================================================================

# humanitarium_responsum_rem="https://proxy.hxlstandard.org/data/download/humanitarium-responsum-rem_hxl.csv?dest=data_edit&filter01=select&filter-label01=%23status%3E-1&select-query01-01=%23status%3E-1&filter02=cut&filter-label02=HXLated&cut-skip-untagged02=on&strip-headers=on&force=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4%2Fedit%23gid%3D1331879749"
DATA_1613="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1281616178"


ROOTDIR="$(pwd)"

# shellcheck source=../999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh


# if true ; then
#     echo ''
#     wget -qO- "$humanitarium_responsum_rem" > "${ROOTDIR}/999999/1613/vaccinum.tm.hxl.csv"
# fi
# wget -qO- "$humanitarium_responsum_rem" > "${ROOTDIR}/999999/1613/vaccinum.tm.hxl.csv"



#######################################
# Download 1603_45_49 from external source files
#
# Globals:
#   ROOTDIR
#   DATA_UN_M49_CSV
# Arguments:
#   None
# Outputs:
#   Writes to 999999/1603/45/49/1603_45_49.hxl.csv
#######################################
1613__external_fetch() {
  objectivum_archivum="${ROOTDIR}/999999/1613/1613.tm.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1613.tm.hxl.csv"

  if [ -z "$(stale_archive "$objectivum_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} stale data on [$objectivum_archivum], refreshing..."

  hxltmcli "$DATA_1613" > "$objectivum_archivum_temporarium"

  # curl --header "Accept: text/csv" \
  #   --compressed --silent --show-error \
  #   --get "$DATA_1613" \
  #   --output "$objectivum_archivum_temporarium"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}


1613__external_fetch
