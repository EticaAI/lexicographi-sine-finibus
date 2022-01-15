# [`1603:3:12`] /Wikidata/

- "Wikidata:Database reports/List of properties/all"
  - https://www.wikidata.org/wiki/Wikidata:Database_reports/List_of_properties/all


## Example queries

###
- Thanks https://stackoverflow.com/questions/43258341/how-to-get-wikidata-labels-in-more-than-one-language

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

SELECT DISTINCT ?RegionIT ?label (lang(?label) as ?label_lang) ?ISO_code ?Geo
{
?RegionIT wdt:P31 wd:Q16110;
wdt:P300 ?ISO_code; 
wdt:P625 ?Geo ;
rdfs:label ?label
}
order by ?RegionIT
```

[LINK](https://query.wikidata.org/#PREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20wikibase%3A%20%3Chttp%3A%2F%2Fwikiba.se%2Fontology%23%3E%0APREFIX%20wd%3A%20%3Chttp%3A%2F%2Fwww.wikidata.org%2Fentity%2F%3E%0APREFIX%20wdt%3A%20%3Chttp%3A%2F%2Fwww.wikidata.org%2Fprop%2Fdirect%2F%3E%0A%0ASELECT%20DISTINCT%20%3FRegionIT%20%3Flabel%20%28lang%28%3Flabel%29%20as%20%3Flabel_lang%29%20%3FISO_code%20%3FGeo%0A%7B%0A%3FRegionIT%20wdt%3AP31%20wd%3AQ16110%3B%0Awdt%3AP300%20%3FISO_code%3B%20%0Awdt%3AP625%20%3FGeo%20%3B%0Ardfs%3Alabel%20%3Flabel%0A%7D%0Aorder%20by%20%3FRegionIT)
