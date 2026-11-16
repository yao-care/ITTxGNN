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

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## Italia: dati di questo sito

Questo sito pubblica rapporti su **{{ site.data.drug_stats.total_drugs }}** medicinali presenti nelle [liste AIFA dei farmaci di classe A e H](https://www.aifa.gov.it/en/liste-farmaci-a-h) (Italia); la classe C non è inclusa.

Set di dati: [AIFA: liste dei farmaci di classe A e H](https://www.aifa.gov.it/en/liste-farmaci-a-h); viene scaricato e confrontato automaticamente ogni settimana (il lunedì). Dettagli: [Fonti dei dati]({{ '/sources/' | relative_url }}).

Rapporti per livello di evidenza:

| Livello di evidenza | Rapporti | Quota |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

45 coppie farmaco–malattia previste su questo sito non compaiono in nessun altro dei 30 siti TxGNN.

<!-- site-data:end -->

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
