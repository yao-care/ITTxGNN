---
layout: default
title: Entecavir
parent: Solo previsione del modello (L5)
nav_order: 174
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-04
monitor_inn: "ENTECAVIR"
predicted_indications: ["chronic hepatitis C virus infection", "HIV infectious disease", "hepatitis C virus infection", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "hepatitis, viral, animal", "hepatitis E virus infection", "hepatitis A virus infection"]
description: "Entecavir: nuova indicazione prevista, Infezione cronica da virus dell'epatite C (chronic hepatitis C virus infection) (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Entecavir
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **9** 
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

## Entecavir: Infezione cronica da virus dell'epatite C (chronic hepatitis C virus infection)
{: .text-alpha }

## Sintesi in una frase

Entecavir è un analogo nucleosidico guanosinico che inibisce la polimerasi del virus dell'epatite B. Il modello TxGNN lo associa all'**infezione cronica da virus dell'epatite C (chronic hepatitis C virus infection)**. Gli studi raccolti (**2 studi clinici** e **20 pubblicazioni**) non testano entecavir come trattamento dell'epatite C: riguardano la prevenzione della riattivazione dell'HBV nei pazienti co-infetti durante la terapia antivirale per l'HCV. Il livello di evidenza per questa predizione è quindi **L5**.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Infezione cronica da virus dell'epatite C (chronic hepatitis C virus infection) |
| Punteggio di predizione TxGNN | 0.9998 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 20 su 20) |
| Numero di autorizzazioni | 20 (valide: 20) |
| Decisione raccomandata | Hold (in attesa) |

---

## Perché questa predizione può essere ragionevole?

Entecavir è un analogo nucleosidico della guanosina che inibisce la polimerasi dell'HBV. Non ha un'attività antivirale diretta nota contro l'HCV. L'HCV è un virus a RNA che replica tramite la RNA polimerasi RNA-dipendente NS5B, un bersaglio diverso da quello di entecavir.

L'unico collegamento plausibile riguarda la co-infezione HBV/HCV. Dopo la clearance dell'HCV con gli antivirali ad azione diretta (DAA), l'HBV può riattivarsi. In questo contesto entecavir sopprime la replicazione dell'HBV. Si tratta quindi della gestione dell'HBV nei pazienti co-infetti e non del trattamento dell'HCV.

Il punteggio elevato del modello va letto come un segnale di associazione computazionale, non come una dimostrazione di efficacia contro l'epatite C. I dati compilati non contengono informazioni dettagliate sul meccanismo d'azione. Le considerazioni sopra derivano dalla letteratura sulla co-infezione.

---

