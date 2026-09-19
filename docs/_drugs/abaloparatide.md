---
layout: default
title: Abaloparatide
parent: Solo previsione del modello (L5)
nav_order: 11
evidence_level: L5
indication_count: 4
---

# Abaloparatide
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **4** 
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

# ABALOPARATIDE: Valutazione preliminare — In attesa di dati di predizione

## Riassunto in una frase

Abaloparatide (DrugBank: DB05084) è un analogo peptidico sintetico della proteina correlata all'ormone paratiroideo (PTHrP), noto a livello internazionale per il trattamento dell'osteoporosi postmenopausale ad alto rischio di frattura. Il modello TxGNN **non ha ancora generato alcuna nuova indicazione predetta** per questo farmaco, e il pacchetto di prove contiene importanti lacune di dati nel meccanismo d'azione e nelle informazioni di sicurezza. Questo rapporto funge da **record di base** in attesa del completamento della predizione e dell'arricchimento dei dati.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originale | Non registrata nel pacchetto di prove attuale (nota esternamente: osteoporosi postmenopausale) |
| Nuova indicazione predetta | — (Nessuna predizione disponibile) |
| Punteggio di predizione TxGNN | — |
| Livello di evidenza | **L5** (Nessuna predizione o studi di supporto) |
| Stato del mercato di Taiwan | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | **Sospensione** |

---

## Perché questa predizione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili nel pacchetto di prove. In base alle informazioni pubblicamente note, abaloparatide è un analogo sintetico della proteina correlata all'ormone paratiroideo umano (PTHrP(1-34)). Agisce come attivatore selettivo della via di segnalazione del recettore PTH1, stimolando preferibilmente la conformazione RG del recettore, che promuove la formazione ossea rispetto al riassorbimento osseo. È approvato negli Stati Uniti (nome commerciale: Tymlos) per il trattamento delle donne in postmenopausa con osteoporosi ad alto rischio di frattura.

**Nessuna predizione TxGNN è stata generata per questo farmaco.** L'array `predicted_indications` è vuoto, il che significa che il modello non ha ancora elaborato questo composto o non ha identificato indicazioni candidate al di sopra della soglia di confidenza. Senza una nuova indicazione predetta, nessuna analisi di plausibilità basata sul meccanismo può essere condotta in questo momento.

Per procedere, sono richiesti i seguenti passi di arricchimento dei dati:
1. Completare la pipeline di predizione TxGNN per ABALOPARATIDE
2. Recuperare e popolare il meccanismo d'azione (MOA) dall'API di DrugBank
3. Ottenere gli avvertimenti e le controindicazioni del foglio illustrativo TFDA

---

## Prove da studi clinici

Attualmente nessuna indicazione predetta è disponibile; pertanto, nessuna ricerca mirata di studi clinici è stata eseguita.

---

## Prove da letteratura

Attualmente nessuna indicazione predetta è disponibile; pertanto, nessuna ricerca mirata della letteratura è stata eseguita.

---

## Informazioni sul mercato di Taiwan

ABALOPARATIDE **non è attualmente commercializzato a Taiwan**. Nessuna autorizzazione commerciale TFDA è stata trovata (data della query: 2026-03-29). Ci sono zero licenze registrate e nessuna forma di dosaggio è disponibile attraversi i canali locali.

---

## Considerazioni sulla sicurezza

> Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.
>
> Nota: gli avvertimenti/controindicazioni del foglio illustrativo TFDA e i dati sulle interazioni farmaco-farmaco non sono attualmente disponibili per questo farmaco a Taiwan. La query DDI non ha restituito risultati. Questi rappresentano **lacune di dati bloccanti** che devono essere risolte prima che qualsiasi valutazione della sicurezza possa procedere.

---

## Riepilogo delle lacune di dati

Le seguenti lacune critiche di dati sono state identificate in questo pacchetto di prove:

| ID lacuna | Categoria | Elemento | Gravità | Rimedio |
|-----------|-----------|----------|---------|---------|
| DG001 | Livello del farmaco | Avvertimenti/Controindicazioni del foglio illustrativo TFDA | **Bloccante** | Scaricare e analizzare il PDF del foglio illustrativo dal sito web TFDA |
| DG002 | Livello del farmaco | Meccanismo d'azione (MOA) | **Alto** | Interrogare l'API di DrugBank |
| — | Predizione | Indicazioni predette da TxGNN | **Bloccante** | Eseguire la pipeline di predizione TxGNN |

---

## Conclusione e fasi successive

**Decisione: Sospensione**

**Motivazione:**
Nessuna indicazione predetta da TxGNN è disponibile per ABALOPARATIDE, e rimangono lacune critiche di dati nel meccanismo d'azione e nelle informazioni di sicurezza. Senza una nuova indicazione predetta, la valutazione del livello di evidenza e l'analisi del rapporto rischio-beneficio non possono essere eseguite. Il farmaco inoltre non è commercializzato a Taiwan, il che aggiunge complessità normativa a qualsiasi potenziale sforzo di riproposta.

**Per procedere, è necessario quanto segue:**
- Eseguire il modello di predizione TxGNN per ABALOPARATIDE per generare nuove indicazioni candidate
- Recuperare i dati dettagliati sul meccanismo d'azione (MOA) dall'API di DrugBank (DG002)
- Ottenere il foglio illustrativo TFDA per gli avvertimenti di sicurezza e le controindicazioni (DG001), o ottenere dati normativi di sicurezza equivalenti da FDA/EMA se l'etichettatura taiwanese non è disponibile
- Se le previsioni vengono generate, condurre ricerche mirate di studi clinici e letteratura per l'indicazione con il ranking più alto
- Rivalutare il livello di evidenza e la decisione una volta che le lacune di cui sopra sono colmate

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

