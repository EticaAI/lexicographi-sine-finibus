#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  999999999_521850.py
#
#         USAGE:  ./999999999/0/999999999_521850.py
#                 ./999999999/0/999999999_521850.py --help
#
#   DESCRIPTION:  RUN /999999999/0/999999999_521850.py --help
#                - Q521850, https://www.wikidata.org/wiki/Q521850
#                  - data scraping (Q521850)
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:  ---
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0.0
#       CREATED:  2022-07-27 04:59 UTC based on 999999999_10263485
#      REVISION:  ---
# ==============================================================================

import sys
import argparse
import csv
import re
from pathlib import Path
from os.path import exists

from functools import reduce
from typing import (
    Any,
    # Dict,
    # List,
)

from L999999999_0 import (
    # hxltm_carricato,
    TabulaAdHXLTM
)

import yaml

import xml.etree.ElementTree as XMLElementTree

STDIN = sys.stdin.buffer

NOMEN = '999999999_521850'

DESCRIPTION = """
{0} Generic pre-processor for data scrapping. Mostly access external services
and prepare their data to HXLTM (which then can be reused by rest of the
tools)

Trivia:
- Q521850, https://www.wikidata.org/wiki/Q521850
  - data scraping (Q521850)
""".format(__file__)

__EPILOGUM__ = """
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
    {0} --methodus=undata

    {0} --methodus=unhcr

    {0} --methodus=unochafts

    {0} --methodus=unwpf

    {0} --methodus=worldbank

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
""".format(__file__)

DATA_SCRAPPING_HELP = {
    'UNDATA': [
        'https://data.un.org/'
    ],
    'UNHCR': [
        'https://www.unhcr.org/global-public-api.html',
        'https://data.unhcr.org/en/geoservices/',
    ],
    'UNOCHAFTS': [
        'https://fts.unocha.org/'
    ],
    'UNWPF': [
        'https://geonode.wfp.org/',
    ],
    'WORLDBANK': [
        'https://data.worldbank.org/',
        # Total population
        'https://data.worldbank.org/indicator/SP.POP.TOTL',
    ],
}

# LIKELY_NUMERIC = [
#     '#item+conceptum+codicem',
#     '#status+conceptum',
#     '#item+rem+i_qcc+is_zxxx+ix_n1603',
#     '#item+rem+i_qcc+is_zxxx+ix_iso5218',
# ]
# # https://en.wiktionary.org/wiki/tabula#Latin
# XML_AD_CSV_TABULAE = {
#     'CO_UNIDADE': 'CO_UNIDADE',
#     'NO_FANTASIA': 'NO_FANTASIA',
#     'CO_MUNICIPIO_GESTOR': 'CO_MUNICIPIO_GESTOR',
#     'NU_CNPJ': 'NU_CNPJ',
#     'CO_CNES': 'CO_CNES',
#     'DT_ATUALIZACAO': 'DT_ATUALIZACAO',
#     'TP_UNIDADE': 'TP_UNIDADE',
# }

# CSV_AD_HXLTM_TABULAE = {
#     # @TODO: create wikiq
#     'CO_UNIDADE': '#item+rem+i_qcc+is_zxxx+ix_brcnae',
#     'NO_FANTASIA': '#meta+NO_FANTASIA',
#     'CO_MUNICIPIO_GESTOR': '#item+rem+i_qcc+is_zxxx+ix_wdatap1585',
#     'NU_CNPJ': '#item+rem+i_qcc+is_zxxx+ix_wdatap6204',
#     'CO_CNES': '#meta+CO_CNES',
#     'DT_ATUALIZACAO': '#meta+DT_ATUALIZACAO',
#     'TP_UNIDADE': '#meta+TP_UNIDADE',
# }

# SYSTEMA_SARCINAE = str(Path(__file__).parent.resolve())
# PROGRAMMA_SARCINAE = str(Path().resolve())
# ARCHIVUM_CONFIGURATIONI_DEFALLO = [
#     SYSTEMA_SARCINAE + '/' + NOMEN + '.meta.yml',
#     PROGRAMMA_SARCINAE + '/' + NOMEN + '.meta.yml',
# ]

# ./999999999/0/999999999_521850.py 999999/0/1603_1_1--old.csv 999999/0/1603_1_1--new.csv


