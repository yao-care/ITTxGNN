---
layout: default
title: Telmisartan
parent: Solo previsione del modello (L5)
nav_order: 192
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: dall'Ipertensione all'Angina di Prinzmetal

## Sintesi in una Frase

Telmisartan è un antagonista dei recettori dell'angiotensina II di tipo 1 (AT1) con una lunga storia consolidata a livello globale nella gestione dell'ipertensione, sebbene attualmente non disponga di autorizzazione all'immissione in commercio in Italia.
Il modello TxGNN gli assegna il punteggio di rivalutazione più elevato per **l'Angina di Prinzmetal** (99.98%), prevedendo un potenziale ruolo nella riduzione della suscettibilità allo spasmo coronarico.
Tuttavia, attualmente **nessuno studio clinico** e **nessuna letteratura pubblicata** supportano direttamente questa indicazione, collocando questa previsione al livello di evidenza più basso (L5).

---

## Panoramica Rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione Originale | Ipertensione (approvazione globale; nessuna autorizzazione italiana registrata) |
| Nuova Indicazione Prevista | Angina di Prinzmetal |
| Punteggio di Predizione TxGNN | 99.98% |
| Livello di Evidenza | L5 |
| Stato del Mercato Italiano | ✗ Non Commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | Sospendere |

---

## Perché questa Previsione è Ragionevole?

Attualmente, i dati dettagliati sui meccanismi d'azione non sono disponibili in questo Evidence Pack. Basandosi sulla conoscenza farmacologica consolidata, telmisartan è un antagonista dei recettori AT1 che blocca selettivamente la segnalazione dell'angiotensina II (AngII) — impedendo la vasoconstrizione mediata da AngII, il rilascio di aldosterone e la proliferazione della muscolatura liscia vascolare. Distintivamente tra gli ARB, telmisartan agisce anche come agonista parziale di PPARγ (peroxisome proliferator-activated receptor gamma), conferendo ulteriori benefici antinfiammatori e metabolici che si estendono oltre la semplice riduzione della pressione arteriosa. Questo duplice meccanismo gli ha valso l'etichetta informale di "metabosartan".

L'angina di Prinzmetal (angina variante) comporta transienti e reversibili spasmi dell'arteria coronarica a riposo, tipicamente in assenza di aterosclerosi ostruttiva significativa. Il collegamento teorico è meccanicisticamente plausibile: il blocco AT1 potrebbe attenuare la contrazione della muscolatura liscia coronarica indotta da AngII, riducendo potenzialmente la suscettibilità agli spasmi. L'attivazione di PPARγ potrebbe inoltre attenuare l'infiammazione endoteliale — un fattore riconosciuto della disfunzione endoteliale che sottostà agli episodi vasospastici.

Nonostante questa razionale teorica, l'inferenza meccanicistica rimane altamente indiretta. Nessun modello animale preclinico, studio osservazionale o studio clinico ha direttamente valutato telmisartan nell'angina di Prinzmetal. Il punteggio elevato del modello TxGNN (99.98%) probabilmente riflette l'ampia connettività condivisa tra i nodi delle malattie vascolari nel grafo della conoscenza — la malattia coronarica, l'ipertensione e i disturbi vasomotori sono densamente interconnessi — piuttosto che una relazione farmaco-specifica validata. Questa previsione dovrebbe essere trattata solo come generatrice di ipotesi e non interpretata come evidenza di efficacia.

---

## Evidenza da Studi Clinici

Attualmente non sono registrati studi clinici correlati per Telmisartan nell'Angina di Prinzmetal.

---

## Evidenza dalla Letteratura

Attualmente nessuna letteratura correlata disponibile per Telmisartan nell'Angina di Prinzmetal.

---

## Informazioni sul Mercato Italiano

Telmisartan attualmente non dispone di autorizzazioni all'immissione in commercio in Italia. Nessun prodotto approvato è registrato in questo dataset.

---

## Considerazioni di Sicurezza

Si rimanda al foglio illustrativo per le informazioni di sicurezza.

---

## Conclusione e Passi Successivi

**Decisione: Sospendere**

**Razionale:**
Nonostante un punteggio TxGNN molto elevato (99.98%), non vi è alcuna evidenza diretta — né studi clinici né letteratura pubblicata — che colleghi telmisartan all'angina di Prinzmetal. Una valutazione L5 significa che si tratta di una previsione basata solo su modello che richiede una sostanziale validazione preclinica prima che possa essere considerato qualsiasi percorso di sviluppo.

**Per procedere, è necessario quanto segue:**

- **Validazione preclinica**: Modelli animali di spasmo coronarico (ad es., spasmo indotto da ergonovina) per testare direttamente se il blocco AT1 o l'attivazione di PPARγ riducono gli eventi vasospastici
- **Indagine indiretta della letteratura**: Revisione sistematica degli studi esistenti con antagonisti AT1 e agonisti di PPARγ per eventuali segnali nell'angina vasospastica o nella disfunzione endoteliale coronarica
- **Documentazione MOA**: Profilo completo del meccanismo d'azione di telmisartan in DrugBank (attualmente non disponibile in questo Evidence Pack)
- **Revisione della sicurezza**: Foglio illustrativo completo (TFDA/EMA) per avvertimenti chiave, controindicazioni e interazioni farmacologiche — particolarmente rilevante dato l'effetto antipertensivo di telmisartan, che potrebbe richiedere un aggiustamento della dose in pazienti normotesi con angina vasospastica
- **Valutazione del rischio emodinamico**: Valutare se la riduzione della pressione arteriosa in una popolazione normotesa vasospastica sia clinicamente appropriata o potenzialmente dannosa

> **Nota per i revisori:** Sebbene l'Angina di Prinzmetal sia classificata al #1 per punteggio TxGNN, l'Evidence Pack contiene anche indicazioni con evidenza clinica sostanzialmente più forte. Notevolmente, **l'emorragia intracerebrale (rank #9)** è supportata da uno studio clinico randomizzato di Fase 3 completato (TRIDENT, NCT02699645, n=1,671) e raggiunge una valutazione L1 con una raccomandazione "Procedere con Protezioni". Un rapporto separato focalizzato su quella indicazione potrebbe avere un valore clinico immediatamente maggiore.

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

