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
# import re
from pathlib import Path
from os.path import exists

# from functools import reduce
from typing import (
    Any,
    # Dict,
    # List,
)
import zipfile

from L999999999_0 import (
    # hxltm_carricato,
    NUMERORDINATIO_BASIM,
    # TabulaAdHXLTM
)

import requests

try:
    from openpyxl import (
        load_workbook
    )
except ModuleNotFoundError:
    # Error handling
    pass
try:
    import xlrd
except ModuleNotFoundError:
    # Error handling
    pass

# import yaml

# import xml.etree.ElementTree as XMLElementTree

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
    {0} --methodus-fonti=undata

    {0} --methodus-fonti=unhcr

    {0} --methodus-fonti=unochafts

    {0} --methodus-fonti=unwpf

    {0} --methodus-fonti=worldbank --methodus=SP.POP.TOTL

    {0} --methodus-fonti=worldbank --methodus=SP.POP.TOTL \
--objectivum-formato=link-fonti

    {0} --methodus-fonti=worldbank --methodus=SP.POP.TOTL \
--objectivum-formato=csv

    {0} --methodus-fonti=worldbank --methodus=SP.POP.TOTL \
--objectivum-formato=hxltm

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

    def make_args(self):
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
            '--methodus-fonti',
            help='External data source',
            dest='methodus_fonti',
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

        parser.add_argument(
            '--methodus',
            help='Underlining method for the data source',
            dest='methodus',
            nargs='?',
            # default=None
            default='help'
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
                'hxltm',
                'link-fonti',
                # 'tsv',
                # 'hxl_csv',
                # 'hxl_tsv',
                # 'hxltm_csv',
                # 'hxltm_tsv',
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

        if pyargs.methodus_fonti == 'undata':
            if pyargs.methodus == 'help':
                print(DATA_SCRAPPING_HELP['UNDATA'])
                return self.EXIT_OK
            raise NotImplementedError
            return self.EXIT_OK

        if pyargs.methodus_fonti == 'unhcr':
            if pyargs.methodus == 'help':
                print(DATA_SCRAPPING_HELP['UNHCR'])
            return self.EXIT_OK

        if pyargs.methodus_fonti == 'unochafts':
            if pyargs.methodus == 'help':
                print(DATA_SCRAPPING_HELP['UNOCHAFTS'])
                return self.EXIT_OK
            raise NotImplementedError
            return self.EXIT_OK

        if pyargs.methodus_fonti == 'unwpf':
            if pyargs.methodus == 'help':
                print(DATA_SCRAPPING_HELP['UNWPF'])
            raise NotImplementedError
            return self.EXIT_OK

        if pyargs.methodus_fonti == 'worldbank':
            # print(DATA_SCRAPPING_HELP['WORLDBANK'])
            ds_worldbank = DataScrappingWorldbank(
                pyargs.methodus, pyargs.objectivum_formato)
            ds_worldbank.praeparatio()
            ds_worldbank.imprimere()
            return self.EXIT_OK

        print('Unknow option.')
        return self.EXIT_ERROR


class DataScrapping:

    def _hxlize_dummy(self, caput: list):
        resultatum = []
        for res in caput:
            if not res:
                resultatum.append('')
            else:
                resultatum.append(
                    '#meta+{0}'.format(res.lower().strip().replace(' ',
                                       '').replace('-', '_'))
                )
        return resultatum

    def de_csv_ad_csvnorm(self, fonti: str, objetivum: str, caput_initiali: list):
        # print("TODO de_csv_ad_csvnorm")
        with open(objetivum, 'w') as _objetivum:
            with open(fonti, 'r') as _fons:
                _csv_reader = csv.reader(_fons)
                _csv_writer = csv.writer(_objetivum)
                started = False
                for linea in _csv_reader:
                    # print(linea)
                    if not started:
                        if linea and linea[0].strip() in caput_initiali:
                            started = True
                        else:
                            continue
                    _csv_writer.writerow(linea)

        # print("TODO")
    def de_csv_ad_hxltm(self, fonti: str, objetivum: str, caput_initiali: list):
        # print("TODO de_csv_ad_csvnorm")
        with open(objetivum, 'w') as _objetivum:
            with open(fonti, 'r') as _fons:
                _csv_reader = csv.reader(_fons)
                _csv_writer = csv.writer(_objetivum)
                started = False
                for linea in _csv_reader:
                    # print(linea)
                    if not started:
                        if linea and linea[0].strip() in caput_initiali:
                            started = True
                            # @TODO remove this draft part
                            _csv_writer.writerow(self._hxlize_dummy(linea))
                            continue
                        else:
                            continue
                    _csv_writer.writerow(linea)

        # print("TODO")


class DataScrappingWorldbank(DataScrapping):

    methodus: str = 'SP.POP.TOTL'
    objectivum_formato: str = 'csv'
    # link_fonti: str = 'https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=excel'
    link_fonti: str = 'https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv'
    temp_fonti_csv: str = ''
    temp_fonti_hxltm: str = ''

    def __init__(self, methodus: str, objectivum_formato: str):

        self.methodus = methodus
        self.objectivum_formato = objectivum_formato

        # print('oioioi', self.dictionaria_codex )

    def imprimere(self, formatum: str = None) -> list:

        if self.objectivum_formato == 'link-fonti':
            print(self.link_fonti)
            return True

        fonti = self.temp_fonti_csv
        if self.objectivum_formato == 'hxltm':
            fonti = self.temp_fonti_hxltm

        with open(fonti, 'r') as _fons:
            _csv_reader = csv.reader(_fons)
            _csv_writer = csv.writer(sys.stdout)
            for linea in _csv_reader:
                _csv_writer.writerow(linea)

    def praeparatio(self):
        """praeparātiō

        Trivia:
        - praeparātiō, s, f, Nom., https://en.wiktionary.org/wiki/praeparatio
        """
        if self.objectivum_formato == 'link-fonti':
            # print(self.link_fonti)
            return True
        # self.temp_fonti = '{0}/999999/0/{1}~{2}.xls'.format(
        #     NUMERORDINATIO_BASIM, __class__.__name__, self.methodus
        # )
        temp_fonti_zip = '{0}/999999/0/{1}~{2}.zip'.format(
            NUMERORDINATIO_BASIM, __class__.__name__, self.methodus
        )
        self.temp_fonti_csv = '{0}/999999/0/{1}~{2}.csv'.format(
            NUMERORDINATIO_BASIM, __class__.__name__, self.methodus
        )
        temp_fonti_csvnorm = '{0}/999999/0/{1}~{2}.norm.csv'.format(
            NUMERORDINATIO_BASIM, __class__.__name__, self.methodus
        )
        self.temp_fonti_hxltm = '{0}/999999/0/{1}~{2}.tm.hxl.csv'.format(
            NUMERORDINATIO_BASIM, __class__.__name__, self.methodus
        )

        if not exists(temp_fonti_zip):
            # Download to local cache if alreayd there
            r = requests.get(self.link_fonti)
            with open(temp_fonti_zip, 'wb') as f:
                f.write(r.content)

        # zip file handler
        zip = zipfile.ZipFile(temp_fonti_zip)
        data_file_main = ''
        for _res in zip.namelist():
            if _res.lower().find('meta') > -1:
                continue
            if _res.lower().startswith('api_'):
                data_file_main = _res
        # list available files in the container
        # print(zip.namelist())

        # extract a specific file from the zip container
        f = zip.open(data_file_main)

        # save the extraced file
        content = f.read()
        f = open(self.temp_fonti_csv, 'wb')
        f.write(content)
        f.close()

        if self.objectivum_formato == 'hxltm':
            # print(self.link_fonti)
            self.de_csv_ad_csvnorm(
                self.temp_fonti_csv, temp_fonti_csvnorm, [
                    'Country Name', 'Country Code'
                ]
            )
            return self.de_csv_ad_hxltm(
                temp_fonti_csvnorm, self.temp_fonti_hxltm, [
                    'Country Name', 'Country Code'
                ]
            )


if __name__ == "__main__":

    est_cli = Cli()
    args = est_cli.make_args()

    est_cli.execute_cli(args)
