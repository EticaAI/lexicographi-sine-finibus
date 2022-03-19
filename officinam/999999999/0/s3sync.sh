#!/bin/bash
#===============================================================================
#
#          FILE:  s3sync.sh
#
#         USAGE:  ./999999999/0/s3sync.sh 1603_NN_NN
#                 time ./999999999/0/s3sync.sh 1603_63_101
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - Bash shell (or better)
#                 - s3cmd (https://github.com/s3tools/s3cmd)
#                   - pip3 install s3cmd
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0
#       CREATED:  2022-03-19 06:35 UTC started
#      REVISION:  ---
#===============================================================================
# Comment next line if not want to stop on first error
set -e

_S3CFG="$HOME/.config/s3cfg/s3cfg-lsf1603.ini"
S3CFG="${S3CFG:-${_S3CFG}}"
ROOTDIR="$(pwd)"

# shellcheck source=../999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh

# See also
# - https://github.com/s3tools/s3cmd)
# - https://github.com/marketplace/actions/use-s3cmd
# - https://wasabi-support.zendesk.com/hc/en-us/articles/360000016712-How-do-I-set-up-Wasabi-for-user-access-separation-
# - https://monotai.com/howto-host-static-websites-on-wasabi.html
# - TODO: maybe also map a subdomain to a domain
#  - https://wasabi-support.zendesk.com/hc/en-us/articles/115001405332-How-do-I-map-a-Wasabi-public-file-s-to-a-website-

# https://console.wasabisys.com/#/file_manager/lsf1603/
# - https://s3.wasabisys.com/lsf1603/63/101/1603_63_101.mul-Latn.codex.pdf
# - https://lsf1603.s3.wasabisys.com/63/101/1603_63_101.mul-Latn.codex.pdf
# - https://lsf1603.s3.eu-central-1.wasabisys.com/63/101/1603_63_101.mul-Latn.codex.pdf
# - https://lsf1603.s3.wasabisys.com/
# Etica.AI DNS
# - lsf1603.etica.ai (cloudflare) -> lsf1603.s3.wasabisys.com
# - https://lsf1603.etica.ai/63/101/1603_63_101.mul-Latn.codex.pdf


# s3cmd info s3://lsf1603
# set -x
# s3cmd info --config "$S3CFG" s3://lsf1603
# s3cmd ls --config "$S3CFG" s3://lsf1603
# s3cmd la --config "$S3CFG"

#######################################
# Test access
#
# Globals:
#   ROOTDIR
#   S3CFG
# Arguments:
#   numerordinatio
# Outputs:
#   Convert files
#######################################
s3cmd_access_test() {
  numerordinatio="$1"
  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
  _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")
  # _path_clean="${$_path/aa/bb}"
  _path_clean=${_path/1603\//''}

  _basim_fontem="${ROOTDIR}/$_path/"
  _basim_objectivum="s3://lsf1603/$_path_clean/"

  echo "_path_clean [$_path_clean]"
  echo "_basim_objectivum [$_basim_objectivum]"

  set -x
  s3cmd ls "$_basim_objectivum" --config "$S3CFG"
  s3cmd du "$_basim_objectivum" --config "$S3CFG"
  s3cmd info "s3://lsf1603" --config "$S3CFG"
  set +x

}

#######################################
# Synchronization of files by numerordinatio
#
# Globals:
#   ROOTDIR
#   S3CFG
# Arguments:
#   numerordinatio
# Outputs:
#   Convert files
#######################################
s3cmd_sync_upload() {
  numerordinatio="$1"
  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
  _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")
  # _path_clean="${$_path/aa/bb}"
  _path_clean=${_path/1603\//''}

  _basim_fontem="${ROOTDIR}/$_path/"
  _basim_objectivum="s3://lsf1603/$_path_clean/"

  echo "_path_clean [$_path_clean]"
  echo "_basim_objectivum [$_basim_objectivum]"

  # s3cmd ls "$_basim_objectivum" --config "$S3CFG"
  # s3cmd du "$_basim_objectivum" --config "$S3CFG"
  # s3cmd info "s3://lsf1603" --config "$S3CFG"
  set -x
  # s3cmd sync --recursive "$_basim_fontem" "$_basim_objectivum" --delete-removed --dry-run --acl-public --config "$S3CFG"
  s3cmd sync --recursive "$_basim_fontem" "$_basim_objectivum" --delete-removed --acl-public --config "$S3CFG"
  set +x
}

# s3cmd_access_test "$1"
s3cmd_sync_upload "$1"
