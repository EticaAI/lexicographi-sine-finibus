#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  999999999_826165.py
#
#         USAGE:  ./999999999/0/999999999_826165.py
#                 ./999999999/0/999999999_826165.py --help
#
#   DESCRIPTION:  RUN /999999999/0/999999999_826165.py --help
#                 - Q826165, https://www.wikidata.org/wiki/Q826165
#                   - Web Ontology Language
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                   - Required (without Cython)
#                     - pip install owlready2
#                   - For performance (~20% faster large ontologies)
#                     - pip install Cython owlready2
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:  ---
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0.0
#       CREATED:  2022-06-04 16:57 UTC based on 999999999_54872.py
#      REVISION:  ---
# ==============================================================================
# /opt/Protege-5.5.0/run.sh

# import json
import sys
import os
import argparse
# import csv
# import re
from pathlib import Path
from os.path import exists

# import json
from typing import Type
import yaml
# import urllib.request
# import requests

import owlready2

# Warning message at:
#     /home/fititnt/.local/lib/python3.8/site-packages/owlready2/driver.py:35

# l999999999_0 = __import__('999999999_0')
from L999999999_0 import (
    RDF_NAMESPACES_EXTRAS,
    bcp47_rdf_extension_poc,
    hxltm_carricato,
    HXLTMAdRDFSimplicis,
    rdf_namespaces_extras
)

STDIN = sys.stdin.buffer

NOMEN = '999999999_826165'

DESCRIPTION = """
{0} Draft!
""".format(__file__)

__EPILOGUM__ = """
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

    # TODO: this is a draft. not implemented


Temporary tests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    {0} --objectivum-formato=_temp_bcp47 --rdf-namespaces-archivo=\
999999999/1568346/data/hxlstandard-rdf-namespaces-example.hxl.csv \
999999999/1568346/data/unesco-thesaurus.bcp47g.tsv

    {0} --objectivum-formato=_temp_bcp47 --rdf-namespaces-archivo=\
999999999/1568346/data/hxlstandard-rdf-namespaces-example.hxl.csv \
--rdf-trivio=2 \
999999999/1568346/data/unesco-thesaurus.bcp47g.tsv

    {0} --objectivum-formato=_temp_bcp47 --rdf-namespaces-archivo=\
999999999/1568346/data/hxlstandard-rdf-namespaces-example.hxl.csv \
999999999/1568346/data/unesco-thesaurus.bcp47g.tsv \
| rapper --quiet --input=turtle --output=turtle /dev/fd/0

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
""".format(__file__)


# https://github.com/seebi/rdf.sh#installation
# /workspace/bin/rdf
# https://github.com/essepuntato/undo/blob/master/ontology/current/undo.ttl

# autopep8 --list-fixes ./999999999/0/999999999_826165.py
# pylint --disable=W0511,C0103,C0116 ./999999999/0/999999999_826165.py

SYSTEMA_SARCINAE = str(Path(__file__).parent.resolve())
PROGRAMMA_SARCINAE = str(Path().resolve())
ARCHIVUM_CONFIGURATIONI_DEFALLO = [
    SYSTEMA_SARCINAE + '/' + NOMEN + '.meta.yml',
    PROGRAMMA_SARCINAE + '/' + NOMEN + '.meta.yml',
]

VENANDUM_INSECTUM = bool(os.getenv('VENANDUM_INSECTUM', ''))

# - https://servicodados.ibge.gov.br/api/v1/localidades
#   /distritos?view=nivelado&oorderBy=municipio-id
# - https://servicodados.ibge.gov.br/api/v1/localidades
#   /municipios?view=nivelado&orderBy=id
# METHODUS_FONTI = {
#     'ibge_un_adm2': 'https://servicodados.ibge.gov.br/api' +
#     '/v1/localidades/municipios?view=nivelado&orderBy=id'
# }


