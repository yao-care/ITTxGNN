---
layout: default
title: Carvedilol
parent: Solo previsione del modello (L5)
nav_order: 91
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Carvedilol: nuova indicazione prevista, Ipertensione renovascolare maligna (livello di evidenza L5). Indicazione originale: Ipertensione arteriosa (disturbo ipertensivo)"
monitor_inn: "carvedilol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Carvedilol
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **5** 
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

# Carvedilolo: dall'ipertensione all'ipertensione renovascolare maligna

## Sintesi in una frase

Il carvedilolo è un beta-bloccante non selettivo con attività alfa-1-bloccante, originariamente utilizzato per il trattamento dell'ipertensione arteriosa.
Il modello TxGNN prevede che possa essere efficace per l'**ipertensione renovascolare maligna**, ma per questa indicazione non risultano **né studi clinici né pubblicazioni** a supporto.
La previsione resta quindi puramente computazionale (livello di evidenza L5).

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione arteriosa (disturbo ipertensivo) |
| Nuova indicazione prevista | Ipertensione renovascolare maligna |
| Punteggio di predizione TxGNN | 99,55% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold (sospendere) |

Nota: l'indicazione originale deriva dagli archi di indicazione del knowledge graph TxGNN; i dati compilati per questo report non riportano il testo delle indicazioni approvate dall'AIFA.

---

## Perché questa previsione è plausibile?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle conoscenze note, il carvedilolo è un beta-bloccante non selettivo con attività alfa-1-bloccante; la sua efficacia nell'ipertensione è consolidata e, sul piano meccanicistico, un effetto ipotensivo potrebbe estendersi a questo sottotipo ipertensivo.

Tuttavia, l'ipertensione renovascolare maligna è sostenuta in larga parte dall'attivazione del sistema renina-angiotensina dovuta a stenosi dell'arteria renale. Non sono stati forniti studi o pubblicazioni che testino il carvedilolo in questo contesto. Il punteggio elevato (0,995) riflette verosimilmente la somiglianza con l'indicazione originale di ipertensione, non un'evidenza indipendente. Si tratta di una predizione e nulla più.

### Altre indicazioni previste (per contesto)

| Posizione | Malattia prevista | Punteggio TxGNN | Livello | Nota |
|------|------|------|------|------|
| 2 | Nefropatia ipertensiva maligna | 99,55% | L5 | Nessuno studio; la gestione acuta usa di norma farmaci parenterali titolabili |
| 3 | Ipertensione polmonare a meccanismo multifattoriale non chiaro | 99,54% | L5 | Rischio teorico di peggioramento della funzione ventricolare destra con i beta-bloccanti |
| 4 | Ipertensione polmonare da malattia polmonare e/o ipossia | 99,54% | L4 | Solo evidenze indirette e precliniche |
| 5 | Sindrome di Braddock | 99,37% | L5 | Nessun razionale meccanicistico evidente |

---

## Evidenze da studi clinici

Al momento non risultano studi clinici registrati correlati.

---

## Evidenze dalla letteratura

Per l'indicazione principale (ipertensione renovascolare maligna) al momento non è disponibile letteratura correlata.

