---
layout: default
title: Galcanezumab
parent: Solo previsione del modello (L5)
nav_order: 115
evidence_level: L5
indication_count: 3
---

# Galcanezumab
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **3** 
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

# Galcanezumab: Dalla prevenzione dell'emicrania alla carenza di eparina-cofattore 2

## Riepilogo in una frase

Galcanezumab (Emgality) è un anticorpo monoclonale umanizzato che bersaglia il CGRP, approvato globalmente per il trattamento preventivo dell'emicrania e della cefalea a grappolo episodica. Il modello TxGNN predice che potrebbe essere efficace per la **carenza di eparina-cofattore 2** — un raro disturbo ereditario della coagulazione — con **0 trial clinici** e **0 pubblicazioni** che attualmente supportano questa direzione. Tutti e tre i principali predicati si raggruppano attorno a disturbi rari della coagulazione con punteggi uniformemente elevati, suscitando gravi preoccupazioni che questi risultati riflettano un artefatto del grafo della conoscenza piuttosto che segnali genuini di riposizionamento biologico.

---

## Panoramica rapida

| Elemento | Contenuto |
|------|---------|
| Indicazione originale | Prevenzione dell'emicrania; cefalea a grappolo episodica (nessuna autorizzazione italiana registrata) |
| Nuova indicazione prevista | Carenza di eparina-cofattore 2 |
| Punteggio di previsione TxGNN | 99.50% |
| Livello di evidenza | L5 |
| Stato del mercato italiano | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | **In attesa** |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili in questo Evidence Pack. Sulla base delle informazioni note, galcanezumab è un anticorpo monoclonale anti-CGRP la cui provata efficacia nella prevenzione dell'emicrania è basata sul blocco della sensibilizzazione del trigemino mediata dal CGRP e sulla vasodilatazione cranica. Opera interamente all'interno dell'asse di segnalazione del dolore del sistema nervoso — nello specifico all'interfaccia recettoriale CGRP–RAMP1/CLR — e non ha un ruolo stabilito nella cascata della coagulazione.

L'eparina-cofattore II (HCFII) è un inibitore della trombina della famiglia dei serpini. La carenza di HCFII porta a un'attività trombina non contrastata e uno stato protrombotico. L'asse inibizione HCFII–trombina e il sistema di segnalazione CGRP–recettore sono percorsi funzionalmente e biochimicamente distinti, senza dimostrata attività di crosstalk nella letteratura scientifica attuale.

È fondamentale notare che la stessa implausibilità si applica a tutti e tre i principali predicati di TxGNN — carenza di HCFII, carenza di antitrombina di tipo 2, e eccesso di fattore V con trombosi spontanea — che sono tutti rari disturbi ereditari della coagulazione con punteggi TxGNN superiori a 0.994. Questo pattern di clustering stretto è un'evidenza di sovrapredizione sistematica del supernodo all'interno del cluster "vascular regulation" del grafo della conoscenza, non segnali biologici genuini individuali. Queste predizioni dovrebbero essere trattate come artefatti della topologia del grafo finché un audit KG dedicato non confermi o refuti questa ipotesi.

---

## Evidenza dai trial clinici

Attualmente nessun trial clinico correlato registrato.

---

## Evidenza dalla letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Informazioni sul mercato italiano

Galcanezumab non è attualmente approvato o commercializzato in Italia. Nessuna autorizzazione di immissione in commercio è registrata. Si noti che galcanezumab (Emgality) possiede l'approvazione EMA in Europa per la prevenzione dell'emicrania — i clinici dovrebbero fare riferimento allo SmPC EMA per l'indicazione autorizzata completa e il profilo di sicurezza.

---

## Considerazioni di sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni di sicurezza.

---

## Conclusioni e fasi successive

**Decisione: In attesa**

**Motivazione:**
Tutte e tre le indicazioni previste da TxGNN sono rari disturbi ereditari della coagulazione senza trial clinici o letteratura di supporto, e il collegamento meccanicistico tra l'inibizione del CGRP e le vie dei fattori della coagulazione è biologicamente non stabilito. L'agglomerazione di punteggi >0.994 tra tre indicazioni tematicamente identiche è un forte indicatore di un artefatto di sovrapredizione del grafo della conoscenza piuttosto che di una genuina opportunità di riposizionamento.

**Per procedere, è necessario quanto segue:**

- **Audit della topologia KG**: Indagare se il supernodo vascolare/coagulazione di TxGNN sta generando segnali falsi positivi sistematici; confrontare il vicinato KG di galcanezumab con controlli negativi confermati
- **Recupero dati MAO** (DG002): Estrarre il profilo completo di interazione biologica di galcanezumab da DrugBank per caratterizzare formalmente qualsiasi attività cross-pathway
- **Screening della letteratura meccanicistica**: Condurre una revisione mirata per determinare se alcuna letteratura peer-reviewed supporta il crosstalk dell'asse CGRP–coagulazione prima di impegnare ulteriori risorse di valutazione
- **Completamento dei dati di sicurezza** (DG001): Recuperare lo SmPC EMA / il foglio illustrativo TFDA per completare gli avvertimenti, le controindicazioni e la valutazione delle interazioni farmaco-farmaco — attualmente mancano dati per tutti i campi di sicurezza

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

