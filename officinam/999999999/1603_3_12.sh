#!/bin/sh
#===============================================================================
#
#          FILE:  1603_3_12.sh
#
#         USAGE:  ./999999999/1603_3_12.sh
#                 time ./999999999/1603_3_12.sh
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - Bash shell (or better)
#                 - wikibase-cli (https://github.com/maxlath/wikibase-cli)
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0
#       CREATED:  2022-01-10 11:03 UTC
#      REVISION:  ---
#===============================================================================
# Comment next line if not want to stop on first error
set -e

ROOTDIR="$(pwd)"

# @see https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples
# @see https://github.com/maxlath/wikibase-cli
# @see - https://www.wikidata.org/wiki/Template:Wikidata_list
#        - http://magnusmanske.de/wordpress/?p=301
# https://www.wikidata.org/wiki/Property:P299
# ISO 3166-1 numeric code (P299)

# https://w.wiki/4fHT
# SELECT ?country ?unm49 ?iso3166n ?iso3166p1a2 ?iso3166p1a3 ?osmrelid ?unescot ?usciafb ?usfips4 ?gadm
# WHERE
# {
#   ?country wdt:P31 wd:Q6256 ;
#   OPTIONAL { ?country wdt:P2082 ?unm49. }
#   OPTIONAL { ?country wdt:P299 ?iso3166n. }
#   OPTIONAL { ?country wdt:P297 ?iso3166p1a2. }
#   OPTIONAL { ?country wdt:P298 ?iso3166p1a3. }
#   OPTIONAL { ?country wdt:P402 ?osmrelid. }
#   OPTIONAL { ?country wdt:P3916 ?unescot. }
#   OPTIONAL { ?country wdt:P9948 ?usciafb. }
#   OPTIONAL { ?country wdt:P901 ?usfips4. }
#   OPTIONAL { ?country wdt:P8714 ?gadm. }   

#   SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
# }
echo "TODO 1603_3_12.sh"

exit 0
