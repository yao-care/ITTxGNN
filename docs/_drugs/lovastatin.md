---
layout: default
title: Lovastatin
parent: Solo previsione del modello (L5)
nav_order: 279
evidence_level: L5
indication_count: 1
monitor_inn: "Lovastatin"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-24
description: "Lovastatin: nuova indicazione prevista, Deficit di proteina di trasferimento degli esteri del colesterolo (livello di evidenza L5). Indicazione originale: Disturbi dei lipidi"
---

# Lovastatin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **1** 
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

## Lovastatina: dall'ipercolesterolemia al deficit di proteina di trasferimento degli esteri del colesterolo (CETP)
{: .text-alpha }

## Sintesi in una frase

La lovastatina è una statina, inibitrice della HMG-CoA reduttasi, utilizzata per i disturbi dei lipidi (ipertrigliceridemia, iperlipidemia, aterosclerosi). Il modello TxGNN prevede che possa essere utile per il **deficit di proteina di trasferimento degli esteri del colesterolo**, ma al momento **non risulta alcuno studio clinico** e **nessuna pubblicazione** che studi direttamente questa malattia: la previsione si basa solo sul modello.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Disturbi dei lipidi (relazioni registrate nel knowledge graph: ipertrigliceridemia, iperlipidemia, iperlipidemia familiare, aterosclerosi); il testo delle autorizzazioni AIFA non riporta l'indicazione |
| Nuova indicazione prevista | Deficit di proteina di trasferimento degli esteri del colesterolo |
| Punteggio di previsione TxGNN | 0,9942 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 14 su 14) |
| Numero di autorizzazioni | 14 (valide: 14) |
| Decisione raccomandata | Hold (sospendere) |

## Perché questa previsione potrebbe essere ragionevole?

Secondo la sezione «Clinical Pharmacology» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Lovastatin (traduzione non ufficiale): «Il meccanismo dell'effetto di riduzione delle LDL della lovastatina può comportare sia la riduzione della concentrazione di VLDL-C sia l'induzione del recettore delle LDL, determinando una ridotta produzione e/o un aumentato catabolismo delle LDL-C. Anche l'apolipoproteina B diminuisce durante il trattamento con lovastatina. La lovastatina è un inibitore specifico della HMG-CoA reduttasi, l'enzima che catalizza la conversione dell'HMG-CoA in mevalonato.» Testo originale in inglese: "The mechanism of the LDL-lowering effect of lovastatin may involve both reduction of VLDL-C concentration, and induction of the LDL receptor, leading to reduced production and/or increased catabolism of LDL-C. Apolipoprotein B also falls during treatment with lovastatin. Lovastatin is a specific inhibitor of HMG-CoA reductase, the enzyme which catalyzes the conversion of HMG-CoA to mevalonate." ([DailyMed: lovastatin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ac86821f-d741-4ab1-bd03-ce8797dd4f34), versione del 2026-11-13; consultato il 2026-11-19). In generale, la lovastatina è un inibitore della HMG-CoA reduttasi (enzima HMGCR, confermato tra i target farmacologici) che riduce il colesterolo LDL. Risulta inoltre tra i suoi target il recettore X del pregnano (NR1I2).

Il deficit di CETP è un disturbo del metabolismo lipoproteico, caratterizzato da HDL-colesterolo elevato e da alterato trasferimento degli esteri del colesterolo. Esiste quindi un legame biologico plausibile attraverso il metabolismo lipidico.

