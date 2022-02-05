# Multilingual dictionaries
**[working draft] The Etica.AI + HXL-CPLP [monorepo](https://en.wikipedia.org/wiki/Monorepo) with public domain automation scripts for [practical lexicography](https://en.wikipedia.org/wiki/Lexicography) on selected topics. Goal of both compilation of existing translations ([such as Wikidata](https://www.wikidata.org/wiki/Wikidata:Licensing)) and preparation for new terminology translation initiatives.**

More about on:
- https://github.com/EticaAI/numerordinatio/issues/5
- https://numerordinatio.etica.ai/

Namespace explanations at [officinam/](officinam/).

## Disclaimers

**Individuals direct and indirect contributors of this project are not affiliated with external organizations. The use of labeled numerical namespaces (need to make easier for implementer) explicitly do not means endorsement of the organizations or theirs internal groups deciding the coding systems.**

Ad-hoc collaboration (such as bug fixes or suggestions to improve interoperability) between @EticaAI / @HXL-CPLP and individuals which work on any specific namespace cannot be considered formal endorsement of their organization.

Even reuse of work (in special pre-compiled translations, or tested workflows on how to re-generate then from external collaborators) cannot be assumed as endorsement by the work on this monorepo and final work do not need to be public domain as the translations. Such feature can also be called [data roundtripping](https://diff.wikimedia.org/2019/12/13/data-roundtripping-a-new-frontier-for-glam-wiki-collaborations/) and can be stimulated on call to actions such as [Wikiprojecs](https://m.wikidata.org/wiki/Wikidata:WikiProjects) or ad hoc initiatives such [TICO-19](https://tico-19.github.io/).

Please note that even successful projects such as GLAM (see [Wikimedia Commons Data Roundtripping Final Report](https://upload.wikimedia.org/wikipedia/commons/e/e8/Wikimedia_Commons_Data_Roundtripping_-_Final_report.pdf)) in addition to lack of more software and workflows, can have issues such as duplication of data import/export because of lack of consistent IDs. So as part of multilingual lexicography, for sake of re usability, we need to give something and already draft how others could do it. A lot of inspiration for this is [strategies used on scientific names](https://en.wikipedia.org/wiki/Scientific_name) (except that you don't need to know Latin grammar).

<!--
- https://www.wikidata.org/wiki/Wikidata:Linked_open_data_workflow
- https://www.youtube.com/watch?v=VOO8IS73Cq0&t=19473s
- praeparatio-ex-codex
  - (...)
- dictionaria-specificis
  - dictiōnāria specificīs; /specific group of dictionaries/@eng-Latn
- reconciliātiō de verba
  - reconciliātiō, f, s, (Nominative) https://en.wiktionary.org/wiki/reconciliatio#Latin
  - reconciliātiōnibus, f, pl, (Dative) https://en.wiktionary.org/wiki/reconciliatio#Latin
  - verba, n, pl, (Nominative) https://en.wiktionary.org/wiki/verbum#Latin
- reconciliātiō ergā verba
 - ergā (+ accusative) https://en.wiktionary.org/wiki/erga#Latin
 - verba, n, pl, (accussative)
 - reconciliātiō, f, s, (Nominative) https://en.wiktionary.org/wiki/reconciliatio#Latin
-->

## Licenses

> _Public domain means each issue only needs to be resolved once_

## Software license

[![Public Domain](https://i.creativecommons.org/p/zero/1.0/88x31.png)](UNLICENSE)

To the extent possible under law, [Etica.AI](https://github.com/EticaAI)
and non anonymous collaborators have waived all copyright and related or
neighboring rights to this work to [Public Domain](UNLICENSE).

Optionally, the [BSD Zero Clause License](https://spdx.org/licenses/0BSD.html)
is also one explicit alternative to the Unlicense as an older license approved
by the Open Source Initiative:

`SPDX-License-Identifier: Unlicense OR 0BSD`

## Creative content license (algorithms and concepts as pivot exchange for other data standards, and user documentation)

[![Public Domain](https://i.creativecommons.org/p/zero/1.0/88x31.png)](UNLICENSE)

To the extent possible under law, [Etica.AI](https://github.com/EticaAI)
and non anonymous collaborators have waived all copyright and related or
neighboring rights to this work to public domain dedication. As 2021, the
[CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/)
with **additional right** to you granted upfront:

- The collaborators explicitly waive any potential **patent rights** for
  algorithms/ideas. We also preemptively ask that potential requests from our
  heirs in unforeseen future in any jurisdiction be ignored by any regional or
  international court.

<details>
<summary>More context about this</summary>

This different license for creative content is mostly for lawyers who would
complain about use of Unlicense for creative content. More context (from the
point of open source) on waiving patent rigths explicitly (since no better license for
creative content do exist) is here: <https://opensource.org/faq#cc-zero>.

There is no interest by ourselves to do _patent troll_ (for monetary gain)
or allow abuse copyrights (to enforce companies, organizations, o
governments) even if:

- we directly strongly disagree
- some entity try to use us as proxy to enforce us some sort of boycott to any
  other entity.

Note that data exchange on humanitarian context, even outside global-like
war-time, already is quite complex and the need of accurate linguistic content
conversion still even more critical to not have know errors. While the idea of
stories behind cases like the "_黙殺_" ("_mokusatsu_") are disputable, the
modern tooling to deal with multilingual terminology (including used to
create dictionaries) is prone to human error.

</details>

## Other notices: about license and copyright of external data files

This software will use intermediate files to do data conciliation and check consistency between different providers. While this is useful as to allow feedback to fix human errors, such files have their own copyrights, sometimes incompatible between themselves. These cached files are not designed to be redistributed, but they exist for technical reasons on the pre-build. Such data is on _[`999999`] /namespace for intermediate cached files/_

At least part of the final compiled result on https://github.com/EticaAI/n-data can actually be viable for re-distribution fully public domain, despite both human and automated being based in part on datasets with incompatible licenses between themselves. Quite often best candidates refer to the same concepts such as country names, or facts, such as human body parts, so their non-altered forms do have copyright, but the facts themselves do not. This is on a case by case basis, **but our intent tends to be focused on helping the existing publishers to have direct access from donated translations for languages outside the English/French**.

This is why the repository https://github.com/EticaAI/multilingual-lexicography-automation have license, and https://github.com/EticaAI/n-data make no clains about copyright.