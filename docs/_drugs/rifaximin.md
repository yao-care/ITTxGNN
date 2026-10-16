---
layout: default
title: Rifaximin
parent: Prove moderate (L3-L4)
nav_order: 380
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-15
description: "Rifaximin: nuova indicazione prevista, Candidiasi orale (livello di evidenza L4). Indicazione originale: Encefalopatia epatica, coma epatico"
---

# Rifaximin
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **6** 
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

# Rifaximina: dall'encefalopatia epatica alla candidiasi orale

## Riepilogo in una frase

La rifaximina è un antibiotico orale non assorbibile, originariamente usato per l'encefalopatia epatica e il coma epatico.
Il modello TxGNN la predice come potenzialmente efficace per la **candidiasi orale**, ma il supporto è **molto debole**: non risultano **sperimentazioni cliniche** e l'unica pubblicazione pertinente segnala un possibile **rischio** (infezioni da *Candida* resistenti alla micafungina), non un beneficio.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Encefalopatia epatica, coma epatico |
| Nuova indicazione prevista | Candidiasi orale |
| Punteggio di predizione TxGNN | 99,75% |
| Livello di evidenza | L4 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 2 |
| Decisione raccomandata | Hold |

## Perché questa predizione è (poco) ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione nei dati compilati per questo report. In base alle conoscenze generali, la rifaximina è un antibiotico non assorbito che inibisce la RNA polimerasi batterica; agisce soprattutto a livello intestinale e non ha attività nota contro *Candida*.

Non emerge quindi un legame meccanicistico plausibile con la candidiasi orale. L'alto punteggio TxGNN è verosimilmente un artefatto della propagazione nel grafo di conoscenza ed è contraddetto dal segnale clinico disponibile.

Lo studio di coorte disponibile suggerisce anzi un possibile effetto avverso: l'uso di rifaximina nei pazienti sottoposti a trapianto allogenico di cellule staminali emopoietiche è stato associato a infezioni da *Candida* resistenti alla micafungina, probabilmente per alterazione del microbioma intestinale.

Le altre indicazioni previste (fistola commissurale del labbro, osteoradionecrosi della mandibola, leucoedema orale, sindrome della bocca urente) hanno punteggi simili ma nessuna evidenza clinica o bibliografica e nessuna giustificazione meccanicistica. La candidiasi (generica) presenta un quadro analogo di evidenza indiretta e di segnale di rischio.

## Evidenza dalle sperimentazioni cliniche

Al momento non risultano sperimentazioni cliniche correlate registrate.

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Studio di coorte | Annals of Hematology | Nei pazienti sottoposti a trapianto allogenico di cellule staminali, la profilassi con rifaximina è stata associata a infezioni da *Candida* resistenti alla micafungina (segnale di danno, non di beneficio) |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 025300029 | NORMIX*12 cpr rivestite 200 mg (ALFASIGMA SpA) | Compresse rivestite | Non disponibile (autorizzazione cancellata) |
| 041924046 | TIXTELLER*56 cpr rivestite 550 mg (ALFASIGMA SpA) | Compresse rivestite | Non disponibile (autorizzazione cancellata) |

Entrambe le autorizzazioni risultano cancellate: attualmente non ci sono autorizzazioni valide in Italia.

## Considerazioni sulla sicurezza

- **Controindicazioni nel grafo di conoscenza** (non derivate dal foglietto illustrativo): colite da *Clostridium difficile* ed enterocolite necrotizzante perinatale.
- **Interazioni farmacologiche**: sono state individuate 69 interazioni. Tra quelle di livello **maggiore** figura il vaccino vivo contro il colera (*Vibrio cholerae* CVD 103-HgR). Tra quelle di livello **moderato** figurano, ad esempio, ciclosporina, warfarin, tolvaptan, cabozantinib, apalutamide, alpelisib, daclatasvir, ledipasvir ed encorafenib.

Per le avvertenze e le controindicazioni complete, consultare il foglietto illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Non esiste un meccanismo antifungino plausibile, non ci sono sperimentazioni cliniche e l'unica evidenza disponibile indica un possibile rischio (selezione di *Candida* resistente) anziché un beneficio. Inoltre, in Italia non vi sono autorizzazioni valide.

**Per procedere sarebbe necessario:**
- Dati sul meccanismo d'azione e valutazione di un'eventuale attività antifungina o di un effetto indiretto sul microbioma orale
- Estrazione e analisi del foglietto illustrativo AIFA (avvertenze e controindicazioni), attualmente mancante e bloccante per lo screening di sicurezza
- Studi preclinici o clinici specifici che valutino la candidiasi orale come esito, con attenzione al segnale di rischio già osservato
- Chiarimento dello stato regolatorio in Italia, considerato che tutte le autorizzazioni sono cancellate
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