## Evidenze da studi clinici

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completato | 23 | Studio prospettico su antivirali ad azione diretta in pazienti co-infetti HCV/HBV, per valutare incidenza, morbilità, mortalità e fattori predisponenti della riattivazione dell'HBV. L'effetto sull'HCV è dovuto ai DAA, non a entecavir. |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | Non applicabile | Sconosciuto | 60 | Studio randomizzato, in aperto, a tre bracci, sulla profilassi con analoghi nucleos(t)idici (12 vs 24 settimane) contro la riattivazione dell'HBV durante terapia DAA. L'obiettivo riguarda l'HBV, non l'efficacia sull'HCV. |

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [34864158](https://pubmed.ncbi.nlm.nih.gov/34864158/) | 2022 | RCT | Clin Gastroenterol Hepatol | Studio randomizzato: entecavir previene la riattivazione dell'HBV durante la terapia con DAA nella doppia infezione HCV/HBV. |
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Coorte | Viruses | Riattivazione dell'HCV in 66 pazienti con epatite B cronica anti-HCV positivi trattati con analoghi nucleos(t)idici. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Revisione | Expert Opin Pharmacother | Progressi nel trattamento della co-infezione HBV/HCV, con rischio elevato di cirrosi e carcinoma epatocellulare. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Revisione | Minerva Gastroenterol Dietol | Antivirali per epatite B e C e loro effetti sulla funzione renale. |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Revisione | Wien Med Wochenschr | Trattamenti attuali e prospettive terapeutiche per le epatiti B e C croniche. |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Non classificato | J Gastroenterol Hepatol | Rischio di riattivazione dell'HBV durante terapia con DAA in pazienti con epatite C cronica e infezione da HBV. |
| [35108715](https://pubmed.ncbi.nlm.nih.gov/35108715/) | 2022 | Non classificato | Digestive Diseases | Incidenza e decorso clinico della riattivazione dell'HBV in pazienti HBsAg e/o anti-HBc positivi trattati con DAA per l'HCV. |
| [35327336](https://pubmed.ncbi.nlm.nih.gov/35327336/) | 2022 | Non classificato | Biomedicines | Panoramica delle terapie per le epatiti virali croniche (B, C e D). |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Non classificato | Clin Res Hepatol Gastroenterol | Gestione presente e futura delle epatiti virali B e C nei bambini. |
| [21497740](https://pubmed.ncbi.nlm.nih.gov/21497740/) | 2011 | Non classificato | Best Pract Res Clin Gastroenterol | Impatto dei trattamenti antivirali sulla progressione della fibrosi nelle epatiti virali croniche. |

---

## Informazioni sul mercato italiano

Secondo i dati locali, tutte le 20 autorizzazioni risultano valide. Il testo dell'indicazione approvata non è registrato nei dati locali. Di seguito le principali autorizzazioni:

| Numero di autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 037221076 | BARACLUDE 30 cpr rivestite 0,5 mg (Bristol-Myers Squibb) | Compresse rivestite | Non disponibile |
| 037221088 | BARACLUDE 30 cpr rivestite 1 mg (Bristol-Myers Squibb) | Compresse rivestite | Non disponibile |
| 045276019 | ENTECAVIR 30x1 cpr rivestite 0,5 mg (DOC Generici) | Compresse rivestite | Non disponibile |
| 047070014 | ENTECAVIR 30 cpr rivestite 0,5 mg (Sun Pharma Italia) | Compresse rivestite | Non disponibile |
| 045155013 | ENTECAVIR 30 cpr rivestite 0,5 mg (Sandoz) | Compresse rivestite | Non disponibile |

---

## Considerazioni di sicurezza

- **Interazioni farmacologiche**: sono state identificate 44 interazioni; quelle elencate sono di livello moderato. Tra le principali: famotidina, ranitidina, cimetidina, metformina, amoxicillina, levofloxacina, vancomicina, kanamicina, neomicina, polimixina B, mesalazina, sulfasalazina, balsalazide, olsalazina, orlistat e le formulazioni di amfotericina B.

Per le avvertenze e le controindicazioni si rimanda al foglio illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Hold (in attesa)**

**Motivazione:**
- Nessuno studio raccolto valuta entecavir come trattamento dell'infezione da HCV. Il solo RCT disponibile mostra che entecavir previene la riattivazione dell'HBV durante la terapia con DAA, e l'efficacia anti-HCV è garantita dai DAA. Senza un meccanismo anti-HCV documentato, il punteggio elevato del modello non basta a giustificare uno sviluppo come nuova indicazione. Il livello di evidenza è L5.

**Per procedere sono necessari:**
- Dati sperimentali che dimostrino un'eventuale attività antivirale diretta di entecavir contro l'HCV (studi in vitro o preclinici).
- Dati sul meccanismo d'azione dettagliato.
- Analisi delle avvertenze e delle controindicazioni dal foglio illustrativo AIFA, per completare la valutazione di sicurezza.
- Se l'interesse riguarda la co-infezione HBV/HCV, una definizione separata e formale dell'obiettivo (prevenzione della riattivazione dell'HBV) con studi di conferma più ampi, dato che i due studi clinici disponibili sono piccoli (n=23 e n=60).

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

