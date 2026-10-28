---
layout: default
title: Galcanezumab
parent: Solo previsione del modello (L5)
nav_order: 218
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
description: "Galcanezumab: nuova indicazione prevista, Carenza di cofattore 2 dell'eparina (livello di evidenza L5). Indicazione originale: Emicrania (anche con o senza aura)"
monitor_inn: "GALCANEZUMAB"
predicted_indications: ["heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis"]
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

<div id="pharmacist" markdown="1">

## Relazione di valutazione farmaceutica

</div>

## Galcanezumab: dall'emicrania alla carenza di cofattore 2 dell'eparina
{: .text-alpha }

## Riepilogo in una frase

Galcanezumab è un anticorpo monoclonale diretto contro il peptide correlato al gene della calcitonina (CGRP), originariamente impiegato nella prevenzione dell'emicrania.
Il modello TxGNN lo predice come potenzialmente efficace per la **carenza di cofattore 2 dell'eparina**, ma i dati compilati per questo report non riportano **alcuno studio clinico** né **alcuna pubblicazione** a supporto: si tratta di una previsione puramente computazionale.

## Quadro di sintesi

| Voce | Contenuto |
|------|------|
| Indicazione originale | Emicrania (anche con o senza aura); il testo dell'indicazione autorizzata in Italia non è disponibile |
| Nuova indicazione prevista | Carenza di cofattore 2 dell'eparina |
| Punteggio di previsione TxGNN | 0,9950 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 1 su 1) |
| Numero di autorizzazioni | 1 (valide: 1) |
| Decisione raccomandata | Hold |

## Perché questa previsione è (poco) ragionevole?

Il meccanismo d'azione dettagliato non è disponibile nei dati compilati. Per quanto noto, galcanezumab neutralizza il CGRP, un neuropeptide coinvolto nella vasodilatazione e nella trasmissione del dolore nell'emicrania.

La carenza di cofattore 2 dell'eparina è un disordine trombofilico, legato a un'inibizione ridotta della trombina mediata dalla serpina (SERPIND1). Non esiste alcun collegamento noto tra il blocco del CGRP e l'inibizione della trombina o l'attività del cofattore dell'eparina. L'elevato punteggio TxGNN (0,9950) proviene dal modello TxGNN (deep learning) e può riflettere somiglianze apprese dal modello tra malattie correlate, non evidenze biologiche.

Anche le altre due previsioni di punta presentano la stessa debolezza:

| Rango | Indicazione prevista | Punteggio TxGNN | Evidenza | Considerazione |
|------|------|------|------|------|
| 2 | Carenza di antitrombina di tipo 2 | 0,9941 | L5, nessuno studio | Nessun ruolo noto del CGRP nella regolazione della coagulazione; gli approcci consolidati sono concentrati di antitrombina e anticoagulazione |
| 3 | Eccesso di fattore V con trombosi spontanea | 0,9941 | L5, nessuno studio | Nessun effetto noto sulla cascata coagulativa; i farmaci della via CGRP richiedono cautela vascolare in popolazioni ad alto rischio trombotico |

## Evidenze da studi clinici

Attualmente non risulta registrato alcuno studio clinico correlato.

## Evidenze dalla letteratura

Attualmente non è disponibile alcuna letteratura correlata.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 047424015 | EMGALITY, 1 penna SC 120 mg/1 ml (Eli Lilly Nederland BV) | Penna sottocutanea | Non disponibile (autorizzazione valida) |

## Considerazioni di sicurezza

Per le informazioni di sicurezza si rimanda al foglio illustrativo. Non sono state rilevate interazioni farmacologiche nei dati compilati.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si basa solo sul modello (livello L5), senza studi clinici né letteratura, e non esiste un collegamento meccanicistico plausibile tra il blocco del CGRP e le vie della coagulazione. L'unica autorizzazione italiana risulta cancellata.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione da DrugBank, per un'analisi del collegamento meccanicistico
- Avvertenze e controindicazioni dal foglio illustrativo AIFA (lacuna bloccante per lo screening di sicurezza)
- Evidenze precliniche o di letteratura che colleghino il CGRP alla regolazione della coagulazione
- Valutazione della sicurezza vascolare dei farmaci anti-CGRP in pazienti con rischio trombotico elevato
- Verifica dello stato commerciale attuale del prodotto in Italia
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

