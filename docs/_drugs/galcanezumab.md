---
layout: default
title: Galcanezumab
parent: Solo previsione del modello (L5)
nav_order: 218
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
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

Secondo la sezione «Mechanism of Action» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Galcanezumab (traduzione non ufficiale): «Galcanezumab-gnlm è un anticorpo monoclonale umanizzato che si lega al ligando del peptide correlato al gene della calcitonina (CGRP) e ne blocca il legame al recettore.» Testo originale in inglese: "Galcanezumab-gnlm is a humanized monoclonal antibody that binds to calcitonin gene-related peptide (CGRP) ligand and blocks its binding to the receptor." ([DailyMed: Emgality (galcanezumab-gnlm) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=33a147be-233a-40e8-a55e-e40936e28db0), versione del 2026-06-05; consultato il 2026-11-19). Per quanto noto, galcanezumab neutralizza il CGRP, un neuropeptide coinvolto nella vasodilatazione e nella trasmissione del dolore nell'emicrania.

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

<!-- licenses:begin -->

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|------|------|------|------|
| 047424015 | EMGALITY\*1 penna SC 120 mg 1 ml | ELI LILLY NEDERLAND BV | Autorizzata |

Fonte: AIFA, elenco delle confezioni autorizzate (open data), stato amministrativo; confezioni autorizzate per prime.

<!-- licenses:end -->

## Considerazioni di sicurezza

Per le informazioni di sicurezza si rimanda al foglio illustrativo. Non sono state rilevate interazioni farmacologiche nei dati compilati.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si basa solo sul modello (livello L5), senza studi clinici né letteratura, e non esiste un collegamento meccanicistico plausibile tra il blocco del CGRP e le vie della coagulazione.

<!-- review:begin it-lic-20261106-galcanezumab-1 -->

> **Correzione di verifica (2026-11-24)**: Testo originale: «La previsione si basa solo sul modello (livello L5), senza studi clinici né letteratura, e non esiste un collegamento meccanicistico plausibile tra il blocco del CGRP e le vie della coagulazione. L'unica autorizzazione italiana risulta cancellata.» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). I numeri aggiornati delle autorizzazioni sono nella panoramica rapida e nella tabella delle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-galcanezumab-1 -->

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione da DrugBank, per un'analisi del collegamento meccanicistico
- Avvertenze e controindicazioni dal foglio illustrativo AIFA (lacuna bloccante per lo screening di sicurezza)
- Evidenze precliniche o di letteratura che colleghino il CGRP alla regolazione della coagulazione
- Valutazione della sicurezza vascolare dei farmaci anti-CGRP in pazienti con rischio trombotico elevato
- Verifica dello stato commerciale attuale del prodotto in Italia

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale).

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-24 | Rimosso: «L'unica autorizzazione italiana risulta cancellata» | Corretto (rivisto il 2026-11-24; versione precedente conservata nel registro) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: Emgality (galcanezumab-gnlm) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=33a147be-233a-40e8-a55e-e40936e28db0) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

