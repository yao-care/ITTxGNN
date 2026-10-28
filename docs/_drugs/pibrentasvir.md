---
layout: default
title: Pibrentasvir
parent: Solo previsione del modello (L5)
nav_order: 349
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
monitor_inn: "pibrentasvir"
predicted_indications: ["hepatitis B virus infection", "HIV infectious disease", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal", "Omsk hemorrhagic fever", "Kyasanur forest disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
description: "Pibrentasvir: nuova indicazione prevista, Infezione da virus dell'epatite B (hepatitis B virus infection) (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Pibrentasvir
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

## Pibrentasvir: Infezione da virus dell'epatite B (hepatitis B virus infection)
{: .text-alpha }

## Sintesi in una frase

Pibrentasvir è un inibitore della proteina virale NS5A, usato in combinazione con glecaprevir per il trattamento dell'infezione cronica da virus dell'epatite C (HCV). Il modello TxGNN lo prevede attivo contro l'**infezione da virus dell'epatite B**, ma per questa indicazione non esistono **studi clinici** e la letteratura recuperata riguarda esclusivamente l'HCV: la previsione è quindi solo di tipo computazionale, senza evidenze a supporto.

---

## Quadro di sintesi

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Infezione da virus dell'epatite B (hepatitis B virus infection) |
| Punteggio di previsione TxGNN | 0.9984 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 2 su 2) |
| Numero di autorizzazioni | 2 (valide: 2) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione è plausibile?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrati per questo farmaco. In base alle informazioni note, pibrentasvir è un inibitore di NS5A, componente della combinazione glecaprevir/pibrentasvir (Maviret), la cui efficacia nell'epatite C è documentata.

Per l'epatite B, però, il collegamento meccanicistico è debole. HBV non possiede un omologo di NS5A, quindi il farmaco non ha un bersaglio antivirale diretto noto. Il punteggio elevato è probabilmente dovuto alla prossimità, nella rete di conoscenza, con altri termini di epatite virale, più che a un meccanismo reale.

Anche la letteratura recuperata riguarda l'HCV (epatite C pediatrica, ritrattamento dopo fallimento dei DAA, farmacocinetica e farmacodinamica) e non mostra alcuna attività anti-HBV. Sul piano clinico, la riattivazione dell'HBV durante la terapia con DAA anti-HCV è un tema di sicurezza, non un effetto terapeutico.

---

## Evidenze dagli studi clinici

Per l'infezione da virus dell'epatite B attualmente non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

Le pubblicazioni recuperate per questa previsione sono tutte di tipo revisione e riguardano l'HCV; nessuna dimostra attività anti-HBV.

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Revisione | Lancet Gastroenterol Hepatol | Infezione da HCV in bambini e adolescenti; i DAA orali a breve durata hanno trasformato il trattamento |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Revisione | World J Gastroenterol | Gestione dell'epatite virale pediatrica: DAA disponibili per l'HCV, trattamento dell'HBV ancora lontano dalla guarigione |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Revisione | Semin Liver Dis | Ritrattamento dei pazienti HCV con fallimento dei DAA |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Revisione | Clin Pharmacokinet | Aspetti farmacocinetici e farmacodinamici della terapia anti-HCV, incluso glecaprevir/pibrentasvir |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Revisione | Eur J Gen Pract | Diagnosi e trattamento semplificati dell'epatite C cronica |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Report di conferenza | AIDS Rev | Aggiornamenti sul trattamento dell'epatite virale e sui DAA pangenotipici |
| [42127258](https://pubmed.ncbi.nlm.nih.gov/42127258/) | 2026 | Revisione | Top Antivir Med | Sintesi generale della conferenza CROI 2026 sull'epatite virale, senza dati specifici su pibrentasvir |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 045445018 | MAVIRET 4x21 cpr rivestite 100 mg + 40 mg, confezione multipla (stato: valida) | — | — |
| 045445032 | MAVIRET 28 bustine orali granulato 50 mg + 20 mg (stato: valida) | — | — |

Entrambe le autorizzazioni, intestate ad AbbVie Deutschland GmbH & Co.

---

## Considerazioni sulla sicurezza

Per le informazioni di sicurezza si rimanda al foglio illustrativo. Non risultano interazioni farmacologiche censite nei dati compilati per questo report.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per l'epatite B si basa solo sul modello di rete (livello di evidenza L5): non ci sono studi clinici, la letteratura riguarda solo l'HCV e manca un razionale meccanicistico, dato che HBV non ha un omologo di NS5A. Inoltre, le autorizzazioni italiane risultano tutte cancellate.

**Per procedere sarebbe necessario:**
- Dati sul meccanismo d'azione da DrugBank
- Testi di avvertenze e controindicazioni dal foglio illustrativo AIFA
- Studi preclinici in vitro sull'attività anti-HBV di pibrentasvir
- Chiarimento sulle ragioni della cancellazione delle autorizzazioni italiane

**Nota sulle altre previsioni:** tra le altre indicazioni previste, solo l'infezione da HIV ha studi clinici di fase 3 (ad esempio EXPEDITION-2, NCT02738138), ma questi misurano la guarigione dell'HCV in pazienti coinfetti e non un'attività anti-HIV; si tratta quindi di un'estensione dell'indicazione originale e non di un vero riposizionamento. Tutte le altre previsioni hanno decisione Hold, senza evidenze a supporto.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

