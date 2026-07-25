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
