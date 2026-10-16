---
layout: default
title: Quinapril
parent: Solo previsione del modello (L5)
nav_order: 370
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Quinapril: nuova indicazione prevista, Malattia renale ipertensiva maligna (livello di evidenza L5). Indicazione originale: Ipertensione (testo dell'indicazione autorizzata non disponibile nei…"
monitor_inn: "QUINAPRIL"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Quinapril
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **5** 
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

# Quinapril: Dall'ipertensione alla malattia renale ipertensiva maligna

## Sintesi in una frase

Quinapril è un inibitore dell'enzima di conversione dell'angiotensina (ACE), originariamente usato per il trattamento dell'ipertensione. Il modello TxGNN prevede che possa essere efficace per la **malattia renale ipertensiva maligna**, ma al momento **non risultano studi clinici né pubblicazioni** a sostegno diretto di questa indicazione: la previsione si basa solo sul modello e su un ragionamento di classe.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione (testo dell'indicazione autorizzata non disponibile nei dati compilati; indicazione tratta dal grafo di conoscenza TxGNN) |
| Nuova indicazione prevista | Malattia renale ipertensiva maligna |
| Punteggio di previsione TxGNN | 99,86% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 4 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione è plausibile?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle conoscenze di classe, quinapril è un inibitore dell'ACE: bloccando il sistema renina-angiotensina riduce la produzione di angiotensina II, un potente vasocostrittore, e quindi la pressione arteriosa.

Nella nefropatia ipertensiva maligna, il danno vascolare e l'ipertensione glomerulare dipendono in parte dall'angiotensina II. Per questo il blocco del sistema renina-angiotensina è meccanicisticamente coerente. Va però sottolineato che questa indicazione è molto vicina a quella originale (l'ipertensione): si tratta più di un'estensione dell'uso esistente che di un vero riposizionamento.

Anche per la seconda previsione, l'ipertensione renovascolare maligna (punteggio 99,86%), il razionale è coerente perché la malattia dipende fortemente dal sistema renina-angiotensina. Gli ACE-inibitori però comportano un rischio noto di peggioramento della funzione renale nella stenosi bilaterale dell'arteria renale, da valutare con attenzione.

Tra le altre previsioni, l'unica con un minimo di supporto è l'ipertensione polmonare da malattia polmonare e/o ipossia (punteggio 99,85%, livello L4). Uno studio preclinico sull'animale del 1996 (PMID 8873672) mostra che quinapril ha ridotto l'ipertensione polmonare ipossica e il rimodellamento vascolare. Mancano studi sull'uomo. Per l'ipertensione polmonare ad eziologia multifattoriale non chiara e per la sindrome di Braddock il razionale meccanicistico è debole o non stabilito.

---

## Evidenze da studi clinici

Attualmente non risultano studi clinici registrati correlati.

---

## Evidenze dalla letteratura

Per l'indicazione principale (malattia renale ipertensiva maligna) non è disponibile letteratura. Le uniche pubblicazioni raccolte riguardano l'ipertensione polmonare da ipossia, una previsione secondaria:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [8873672](https://pubmed.ncbi.nlm.nih.gov/8873672/) | 1996 | Studio preclinico su animali | Circulation | L'inibizione dell'ACE tissutale con quinapril riduce l'ipertensione polmonare ipossica e il rimodellamento vascolare polmonare |
| [8720418](https://pubmed.ncbi.nlm.nih.gov/8720418/) | 1996 | Studio preclinico su animali | Journal of Cardiovascular Pharmacology | Quinapril preserva la funzione meccanica ventricolare sinistra e il metabolismo energetico nei ratti dopo infarto miocardico (non riguarda direttamente l'ipertensione polmonare) |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 027225010 | QUINAZIL 28 cpr rivestite div 5 mg (Malesci) | Non indicata | Non disponibile (autorizzazione cancellata) |
| 027225034 | QUINAZIL 14 cpr rivestite div 20 mg (Malesci) | Non indicata | Non disponibile (autorizzazione cancellata) |
| 037301227 | QUINAPRIL 14 cpr rivestite 20 mg (Zentiva Italia) | Non indicata | Non disponibile (autorizzazione cancellata) |
| 037203229 | QUINAPRIL 14 cpr rivestite 20 mg (EG SpA) | Non indicata | Non disponibile (autorizzazione cancellata) |

Nessuna autorizzazione risulta attualmente valida.

---

## Considerazioni sulla sicurezza

Le informazioni del foglio illustrativo AIFA (avvertenze e controindicazioni) non sono disponibili. Di seguito i dati reperibili da altre fonti.

- **Condizioni associate a controindicazione o cautela (dal grafo di conoscenza TxGNN, non dal testo dell'etichetta)**: angioedema (acquisito, ereditario, indotto da bloccanti del sistema renina-angiotensina), malattia renale, anuria, malattia epatica ed encefalopatia epatica, pancreatite, malattia della colecisti, lupus eritematoso sistemico, diabete mellito e chetoacidosi diabetica, carenza di potassio, ipotensione, iperparatiroidismo, neutropenia e agranulocitosi, gotta/iperuricemia, malattie del tessuto connettivo, malattie ossee e cartilaginee, ittero neonatale.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni; tra quelle mostrate, una di livello **maggiore** con il citrato di potassio (rischio di iperpotassiemia) e numerose di livello moderato, tra cui metformina, acido acetilsalicilico, corticosteroidi (idrocortisone, desametasone, betametasone, triamcinolone, budesonide), tetracicline (doxiciclina, tetraciclina), dapagliflozin, canagliflozin, clorpropamide, morfina, bupropione e atropina.
- Per l'indicazione nefrologica/renovascolare è rilevante in particolare il rischio di peggioramento della funzione renale con ACE-inibitori nella stenosi bilaterale dell'arteria renale.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione ha un punteggio elevato (99,86%), ma l'evidenza è solo di livello L5: nessuno studio clinico né pubblicazione per l'indicazione principale. L'indicazione è inoltre molto vicina a quella originale, e tutte le autorizzazioni italiane risultano cancellate. Non è possibile procedere allo screening di sicurezza in assenza del foglio illustrativo.

**Per procedere sono necessari:**
- Scaricare e analizzare il foglio illustrativo AIFA (avvertenze e controindicazioni), lacuna bloccante per la valutazione di sicurezza
- Dati sul meccanismo d'azione da DrugBank
- Ricerca di studi clinici e di letteratura specifica sulla nefropatia ipertensiva maligna e sull'ipertensione renovascolare maligna
- Per l'ipertensione polmonare da ipossia: studi sull'uomo che confermino i dati preclinici (livello L4)
- Verifica della disponibilità commerciale in Italia, dato che non esistono autorizzazioni valide
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

