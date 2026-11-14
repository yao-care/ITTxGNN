---
layout: default
title: Guida per l'utente
nav_order: 92
permalink: /guide/
description: "Guida per l'utente di ITTxGNN: come cercare i farmaci, leggere i livelli di prova e interpretare le raccomandazioni."
---

# Guida per l'utente

<div class="key-takeaway">
Controlla prima il livello di prova, poi la raccomandazione, quindi leggi la letteratura di riferimento.
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

2 coppie farmaco–malattia previste su questo sito non compaiono in nessun altro dei 30 siti TxGNN.

<!-- site-data:end -->

## Cercare un farmaco

<ol class="actionable-steps">
<li>Usa il campo di ricerca in cima alla pagina (i nomi dei principi attivi danno risultati migliori rispetto ai nomi commerciali).</li>
<li>Oppure consulta l'elenco completo in <a href="{{ '/drugs/' | relative_url }}">Tutti i farmaci</a>.</li>
<li>Puoi anche navigare per livello di prova: <a href="{{ '/evidence-high/' | relative_url }}">elevato</a>, <a href="{{ '/evidence-medium/' | relative_url }}">moderato</a>, <a href="{{ '/evidence-low/' | relative_url }}">solo previsione del modello</a>.</li>
</ol>

---

## Leggere una scheda

<p class="key-answer" data-question="Che cosa significano i livelli di prova da L1 a L5?">
Ogni scheda farmaco elenca le nuove indicazioni previste e ciascuna indicazione riporta un livello di prova
da L1 a L5. <strong>L1 significa che più studi clinici randomizzati controllati di Fase 3 la supportano già; L5 significa
solo previsione del modello, senza prove sull'uomo.</strong> I criteri completi sono nella pagina
<a href="{{ '/methodology/' | relative_url }}">Metodologia</a>.
</p>

| Se vedi | Significa | Azione suggerita |
|-----------|----------|------------------|
| L1 / L2 | Esistono prove da studi clinici | Consulta i record NCT e PMID di riferimento |
| L3 / L4 | Prove osservazionali o precliniche | Considerala una pista di ricerca |
| L5 | Solo previsione del modello | Solo generazione di ipotesi; non utilizzabile come riferimento clinico |

---

## Citazione e tracciabilità

Ogni prova presente in una scheda riporta un identificativo tracciabile:

- **Numero NCT**: rimanda alla registrazione su ClinicalTrials.gov
- **PMID**: rimanda al record su PubMed
- **DrugBank ID**: rimanda ai dati su farmaci e bersagli

Si prega di leggere la letteratura di riferimento per verificare il contesto prima di citare qualsiasi conclusione di questa piattaforma.

---

## Domande frequenti

<p class="key-answer" data-question="Le previsioni possono essere usate in ambito clinico?">
<strong>No.</strong> Le previsioni di questa piattaforma sono piste di ricerca, non consulenze cliniche. Qualsiasi
applicazione clinica del riposizionamento dei farmaci deve superare una validazione completa tramite studi clinici e
una revisione regolatoria.
</p>

<p class="key-answer" data-question="Perché non riesco a trovare un determinato farmaco?">
Un principio attivo deve essere mappabile sul vocabolario DrugBank per essere incluso nella previsione. Estratti vegetali,
vaccini, eccipienti e altri elementi non catalogati da DrugBank non compaiono su questa piattaforma.
</p>

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
