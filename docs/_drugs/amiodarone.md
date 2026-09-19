---
layout: default
title: Amiodarone
parent: Solo previsione del modello (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
---

# Amiodarone
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
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

# AMIODARONE: Relazione di Valutazione del Ripropositioning Farmacologico

## Riassunto in Una Frase

L'amiodarone è un noto agente antiaritmico di Classe III ampiamente utilizzato a livello internazionale per la gestione delle aritmie ventricolari e sopraventricolari. Il modello TxGNN **non ha generato alcuna indicazione nuova prevista** per questo farmaco al momento attuale. Il pacchetto di prove contiene importanti lacune di dati che devono essere risolte prima di poter procedere con ulteriori valutazioni.

## Panoramica Rapida

| Elemento | Contenuto |
|----------|-----------|
| Nome del Farmaco (INN) | Amiodarone |
| ID DrugBank | [DB01118](https://go.drugbank.com/drugs/DB01118) |
| Indicazione Originale | Non disponibile nel pacchetto di prove (noto a livello internazionale: aritmie cardiache) |
| Indicazione Nuova Prevista | — (Nessuna predizione TxGNN disponibile) |
| Punteggio di Predizione TxGNN | — |
| Livello di Evidenza | L5 (Nessuna predizione, nessuno studio di supporto) |
| Stato del Mercato Taiwan (TFDA) | ❌ Non commercializzato (Non commercializzato) |
| Numero di Autorizzazioni TFDA | 0 |
| Decisione Consigliata | **Sospensione** |

---

## Perché Non c'è Previsione?

L'amiodarone (DrugBank: DB01118) è stato interrogato attraverso la pipeline TxGNN, ma il modello ha restituito **nessuna indicazione nuova prevista**. Questo potrebbe essere dovuto a uno o più dei seguenti motivi:

1. **Caratteristiche di input insufficienti** — Il pacchetto di prove è privo di dati critici inclusi il meccanismo d'azione (MOA), gli avvertimenti del foglio illustrativo TFDA e i profili di controindicazione. Senza questi, il collegamento del grafo di conoscenza del modello potrebbe essere incompleto.
2. **Nessuna presenza sul mercato TFDA** — L'amiodarone ha zero autorizzazioni TFDA a Taiwan, il che significa che non c'è un ancoraggio normativo locale da cui derivare il testo dell'indicazione o i metadati di sicurezza per la pipeline di ripropositioning.

A livello internazionale, l'amiodarone è riconosciuto come un potente agente antiaritmico di Classe III che funziona principalmente bloccando i canali del potassio, prolungando il potenziale d'azione cardiaco e il periodo refrattario. Inoltre, mostra proprietà di Classe I (blocco dei canali del sodio), Classe II (blocco beta-adrenergico) e Classe IV (blocco dei canali del calcio), rendendolo uno degli antiaritmici più complessi dal punto di vista farmacologico disponibili. Le sue indicazioni note includono aritmie ventricolari potenzialmente mortali (fibrillazione ventricolare, tachicardia ventricolare emodinamicamente instabile) e fibrillazione/flutter atriale refrattaria ad altri trattamenti.

---

## Evidenza di Studi Clinici

Attualmente nessuna indicazione prevista da TxGNN è disponibile; pertanto, nessuna ricerca mirata di studi clinici è stata eseguita per un'indicazione di ripropositioning.

---

## Evidenza della Letteratura

Attualmente nessuna indicazione prevista da TxGNN è disponibile; pertanto, nessuna ricerca mirata della letteratura è stata eseguita per un'indicazione di ripropositioning.

---

## Informazioni sul Mercato Taiwan (TFDA)

L'amiodarone attualmente ha **zero autorizzazioni TFDA** a Taiwan. La query TFDA (2026-03-29) ha restituito zero risultati. Questo farmaco è classificato come **Non commercializzato (non commercializzato)** nel sistema normativo taiwanese.

---

## Considerazioni sulla Sicurezza

> I dati sulla sicurezza (avvertimenti, controindicazioni e interazioni farmaco-farmaco) non potevano essere recuperati dalle fonti del pacchetto di prove. Si prega di fare riferimento al foglio illustrativo internazionale (ad es., etichettatura approvata dalla FDA per Cordarone®/Pacerone®) per informazioni complete sulla sicurezza.
>
> **Problemi di sicurezza critica noti (dall'etichettatura internazionale):**
> - **Avvertimento Black Box (FDA):** Tossicità polmonare (potenzialmente fatale), epatotossicità ed effetti pro-aritmici. Dovrebbe essere utilizzato solo per aritmie potenzialmente mortali a causa della sostanziale tossicità.
> - **Disfunzione tiroidea:** L'amiodarone contiene circa il 37% di iodio in peso; sia l'ipotiroidismo che l'ipertiroidismo sono comuni.
> - **Rischio di prolungamento dell'intervallo QT e Torsades de Pointes.**
> - **Depositi di microcristalli corneali** si verificano in quasi tutti i pazienti.
> - **Estese interazioni farmaco-farmaco** dovute all'inibizione di CYP3A4 e CYP2C8 (ad es., con warfarin, digossina, simvastatina e altri agenti che prolungano l'intervallo QT).
>
> ⚠️ *Queste note sulla sicurezza si basano su conoscenze farmacologiche generali e non provengono dal pacchetto di prove. Sono fornite solo come riferimento.*

---

## Lacune di Dati che Richiedono Risoluzione

Il pacchetto di prove ha segnalato le seguenti lacune critiche:

| ID Lacuna | Categoria | Elemento | Gravità | Impatto | Rimedio |
|-----------|-----------|----------|---------|---------|---------|
| DG001 | Livello Farmaco | Avvertimenti del Foglio Illustrativo TFDA/Controindicazioni | **Bloccante** | Non può entrare nella valutazione preliminare di sicurezza S1 | Scaricare e analizzare il PDF del foglio illustrativo dal sito web TFDA |
| DG002 | Livello Farmaco | Meccanismo d'Azione (MOA) | Alto | Influisce sull'analisi di associazione del meccanismo | Interrogare l'API DrugBank |

---

## Conclusione e Prossimi Passi

**Decisione: Sospensione**

**Razionale:**
Il modello TxGNN non ha prodotto alcuna indicazione nuova prevista per l'amiodarone. Inoltre, ci sono **lacune di dati a livello bloccante** (dati di sicurezza TFDA mancanti e MOA) che impediscono al candidato di entrare anche nella fase preliminare di valutazione della sicurezza (S1). Senza un'indicazione prevista da valutare, non c'è al momento alcuna ipotesi di ripropositioning attuabile.

**Per procedere, è necessario quanto segue:**
- **[Bloccante]** Ottenere i dati del foglio illustrativo TFDA (avvertimenti, controindicazioni) — oppure, se nessuna approvazione TFDA esiste, reperire dati equivalenti dall'etichettatura FDA/EMA
- **[Alto]** Completare il meccanismo d'azione (MOA) dall'API DrugBank per abilitare il collegamento del grafo di conoscenza
- **[Alto]** Investigare perché TxGNN non ha prodotto alcuna previsione — verificare che il nodo del farmaco sia propriamente collegato nel grafo di conoscenza e che le caratteristiche di input siano complete
- **[Medio]** Se l'amiodarone non è commercializzato a Taiwan, considerare se la pipeline di ripropositioning dovrebbe valutarlo secondo un quadro normativo alternativo (ad es., riferimenti incrociati con indicazioni FDA/EMA)
- **[Opzionale]** Rieseguire la predizione TxGNN dopo la risoluzione delle lacune di dati per determinare se emergono nuove indicazioni

---

*Questo rapporto è stato generato il 2026-04-03 sulla base del Pacchetto di Prove v4 (data di aggiornamento: 2026-04-03). I risultati sono solo per riferimento di ricerca e non costituiscono consulenza medica. Qualsiasi candidato di ripropositioning farmacologico richiede convalida clinica prima dell'applicazione.*

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

