#!/bin/sh
#===============================================================================
#
#          FILE:  s3sync.sh
#
#         USAGE:  ./999999999/0/s3sync.sh 1603_NN_NN
#                 time ./999999999/s3sync.sh 1603_NN_NN
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

# See also
# - https://github.com/s3tools/s3cmd)
# - https://github.com/marketplace/actions/use-s3cmd

# https://console.wasabisys.com/#/file_manager/lsf1603/
# https://s3.wasabisys.com/lsf1603/63/101/1603_63_101.mul-Latn.codex.pdf