class Cli:

    EXIT_OK = 0
    EXIT_ERROR = 1
    EXIT_SYNTAX = 2

    def __init__(self):
        """
        Constructs all the necessary attributes for the Cli object.
        """

    def _quod_configuratio(self, archivum_configurationi: str = None) -> dict:
        """_quod_configuratio

        Args:
            archivum_configurationi (str, optional):

        Returns:
            (dict):
        """
        archivae = ARCHIVUM_CONFIGURATIONI_DEFALLO
        if archivum_configurationi is not None:
            if not exists(archivum_configurationi):
                raise FileNotFoundError(
                    'archivum_configurationi {0}'.format(
                        archivum_configurationi))
            archivae.append(archivum_configurationi)

        for item in archivae:
            if exists(item):
                with open(item, "r") as read_file:
                    datum = yaml.safe_load(read_file)
                    return datum

    def make_args(self, hxl_output=True):
        # parser = argparse.ArgumentParser(description=DESCRIPTION)
        parser = argparse.ArgumentParser(
            prog="999999999_10263485",
            description=DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=__EPILOGUM__
        )

        parser.add_argument(
            'infile',
            help='Arquivo de entrada',
            nargs='?'
        )

        parser.add_argument(
            '--methodus',
            help='Modo de operação.',
            dest='methodus',
            nargs='?',
            choices=[
                'undata',  # https://data.un.org/
                'unochafts',  # https://fts.unocha.org/
                'unhcr',  # https://www.unhcr.org/global-public-api.html
                          # https://data.unhcr.org/en/geoservices/
                'unwpf',  # https://geonode.wfp.org/
                'worldbank',  # https://data.worldbank.org/
            ],
            # required=True
            default='undata'
        )

        # objectīvum, n, s, nominativus,
        #                       https://en.wiktionary.org/wiki/objectivus#Latin
        # fōrmātō, n, s, dativus, https://en.wiktionary.org/wiki/formatus#Latin
        parser.add_argument(
            '--objectivum-formato',
            help='Formato do arquivo exportado',
            dest='objectivum_formato',
            nargs='?',
            choices=[
                'csv',
                'tsv',
                'hxl_csv',
                'hxl_tsv',
                'hxltm_csv',
                'hxltm_tsv',
            ],
            # required=True
            default='csv'
        )

        # archīvum, n, s, nominativus, https://en.wiktionary.org/wiki/archivum
        # cōnfigūrātiōnī, f, s, dativus,
        #                      https://en.wiktionary.org/wiki/configuratio#Latin
        # parser.add_argument(
        #     '--archivum-configurationi',
        #     help='Arquivo de configuração .meta.yml',
        #     dest='archivum_configurationi',
        #     nargs='?',
        #     default=None
        # )

        # parser.add_argument(
        #     'outfile',
        #     help='Output file',
        #     nargs='?'
        # )

        return parser.parse_args()

    def execute_cli(self, pyargs, stdin=STDIN, stdout=sys.stdout,
                    stderr=sys.stderr):
        # self.pyargs = pyargs

        _infile = None
        _stdin = None

        # configuratio = self._quod_configuratio(pyargs.archivum_configurationi)

        if stdin.isatty():
            # print("ERROR. Please pipe data in. \nExample:\n"
            #       "  cat data.txt | {0} --actionem-quod-sparql\n"
            #       "  printf \"Q1065\\nQ82151\\n\" | {0} --actionem-quod-sparql"
            #       "".format(__file__))
            # print('non stdin')
            _infile = pyargs.infile
            # return self.EXIT_ERROR
        else:
            # print('est stdin')
            _stdin = stdin

        # print(pyargs.objectivum_formato)
        # print(pyargs)

        # if _stdin is not None:
        #     for line in sys.stdin:
        #         # print('oi')
        #         codicem = line.replace('\n', ' ').replace('\r', '')

        # hf = CliMain(self.pyargs.infile, self.pyargs.outfile)

        if pyargs.methodus == 'undata':
            print(DATA_SCRAPPING_HELP['UNDATA'])
            return self.EXIT_OK

        if pyargs.methodus == 'unhcr':
            print(DATA_SCRAPPING_HELP['UNHCR'])
            return self.EXIT_OK


        if pyargs.methodus == 'unochafts':
            print(DATA_SCRAPPING_HELP['UNOCHAFTS'])
            return self.EXIT_OK

        if pyargs.methodus == 'unwpf':
            print(DATA_SCRAPPING_HELP['UNWPF'])
            return self.EXIT_OK

        if pyargs.methodus == 'worldbank':
            print(DATA_SCRAPPING_HELP['WORLDBANK'])
            return self.EXIT_OK

        print('Unknow option.')
        return self.EXIT_ERROR



if __name__ == "__main__":

    est_cli = Cli()
    args = est_cli.make_args()

    est_cli.execute_cli(args)
