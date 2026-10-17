---
layout: default
title: Amoxicillin
parent: Solo previsione del modello (L5)
nav_order: 45
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Amoxicillin: nuova indicazione prevista, Iperamilasemia (livello di evidenza L5). Indicazione originale: Infezioni batteriche (vie urinarie, otite media, faringite, polmonite…"
monitor_inn: "amoxicillin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Amoxicillin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **8** 
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

# Amoxicillina: dalle infezioni batteriche all'iperamilasemia

## Riepilogo in una frase

L'amoxicillina è un antibiotico beta-lattamico, originariamente usato per infezioni batteriche come le infezioni delle vie urinarie, l'otite media, la faringite e la polmonite batterica.
Il modello TxGNN la prevede potenzialmente efficace per l'**iperamilasemia**, ma per questa indicazione non esistono **studi clinici** né **pubblicazioni** a supporto: la predizione è esclusivamente computazionale.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezioni batteriche (vie urinarie, otite media, faringite, polmonite, infezioni da streptococco, stafilococco, *Escherichia coli* e *Klebsiella*). Il testo delle indicazioni autorizzate AIFA non è disponibile; l'elenco deriva dal grafo di conoscenza |
| Nuova indicazione prevista | Iperamilasemia |
| Punteggio di predizione TxGNN | 99,63% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa predizione può (o non può) essere ragionevole?

I dati compilati per questo report non contengono informazioni dettagliate sul meccanismo d'azione. In base alle conoscenze generali, l'amoxicillina è un beta-lattamico che inibisce la sintesi della parete cellulare batterica, e la sua efficacia nelle infezioni batteriche sensibili è consolidata.

L'iperamilasemia, però, è un reperto biochimico senza un chiaro bersaglio batterico. Non è stato identificato alcun legame meccanicistico con l'amoxicillina. Il punteggio elevato (0,996) riflette una vicinanza nel grafo di conoscenza, non un'evidenza terapeutica.

Le altre indicazioni previste hanno un profilo analogo. Iperviscosità policlonale, analbuminemia congenita, incompatibilità di gruppo sanguigno, malattie ematologiche premaligne e gammopatia monoclonale non hanno una base meccanicistica plausibile. Fa eccezione la **peste setticemica**, biologicamente plausibile perché causata da *Yersinia pestis*, ma l'amoxicillina non è una terapia standard: le linee guida indicano aminoglicosidi, fluorochinoloni e tetracicline. Per questa indicazione il livello di evidenza è L4, basato solo su dati in vitro e su modello animale.

## Evidenza dagli studi clinici

Per l'iperamilasemia non risulta alcuno studio clinico registrato.

## Evidenza dalla letteratura

Per l'iperamilasemia non è disponibile alcuna letteratura correlata.

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate. Le prime cinque:

| N. autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 023097102 | VELAMOX 12 cpr orodispersibili 1 g (Neopharmed Gentili) | Compresse orodispersibili | Non disponibile |
| 033151034 | Amoxicillina sospensione orale da polvere 5 g/100 ml (Sandoz) | Sospensione orale | Non disponibile |
| 032892010 | Amoxicillina 12 cpr 1 g (Tecnigen) | Compresse | Non disponibile |
| 023966106 | AMOXINA sospensione orale 250 mg/5 ml 100 ml (Aesculapius Farmaceutici) | Sospensione orale | Non disponibile |
| 023966094 | AMOXINA 12 cpr dispersibili 1 g (Aesculapius Farmaceutici) | Compresse dispersibili | Non disponibile |

## Considerazioni di sicurezza

- **Controindicazioni segnalate nel grafo di conoscenza** (non provenienti dal foglietto illustrativo): sindrome del QT lungo, torsione di punta, tachicardia ventricolare, insufficienza epatica e malattie del fegato, colestasi, porfiria, malattia renale, colite da *Clostridium difficile*, miastenia grave, mononucleosi infettiva, osteoporosi, fratture ossee e malattie della colecisti.
- **Interazioni farmacologiche**: individuate 271 interazioni. Quelle principali:
  - **Maggiori**: metotrexato; vaccino vivo anticolera (*Vibrio cholerae* CVD 103-HgR).
  - **Moderate**: doxiciclina, minociclina, demeclociclina, etinilestradiolo, estradiolo, anisindione, dicumarolo, entecavir, micofenolato mofetile, balsalazide, probiotici (*Lactobacillus acidophilus*, *Bifidobacterium longum infantis*) e indio In-111 ossichinolina.
  - **Minori**: allopurinolo, amiloride, azitromicina, claritromicina, eritromicina.

Per avvertenze e controindicazioni ufficiali, consultare il foglietto illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Per l'iperamilasemia non esistono studi né letteratura e non è identificabile alcun meccanismo plausibile; la predizione è puramente computazionale (L5). Inoltre, tutte le autorizzazioni italiane risultano cancellate.

**Per procedere sarebbe necessario:**
- Reperire le avvertenze e controindicazioni dal foglietto illustrativo AIFA (dato bloccante per lo screening di sicurezza)
- Ottenere i dati sul meccanismo d'azione da DrugBank
- Valutare se la peste setticemica (L4) meriti un'ulteriore indagine come questione di ricerca, tenendo conto che l'amoxicillina non è una terapia standard
- Chiarire lo stato regolatorio in Italia, poiché non esistono autorizzazioni valide
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

