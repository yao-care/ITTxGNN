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

Questa piattaforma è sviluppata e gestita da **藥提醒科技有限公司** (yao.care, numero di registrazione
societaria 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

ITTxGNN è il sito italiano della linea di prodotti "TxGNN Drug Repurposing" dell'azienda.
Lo stesso sistema è distribuito in 30 paesi e regioni, ciascuno denominato `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN e così via) all'indirizzo `{cc}txgnn.yao.care`.
Panoramica del prodotto: <https://www.yao.care/medical/txgnn/>.

Il modello TxGNN è stato sviluppato dallo Zitnik Lab della Harvard Medical School ed è stato pubblicato
su *Nature Medicine*. Questa piattaforma è il sistema di produzione che 藥提醒科技有限公司 ha costruito
su tale modello e comprende l'integrazione dei dati nazionali di registrazione dei farmaci, la previsione
combinata tramite grafo di conoscenza e deep learning, la classificazione delle prove da
PubMed / ClinicalTrials e l'integrazione con le cartelle cliniche elettroniche tramite SMART on FHIR.

---

<div class="disclaimer">
<strong>Esclusione di responsabilità</strong><br>
Il presente rapporto ha finalità esclusivamente di ricerca accademica e <strong>non costituisce un parere medico</strong>. Seguire sempre le indicazioni del proprio medico; non modificare mai la terapia di propria iniziativa. Qualsiasi decisione di riposizionamento di un farmaco richiede una validazione clinica completa e una revisione regolatoria.
<br><br>
<small>Revisionato da: 藥提醒科技有限公司 (yao.care)</small>
</div>
