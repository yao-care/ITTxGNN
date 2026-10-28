---
layout: default
title: Moxifloxacin
parent: Solo previsione del modello (L5)
nav_order: 312
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Moxifloxacina: nuova indicazione prevista, sindrome da iperviscosità policlonale (livello di evidenza L5). Indicazione originale: Infezioni batteriche (polmonite, peritonite, congiuntivite, peste…"
monitor_inn: "Moxifloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder", "hematopoietic and lymphoid system neoplasm"]
---

# Moxifloxacin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **9** 
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

## Moxifloxacina: dalle infezioni batteriche alla sindrome da iperviscosità policlonale
{: .text-alpha }

## Riepilogo in una frase

La moxifloxacina è un antibiotico fluorochinolonico, utilizzato originariamente per infezioni batteriche come polmonite, peritonite, congiuntivite e peste.
Il modello TxGNN (deep learning) la indica come potenzialmente efficace per la **sindrome da iperviscosità policlonale**, ma per questa predizione **non esistono studi clinici né pubblicazioni** a supporto. Il punteggio elevato deriva dal modello TxGNN (deep learning) e può riflettere similarità apprese dal modello tra malattie correlate, non evidenza biologica.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezioni batteriche (polmonite, peritonite, congiuntivite, peste, infezioni da stafilococco e streptococco, ecc.); il testo delle indicazioni autorizzate AIFA non è disponibile |
| Nuova indicazione predetta | Sindrome da iperviscosità policlonale |
| Punteggio di predizione TxGNN | 0,9998 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 5 su 5) |
| Numero di autorizzazioni | 5 (valide: 5) |
| Decisione raccomandata | Hold |

## Perché questa predizione è ragionevole?

I dati compilati per questo report non contengono informazioni dettagliate sul meccanismo d'azione. In generale, la moxifloxacina inibisce la DNA girasi e la topoisomerasi IV batteriche, e la sua efficacia nelle infezioni è consolidata.

Per la sindrome da iperviscosità policlonale, causata da un eccesso di immunoglobuline policlonali, **non si identifica un meccanismo plausibile**. Un antibatterico non agisce sulla produzione o sull'accumulo di immunoglobuline. Il punteggio TxGNN molto alto (0,9998) proviene dal modello TxGNN (deep learning) e può riflettere similarità apprese dal modello tra malattie correlate, non un legame biologico reale.

Anche le altre predizioni ad alto punteggio mostrano lo stesso limite: iperamilasemia, analbuminemia congenita, incompatibilità di gruppo sanguigno e condizioni ematologiche premaligne non hanno alcun razionale meccanicistico. Le uniche piste con un legame indiretto sono:

- **Gammopatia monoclonale**: i pazienti immunocompromessi sono soggetti a infezioni (come la nocardiosi), che la moxifloxacina può trattare, ma non cura la gammopatia di base.
- **Peste bubbonica**: la peste è già tra le indicazioni originali, quindi non si tratta di un vero riposizionamento. L'evidenza è solo preclinica.

## Evidenze da studi clinici

Per l'indicazione principale (sindrome da iperviscosità policlonale) attualmente non risultano studi clinici registrati.

## Evidenze dalla letteratura

Per l'indicazione principale attualmente non è disponibile letteratura correlata.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 046817019 | Moxifloxacina*5 cpr rivestite 400 mg (Towa Pharmaceutical) | Compresse rivestite | Non disponibile (autorizzazione valida) |
| 040580019 | Moxifloxacina*5 cpr rivestite 400 mg (Teva Italia) | Compresse rivestite | Non disponibile (autorizzazione valida) |
| 043000013 | Moxifloxacina*5 cpr rivestite 400 mg (Krka) | Compresse rivestite | Non disponibile (autorizzazione valida) |
| 042077026 | Moxifloxacina*5 cpr rivestite 400 mg (Aurobindo Pharma Italia) | Compresse rivestite | Non disponibile (autorizzazione valida) |
| 034436016 | Avalox*5 cpr rivestite 400 mg (Bayer) | Compresse rivestite | Non disponibile (autorizzazione valida) |

## Considerazioni sulla sicurezza

- **Controindicazioni desunte dal grafo di conoscenza** (non dal foglietto illustrativo): sindrome del QT lungo (anche familiare), torsade de pointes, arresto cardiaco improvviso, disturbi della conduzione cardiaca, ischemia miocardica, coronaropatia, epilessia, cirrosi epatica, danno epatico indotto da farmaci, carenza di potassio, tendinite e patologie tendinee/periarticolari, neuropatia periferica e malattie del sistema nervoso periferico, miastenia gravis e malattie della giunzione neuromuscolare, colite da *Clostridium difficile*, enterocolite necrotizzante perinatale.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni; tra le principali di livello **Maggiore**: idrocortisone, desametasone, betametasone, triamcinolone (corticosteroidi, con rischio per tendini), bupropione e clorpropamide. Tra quelle di livello **Moderato**: antidiabetici (acarbosio, alogliptin, albiglutide, canagliflozin, metformina, pioglitazone, con rischio di alterazioni glicemiche), famotidina, loperamide, acido acetilsalicilico, balsalazide, bisacodile, sali di calcio e citrato di potassio.
- **Nota specifica**: i fluorochinoloni sono associati a neuropatia periferica; ciò è sfavorevole per la predizione relativa alle malattie ematologiche associate a neuropatia periferica acquisita.

Per le avvertenze e le controindicazioni ufficiali, consultare il foglietto illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa solo sul punteggio del modello, senza studi clinici, letteratura né razionale meccanicistico (livello L5). Inoltre tutte le autorizzazioni italiane sono cancellate e il profilo di sicurezza (QT, tendini, sistema nervoso) pesa a sfavore.

**Per procedere sarebbe necessario:**
- Un razionale biologico plausibile e dati preclinici per la sindrome da iperviscosità policlonale
- Dati sul meccanismo d'azione (MOA) da fonti dedicate
- Avvertenze e controindicazioni dal foglietto illustrativo AIFA
- Chiarimento dello stato regolatorio (autorizzazioni cancellate)
- In alternativa, valutare la pista della peste bubbonica come questione di ricerca: l'evidenza è solo preclinica, ma si tratta di un uso già vicino alle indicazioni originali
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

