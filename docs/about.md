---
layout: default
title: Informazioni
nav_order: 90
permalink: /about/
description: "ITTxGNN è una piattaforma di previsione per il riposizionamento dei farmaci sviluppata da 藥提醒科技有限公司 (yao.care), basata sul modello TxGNN di Harvard e dedicata ai medicinali approvati dall'AIFA in Italia."
---

# Informazioni

<div class="key-takeaway">
Accelerare la validazione delle prove sul riposizionamento dei farmaci con l'IA — dalla previsione alle prove in un colpo d'occhio.
</div>

---

## Contesto

<p class="key-answer" data-question="Che cos'è ITTxGNN?">
<strong>ITTxGNN</strong> è una piattaforma di supporto alla ricerca sul riposizionamento dei farmaci, basata sul modello TxGNN
pubblicato su <em>Nature Medicine</em> dallo Zitnik Lab dell'Università di Harvard. Prevede
l'ampliamento delle indicazioni terapeutiche per i medicinali approvati dall'AIFA in Italia. Oltre ai punteggi di previsione dell'IA,
la piattaforma integra prove cliniche provenienti da ClinicalTrials.gov e PubMed, così che i ricercatori possano
valutare rapidamente quanto sia attendibile ciascuna previsione.
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

## Che cos'è il riposizionamento dei farmaci?

<p class="key-answer" data-question="Che cos'è il riposizionamento dei farmaci?">
<strong>Il riposizionamento dei farmaci</strong> consiste nell'individuare nuovi impieghi terapeutici per medicinali già esistenti.
Rispetto allo sviluppo di un nuovo farmaco da zero — dai 10 ai 15 anni e da 1 a 2 miliardi di dollari USA —
il riposizionamento richiede dai 3 ai 5 anni e da 100 a 300 milioni di dollari USA, e i dati di sicurezza sull'uomo sono già disponibili,
per cui il rischio di fallimento è inferiore.
</p>

<table class="comparison-table">
<thead>
<tr><th>Aspetto</th><th>Sviluppo di un nuovo farmaco</th><th>Riposizionamento dei farmaci</th></tr>
</thead>
<tbody>
<tr><td>Tempo</td><td>10&ndash;15 anni</td><td>3&ndash;5 anni</td></tr>
<tr><td>Costo</td><td>1&ndash;2 miliardi di USD</td><td>100&ndash;300 milioni di USD</td></tr>
<tr><td>Dati di sicurezza</td><td>Devono essere generati</td><td>Dati sull'uomo già disponibili</td></tr>
<tr><td>Rischio di fallimento</td><td>Molto elevato (&gt;90%)</td><td>Inferiore</td></tr>
</tbody>
</table>

---

## Che cos'è TxGNN?

<p class="key-answer" data-question="Che cos'è TxGNN?">
<a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> è un modello di deep learning
sviluppato dallo Zitnik Lab della Harvard Medical School e pubblicato su <em>Nature Medicine</em>.
Prevede nuove associazioni farmaco&ndash;malattia ed è il primo modello di base per il riposizionamento
dei farmaci progettato specificamente per i clinici.
</p>

<blockquote class="expert-quote">
"TxGNN integra un grafo di conoscenza di 17.080 entità biomediche e utilizza reti neurali a grafo
per apprendere le relazioni complesse tra i nodi, prevedendo la potenziale efficacia dei farmaci contro
le malattie rare."
<cite>&mdash; Huang et al., Nature Medicine (2023)</cite>
</blockquote>

---

## Fonti dei dati

<table class="comparison-table">
<thead>
<tr><th>Tipo</th><th>Fonte</th><th>Descrizione</th></tr>
</thead>
<tbody>
<tr><td>Previsione IA</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Modello di previsione su grafo di conoscenza di Harvard</td></tr>
<tr><td>Studi clinici</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Registro globale degli studi clinici</td></tr>
<tr><td>Letteratura</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Banca dati della letteratura biomedica</td></tr>
<tr><td>Informazioni sui farmaci</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Banca dati di farmaci e bersagli</td></tr>
<tr><td>Dati di registrazione</td><td><a href="https://www.aifa.gov.it/">AIFA</a></td><td>Dati sulle approvazioni dei farmaci in Italia</td></tr>
</tbody>
</table>

---

## Base accademica

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## Dimensioni

| Voce | Valore |
|------|-------|
| Schede farmaco | 539 |
| Autorità regolatoria | AIFA |
| Siti attivi | 30 paesi / regioni |

---

## Contatti

- **GitHub Issues**: <https://github.com/yao-care/ITTxGNN/issues>
- **Sviluppatore**: 藥提醒科技有限公司 (<https://www.yao.care>, service@yao.care)
- **Panoramica del prodotto**: <https://www.yao.care/medical/txgnn/>

---

<div class="disclaimer">
<strong>Esclusione di responsabilità</strong><br>
Il presente rapporto ha finalità esclusivamente di ricerca accademica e <strong>non costituisce un parere medico</strong>. Seguire sempre le indicazioni del proprio medico; non modificare mai la terapia di propria iniziativa. Qualsiasi decisione di riposizionamento di un farmaco richiede una validazione clinica completa e una revisione regolatoria.
<br><br>
<small>Revisionato da: 藥提醒科技有限公司 (yao.care)</small>
</div>
