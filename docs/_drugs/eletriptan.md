---
layout: default
title: Eletriptan
parent: Solo previsione del modello (L5)
nav_order: 88
evidence_level: L5
indication_count: 4
---

# Eletriptan
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

# Eletriptan: Valutazione di Riutilizzo Farmacologico — Nessuna Predizione TxGNN Disponibile

## Riassunto in Una Frase

L'eletriptan è un agonista selettivo del recettore della serotonina 5-HT1B/1D appartenente alla classe dei triptani, utilizzato nel trattamento acuto dell'emicrania con o senza aura.
Il Pacchetto di Evidenza attuale contiene **nessuna predizione del modello TxGNN** per nuove indicazioni, e il farmaco è **non commercializzato a Taiwan** con zero autorizzazioni approvate.
La valutazione non può procedere fino a quando i dati di predizione TxGNN e le informazioni sulla sicurezza non vengono integrati.

---

## Panoramica Rapida

| Item | Contenuto |
|------|---------|
| Indicazione Originale | Emicrania — trattamento acuto (classe dei triptani) |
| Indicazione Predetta Nuova | N/A — Nessuna predizione TxGNN disponibile |
| Punteggio di Predizione TxGNN | N/A |
| Livello di Evidenza | N/A |
| Stato del Mercato Taiwan | ✗ Non Commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | In Attesa |

---

## Perché Questa Predizione è Ragionevole?

Nessuna indicazione predetta da TxGNN è presente in questo Pacchetto di Evidenza, quindi l'analisi della plausibilità meccanicistica per una nuova indicazione non può essere eseguita in questa fase.

Per contesto, l'eletriptan appartiene alla classe dei triptani e agisce come agonista selettivo dei recettori della serotonina 5-HT1B e 5-HT1D. Questo meccanismo a doppio recettore produce vasocostrizione cranica selettiva e inibisce il rilascio presinaptico di neuropeptidi vasoattivi — inclusi CGRP e sostanza P — interrompendo così il ciclo trigeminovascolare responsabile del dolore emicranico. I dati dettagliati sul meccanismo di azione sono stati contrassegnati come lacuna nei dati (DG002: gravità alta) e richiedono un recupero formale da DrugBank prima che qualsiasi ponte meccanicistico verso una nuova indicazione possa essere valutato.

Una volta generate le predizioni del modello TxGNN, l'analisi dovrebbe concentrarsi su se la segnalazione del recettore 5-HT1 o la modulazione del percorso CGRP si sovrappongono alla biologia della malattia di qualsiasi indicazione candidata. Il sistema serotoninergico ha un coinvolgimento documentato nei disturbi dell'umore, nell'emicrania a grappolo e in alcune sindromi dolorose, che possono fornire ancore meccanicistiche plausibili — ma questo rimane speculativo fino a quando i dati di predizione non saranno disponibili.

---

## Evidenza da Trial Clinici

Attualmente nessun trial clinico correlato registrato — nessuna nuova indicazione predetta è disponibile per la ricerca.

---

## Evidenza da Letteratura

Attualmente nessuna letteratura correlata disponibile — nessuna nuova indicazione predetta è disponibile per la ricerca.

---

## Informazioni sul Mercato Taiwan

L'eletriptan non ha autorizzazioni approvate a Taiwan. Nessun record di licenza è disponibile per la visualizzazione.

> Nota: L'eletriptan (nome commerciale Relpax, Pfizer) è approvato nell'UE, negli USA e in diversi altri mercati per il trattamento dell'emicrania acuta. Un deposito normativo a Taiwan non è stato presentato o approvato in base ai dati TFDA attuali.

---

## Considerazioni sulla Sicurezza

I dati sulla sicurezza inclusi avvisi chiave e controindicazioni sono attualmente non disponibili a causa di lacune nei dati identificate durante la costruzione del Pacchetto di Evidenza:

- **DG001 (Blocking):** Avvisi del foglio illustrativo TFDA e controindicazioni — necessari per lo screening di sicurezza S1; devono essere recuperati dal sito web TFDA prima che la valutazione possa procedere.
- **DG002 (Alta):** Dettaglio del meccanismo di azione — necessario per l'analisi della plausibilità meccanicistica; deve essere recuperato da DrugBank.
- **Query DDI:** Non ha restituito risultati (stato della query: non trovato).

Si prega di fare riferimento al foglio illustrativo internazionale (SmPC / USPI) per una guida sulla sicurezza provvisoria.

---

## Conclusione e Prossimi Passi

**Decisione: In Attesa**

**Razionale:**
Il Pacchetto di Evidenza per l'eletriptan è criticamente incompleto — l'array `predicted_indications` è vuoto e due lacune nei dati di blocco/alta gravità impediscono al screening di sicurezza e all'analisi meccanicistica di procedere. Non esiste attualmente alcun segnale di riutilizzo farmacologico fruibile da valutare.

**Per procedere, è necessario quanto segue:**

- **Predizioni del modello TxGNN** devono essere generate per l'eletriptan (`predicted_indications` è attualmente vuoto — la pipeline potrebbe non aver processato DB00216)
- **Dati MOA** da DrugBank (DG002 — Alta): necessari per l'analisi della plausibilità meccanicistica
- **Dati sulla sicurezza** dal foglio illustrativo TFDA (DG001 — Blocking): avvisi chiave e controindicazioni necessari prima dello screening di sicurezza S1
- **Ri-query del database DDI**: il risultato non trovato attuale può riflettere un problema di query; i dati di interazione per un agonista 5-HT1 sono clinicamente rilevanti (in particolare con MAOI, SSRI e altri triptani)
- **Definizione del Percorso Normativo**: se l'ingresso nel mercato Taiwan è un obiettivo, sarebbe richiesta una domanda di nuovo farmaco (NDA) completa data l'assenza di autorizzazioni esistenti

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

