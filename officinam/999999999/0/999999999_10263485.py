#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  999999999_10263485.py
#
#         USAGE:  ./999999999/0/999999999_10263485.py
#                 ./999999999/0/999999999_10263485.py --help
#
#   DESCRIPTION:  RUn /999999999/0/999999999_10263485.py --help
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
#       CREATED:  2022-05-16 16:29 UTC based on hotfix0s.py
#      REVISION:  ---
# ==============================================================================

import sys
import argparse
import csv
import re

import xml.etree.ElementTree as XMLElementTree

STDIN = sys.stdin.buffer

DESCRIPTION = """
{0} Processamento de dados de referência do CNES (Cadastro Nacional de
Estabelecimentos de Saúde) do Brasil.

@see https://github.com/EticaAI/lexicographi-sine-finibus/issues/42

Trivia:
- Q10263485, https://www.wikidata.org/wiki/Q10263485
  - DATASUS
  - "DATASUS é o departamento de informática do Sistema Único de Saúde do
     Brasil. É responsável, também, pelos sistemas e aplicativos necessários
     para registrar e processar as informações de saúde. Um exemplo
     é o Cadastro Nacional de Estabelecimentos de Saúde (CNES), (...)"
""".format(__file__)

__EPILOGUM__ = """
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
    {0} --methodus=datasus-xmlcnae 999999/0/xmlCNES.xml
    cat 999999/0/xmlCNES.xml | {0} --methodus=datasus-xmlcnae


@TODO: fazer funcionar com stream de XML (não apenas por arquivo)
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
""".format(__file__)

LIKELY_NUMERIC = [
    '#item+conceptum+codicem',
    '#status+conceptum',
    '#item+rem+i_qcc+is_zxxx+ix_n1603',
    '#item+rem+i_qcc+is_zxxx+ix_iso5218',
]
# https://en.wiktionary.org/wiki/tabula#Latin
XML_AD_CSV_TABULAE = {
    'CO_UNIDADE': 'CO_UNIDADE',
    'NO_FANTASIA': 'NO_FANTASIA',
    'CO_MUNICIPIO_GESTOR': 'CO_MUNICIPIO_GESTOR',
    'NU_CNPJ': 'NU_CNPJ',
    'CO_CNES': 'CO_CNES',
    'DT_ATUALIZACAO': 'DT_ATUALIZACAO',
    'TP_UNIDADE': 'TP_UNIDADE',
}

CSV_AD_HXLTM_TABULAE = {
    # @TODO: create wikiq
    'CO_UNIDADE': '#item+rem+i_qcc+is_zxxx+ix_brcnae',
    'NO_FANTASIA': '#meta+NO_FANTASIA',
    'CO_MUNICIPIO_GESTOR': '#item+rem+i_qcc+is_zxxx+ix_wikip1585',
    'NU_CNPJ': '#item+rem+i_qcc+is_zxxx+ix_wikip6204',
    'CO_CNES': '#meta+CO_CNES',
    'DT_ATUALIZACAO': '#meta+DT_ATUALIZACAO',
    'TP_UNIDADE': '#meta+TP_UNIDADE',
}

# ./999999999/0/999999999_10263485.py 999999/0/1603_1_1--old.csv 999999/0/1603_1_1--new.csv


class Cli:

    EXIT_OK = 0
    EXIT_ERROR = 1
    EXIT_SYNTAX = 2

    def __init__(self):
        """
        Constructs all the necessary attributes for the Cli object.
        """

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
                'datasus-xmlcnae',
                # 'data-apothecae',
                # 'hxltm-explanationi',
                # 'opus-temporibus',
                # 'status-quo',
                # 'deprecatum-dictionaria-numerordinatio'
            ],
            # required=True
            default='datasus-xmlcnae'
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
                'hxltm-csv',
                'hxltm-tsv',
            ],
            # required=True
            default='csv'
        )

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

        if _stdin is not None:
            for line in sys.stdin:
                # print('oi')
                codicem = line.replace('\n', ' ').replace('\r', '')

        # hf = CliMain(self.pyargs.infile, self.pyargs.outfile)
        climain = CliMain(infile=_infile, stdin=_stdin,
                          objectivum_formato=pyargs.objectivum_formato)
        if pyargs.methodus == 'datasus-xmlcnae':
            return climain.execute_ex_datasus_xmlcnae()

        print('Unknow option.')
        return self.EXIT_ERROR


