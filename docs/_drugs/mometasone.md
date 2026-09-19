---
layout: default
title: Mometasone
parent: Prove moderate (L3-L4)
nav_order: 150
evidence_level: L4
indication_count: 1
---

# Mometasone
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **1** 
{: .fs-6 .fw-300 }

---

## Indice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relazione di valutazione farmaceutica

</div>

# Mometasone: Dalle Condizioni Infiammatorie della Pelle al Linfoma Cutaneo Primario a Cellule T

## Riassunto in una Frase

La mometasone è un potente corticosteroide topico originariamente utilizzato per condizioni infiammatorie della pelle come eczema e dermatite.
Il modello TxGNN prevede che potrebbe essere efficace per il **linfoma cutaneo primario a cellule T (CTCL)**,
con **0 studi clinici** e **2 pubblicazioni** (entrambi case report) che attualmente supportano questa direzione — uno dei quali ha registrato la mometasone come trattamento precedente fallito.

---

## Panoramica Rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione Originaria | Condizioni infiammatorie della pelle (corticosteroide topico; nessun testo di indicazione formale disponibile dalle registrazioni normative) |
| Nuova Indicazione Prevista | Linfoma Cutaneo Primario a Cellule T (CTCL) |
| Punteggio di Previsione TxGNN | 99.36% |
| Livello di Evidenza | L4 |
| Stato del Mercato Taiwan | ✗ Non Commercializzato (Non commercializzato) |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | Mantenere in Sospeso |

---

## Perché Questa Previsione è Ragionevole?

Attualmente, i dati dettagliati del meccanismo d'azione non sono disponibili dalla fonte di dati strutturati. In base alle informazioni farmacologiche note, la mometasone è un glucocorticoide topico potente. Esercita i suoi effetti attivando il recettore glucocorticoide (GR), che a sua volta sopprime la via di segnalazione NF-κB — risultando in effetti pro-apoptotici e anti-proliferativi sui linfociti T. Questa attività a livello cellulare forma la base meccanicistica per la previsione TxGNN.

Il linfoma cutaneo primario a cellule T, in particolare la Micosi Fungoide (MF), è definito dalla proliferazione clonale di cellule T maligne all'interno della pelle. Poiché il bersaglio primario della malattia (il linfocita T) è lo stesso tipo di cellula soppressa dai corticosteroidi, esiste un ponte meccanicistico plausibile. Le linee guida NCCN per la MF in stadio iniziale elencano già i corticosteroidi topici come un'opzione di trattamento riconosciuta con effetto di classe, prestando rilevanza clinica indiretta a questa previsione.

Tuttavia, è importante notare che nessuno studio clinico che valuta specificamente la mometasone per CTCL è stato registrato. La letteratura pubblicata disponibile non fornisce prove di efficacia controllate; un case report ha esplicitamente documentato la mometasone come trattamento precedente fallito prima che la condizione del paziente rispondesse a un agente alternativo (tapinarof). Il collegamento meccanicistico è presente, ma la prova specifica del farmaco è assente.

---

## Evidenza da Studi Clinici

Attualmente nessuno studio clinico correlato registrato.

---

## Evidenza dalla Letteratura

| PMID | Anno | Tipo | Rivista | Risultati Chiave |
|------|------|------|---------|------------------|
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Case Report | Proceedings (Baylor University. Medical Center) | Donna di 62 anni con pseudolinfoma cutaneo (infiltrato atipico di cellule T); mometasone e tacrolimus entrambi falliti, il paziente ha successivamente risposto a tapinarof — la mometasone appare come trattamento precedente fallito, non uno riuscito |
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Case Report | Journal of Cutaneous Pathology | Ragazzo di 11 anni con micosi fungoide CD8+CD56+ di immunofenotipo citotossico; malattia lentamente progressiva per 7 anni che colpisce il tronco e gli arti — documenta la presentazione clinica di MF pediatrica, nessun dato di efficacia diretto della mometasone |

---

## Informazioni sul Mercato Taiwan

La mometasone attualmente non ha prodotti approvati sul mercato Taiwan (registrazioni TFDA). Nessuna tabella di autorizzazione può essere generata.

---

## Considerazioni di Sicurezza

Si prega di consultare il foglio illustrativo per le informazioni di sicurezza.

---

## Conclusioni e Prossimi Passi

**Decisione: Mantenere in Sospeso**

**Motivazione:**
L'evidenza per la mometasone specificamente nel CTCL primario è limitata a L4 (meccanicistica/indiretta), con zero studi clinici registrati e solo due case report — uno dei quali registra la mometasone come fallimento del trattamento. Il punteggio del modello TxGNN è alto (99.36%), indicando un forte segnale a livello di grafo, ma questo riflette la plausibilità dell'effetto di classe piuttosto che la validazione specifica del farmaco.

**Per procedere, è necessario quanto segue:**

- **Dati del meccanismo d'azione (MOA)**: Recuperare il profilo farmacodinamico completo dall'API DrugBank per confermare l'attività pro-apoptotica mediata da GR nelle cellule T
- **Dati di sicurezza**: Scaricare e analizzare il PDF del foglio illustrativo TFDA per valutare controindicazioni e avvisi chiave prima che possa procedere qualsiasi valutazione di sicurezza S1
- **Benchmarking dell'effetto di classe**: Identificare i dati dei trial clinici per altri corticosteroidi topici potenti (ad es., clobetasol) nella MF in stadio iniziale per stabilire un'ancora di evidenza a livello di classe
- **Ricerca letteraria specifica del farmaco**: Ampliare la query PubMed (ad es., "mometasone AND mycosis fungoides") per determinare se esistono dati osservazionali non basati su trial
- **Valutazione della compatibilità della via**: Confermare se le formulazioni topiche di mometasone (crema/pomata) sono appropriate per la distribuzione e lo stadio delle lesioni CTCL target

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

