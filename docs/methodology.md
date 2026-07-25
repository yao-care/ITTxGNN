---
layout: default
title: Metodologia
nav_order: 91
permalink: /methodology/
description: "Come ITTxGNN genera e valida le previsioni: previsione tramite grafo di conoscenza TxGNN, raccolta delle prove, classificazione L1-L5 e raccomandazioni decisionali."
---

# Metodologia

<div class="key-takeaway">
Dalla previsione dell'IA alla classificazione delle prove — ogni candidato ha una base tracciabile per la propria valutazione.
</div>

---

## Flusso complessivo

<p class="key-answer" data-question="Come genera le sue previsioni ITTxGNN?">
La piattaforma utilizza un flusso in quattro fasi: il modello a grafo di conoscenza TxGNN prevede potenziali
associazioni farmaco&ndash;malattia, le prove vengono poi raccolte automaticamente per ciascuna coppia prevista,
le prove vengono classificate da L1 a L5 e infine viene emessa una raccomandazione decisionale.
</p>

<ol class="actionable-steps">
<li><strong>Previsione TxGNN</strong>: relazioni farmaco&ndash;malattia previste con un grafo di conoscenza combinato con reti neurali a grafo.</li>
<li><strong>Raccolta delle prove</strong>: per ciascuna coppia prevista, le prove vengono raccolte da ClinicalTrials.gov, PubMed, DrugBank e AIFA.</li>
<li><strong>Classificazione delle prove</strong>: classificate da L1 a L5, dove L1 è il livello più forte (più RCT di Fase 3) e L5 corrisponde alla sola previsione del modello.</li>
<li><strong>Raccomandazione decisionale</strong>: Go, Proceed, Consider, Explore o Hold, in base al livello di prova.</li>
</ol>

---

## Criteri di classificazione delle prove

<table class="comparison-table">
<thead>
<tr><th>Livello</th><th>Definizione</th><th>Significato clinico</th></tr>
</thead>
<tbody>
<tr><td><strong>L1</strong></td><td>Più RCT di Fase 3 / revisioni sistematiche</td><td>Supporto forte; l'uso clinico può essere preso in considerazione</td></tr>
<tr><td><strong>L2</strong></td><td>Un singolo RCT o più studi di Fase 2</td><td>Supporto moderato; è possibile progettare studi di validazione</td></tr>
<tr><td><strong>L3</strong></td><td>Studi osservazionali / ampie serie di casi</td><td>Supporto preliminare; necessita di ulteriore validazione</td></tr>
<tr><td><strong>L4</strong></td><td>Studi preclinici / meccanicistici</td><td>Supporto teorico; lontano dall'uso clinico</td></tr>
<tr><td><strong>L5</strong></td><td>Solo previsione del modello</td><td>Fase ipotetica; nessuna prova sull'uomo</td></tr>
</tbody>
</table>

---

## Previsione a doppio motore

Due metodi vengono eseguiti in parallelo e un'etichetta di confidenza registra se concordano:

| Metodo | Velocità | Precisione | Descrizione |
|--------|-------|-----------|-------------|
| Grafo di conoscenza (KG) | Rapido | Inferiore | Inferenza sulle relazioni DrugBank e sulla struttura del grafo |
| Deep learning (DL) | Lento | Superiore | Modello di rete neurale a grafo TxGNN |

| Confidenza | Origine | Significato |
|------------|--------|---------|
| very_high | KG + DL | Entrambi i metodi concordano |
| high | Solo DL | Supporto del deep learning con punteggio elevato |
| medium | Solo KG | Supporto del grafo di conoscenza |

---

## Integrazione dei dati regolatori

I dati sulle approvazioni dei farmaci in Italia provengono dall'AIFA. I nomi dei principi attivi sono mappati sul
vocabolario DrugBank; i principi attivi che non possono essere mappati — estratti vegetali, vaccini, eccipienti
e altri elementi non catalogati da DrugBank — sono esclusi dalla previsione.

---

## Limiti

<ol class="actionable-steps">
<li>Le previsioni sono associazioni statistiche e <strong>non implicano un rapporto di causalità né un'efficacia clinica</strong>.</li>
<li>Una valutazione L5 indica la sola previsione del modello, senza prove di supporto sull'uomo.</li>
<li>La raccolta delle prove dipende da banche dati pubbliche; gli studi non pubblicati o non indicizzati non vengono rilevati.</li>
<li>La mappatura dei principi attivi può omettere alcuni elementi a causa di differenze nella denominazione.</li>
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