class CliMain:
    """Remove .0 at the end of CSVs from data exported from XLSX and likely
    to have numeric values (and trigger weird bugs)
    """

    def __init__(self, infile: str = None, stdin=None,
                 objectivum_formato: str = 'hxltm-csv'):
        """
        Constructs all the necessary attributes for the Cli object.
        """
        self.infile = infile
        self.stdin = stdin
        self.objectivum_formato = objectivum_formato

        # self.outfile = outfile
        self.header = []
        self.header_index_fix = []

    def process_row(self, row: list) -> list:
        if len(self.header) == 0:
            if row[0].strip().startswith('#'):
                self.header = row
                for index, item in enumerate(self.header):
                    item_norm = item.strip().replace(" ", "")
                    for likely in LIKELY_NUMERIC:
                        # print(item_norm, likely)
                        if item_norm.startswith(likely):
                            self.header_index_fix.append(index)
                # print('oi header', self.header_index_fix, self.header)
        else:
            for index_fix in self.header_index_fix:
                row[index_fix] = re.sub('\.0$', '', row[index_fix].strip())
        return row

    def execute_ex_datasus_xmlcnae(self):
        # print('@TODO copy logic from https://github.com/EticaAI/hxltm/blob/main/bin/hxltmdexml.py')

        _source = self.infile if self.infile is not None else self.stdin
        delimiter = ','
        if self.objectivum_formato in ['tsv', 'hxltm-tsv']:
            delimiter = "\t"
        objectivum = csv.writer(
            sys.stdout, delimiter=delimiter, quoting=csv.QUOTE_MINIMAL)

        # self.iteratianem = XMLElementTree.iterparse(
        iteratianem = XMLElementTree.iterparse(
            # source=self.fontem_archivum,
            # source=self.infile,
            source=_source,
            events=('start', 'end')
            # events=('end')
        )

        # print(iteratianem)

        # for item in iteratianem:
        # print(item)
        # print(item.text)

        # for event, elem in ET.iterparse(file_path, events=("start", "end")):

        caput = []
        caput22 = []
        caput_okay = False
        for event, elem in iteratianem:
            # if event == 'start':
            # path.append(elem.tag)
            #     pass
            # elif event == 'end':
            # print(elem.tag)
            # return 1
            if event == 'end':
                # print(elem)
                if elem.tag.upper() != 'ROW':
                    continue
                if hasattr(elem, 'attrib'):
                    lineam = []

                    for clavem, res in elem.attrib.items():
                        if caput_okay is False:
                            caput.append(clavem)
                            # caput22.append(clavem)
                        lineam.append(res)

                    if caput_okay is False and len(caput) > 0:
                        # if 'CO_CNES' in caput:
                        caput_okay = True
                        # print('OIOI', caput, caput22)
                        objectivum.writerow(caput)
                    if len(lineam) > 0:
                        objectivum.writerow(lineam)
                # process the tag
                # if elem.tag == 'name':
                #     if 'members' in path:
                #         print 'member'
                #     else:
                #         print 'nonmember'
                # path.pop()

        return Cli.EXIT_OK
        with open(self.infile, newline='') as infilecsv:
            with open(self.outfile, 'w', newline='') as outfilecsv:
                spamreader = csv.reader(infilecsv)
                spamwriter = csv.writer(outfilecsv)
                for row in spamreader:
                    # spamwriter.writerow(row)
                    spamwriter.writerow(self.process_row(row))
                    # self.data.append(row)

    def execute(self):
        with open(self.infile, newline='') as infilecsv:
            with open(self.outfile, 'w', newline='') as outfilecsv:
                spamreader = csv.reader(infilecsv)
                spamwriter = csv.writer(outfilecsv)
                for row in spamreader:
                    # spamwriter.writerow(row)
                    spamwriter.writerow(self.process_row(row))
                    # self.data.append(row)


if __name__ == "__main__":

    est_cli = Cli()
    args = est_cli.make_args()

    est_cli.execute_cli(args)