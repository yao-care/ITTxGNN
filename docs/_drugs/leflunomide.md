---
layout: default
title: Leflunomide
parent: Solo previsione del modello (L5)
nav_order: 259
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Leflunomide: nuova indicazione prevista, Sindrome brachidattilia-sindattilia (livello di evidenza L5). Indicazione originale: Artrite reumatoide e artrite psoriasica"
monitor_inn: "LEFLUNOMIDE"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Leflunomide
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **2** 
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

# Leflunomide: Dall'artrite reumatoide alla sindrome brachidattilia-sindattilia

## Sintesi in una frase

Leflunomide è un farmaco immunomodulatore, originariamente utilizzato per il trattamento dell'artrite reumatoide e dell'artrite psoriasica.
Il modello TxGNN ne prevede una possibile efficacia nella **sindrome brachidattilia-sindattilia**,
ma al momento **non sono presenti studi clinici né pubblicazioni** a supporto: la previsione si basa esclusivamente sul punteggio del modello.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Artrite reumatoide e artrite psoriasica |
| Nuova indicazione prevista | Sindrome brachidattilia-sindattilia |
| Punteggio di previsione TxGNN | 99,93% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 7 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione potrebbe essere ragionevole?

I dati compilati per questo report non contengono una descrizione dettagliata del meccanismo d'azione. Sulla base delle conoscenze generali, leflunomide (tramite il suo metabolita attivo teriflunomide) inibisce l'enzima diidroorotato deidrogenasi (DHODH), riducendo la sintesi delle pirimidine nelle cellule a rapida proliferazione, in particolare i linfociti attivati. Questo spiega la sua efficacia nelle patologie autoimmuni.

Il legame con una malformazione congenita degli arti è, allo stato attuale, **speculativo**. Si potrebbe ipotizzare un coinvolgimento di vie di sviluppo dipendenti dal metabolismo delle pirimidine, ma nessun dato disponibile lo conferma. Inoltre l'inibizione di DHODH è associata a teratogenicità, il che rappresenta una criticità rilevante in qualsiasi contesto di disturbo dello sviluppo.

Il punteggio elevato di TxGNN (0,9993) è l'unico elemento a supporto; da solo non è sufficiente a giustificare un avanzamento.

Una seconda previsione, la **sindrome da microftalmia colobomatosa-displasia rizomelica** (punteggio 99,93%), presenta lo stesso profilo: livello L5, nessuno studio o pubblicazione, rationale puramente speculativo e decisione Hold.

## Evidenze da studi clinici

Attualmente non sono registrati studi clinici correlati.

## Evidenze dalla letteratura

Attualmente non sono disponibili pubblicazioni correlate.

## Informazioni sul mercato italiano

Tutte le autorizzazioni risultano cancellate. Il testo dell'indicazione approvata non è presente nei dati compilati.

| N. autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 050037098 | Leflunomide 30 cpr rivestite 20 mg | Aurobindo Pharma Italia Srl | Cancellata |
| 034702098 | Arava 3 cpr rivestite 100 mg | Sanofi Aventis Deutschland GmbH | Cancellata |
| 042083067 | Leflunomide 30 cpr rivestite 20 mg (flacone) | Medac GmbH | Cancellata |
| 041230107 | Leflunomide 30 cpr rivestite 20 mg | Mylan SpA | Cancellata |
| 034702074 | Arava 30 cpr rivestite 20 mg (flacone) | Sanofi Aventis Deutschland GmbH | Cancellata |

## Considerazioni sulla sicurezza

- **Controindicazioni derivate dal knowledge graph** (non dal foglietto illustrativo): insufficienza epatica, malattie epatiche e della colecisti, epatite B e C croniche, malattie renali, trombocitopenia, neutropenia (comprese varie forme congenite), agranulocitosi, pancitopenia, anemia, neuropatia periferica, malattia polmonare interstiziale, pneumocistosi e aspergillosi.
- **Interazioni farmacologiche**: sono state rilevate 100 interazioni complessive. Tra quelle di livello **maggiore** figurano:
  - corticosteroidi (idrocortisone, desametasone, betametasone, triamcinolone, budesonide);
  - antidiabetici (acarbosio, pioglitazone);
  - bupropione, acido acetilsalicilico, naltrexone, claritromicina, minociclina;
  - steroidi anabolizzanti (oxandrolone, oxymetholone) e acido chenodesossicolico.

  Sono presenti anche interazioni moderate (ad es. metronidazolo, clorpropamide, acetoesamide) e minori (solfato e acetato di zinco).
- **Teratogenicità**: l'inibizione di DHODH è nota per il rischio teratogeno, particolarmente rilevante per disturbi dello sviluppo.

Per le avvertenze e le controindicazioni ufficiali si rimanda al foglietto illustrativo.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si fonda unicamente sul punteggio del modello (livello L5), senza studi clinici né letteratura. Il meccanismo è speculativo, il profilo teratogeno è preoccupante e tutte le autorizzazioni italiane sono cancellate.

**Per procedere è necessario:**
- Reperire e analizzare il foglietto illustrativo AIFA (avvertenze e controindicazioni), attualmente mancante
- Acquisire i dati dettagliati sul meccanismo d'azione (ad es. da DrugBank)
- Condurre studi preclinici o una revisione della letteratura che colleghi DHODH/metabolismo delle pirimidine alla patogenesi della sindrome prevista
- Valutare in modo approfondito il rischio teratogeno rispetto al contesto di malattia dello sviluppo
- Chiarire la situazione regolatoria, dato che nessuna autorizzazione è attualmente valida in Italia
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