Tuttavia, non esistono prove dirette che colleghino la lovastatina a questa condizione. Il deficit di CETP è tipicamente un tratto genetico con HDL-C elevato e in genere non richiede un trattamento ipolipemizzante, per cui la logica terapeutica resta poco chiara. Il punteggio del modello è una semplice previsione.

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [19965609](https://pubmed.ncbi.nlm.nih.gov/19965609/) | 2010 | Studio preclinico (modello animale knockout) | Journal of lipid research | La delezione di StARD4, proteina di trasferimento lipidico, nel topo causa modesta riduzione del peso e lievi alterazioni del metabolismo lipidico. Non riguarda né la lovastatina né il deficit di CETP |

## Informazioni sul mercato italiano

Le 14 autorizzazioni sono tutte valide e riguardano prodotti a singolo principio attivo. Il testo dell'indicazione approvata e la forma farmaceutica non sono riportati nei dati.

<!-- licenses:begin -->

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|------|------|------|------|
| 046720025 | LOVASTATINA\*30 cpr 20 mg | DOC GENERICI Srl | Autorizzata |
| 035638055 | REXTAT\*30 cpr 20 mg | RECORDATI SpA | Autorizzata |
| 046720037 | LOVASTATINA\*30 cpr 40 mg | DOC GENERICI Srl | Autorizzata |
| 035638067 | REXTAT\*30 cpr 40 mg | RECORDATI SpA | Autorizzata |
| 047443027 | LOVASTATINA\*30 cpr 20 mg | EG SpA | Autorizzata |
| 035623053 | TAVACOR\*30 cpr 20 mg | I.B.N. SAVIO Srl | Autorizzata |
| 035615057 | LOVINACOR\*30 cpr 40 mg | INNOVA PHARMA SpA | Autorizzata |
| 035623077 | TAVACOR\*30 cpr 40 mg | I.B.N. SAVIO Srl | Autorizzata |
| 035615069 | LOVINACOR\*30 cpr 20 mg | INNOVA PHARMA SpA | Autorizzata |
| 046526012 | LOVASTATINA\*30 cpr 20 mg | TEVA B.V. | Autorizzata |
| 046526024 | LOVASTATINA\*30 cpr 40 mg | TEVA B.V. | Autorizzata |
| 046527014 | LOVASTATINA\*30 cpr 20 mg | MYLAN SpA | Autorizzata |
| 046527026 | LOVASTATINA\*30 cpr 40 mg | MYLAN SpA | Autorizzata |
| 047443039 | LOVASTATINA\*30 cpr 40 mg | EG SpA | Autorizzata |

Fonte: AIFA, elenco delle confezioni autorizzate (open data), stato amministrativo; confezioni autorizzate per prime.

<!-- licenses:end -->

## Considerazioni sulla sicurezza

- **Controindicazioni riportate nel knowledge graph** (relazioni del grafo, non testo del foglio illustrativo): malattia epatica, malattia della colecisti, trombocitopenia, iperglicemia, ulcera peptica, miopatia e malattie muscolari, rabdomiolisi, diabete mellito e chetoacidosi diabetica, ipotensione, gotta, abuso/dipendenza da sostanze, disturbi della coagulazione, sindrome coronarica acuta, coronaropatia, infarto miocardico, trombosi coronarica, emoglobinopatie, ipofosfatemia e altre condizioni.
- **Interazioni farmacologiche**: i dati compilati riportano solo interazioni di tipo farmacologico con i target, cioè il recettore X del pregnano (NR1I2) e la HMG-CoA reduttasi (HMGCR). Non sono disponibili interazioni con altri farmaci a livello clinico.

Per avvertenze e controindicazioni ufficiali si rimanda al foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Non esiste alcuno studio clinico né alcuna pubblicazione che studi direttamente il deficit di CETP con la lovastatina; l'unica fonte è una previsione del modello (livello L5). Inoltre, il deficit di CETP di norma non richiede una terapia ipolipemizzante, quindi il razionale terapeutico è debole.

**Per procedere sarebbe necessario:**
- Dati sul meccanismo d'azione e un'analisi del legame meccanicistico con il deficit di CETP
- Evidenze cliniche o precliniche che riguardino direttamente questa malattia
- Una definizione chiara del bisogno clinico (beneficio atteso in una condizione con HDL elevato)
- Avvertenze e controindicazioni dal foglio illustrativo AIFA, per completare la valutazione di sicurezza

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale); le predizioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti.

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: lovastatin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ac86821f-d741-4ab1-bd03-ce8797dd4f34) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

