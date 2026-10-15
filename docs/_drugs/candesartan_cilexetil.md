---
layout: default
title: Candesartan Cilexetil
parent: Solo previsione del modello (L5)
nav_order: 86
evidence_level: L5
indication_count: 5
---

# Candesartan Cilexetil
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **5** 
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

# Candesartan cilexetil: dall'ipertensione all'ipertensione renovascolare maligna

## Sintesi in una frase

Candesartan cilexetil è un antagonista del recettore dell'angiotensina II di tipo 1, utilizzato originariamente per il trattamento dell'ipertensione.
Il modello TxGNN prevede che possa essere efficace per la **ipertensione renovascolare maligna**, ma al momento **non risultano studi clinici né pubblicazioni** che supportino direttamente questa indicazione: si tratta di una predizione puramente computazionale.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione (disturbo ipertensivo) |
| Nuova indicazione prevista | Ipertensione renovascolare maligna |
| Punteggio di predizione TxGNN | 99,68% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è ragionevole?

Allo stato attuale, i dati dettagliati sul meccanismo d'azione non sono disponibili nei dati compilati per questo report. Sulla base delle conoscenze generali, candesartan è un bloccante del recettore AT1 dell'angiotensina II (sartano) ed è utilizzato nell'ipertensione.

L'ipertensione renovascolare è sostenuta in larga parte dall'attivazione del sistema renina-angiotensina, quindi il meccanismo è biologicamente plausibile. Tuttavia, nella stenosi bilaterale dell'arteria renale e nella fase maligna della malattia, il blocco del sistema renina-angiotensina comporta un rischio di peggioramento acuto della funzione renale, che richiede una valutazione attenta della sicurezza.

Va inoltre sottolineato che questa indicazione si sovrappone in modo sostanziale all'indicazione originale (ipertensione): non rappresenta un vero segnale di riposizionamento verso una malattia nuova, ma piuttosto una forma grave o secondaria della stessa condizione. Il punteggio TxGNN elevato (0,997) potrebbe riflettere la vicinanza nel grafo di conoscenza ad altri termini legati all'ipertensione.

### Altre predizioni nel modello

| Rango | Malattia prevista | Punteggio TxGNN | Evidenza | Note |
|------|------|------|------|------|
| 2 | Nefropatia ipertensiva maligna | 99,68% | L5 | Forma grave dell'ipertensione già indicata; da valutare iperkaliemia e danno renale acuto |
| 3 | Ipertensione polmonare da malattia polmonare e/o ipossia | 99,67% | L5 | Due lavori reperiti, ma non pertinenti (studio preclinico murino sull'ipossia neonatale e studio su una formula erboristica nel danno renale) |
| 4 | Ipertensione polmonare a meccanismo multifattoriale non chiaro | 99,67% | L5 | Legame indiretto; rischio di ipotensione sistemica |
| 5 | Sindrome di Braddock | 99,56% | L5 | Malattia rarissima, nessun legame meccanicistico evidente; probabile artefatto del grafo |

---

## Evidenze da studi clinici

Al momento non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

Al momento non risulta letteratura correlata disponibile per l'indicazione principale (ipertensione renovascolare maligna).

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; nessuna è attualmente valida. Di seguito le principali (il testo dell'indicazione approvata non è presente nei dati compilati).

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 033577469 | RATACAND 28 cpr 32 mg | Cheplapharm Arzneimittel GmbH | Cancellata |
| 033577305 | RATACAND 28 cpr 16 mg | Cheplapharm Arzneimittel GmbH | Cancellata |
| 033577180 | RATACAND 28 cpr 8 mg | Cheplapharm Arzneimittel GmbH | Cancellata |
| 033451360 | BLOPRESS 28 cpr 32 mg | Cheplapharm Arzneimittel GmbH | Cancellata |
| 044804021 | BLOPRESS 28 cpr 32 mg | Medifarm Srl | Cancellata |

---

## Considerazioni sulla sicurezza

Dal grafo di conoscenza (non dal foglio illustrativo) emergono associazioni di controindicazione con le seguenti condizioni:

- **Condizioni renali e vascolari**: anuria, compromissione della funzione renale, ostruzione dell'arteria renale, ipotensione
- **Condizioni epatiche e biliari**: epatopatia, coma epatico, encefalopatia epatica, malattia della colecisti, pancreatite, ittero neonatale
- **Condizioni metaboliche ed elettrolitiche**: diabete mellito, chetoacidosi diabetica, carenza di potassio, ipercalcemia, disturbi del metabolismo del fosforo, nefrocalcinosi, iperparatiroidismo, osteite fibrosa, iperuricemia, gotta
- **Condizioni autoimmuni**: lupus eritematoso sistemico (inclusa la forma pediatrica)

Si tratta di segnali provenienti da un grafo di conoscenza e non di testo di scheda tecnica: vanno verificati con il foglio illustrativo ufficiale. Per le avvertenze e le interazioni farmacologiche, consultare il foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Tutte le predizioni sono supportate solo dal modello (L5), senza studi clinici né letteratura pertinente. L'indicazione principale coincide in larga parte con l'indicazione originale e comporta un rischio renale specifico; inoltre, tutte le autorizzazioni italiane sono cancellate.

**Per procedere sono necessari:**
- Acquisizione del foglio illustrativo AIFA (avvertenze e controindicazioni), attualmente mancante e bloccante per la valutazione di sicurezza
- Dati sul meccanismo d'azione da DrugBank
- Ricerca di studi clinici e letteratura specifici su candesartan nell'ipertensione renovascolare maligna
- Valutazione della sicurezza renale (iperkaliemia, danno renale acuto, stenosi bilaterale dell'arteria renale)
- Chiarimento della situazione regolatoria in Italia (nessuna autorizzazione valida)
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

