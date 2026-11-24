---
layout: default
title: Balsalazide
parent: Solo previsione del modello (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
monitor_inn: "BALSALAZIDE"
predicted_indications: ["gout", "congenital hypotrichosis with juvenile macular dystrophy", "ankylosing spondylitis", "rheumatoid arthritis", "rheumatoid vasculitis", "hypermobility of coccyx", "inflammatory spondylopathy", "Kummell disease", "polyarticular juvenile rheumatoid arthritis", "anus disease"]
last_modified_at: 2026-11-24
description: "Balsalazide: nuova indicazione prevista, Gotta (gout) (livello di evidenza L5). In Italia, confezioni AIFA: 1 (autorizzate: 1)"
---

# Balsalazide
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

## Balsalazide: profarmaco della mesalazina (5-ASA) → Gotta (gout)
{: .text-alpha }

## Sintesi

Balsalazide è un profarmaco dell'acido 5-aminosalicilico (5-ASA, mesalazina) con attività antinfiammatoria a livello del colon. Il modello TxGNN prevede che possa essere efficace per la **gotta (gout)**, con un punteggio di 0,9975. Al momento nei dati compilati per questo report non risultano **né sperimentazioni cliniche né pubblicazioni** a sostegno di questa direzione: si tratta di una previsione basata solo sul modello.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Gotta (gout) |
| Punteggio di previsione TxGNN | 0,9975 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 1 su 1) |
| Numero di autorizzazioni | 1 (valide: 1) |
| Decisione raccomandata | Hold (sospendere) |

---

## Perché questa previsione potrebbe essere ragionevole?

Secondo la sezione «Mechanism of Action» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Balsalazide (traduzione non ufficiale): «Balsalazide disodico viene rilasciato intatto nel colon, dove viene scisso mediante azoriduzione batterica con rilascio di quantità equimolari di mesalazina, che è la porzione terapeuticamente attiva della molecola, e della frazione carrier 4-aminobenzoil-β-alanina. La frazione carrier rilasciata quando balsalazide disodico viene scisso è assorbita solo in misura minima ed è in gran parte inerte.» Testo originale in inglese: "Balsalazide disodium is delivered intact to the colon where it is cleaved by bacterial azoreduction to release equimolar quantities of mesalamine, which is the therapeutically active portion of the molecule, and the 4-aminobenzoyl-β-alanine carrier moiety. The carrier moiety released when balsalazide disodium is cleaved is only minimally absorbed and is largely inert." ([DailyMed: balsalazide disodium prescribing information, Zydus Pharmaceuticals (USA) Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0ed73067-e2ca-4184-a93a-5a2141bb4898), versione del 2026-11-03; consultato il 2026-11-19). Sulla base delle informazioni note, balsalazide rilascia 5-ASA nel colon, dove esercita un'azione antinfiammatoria locale.

Un legame con l'infiammazione gottosa (ad esempio tramite la via NLRP3/IL-1β o l'infiammazione mediata dai neutrofili) è puramente speculativo. Il 5-ASA non è noto per influire sul metabolismo dell'urato. Il punteggio elevato (0,9975) riflette quindi una previsione del modello e non un'evidenza biologica o clinica verificata; il meccanismo non può essere confermato con i dati forniti.

---

## Evidenze da sperimentazioni cliniche

Attualmente non risulta registrata alcuna sperimentazione clinica correlata.

---

## Evidenze dalla letteratura

Attualmente non è disponibile alcuna letteratura correlata.

---

## Informazioni sul mercato italiano

<!-- licenses:begin -->

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|------|------|------|------|
| 033858022 | BALZIDE\*112 cps 750 mg | MENARINI INTERNAT. O.L.S.A | Autorizzata |

Fonte: AIFA, elenco delle confezioni autorizzate (open data), stato amministrativo; confezioni autorizzate per prime.

<!-- licenses:end -->

---

## Considerazioni sulla sicurezza

- **Interazioni farmacologiche**: dalla ricerca sono emerse 100 interazioni complessive. Tra quelle elencate, una è di livello **maggiore** (immunoglobulina G umana per via endovenosa); le altre sono di livello **moderato**, tra cui:
  - Antinfiammatori non steroidei: ketorolac, ibuprofene, celecoxib
  - Antibiotici e antivirali: doxiciclina, aciclovir, foscarnet, fosfomicina, amoxicillina, ampicillina, amikacina, azitromicina, bacitracina
  - Altri: amfotericina B, nitrato di gallio, azatioprina, acetoesamide

Per le avvertenze e le controindicazioni si rimanda al foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per la gotta si basa unicamente sul modello, senza sperimentazioni né pubblicazioni dirette, e il legame meccanicistico è speculativo (il 5-ASA non agisce sul metabolismo dell'urato). Il livello di evidenza è L5.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione di balsalazide
- Studi preclinici o clinici che valutino direttamente balsalazide nella gotta
- Avvertenze e controindicazioni dal foglio illustrativo AIFA
- Verifica della compatibilità della via di somministrazione e valutazione di sicurezza per la popolazione target

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale); le predizioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti.

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: balsalazide disodium prescribing information, Zydus Pharmaceuticals (USA) Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0ed73067-e2ca-4184-a93a-5a2141bb4898) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

