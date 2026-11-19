---
layout: default
title: Download
nav_order: 94
permalink: /downloads/
description: "Download dei dati aperti di ITTxGNN: risorse FHIR, risultati delle previsioni e indice di ricerca."
---

# Download

<div class="key-takeaway">
Le previsioni sono pubblicate in formato FHIR R4, pronte per l'integrazione con i sistemi di cartella clinica elettronica.
</div>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Italia: cosa contengono ora i file

| File | Contenuto attuale |
|---|---|
| `/data/search-index.json` | {{ site.data.local_facts.files.search_index }} medicinali con le indicazioni previste |
| `/data/drugs.json` | {{ site.data.local_facts.files.drugs_json }} medicinali con livello di evidenza e indicazione originale |
| `/fhir/MedicationKnowledge/` | {{ site.data.local_facts.fhir.medication_knowledge }} risorse MedicationKnowledge (una per medicinale) |
| `/fhir/ClinicalUseDefinition/` | {{ site.data.local_facts.fhir.clinical_use_definition }} risorse ClinicalUseDefinition (una per indicazione prevista) |

Riutilizzo del set di dati locale: [AIFA: liste dei farmaci di classe A e H](https://www.aifa.gov.it/en/liste-farmaci-a-h), pubblicato da Agenzia Italiana del Farmaco (AIFA); il riutilizzo è regolato dalle condizioni dell'editore e questo sito non concede ulteriori diritti.

{% if site.data.local_facts.top_licensed.size > 0 %}Medicinali con più confezioni AIFA (AIC) autorizzate: {% for r in site.data.local_facts.top_licensed limit: 5 offset: 3 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Ultime correzioni nel registro delle verifiche: {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 16 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

<!-- local-facts:end -->

## Risorse FHIR

Questo sito pubblica le previsioni come risorse FHIR R4, utilizzabili direttamente dalle app SMART on FHIR:

| Risorsa | Percorso | Descrizione |
|----------|------|-------------|
| CapabilityStatement | `/fhir/metadata` | Dichiarazione delle funzionalità del server FHIR |
| MedicationKnowledge | `/fhir/MedicationKnowledge/` | Risorse sui farmaci |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/` | Indicazioni previste |
| Bundle | `/fhir/Bundle/all-predictions.json` | Tutte le previsioni raccolte in un bundle |

---

## Indice di ricerca

`/data/search-index.json` fornisce un indice di ricerca di farmaci e indicazioni, utile per costruire la propria
interfaccia di consultazione.

---

## Condizioni d'uso

<ol class="actionable-steps">
<li>I dati di questo sito sono <strong>destinati esclusivamente a fini di ricerca</strong> e non devono essere utilizzati come base per decisioni mediche.</li>
<li>In caso di citazione, attribuire il credito a ITTxGNN (藥提醒科技有限公司) e citare l'articolo originale su TxGNN.</li>
<li>I dati derivati restano soggetti ai termini di licenza di ciascuna fonte originale (vedi <a href="{{ '/sources/' | relative_url }}">Fonti dei dati</a>).</li>
</ol>

---

## Informazioni sullo Sviluppatore

Questa piattaforma è sviluppata e gestita da **藥提醒科技有限公司** (yao.care). Le informazioni sull'azienda,
il contesto del modello TxGNN e l'elenco completo dei siti della linea di prodotti si trovano nella pagina
<a href="{{ '/about/' | relative_url }}">Informazioni</a>.

---

<div class="disclaimer">
<strong>Esclusione di responsabilità</strong><br>
Il presente rapporto ha finalità esclusivamente di ricerca accademica e <strong>non costituisce un parere medico</strong>. Seguire sempre le indicazioni del proprio medico; non modificare mai la terapia di propria iniziativa. Qualsiasi decisione di riposizionamento di un farmaco richiede una validazione clinica completa e una revisione regolatoria.
<br><br>
<small>Revisionato da: 藥提醒科技有限公司 (yao.care)</small>
</div>
