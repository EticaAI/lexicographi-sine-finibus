# Multilingual lexicography automation
**[working draft] The Etica.AI + HXL-CPLP [monorepo](https://en.wikipedia.org/wiki/Monorepo) with public domain automation scripts for [practical lexicography](https://en.wikipedia.org/wiki/Lexicography) on selected topics. Goal of both compilation of existing translations ([such as Wikidata](https://www.wikidata.org/wiki/Wikidata:Licensing)) and preparation for new terminology translation initiatives.**


More about on:
- https://github.com/EticaAI/numerordinatio/issues/5
- https://numerordinatio.etica.ai/


Namespace explanations at [officinam/](officinam/).

<!--
> **Extra general current explanation**
>
> - The [EticaAI/multilingual-lexicography-automation](https://github.com/EticaAI/multilingual-lexicography-automation) uses writing system neutral codes to reference selected datasets and automation scripts to bootstrap them.
>   - When existing data exchange codes already have published numeric equivalence, such convention will be used.
>   - For relevant data standards without numeric alternative, we're already testing algorithmic **reversible** numeric mappings to be used as key
>     - Trivia: the least significant digits provide [error detection checks](https://en.wikipedia.org/wiki/Error_detection_and_correction) and [guidance on what base system](https://cs.stackexchange.com/questions/10318/the-math-behind-converting-from-any-base-to-any-base-without-going-through-base) was used to generate such mappings.
>       - While this is not as compact and beauty was well planned numeric codes, it still allow reduce burden of lexicography to not be able to publish up to date numeric equivalences.
> - The programs ([999999999](officinam/999999999)) and handcrafted data tables (`1613`), and overall taxonomy of organizing everything are public domain dedication. Pre-compiled multiplication tables (`2600`) are not creative work, so also public domain.
> - Whatever possible, we already priorize interlink with existing human translations (such as Wikidata) under public domain and plan to allow data consolidation / cross validation from different sources.
>   - Datasets under temporary working directory `999999`, while can work as a cache to avoid overload sources and (as everyone interests) check for inconsistencies, are not aimed for final usage.
>     - Our experiences trying to get authorized use even for humanitarian/emergency response (ironically even from humanitarian organizations, despite major use by other humanitarian actors) are underwhelming.
> - The repository [EticaAI/n-data](https://github.com/EticaAI/n-data) contains snapshots of compiled results of these automation scripts.
-->

## License
TL;DR: all content from `EticaAI/multilingual-lexicography-automation` are public domain dedication, with alternatives for jurisdictions where waiving rights is not possible.

### multilingual-lexicography-automation
#### Software files
> TODO: add public domain dedication here
#### Data files (automated multiplication tables and reference tables by our volunteers)
> TODO: add public domain dedication here

### Data files from external sources

> TODO: explain more
<!--
Content from _[`999999`] /namespace for intermediate cached files/_ (**not** distributed on `EticaAI/multilingual-lexicography-automation`, the repository you are reading now, and not part of intended final usage for users) have different licences, including incompatible between themselves. The default response on this topic is: all rights to it's authors. However, note that final compiled results (in addition to use neutral numbers, since name of standards and organizations do have rights) when reefer to facts, already are likely to be considered non-copyritable, so:

- This makes _viral_ document licenses such as [GNU Free Documentation License](https://en.wikipedia.org/wiki/GNU_Free_Documentation_License) not applicable to enforce global license.
- On extreme cases such as [Attribution-NoDerivs 3.0 IGO (CC BY-ND 3.0 IGO)](https://creativecommons.org/licenses/by-nd/3.0/igo/deed.en) with explicitly forbidden derivated still not apply for material already in the public domain.
-->