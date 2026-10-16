---
layout: default
title: Prulifloxacin
parent: Solo previsione del modello (L5)
nav_order: 367
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Prulifloxacin: nuova indicazione prevista, Malattia cardiaca (heart disease) (livello di evidenza L5). Indicazione originale: Non disponibile nei dati AIFA compilati (il testo dell'indicazione è…"
monitor_inn: "prulifloxacin"
predicted_indications: ["heart disease", "Laubry-Pezzi syndrome", "Pierre Robin syndrome associated with a chromosomal anomaly", "genetic syndromic Pierre Robin syndrome", "partial deletion of the long arm of chromosome 7", "orofacial clefting syndrome", "pulmonary valve disease", "disorder of fucoglycosan synthesis", "mitral valve disease", "Jeune syndrome situs inversus"]
---

# Prulifloxacin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
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

# Prulifloxacina: dall'uso antibatterico alla malattia cardiaca (predizione non supportata)

## Sintesi in una frase

La prulifloxacina è un antibatterico fluorochinolonico (profarmaco dell'ulifloxacina). Il modello TxGNN ne predice l'efficacia per la **malattia cardiaca**, ma i dati compilati per questo report non contengono **nessuno studio clinico** e l'unica pubblicazione pertinente è uno studio preclinico sul coniglio, che riguarda il rischio proaritmico del farmaco e non un beneficio terapeutico.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile nei dati AIFA compilati (il testo dell'indicazione è vuoto); in base alla classe è un antibatterico fluorochinolonico |
| Nuova indicazione predetta | Malattia cardiaca (heart disease) |
| Punteggio di predizione TxGNN | 99,94% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 4 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa predizione è (poco) ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrati per questo farmaco. In base alle conoscenze generali, la prulifloxacina è un profarmaco dell'ulifloxacina, che inibisce la DNA girasi e la topoisomerasi IV batteriche. Questo meccanismo è specifico per i batteri e non ha un legame plausibile con la fisiopatologia delle malattie cardiache.

Il punteggio TxGNN elevato (99,94%) è solo una predizione computazionale. Va notato che i punteggi delle prime 10 predizioni sono tutti quasi identici (circa 99,93–99,94%), e comprendono condizioni molto eterogenee, come difetti cardiaci congenitali, sindromi craniofacciali e anomalie cromosomiche. Ciò suggerisce che il punteggio da solo non discrimina tra indicazioni plausibili e non plausibili.

Inoltre, i fluorochinoloni sono associati a preoccupazioni di sicurezza cardiaca, in particolare al prolungamento dell'intervallo QT e, raramente, ad aritmie ventricolari come la torsione di punta. Questo elemento va contro, e non a favore, un uso in ambito cardiaco.

## Evidenza clinica (studi clinici)

Al momento non risultano studi clinici correlati registrati.

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [15018156](https://pubmed.ncbi.nlm.nih.gov/15018156/) | 2004 | Preclinico (animale) | The Journal of Toxicological Sciences | Confronto del potenziale proaritmico e del prolungamento del QT di NM394 (ulifloxacina, metabolita attivo della prulifloxacina) e di altri chinoloni (sparfloxacina, gatifloxacina, levofloxacina) in un modello di aritmia nel coniglio. È uno studio di sicurezza, non di efficacia. |

Per le altre predizioni (ad esempio sindrome di Laubry-Pezzi, sindromi di Pierre Robin, malattie delle valvole mitrale e polmonare) non è disponibile alcuna evidenza clinica o letteraria. Per il "disturbo della sintesi dei fucoglicani" (rank 8) sono state recuperate sette pubblicazioni, ma riguardano penetrazione tissutale, metodi analitici, legame con l'albumina e altri temi non correlati: la corrispondenza sembra dovuta a parole chiave e non è rilevante.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 035679036 | CHINOPLUS*5 cpr rivestite 600 mg | Compresse rivestite | Cancellata |
| 035680038 | KERAFLOX*5 cpr rivestite 600 mg | Compresse rivestite | Cancellata |
| 035678022 | UNIDROX*5 cpr rivestite 600 mg | Compresse rivestite | Cancellata |
| 035678034 | UNIDROX*1 cpr rivestite 600 mg | Compresse rivestite | Cancellata |

Tutte e quattro le autorizzazioni risultano cancellate; non vi sono autorizzazioni valide attualmente in Italia.

## Considerazioni sulla sicurezza

- **Segnale di sicurezza cardiaca (letteratura)**: i chinoloni, incluso il metabolita attivo della prulifloxacina, sono stati valutati per il prolungamento dell'intervallo QT e il potenziale proaritmico in modelli animali.
- **Interazioni farmacologiche**: nessuna interazione è stata trovata nei dati compilati.

Per le avvertenze e le controindicazioni complete si rimanda al foglietto illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa solo su un modello computazionale (livello L5), senza studi clinici e senza un legame meccanicistico credibile; l'unica evidenza pertinente riguarda un rischio di sicurezza cardiaca. Inoltre, il farmaco non ha attualmente autorizzazioni valide in Italia.

**Per procedere sarebbe necessario:**
- Recuperare il foglietto illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per la valutazione di sicurezza)
- Ottenere i dati sul meccanismo d'azione da DrugBank
- Dimostrare un'ipotesi biologica plausibile per l'uso cardiaco, oltre al solo punteggio del modello
- Valutare in modo approfondito il rischio di prolungamento del QT e di aritmie
- Chiarire lo stato regolatorio (autorizzazioni cancellate) e la disponibilità di vie di somministrazione
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

