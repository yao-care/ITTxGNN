---
layout: default
title: Methylergometrine
parent: Solo previsione del modello (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Methylergometrine: nuova indicazione prevista, Ipertricosi (livello di evidenza L5). Indicazione originale: Non disponibile nei dati compilati (i testi delle indicazioni nelle a…"
monitor_inn: "methylergometrine"
predicted_indications: ["hypertrichosis (disease)", "pulmonary hypertension", "migraine disorder", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "kyphoscoliotic heart disease", "migraine with brainstem aura", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Methylergometrine
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
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

## Metilergometrina: Dall'uso ostetrico a Ipertricosi (predizione TxGNN, evidenza solo computazionale)
{: .text-alpha }

## Sintesi in una frase

La metilergometrina (methylergometrine) è un alcaloide semisintetico della segale cornuta con attività uterotonica. Nei dati compilati per questo report non risulta alcuna indicazione approvata registrata. Il modello TxGNN prevede come prima indicazione l'**ipertricosi**, ma **non esistono studi clinici né pubblicazioni** a sostegno. L'unica area con qualche letteratura indiretta è l'**emicrania** (2 pubblicazioni di tipo review).

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile nei dati compilati (i testi delle indicazioni nelle autorizzazioni AIFA sono vuoti) |
| Nuova indicazione prevista | Ipertricosi |
| Punteggio di predizione TxGNN | 0,9987 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 2 su 2) |
| Numero di autorizzazioni | 2 (valide: 2) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è ragionevole?

I dati di meccanismo d'azione (MOA) non sono al momento disponibili. In base alle informazioni generali, la metilergometrina è un derivato semisintetico dell'ergot che agisce come ligando dei recettori serotoninergici 5-HT2, alfa-adrenergici e dopaminergici, con effetto uterotonico.

**Per l'ipertricosi non è stato individuato alcun razionale meccanicistico.** Il punteggio molto alto (0,9987) proviene dal modello TxGNN (deep learning), senza dati clinici o di letteratura a supporto, e può riflettere somiglianze apprese dal modello tra malattie correlate, non evidenze biologiche. L'ipertricosi indotta da farmaci non è un effetto noto dei derivati dell'ergot.

Tra le altre predizioni ad alto punteggio, la più plausibile è l'**emicrania** (rank 3, punteggio 0,9984). La metilergometrina è il metabolita attivo della metisergide, storico farmaco di profilassi dell'emicrania che agisce sui recettori 5-HT1B/1D/2. Le due pubblicazioni trovate offrono però solo evidenza indiretta e sottolineano i rischi vascolari e fibrotici della classe, come vasocostrizione coronarica e fibrosi.

Le altre predizioni non hanno un razionale credibile:
- **Ipertensione polmonare**: i derivati dell'ergot sono associati a peggioramento dell'ipertensione polmonare e a valvulopatia tramite agonismo 5-HT2B, quindi un beneficio è dubbio e il rischio per la sicurezza è probabile.
- **Ipertricosi di tipo Ambras, sindromi malformative, sindrome con malformazione di Dandy-Walker, anomalie genetiche del fusto del pelo, sindrome nefrogenica da inappropriata antidiuresi**: condizioni genetiche o strutturali senza alcun legame farmacologico plausibile.
- **Cardiopatia cifoscoliotica**: condizione cardiopolmonare secondaria in cui i rischi vasocostrittivi dei derivati dell'ergot rendono improbabile un beneficio.
- **Emicrania con aura del tronco encefalico**: i vasocostrittori sono tradizionalmente sconsigliati per il rischio ischemico.

---

## Evidenza dagli studi clinici

Attualmente non risultano studi clinici registrati correlati all'ipertricosi (né alle altre nove indicazioni previste).

---

## Evidenza dalla letteratura

Per l'ipertricosi non è disponibile alcuna letteratura. Per l'emicrania (rank 3), indicazione più plausibile, sono state trovate due pubblicazioni di tipo review:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [18644039](https://pubmed.ncbi.nlm.nih.gov/18644039/) | 2008 | Review | Cephalalgia | Storia della metisergide nell'emicrania: dalla teoria vasodilatatoria di Wolff alla ricerca di un farmaco anti-serotoninico |
| [9665056](https://pubmed.ncbi.nlm.nih.gov/9665056/) | 1998 | Review | Circulation | Confronto del potenziale vasocostrittore coronarico di farmaci antiemicranici (ergotamina, diidroergotamina, metisergide e il suo metabolita metilergometrina, triptani) |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 004225037 | METHERGIN*15 cpr rivestite 0,125 mg | Compresse rivestite | Non disponibile (autorizzazione valida) |
| 004225025 | METHERGIN*6 fiale IM EV 1 ml 0,2 mg/ml | Fiale per uso IM/EV | Non disponibile (autorizzazione valida) |

Entrambe le autorizzazioni, intestate a Essential Pharma (M) Ltd, risultano cancellate.

---

## Considerazioni di sicurezza

**Controindicazioni suggerite dal grafo di conoscenza** (relazioni farmaco-malattia di TxGNN, non testo di scheda tecnica): ipertensione, epilessia, malattia renale, malattia epatica, malattia della colecisti, ictus e disturbi cerebrovascolari, infarto cerebrale, arteriosclerosi obliterante, sindrome HELLP, piureter.

**Interazioni farmacologiche**: sono state rilevate 92 interazioni; tra quelle elencate, le principali di gravità **maggiore** sono:
- Isometeptene
- Epinefrina (anche nelle formulazioni oftalmica e topica)
- Efedrina (anche nasale)
- Lorcaserina
- Claritromicina

Tra quelle di gravità **moderata**: doxiciclina, tetraciclina, minociclina, aprepitant, desametasone, cimetidina, eluxadone, clotrimazolo, miconazolo, glicerolo fenilbutirrato, metreleptina e troglitazone.

Per avvertenze e controindicazioni ufficiali si rimanda alla scheda tecnica.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione principale (ipertricosi) ha solo supporto computazionale (L5), nessuno studio e nessun razionale farmacologico. Il profilo di sicurezza della classe dell'ergot è sfavorevole, e le autorizzazioni italiane sono tutte cancellate. L'emicrania potrebbe essere trattata come una domanda di ricerca (L4), ma con evidenza solo indiretta e rilevanti rischi vascolari.

**Per procedere sarebbe necessario:**
- Acquisire e analizzare la scheda tecnica AIFA (avvertenze e controindicazioni), attualmente un blocco per lo screening di sicurezza
- Reperire i dati sul meccanismo d'azione (ad esempio da DrugBank)
- Chiarire l'indicazione originale approvata
- Per l'emicrania: revisione sistematica della letteratura e valutazione del rischio cardiovascolare/fibrotico
- Valutare la disponibilità reale del prodotto, dato che tutte le autorizzazioni sono cancellate
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