class Cli:

    EXIT_OK = 0
    EXIT_ERROR = 1
    EXIT_SYNTAX = 2

    venandum_insectum: bool = False  # noqa: E701

    def __init__(self):
        """
        Constructs all the necessary attributes for the Cli object.
        """

    def make_args(self, hxl_output=True):
        # parser = argparse.ArgumentParser(description=DESCRIPTION)
        parser = argparse.ArgumentParser(
            prog="999999999_826165",
            description=DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=__EPILOGUM__
        )

        parser.add_argument(
            'infile',
            help='Input file',
            # required=False,
            nargs='?'
        )

        parser.add_argument(
            '--methodus',
            help='Modo de operação.',
            dest='methodus',
            nargs='?',
            choices=[
                'validate',
                # 'data-apothecae',
                # 'hxltm-explanationi',
                # 'opus-temporibus',
                # 'status-quo',
                # 'deprecatum-dictionaria-numerordinatio'
            ],
            # required=True
            default='ibge_un_adm2'
        )

        # objectīvum, n, s, nominativus,
        #                       https://en.wiktionary.org/wiki/objectivus#Latin
        # fōrmātō, n, s, dativus, https://en.wiktionary.org/wiki/formatus#Latin
        # @see about formats and discussion
        # - https://github.com/semantalytics/awesome-semantic-web#serialization
        # - https://ontola.io/blog/rdf-serialization-formats/
        # - doc.wikimedia.org/Wikibase/master/php/md_docs_topics_json.html
        parser.add_argument(
            '--objectivum-formato',
            help='Formato do arquivo exportado',
            dest='objectivum_formato',
            nargs='?',
            choices=[
                # 'text/csv',
                # # https://www.w3.org/TR/turtle/
                # 'application/x-turtle',
                # https://www.w3.org/TR/n-triples/
                'application/n-triples',
                # # http://ndjson.org/
                # # https://github.com/ontola/hextuples
                # # mimetype???
                # #  - https://stackoverflow.com/questions/51690624
                # #    /json-lines-mime-type
                # #  - https://github.com/wardi/jsonlines/issues/9
                # #  - https://bugzilla.mozilla.org/show_bug.cgi?id=1603986
                # #  - https://stackoverflow.com/questions/41609586
                # #    /loading-wikidata-dump
                # #    - Uses '.ndjson' as extension
                # 'application/x-ndjson',
                '_temp_bcp47',
            ],
            # required=True
            default='application/n-triples'
        )

        # # archīvum, n, s, nominativus, https://en.wiktionary.org/wiki/archivum
        # # cōnfigūrātiōnī, f, s, dativus,
        # #                      https://en.wiktionary.org/wiki/configuratio#Latin
        # # ex
        # # fontī, m, s, dativus, https://en.wiktionary.org/wiki/fons#Latin
        parser.add_argument(
            '--rdf-trivio',
            help='(Advanced) RDF bag; extract triples from tabular data from '
            'other groups than 1',
            dest='rdf_bag',
            nargs='?',
            # required=True,
            default='1'
        )

        parser.add_argument(
            '--rdf-namespaces-archivo',
            help='HXL file with additional RDF namespaces',
            dest='rdf_namespace_archivo',
            nargs='?',
            # required=True,
            default=None
        )

        # archīvum, n, s, nominativus, https://en.wiktionary.org/wiki/archivum
        # cōnfigūrātiōnī, f, s, dativus,
        #                      https://en.wiktionary.org/wiki/configuratio#Latin
        # ex
        # fontī, m, s, dativus, https://en.wiktionary.org/wiki/fons#Latin
        parser.add_argument(
            '--archivum-configurationi',
            help=f'Define a custom {NOMEN}.meta.yml path. Default will search '
            '{0}'.format(ARCHIVUM_CONFIGURATIONI_DEFALLO),
            dest='archivum_configurationi',
            nargs='?',
            # required=True,
            default=None
        )


        # praefīxum	, n, s, nominativus,
        #                         https://en.wiktionary.org/wiki/praefixus#Latin
        # cōnfigūrātiōnī, f, s, dativus,
        #                      https://en.wiktionary.org/wiki/configuratio#Latin
        # ex
        # fontī, m, s, dativus, https://en.wiktionary.org/wiki/fons#Latin
        # parser.add_argument(
        #     '--praefixum-configurationi-ex-fonti',
        #     help='Prefixo (separado por vírgula) que contém os metadados que'
        #     'ajudam a entender como HXLTM deveria ser serializado para RDF',
        #     dest='praefixum_configurationi',
        #     nargs='?',
        #     default=None
        # )

        parser.add_argument(
            # '--venandum-insectum-est, --debug',
            '--venandum-insectum-est', '--debug',
            help='Habilitar depuração? Informações adicionais',
            metavar="venandum_insectum",
            dest="venandum_insectum",
            action='store_const',
            const=True,
            default=False
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

        if stdin.isatty():
            _infile = pyargs.infile
            _stdin = False
        else:
            _infile = None
            _stdin = True


        go = owlready2.get_ontology("http://purl.obolibrary.org/obo/go.owl").load()
        obo = owlready2.get_namespace("http://purl.obolibrary.org/obo/")
        print(obo.GO_0000001.label)

        return self.EXIT_OK

        # # rdf_namespace_archivo
        # if pyargs.rdf_namespace_archivo:
        #     rdf_namespaces_extras(pyargs.rdf_namespace_archivo)
        #     # print(RDF_NAMESPACES_EXTRAS)
        #     # pass

        # # @TODO remove thsi temporary part
        # if pyargs.objectivum_formato == '_temp_bcp47':
        #     caput, data = hxltm_carricato(
        #         _infile, _stdin, punctum_separato="\t")
        #     # print(caput, data)
        #     # print('')
        #     meta = bcp47_rdf_extension_poc(
        #         caput, data, objective_bag=pyargs.rdf_bag)
        #     # print(json.dumps(meta, sort_keys=True ,ensure_ascii=False))
        #     # return self.EXIT_OK

        #     for prefix, iri in meta['prefixes'].items():
        #         print('@prefix {0}: <{1}> .'.format(prefix, iri))

        #     for triple in meta['triples']:
        #         print('{0} {1} {2} .'.format(triple[0], triple[1], triple[2]))

        #     return self.EXIT_OK

        # # _infile = None
        # # _stdin = None
        # configuratio = self.quod_configuratio(
        #     pyargs.archivum_configurationi, pyargs.praefixum_configurationi)
        # if pyargs.venandum_insectum or VENANDUM_INSECTUM:
        #     self.venandum_insectum = True

        # climain = CliMain(
        #     infile=_infile, stdin=_stdin,
        #     pyargs=pyargs,
        #     configuratio=configuratio,
        #     venandum_insectum=self.venandum_insectum
        # )

        # if pyargs.objectivum_formato == 'text/csv':
        #     return climain.actio()
        # if pyargs.objectivum_formato == 'application/x-turtle':
        #     return climain.actio()
        #     # return self.EXIT_OK
        # if pyargs.objectivum_formato == 'application/n-triples':
        #     return climain.actio()
        #     # return self.EXIT_OK

        # if pyargs.objectivum_formato == 'uri_fonti':
        #     print(METHODUS_FONTI[pyargs.methodus])
        #     return self.EXIT_OK

        # if pyargs.objectivum_formato == 'json_fonti':
        #     return climain.json_fonti(METHODUS_FONTI[pyargs.methodus])

        # if pyargs.objectivum_formato == 'json_fonti_formoso':
        #     return climain.json_fonti(
        #         METHODUS_FONTI[pyargs.methodus],
        #         formosum=True,
        #         # ex_texto=True
        #     )

        # if pyargs.objectivum_formato in ['csv', 'tsv']:
        #     if json_fonti_texto is None:
        #         json_fonti_texto = climain.json_fonti(
        #             METHODUS_FONTI[pyargs.methodus], ex_texto=True)
        #     # print('json_fonti_texto', json_fonti_texto)
        #     return climain.objectivum_formato_csv(json_fonti_texto)

        # if pyargs.objectivum_formato in [
        #         'hxl_csv', 'hxltm_csv', 'hxl_tsv', 'hxltm_tsv']:
        #     if json_fonti_texto is None:
        #         json_fonti_texto = climain.json_fonti(
        #             METHODUS_FONTI[pyargs.methodus], ex_texto=True)
        #     return climain.objectivum_formato_csv(json_fonti_texto)

        print('Unknow option.')
        return self.EXIT_ERROR

    # def quod_configuratio(
    #     self,
    #     archivum_configurationi: str = None,
    #     praefixum_configurationi: str = None
    # ) -> dict:
    #     """quod_configuratio

    #     Args:
    #         archivum_configurationi (str, optional):

    #     Returns:
    #         (dict):
    #     """
    #     praefixum = []
    #     if praefixum_configurationi:
    #         praefixum = praefixum_configurationi.split(',')

    #     if exists(archivum_configurationi):
    #         with open(archivum_configurationi, "r") as read_file:
    #             datum = yaml.safe_load(read_file)
    #             while len(praefixum) > 0:
    #                 ad_hoc = praefixum.pop(0)
    #                 if ad_hoc in datum:
    #                     datum = datum[ad_hoc]
    #                 else:
    #                     raise ValueError('{0} [{1}]: [{2}?]'.format(
    #                         archivum_configurationi,
    #                         praefixum_configurationi,
    #                         ad_hoc,
    #                     ))
    #             return datum

    #     raise FileNotFoundError(
    #         'archivum_configurationi {0}'.format(
    #             str(archivum_configurationi)))


# class CliMain:
#     """Remove .0 at the end of CSVs from data exported from XLSX and likely
#     to have numeric values (and trigger weird bugs)
#     """

#     delimiter = ','

#     hxltm_ad_rdf: Type['HXLTMAdRDFSimplicis'] = None
#     pyargs: dict = None
#     venandum_insectum: bool = False  # noqa

#     def __init__(
#             self, infile: str = None, stdin: bool = None,
#             pyargs: dict = None, configuratio: dict = None,
#             venandum_insectum: bool = False  # noqa
#     ):
#         """
#         Constructs all the necessary attributes for the Cli object.
#         """
#         self.infile = infile
#         self.stdin = stdin
#         self.pyargs = pyargs
#         self.objectivum_formato = pyargs.objectivum_formato
#         # self.methodus = pyargs.methodus
#         self.configuratio = configuratio
#         self.venandum_insectum = venandum_insectum

#         caput, datum = hxltm_carricato(infile, stdin)

#         # delimiter = ','
#         if self.objectivum_formato in ['tsv', 'hxltm_tsv', 'hxl_tsv']:
#             self.delimiter = "\t"
#         # print('oi HXLTMAdRDFSimplicis')
#         self.hxltm_ad_rdf = HXLTMAdRDFSimplicis(
#             configuratio, pyargs.objectivum_formato, caput, datum,
#             venandum_insectum=self.venandum_insectum
#         )

#         # methodus_ex_tabulae = configuratio['methodus'][self.methodus]

#         # self.tabula = TabulaAdHXLTM(
#         #     methodus_ex_tabulae=methodus_ex_tabulae,
#         #     methodus=self.methodus,
#         #     objectivum_formato=self.objectivum_formato
#         # )

#         # self.outfile = outfile
#         # self.header = []
#         # self.header_index_fix = []

#     def actio(self):
#         # āctiō, f, s, nominativus, https://en.wiktionary.org/wiki/actio#Latin
#         if self.pyargs.objectivum_formato == 'text/csv':
#             return self.hxltm_ad_rdf.resultatum_ad_csv()
#         if self.pyargs.objectivum_formato == 'application/x-turtle':
#             return self.hxltm_ad_rdf.resultatum_ad_turtle()
#         if self.pyargs.objectivum_formato == 'application/n-triples':
#             raise NotImplementedError(
#                 'Use turtle output and pipe to rapper '
#                 '(raptor2-utils) or similar')
#             return self.hxltm_ad_rdf.resultatum_ad_ntriples()
#             # print('oi actio')
#             # numerordinatio_neo_separatum
#         # print('failed')


# def numerordinatio_neo_separatum(
#         numerordinatio: str, separatum: str = "_") -> str:
#     resultatum = ''
#     resultatum = numerordinatio.replace('_', separatum)
#     resultatum = resultatum.replace('/', separatum)
#     resultatum = resultatum.replace(':', separatum)
#     # TODO: add more as need
#     return resultatum


# def numerordinatio_ordo(numerordinatio: str) -> int:
#     normale = numerordinatio_neo_separatum(numerordinatio, '_')
#     return (normale.count('_') + 1)


# def numerordinatio_progenitori(
#         numerordinatio: str, separatum: str = "_") -> int:
#     # prōgenitōrī, s, m, dativus, https://en.wiktionary.org/wiki/progenitor
#     normale = numerordinatio_neo_separatum(numerordinatio, separatum)
#     _parts = normale.split(separatum)
#     _parts = _parts[:-1]
#     if len(_parts) == 0:
#         return "0"
#     return separatum.join(_parts)


if __name__ == "__main__":

    est_cli = Cli()
    args = est_cli.make_args()

    est_cli.execute_cli(args)
