#!/bin/bash
#===============================================================================
#
#          FILE:  s3sync.sh
#
#         USAGE:  ./999999999/0/s3sync.sh 1603_NN_NN
#                 time ./999999999/0/s3sync.sh 1603_63_101
#
#   DESCRIPTION:  @DEPRECATED. Logit moved to 999999999.lib.sh. No really
#                 necessary have additional script for this
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

#### Additional configurations, start __________________________________________

### Wasabi client configuration ------------------------------------------------
# - Create account with read/write access only to the desired bucked
# - Make sure it already works before trying to setup CDN

### CDN (If using Wasabi as CND + Cloudflare as frontend) ----------------------
# Check this documentations:
#   - https://wasabi-support.zendesk.com/hc/en-us/articles
#     /360000016712-How-do-I-set-up-Wasabi-for-user-access-separation-
#   - https://wasabi-support.zendesk.com/hc/en-us/articles
#     /360018526192-How-do-I-use-Cloudflare-with-Wasabi-?source=search
#
# Bucket name:
#   - lsf1603.etica.ai
# DNS Configuration (on CloudFlare frontend, if using eu-central-1)
#   > lsf1603 CNAME s3.eu-central-1.wasabisys.com

#### Additional configurations, end ____________________________________________

# #######################################
# # Test access
# #
# # Globals:
# #   ROOTDIR
# #   S3CFG
# # Arguments:
# #   numerordinatio
# # Outputs:
# #   Convert files
# #######################################
# s3cmd_access_test() {
#   numerordinatio="$1"
#   _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
#   _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
#   _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")
#   # _path_clean="${$_path/aa/bb}"
#   _path_clean=${_path/1603\//''}

#   _basim_fontem="${ROOTDIR}/$_path/"
#   _basim_objectivum="s3://lsf1603.etica.ai/$_path_clean/"

#   echo "_path_clean [$_path_clean]"
#   echo "_basim_objectivum [$_basim_objectivum]"

#   set -x
#   s3cmd ls "$_basim_objectivum" --list-md5 --config "$S3CFG"
#   s3cmd du "$_basim_objectivum" --config "$S3CFG"
#   s3cmd info "s3://lsf1603.etica.ai" --config "$S3CFG"
#   set +x

# }

# #######################################
# # Synchronization of files by numerordinatio
# #
# # Globals:
# #   ROOTDIR
# #   S3CFG
# # Arguments:
# #   numerordinatio
# # Outputs:
# #   Convert files
# #######################################
# s3cmd_sync_upload() {
#   numerordinatio="$1"
#   _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
#   _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
#   _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")
#   # _path_clean="${$_path/aa/bb}"
#   _path_clean=${_path/1603\//''}

#   _basim_fontem="${ROOTDIR}/$_path/"
#   _basim_objectivum="s3://lsf1603.etica.ai/$_path_clean/"

#   # echo "_path_clean [$_path_clean]"
#   # echo "_basim_objectivum [$_basim_objectivum]"
#   blue=$(tput setaf 4)
#   normal=$(tput sgr0)
#   printf "%40s\n" "${blue}${FUNCNAME[0]} [$numerordinatio]${normal}"
#   # echo "${FUNCNAME[0]} [$numerordinatio]"

#   # NOTE: we could implement explicit file patterns to (not) syncronize.
#   #       However, as long as local disk already have excatly what we need
#   #       Leave strict syncronization tend to be better

#   # NOTE: the current approach, if current directory does not have
#   #       all files re-generated, will delete files on the CDN. This is the
#   #       expected behavior (but means only syncronize really at the end
#   #       of operations)

#   # set -x
#   s3cmd sync "$_basim_fontem" "$_basim_objectivum" \
#     --recursive --delete-removed --acl-public \
#     --no-progress --stats \
#     --config "$S3CFG"
#   # set +x
# }

# s3cmd_access_test "$1"
# s3cmd_sync_upload "$1"
# upload_cdn "$1"
upload_cdn "$1"
# upload_cdn_test "$1"
