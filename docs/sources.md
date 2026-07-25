---
layout: default
title: Fonti dei dati
nav_order: 93
permalink: /sources/
description: "Le fonti dei dati alla base di ITTxGNN: dati di registrazione AIFA, TxGNN, ClinicalTrials.gov, PubMed e DrugBank."
---

# Fonti dei dati

<div class="key-takeaway">
Ogni conclusione è riconducibile a una fonte di dati pubblica — nulla è una scatola nera.
</div>

---

## Panoramica delle fonti

<table class="comparison-table">
<thead>
<tr><th>Tipo</th><th>Fonte</th><th>Utilizzata per</th></tr>
</thead>
<tbody>
<tr><td>Dati di registrazione</td><td><a href="https://www.aifa.gov.it/">AIFA</a></td><td>Elenco dei farmaci approvati e dei principi attivi per l'Italia</td></tr>
<tr><td>Modello di previsione</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Previsione delle associazioni farmaco&ndash;malattia</td></tr>
<tr><td>Studi clinici</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Classificazione delle prove (NCT)</td></tr>
<tr><td>Letteratura</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Classificazione delle prove (PMID)</td></tr>
<tr><td>Informazioni sui farmaci</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Mappatura dei principi attivi e dati sui bersagli</td></tr>
<tr><td>Interazioni</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Dati sulle interazioni tra farmaci</td></tr>
</tbody>
</table>

---

## Licenze

Ogni fonte ha la propria licenza — si prega di verificarla prima di citarla:

- **TxGNN**: uso accademico; citare Huang et al. (2023)
- **ClinicalTrials.gov / PubMed**: dati pubblici del NIH statunitense
- **DrugBank**: uso non commerciale soggetto ai termini della relativa licenza
- **AIFA**: soggetta ai termini di open data dell'autorità regolatoria italiana

---

## Frequenza di aggiornamento

| Dati | Frequenza |
|------|-----------|
| Dati di registrazione | Come pubblicati dall'autorità regolatoria |
| Prove da studi clinici / letteratura | Raccolte nuovamente a intervalli periodici |
| Dati sulle interazioni | Riesaminati trimestralmente |

---

## Citazione accademica

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

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
