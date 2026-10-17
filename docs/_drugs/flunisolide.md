---
layout: default
title: Flunisolide
parent: Prove moderate (L3-L4)
nav_order: 202
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Flunisolide: nuova indicazione prevista, Eczema atopico (livello di evidenza L4). Indicazione originale: Asma, asma intrinseca, asma allergica, rinite allergica…"
monitor_inn: "FLUNISOLIDE"
predicted_indications: ["atopic eczema", "bronchitis", "dermatitis, atopic", "2-hydroxyethyl methacrylate sensitization", "polyp of vocal cord", "polyp of middle ear", "fibroepithelial polyp", "polyp of frontal sinus", "polyp of external auditory canal"]
---

# Flunisolide
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **10** 
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

# Flunisolide: dall'asma alla dermatite atopica (eczema atopico)

## Riepilogo in una frase

Il flunisolide è un corticosteroide per via inalatoria/nasale, originariamente impiegato per asma e rinite allergica o vasomotoria. Il modello TxGNN ne prevede una possibile efficacia nell'**eczema atopico**, ma al momento non risultano **studi clinici registrati** e sono disponibili solo **1 pubblicazione osservazionale** indiretta. La previsione si basa quindi essenzialmente sul modello.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Asma, asma intrinseca, asma allergica, rinite allergica, rinite vasomotoria (derivate dal grafo di conoscenza; i testi autorizzativi AIFA non riportano l'indicazione) |
| Nuova indicazione prevista | Eczema atopico |
| Punteggio di previsione TxGNN | 99,98% |
| Livello di evidenza | L4 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate; nessuna valida) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione è plausibile?

Nei dati compilati per questo report non è disponibile una descrizione dettagliata del meccanismo d'azione. In base alle conoscenze generali, il flunisolide è un corticosteroide con attività antinfiammatoria. Questa classe di farmaci è già utilizzata, per via topica o sistemica, nella dermatite atopica.

Asma, rinite allergica e dermatite atopica sono malattie atopiche, con infiammazione di tipo Th2 in comune. Ciò rende biologicamente ragionevole un'estensione a livello di classe terapeutica.

Il legame resta però **indiretto**: l'unico studio recuperato misura citochine e pH nel condensato dell'aria espirata in bambini con asma e dermatite atopica. È uno studio osservazionale su biomarcatori e non testa il flunisolide nell'eczema. Inoltre, il flunisolide è formulato soprattutto per inalazione e nebulizzazione, e la compatibilità della via di somministrazione con un uso dermatologico non è stata valutata.

---

## Evidenze dagli studi clinici

Al momento non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [18926054](https://pubmed.ncbi.nlm.nih.gov/18926054/) | 2008 | Coorte | Allergy and Asthma Proceedings | Misura citochine (Th1, Th2, T regolatori) e pH nel condensato dell'aria espirata in bambini con asma e dermatite atopica, valutando l'effetto di un breve ciclo di corticosteroide inalatorio. Studio su biomarcatori, senza dati di efficacia del flunisolide sull'eczema. |

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate. Testo dell'indicazione e forma farmaceutica non sono riportati nei dati. Sono elencate le prime 5:

| N. autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 036372035 | NEBULGEN AD soluz. nebul. 30 flaconi 1 mg/1 ml | Soluzione per nebulizzatore | Non riportata |
| 036364040 | FORBEST BB soluz. nebul. 30 fiale 0,5 mg/1 ml | Soluzione per nebulizzatore | Non riportata |
| 036321026 | ELIOSID soluz. nebul. 15 fiale 1 mg/2 ml | Soluzione per nebulizzatore | Non riportata |
| 033339045 | PULMIST BB soluz. nebul. 15 fiale 1 mg/2 ml | Soluzione per nebulizzatore | Non riportata |
| 036363036 | SAFLINEB AD soluz. nebul. 30 fiale 1 mg/1 ml | Soluzione per nebulizzatore | Non riportata |

---

## Considerazioni di sicurezza

- **Controindicazioni (da relazioni del grafo di conoscenza, non da testo di scheda tecnica)**: malattia epatica, malattia della cistifellea, morbillo, cheratite da herpes simplex, insufficienza corticosurrenalica, morbo di Addison, infezione da varicella zoster, infezioni fungine, dermatofitosi, glaucoma, infezioni parassitarie, malattie infettive, malattie delle basse e alte vie respiratorie, malattie dei seni paranasali e della cavità nasale.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni in totale. Quelle di livello moderato includono **claritromicina**, **insulina umana (inalatoria, ad azione rapida)** e **cobicistat**. Per molte altre (ad es. prednisone, desametasone, morfina, omeprazolo, simvastatina, glibenclamide, glipizide) il livello di gravità non è classificato.

Per avvertenze e controindicazioni ufficiali consultare il foglietto illustrativo; i dati AIFA corrispondenti non sono stati reperiti.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
Il punteggio del modello è molto alto, ma non esistono studi clinici né evidenze dirette sul flunisolide nell'eczema atopico. Il farmaco non ha inoltre autorizzazioni valide in Italia, e mancano dati di sicurezza ufficiali.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) del flunisolide
- Scheda tecnica AIFA con avvertenze e controindicazioni ufficiali
- Valutazione della compatibilità della via di somministrazione e della formulazione per l'uso dermatologico
- Studi clinici o evidenze comparative con i corticosteroidi topici già approvati per la dermatite atopica
- Verifica della situazione regolatoria (autorizzazioni attualmente tutte cancellate)

**Nota su altre previsioni:** tra le successive previsioni, la **bronchite** (punteggio 99,93%, livello L3) ha un supporto debole, costituito da uno studio clinico del 1981 con disegno poco chiaro. Le altre previsioni (polipi di orecchio, seni paranasali, ecc.) sono basate solo sul modello o su evidenze indirette.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