Per completezza, per la quarta indicazione (ipertensione polmonare da malattia polmonare/ipossia) sono state recuperate pubblicazioni solo indirette e precliniche; le più pertinenti:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [26291659](https://pubmed.ncbi.nlm.nih.gov/26291659/) | 2015 | Studio animale | Eur J Pharmacol | Il carvedilolo ha invertito l'ipertensione indotta da ipossia intermittente cronica nel ratto (modello sistemico, non polmonare) |
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Revisione | Cardiovasc Drugs Ther | Effetti respiratori dei beta-bloccanti nello scompenso cardiaco; rilevante per la sicurezza nei pazienti con malattia polmonare |
| [20508210](https://pubmed.ncbi.nlm.nih.gov/20508210/) | 2010 | Studio animale | Am J Respir Crit Care Med | Il blocco adrenergico ha invertito il rimodellamento del cuore destro in ratti con ipertensione polmonare |
| [16639551](https://pubmed.ncbi.nlm.nih.gov/16639551/) | 2006 | Studio animale | Pflugers Arch | Il carvedilolo ha inibito l'ipertrofia ventricolare destra indotta da ipossia ipobarica cronica |
| [25187802](https://pubmed.ncbi.nlm.nih.gov/25187802/) | 2014 | Studio in vitro | Exp Ther Med | Effetto cardioprotettivo e anti-apoptotico in cardiomiociti H9c2 dopo ischemia/riperfusione |
| [24798657](https://pubmed.ncbi.nlm.nih.gov/24798657/) | 2014 | Studio crociato (11 pazienti) | J Clin Hypertens | Carvedilolo 20 mg vs nifedipina 40 mg alla sera sulla pressione notturna in pazienti ipertesi con apnee notturne |

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; non ne è attiva alcuna. Testo dell'indicazione e forma farmaceutica non sono presenti nei dati compilati. Principali autorizzazioni:

| N. autorizzazione | Nome prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 027604040 | DILATREND 28 cpr div 6,25 mg | Cheplapharm Arzneimittel GmbH | Cancellata |
| 035987054 | ACARDEN 28 cpr 12,5 mg | SO.SE.PHARM Srl | Cancellata |
| 036512022 | CURCIX 30 cpr div 25 mg | SO.SE.PHARM Srl | Cancellata |
| 036454320 | CARVEDILOLO 30 cpr 25 mg | Sandoz SpA | Cancellata |
| 042234068 | CARVEDILOLO 30 cpr rivestite 25 mg | Aurobindo Pharma Italia Srl | Cancellata |

---

## Considerazioni di sicurezza

- **Controindicazioni (da archi del knowledge graph TxGNN, non dal foglio illustrativo)**: insufficienza epatica, asma (inclusi intrinseco e allergico), bronchite, enfisema polmonare e altre malattie bronchiali, diabete mellito, chetoacidosi diabetica, ipotensione, malattia vascolare periferica (claudicatio intermittente, arteriopatia periferica), blocco atrioventricolare, angina di Prinzmetal, malattia del nodo del seno (anche familiare), anafilassi, sindrome dell'iride flaccida intraoperatoria.
- **Interazioni farmacologiche**: individuate 329 interazioni. Tra quelle elencate, la più rilevante è di livello **maggiore** con **epinefrina**. Numerose interazioni di livello **moderato**, ad esempio con corticosteroidi (idrocortisone, desametasone, betametasone, budesonide, triamcinolone), anticolinergici (atropina, iosciamina), bupropione, morfina, lorcaserina, canagliflozin, acetoesamide e sali di calcio. Interazioni **minori** con acido acetilsalicilico, idrossido di alluminio e attapulgite.
- **Considerazione specifica**: nelle forme polmonari, i beta-bloccanti presentano un rischio teorico di peggioramento della funzione ventricolare destra e delle vie respiratorie; vale anche la controindicazione in presenza di asma e malattie bronchiali.

Per avvertenze e controindicazioni ufficiali, consultare il foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa solo sul modello (L5), senza studi clinici né letteratura per l'ipertensione renovascolare maligna; il punteggio elevato riflette probabilmente la vicinanza semantica con l'ipertensione. Inoltre, tutte le autorizzazioni italiane sono cancellate e il ruolo di un farmaco orale è poco chiaro in una condizione che richiede spesso un controllo pressorio acuto con farmaci parenterali.

**Per procedere, è necessario:**
- Recuperare avvertenze e controindicazioni ufficiali dal foglio illustrativo AIFA (lacuna bloccante per lo screening di sicurezza)
- Ottenere i dati sul meccanismo d'azione da DrugBank
- Condurre una ricerca di letteratura mirata sul carvedilolo nell'ipertensione renovascolare maligna e nella nefropatia ipertensiva maligna
- Chiarire la fattibilità regolatoria, dato che non vi sono autorizzazioni attive in Italia
- Per le forme polmonari, valutare specificamente la sicurezza respiratoria e del ventricolo destro prima di qualsiasi sviluppo
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

