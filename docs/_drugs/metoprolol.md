---
layout: default
title: Metoprolol
parent: Solo previsione del modello (L5)
nav_order: 296
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Metoprolol: nuova indicazione prevista, Malattia renale ipertensiva maligna (livello di evidenza L5). Indicazione originale: Ipertensione, sindrome coronarica acuta…"
monitor_inn: "metoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "chronic pulmonary heart disease", "trichotillomania"]
---

# Metoprolol
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

# Metoprololo: Dall'ipertensione alla malattia renale ipertensiva maligna

## Sintesi in una frase

Il metoprololo è un beta-bloccante cardioselettivo (beta-1), originariamente utilizzato per ipertensione, sindrome coronarica acuta e infarto del miocardio.
Il modello TxGNN prevede una possibile efficacia nella **malattia renale ipertensiva maligna**, ma per questa indicazione **non risultano né studi clinici né pubblicazioni** a supporto: la previsione resta puramente computazionale.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione, sindrome coronarica acuta, infarto del miocardio (dal grafo di conoscenza TxGNN; il testo dell'indicazione AIFA non è disponibile) |
| Nuova indicazione prevista | Malattia renale ipertensiva maligna |
| Punteggio di previsione TxGNN | 99,91% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 15 (tutte cancellate, nessuna valida) |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle conoscenze generali, il metoprololo è un beta-bloccante beta-1 selettivo che riduce la pressione arteriosa, la frequenza cardiaca e il rilascio di renina. Questo lo rende un'estensione naturale dell'indicazione già approvata per l'ipertensione.

Il rilascio di renina ridotto è teoricamente rilevante per il danno d'organo ipertensivo, compreso quello renale. Tuttavia la ipertensione maligna è un'emergenza ipertensiva, di solito gestita con farmaci per via endovenosa, e i beta-bloccanti non sono di prima scelta. Il punteggio elevato è probabilmente dovuto alla vicinanza ontologica con "ipertensione" più che a evidenze specifiche.

Altre previsioni in classifica (stesso profilo L5, senza studi): ipertensione renovascolare maligna (99,91%), ipertensione polmonare multifattoriale (99,91%), sindrome di Braddock e tricotillomania, per le quali non è stato individuato un razionale meccanicistico solido. Ipertensione polmonare da malattia polmonare/ipossia (99,91%) ha 20 pubblicazioni recuperate, ma quasi tutte non pertinenti. Gli infarti miocardici posteroinferiore, posterolaterale e settale sono sottotipi di un'indicazione già approvata, quindi con valore di riposizionamento minimo. Per la cardiopatia polmonare cronica (99,40%) esistono 4 studi clinici e numerose pubblicazioni, per lo più sulla sicurezza nei pazienti con BPCO e malattie cardiovascolari.

## Evidenza clinica

Attualmente non sono registrati studi clinici correlati alla malattia renale ipertensiva maligna.

A titolo di contesto, per la cardiopatia polmonare cronica (previsione di rango 9) sono stati individuati i seguenti studi:

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT06825728](https://clinicaltrials.gov/study/NCT06825728) | Fase 4 | Non ancora in reclutamento | 311 | Metoprololo in scompenso con frazione di eiezione ridotta e BPCO; esiti: mortalità e riospedalizzazioni |
| [NCT02587351](https://clinicaltrials.gov/study/NCT02587351) | Fase 3 | Terminato | 532 | BLOCK-COPD: metoprololo per prevenire le riacutizzazioni di BPCO; interrotto, nessun segnale di efficacia |
| [NCT00384566](https://clinicaltrials.gov/study/NCT00384566) | Fase 4 | Ritirato | 0 | CAMERA: effetti respiratori di carvedilolo vs metoprololo; nessun arruolamento |
| [NCT05096884](https://clinicaltrials.gov/study/NCT05096884) | Fase 1 precoce | Terminato | 14 | Dispnea da sforzo e tachicardia post-COVID; popolazione poco pertinente |

## Evidenza dalla letteratura

Attualmente non è disponibile letteratura correlata alla malattia renale ipertensiva maligna.

Per la cardiopatia polmonare cronica (contesto) le pubblicazioni più rilevanti sono:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [38587241](https://pubmed.ncbi.nlm.nih.gov/38587241/) | 2024 | RCT | N Engl J Med | Beta-bloccanti dopo infarto con frazione di eiezione preservata |
| [38762800](https://pubmed.ncbi.nlm.nih.gov/38762800/) | 2024 | RCT | JAMA | Studio BICS: bisoprololo in BPCO ad alto rischio di riacutizzazione; cita che il metoprololo non ha ridotto le riacutizzazioni e ha aumentato quelle con ricovero |
| [32000982](https://pubmed.ncbi.nlm.nih.gov/32000982/) | 2020 | Coorte | Am J Cardiol | Metoprololo vs carvedilolo in anziani con scompenso, BPCO, diabete e insufficienza renale |
| [26844454](https://pubmed.ncbi.nlm.nih.gov/26844454/) | 2016 | Coorte | Medicine | Beta-bloccanti in scompenso e BPCO coesistenti (database taiwanese) |
| [29159953](https://pubmed.ncbi.nlm.nih.gov/29159953/) | 2018 | Coorte | Eur J Heart Fail | Carvedilolo vs metoprololo/bisoprololo/nebivololo in scompenso con BPCO (Danimarca) |
| [33784233](https://pubmed.ncbi.nlm.nih.gov/33784233/) | 2021 | Analisi secondaria di RCT | Ann Am Thorac Soc | Indice cronotropico e riacutizzazioni di BPCO in BLOCK-COPD |
| [32250198](https://pubmed.ncbi.nlm.nih.gov/32250198/) | 2020 | Revisione | Expert Rev Respir Med | Raccomandazioni pratiche sui beta-bloccanti in BPCO |
| [14520486](https://pubmed.ncbi.nlm.nih.gov/14520486/) | 2003 | Studio clinico | Heart Vessels | Metoprololo usato in sicurezza in pazienti con coronaropatia e BPCO |

Si tratta di evidenze indirette: riguardano la sicurezza nei pazienti con BPCO, non l'efficacia nella cardiopatia polmonare cronica né nella malattia renale ipertensiva maligna.

## Informazioni sul mercato italiano

Tutte le 15 autorizzazioni risultano cancellate; il testo dell'indicazione approvata non è disponibile.

| Numero di autorizzazione | Nome prodotto | Titolare |
|---------|------|-----------|
| 041704038 | Metoprololo 30 cpr rivestite 100 mg | Aurobindo Pharma Italia Srl |
| 029036098 | Metoprololo 30 cpr 100 mg | EG SpA |
| 023616028 | Seloken 50 cpr 100 mg | Recordati SpA |
| 032019034 | Metoprololo 28 cpr 200 mg rilascio prolungato | Sandoz SpA |
| 023610013 | Lopresor 30 cpr rivestite 100 mg | Bruno Farmaceutici SpA |

## Citotossicità

Il metoprololo non è un farmaco antineoplastico: sezione non applicabile.

## Considerazioni sulla sicurezza

- **Controindicazioni (dal grafo di conoscenza TxGNN, non dal foglietto illustrativo)**: il grafo associa il metoprololo a controindicazioni in diverse condizioni, tra cui diabete mellito e chetoacidosi diabetica, miastenia gravis, feocromocitoma, ipotensione, malattie epatiche ed encefalopatia epatica, pancreatite, malattie della colecisti, lupus eritematoso sistemico, psoriasi, gotta, anuria, ipercalcemia, iperparatiroidismo, disturbi d'ansia e distimia. Queste indicazioni richiedono conferma sul foglietto illustrativo.
- **Interazioni farmacologiche**: sono state identificate 338 interazioni. Le principali di livello moderato includono epinefrina, corticosteroidi (idrocortisone, desametasone, betametasone, budesonide, triamcinolone), anticolinergici (atropina, iosciamina, glicopirronio), bupropione, morfina, cimetidina, canagliflozin, dapagliflozin, clorpropamide, lorcaserina e sali di calcio. Interazioni minori: acido acetilsalicilico e ossido di magnesio.
- **Nota su BPCO**: lo studio BLOCK-COPD ha mostrato un aumento delle riacutizzazioni con ricovero con il metoprololo in pazienti con BPCO.

Per avvertenze e precauzioni complete, consultare il foglietto illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per la malattia renale ipertensiva maligna si basa solo sul punteggio TxGNN (livello L5), senza studi né letteratura, e il metoprololo non è di prima scelta in questa emergenza ipertensiva. Inoltre, tutte le autorizzazioni italiane sono cancellate.

**Per procedere è necessario:**
- Reperire e analizzare il foglietto illustrativo AIFA (avvertenze e controindicazioni), attualmente mancante
- Acquisire i dati sul meccanismo d'azione da DrugBank
- Verificare lo stato attuale del farmaco sul mercato italiano
- Condurre una revisione sistematica della letteratura specifica sui beta-bloccanti nell'ipertensione maligna/nefropatia ipertensiva
- Valutare, come eventuale questione di ricerca separata, la sicurezza e gli esiti del metoprololo in scompenso con BPCO (la previsione con evidenza più consistente, livello L3), tenendo conto dei risultati negativi di BLOCK-COPD
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

