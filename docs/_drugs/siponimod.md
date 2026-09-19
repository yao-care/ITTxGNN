---
layout: default
title: Siponimod
parent: Solo previsione del modello (L5)
nav_order: 187
evidence_level: L5
indication_count: 8
---

# Siponimod
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **8** 
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

# Siponimod: dalla sclerosi multipla progressiva secondaria all'ipertensione polmonare

## Sommario

Siponimod (Mayzent) è un modulatore selettivo dei recettori della sfingosina-1-fosfato (S1P) approvato per la sclerosi multipla progressiva secondaria (SPMS), dove riduce l'infiltrazione di linfociti nel SNC e rallenta la progressione della malattia.
Il modello TxGNN predice che potrebbe essere efficace per l'**ipertensione polmonare**,
tuttavia attualmente ci sono **0 trial clinici** e **0 pubblicazioni** che supportano direttamente questa direzione.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originale | Sclerosi Multipla Progressiva Secondaria (SPMS) |
| Indicazione nuova predetta | Ipertensione polmonare |
| Punteggio di predizione TxGNN | 99.68% |
| Livello di evidenza | L5 |
| Stato di commercializzazione in Italia | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Sospendere |

---

## Perché questa predizione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili in questo pacchetto di evidenze. In base alle informazioni note, siponimod è un modulatore selettivo dei recettori S1P1/S1P5 approvato per la sclerosi multipla progressiva secondaria. Agisce trattenendo i linfociti nei linfonodi, riducendo la loro infiltrazione nel SNC, e inoltre esercita effetti neuroprotettivi attraverso i recettori S1P5 nel cervello e nel midollo spinale.

Il collegamento teorico all'ipertensione polmonare risiede nella biologia vascolare della segnalazione S1P. I recettori S1P1 sono espressi sulle cellule endoteliali vascolari polmonari, e l'asse S1P regola il tono vascolare, l'integrità della barriera endoteliale e la proliferazione delle cellule muscolari lisce — tutti processi disregolati nell'ipertensione polmonare arteriosa (PAH). Un modulatore S1P1 potrebbe, in linea di principio, influenzare il rimodellamento vascolare polmonare patologico.

Tuttavia, questo collegamento meccanicistico opera in entrambe le direzioni. Siponimod ha avvertimenti di sicurezza cardiaca consolidati — inclusa bradicardia alla prima dose e blocco della conduzione AV — che rappresentano una preoccupazione specifica nei pazienti affetti da ipertensione polmonare che comunemente hanno funzione ventricolare destra compromessa. Questo profilo di sicurezza può costituire una controindicazione relativa o assoluta in questa popolazione. La validazione preclinica in modelli di malattia vascolare polmonare sarebbe essenziale prima di qualsiasi ulteriore sviluppo in questa direzione.

---

## Evidenza da trial clinici

Attualmente nessun trial clinico correlato è registrato.

---

## Evidenza da letteratura

Attualmente nessuna letteratura correlata è disponibile.

---

## Informazioni sul mercato italiano

Siponimod non è attualmente commercializzato in Italia. Nessuna autorizzazione AIFA è registrata.

---

## Considerazioni sulla sicurezza

Si prega di consultare il foglio illustrativo per le informazioni sulla sicurezza.

> **Nota:** I dati sugli avvertimenti del foglio illustrativo e sulle controindicazioni non erano recuperabili in questo pacchetto di evidenze. In base alla classe farmacologica del farmaco (modulatore del recettore S1P), le considerazioni di sicurezza clinicamente rilevanti includono: bradicardia alla prima dose, blocco della conduzione AV, edema maculare, rischio di infezioni dovute a linfopenia e requisiti di dosaggio dipendenti dal genotipo CYP2C9.

---

## Conclusioni e prossimi passi

**Decisione: Sospendere**

**Razionale:**
Il modello TxGNN assegna un punteggio di predizione elevato (99.68%) basato sulla connettività del grafo di conoscenza tra la biologia del recettore S1P1 e la malattia vascolare polmonare, ma attualmente non esiste alcuna evidenza clinica o letteraria pubblicata che supporti specificamente siponimod nell'ipertensione polmonare. Inoltre, il noto profilo di sicurezza cardiaca del farmaco suscita preoccupazioni specifiche in questa popolazione di pazienti.

**Per procedere, è necessario quanto segue:**

- **Validazione preclinica:** Studi su modelli animali di ipertensione polmonare arteriosa (ad es., modello di ratto con monocrotalina o Sugen/ipossia) che esaminano l'effetto della modulazione S1P1 sul rimodellamento vascolare polmonare
- **Valutazione della sicurezza cardiaca:** Valutazione emodinamica ventricolare destra in un contesto specifico per PH, dato il rischio noto di bradicardia e blocco AV
- **Recupero dati MOA completi:** Query dell'API DrugBank per confermare il profilo di selettività dei recettori (S1P1 vs. S1P5 vs. altri sottotipi) e la segnalazione a valle
- **Revisione della sicurezza normativa:** Scaricare e analizzare il foglio illustrativo completo EMA/AIFA per identificare se l'ipertensione polmonare o le anomalie della conduzione cardiaca sono elencate come controindicazioni
- **Revisione del panorama comparativo:** Esaminare altri modulatori S1P (fingolimod, ozanimod) per eventuali dati preclinici o clinici PAH disponibili per valutare la plausibilità a livello di classe

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

