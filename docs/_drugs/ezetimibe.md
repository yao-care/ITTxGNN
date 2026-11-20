---
layout: default
title: Ezetimibe
parent: Solo previsione del modello (L5)
nav_order: 188
evidence_level: L5
indication_count: 1
monitor_inn: "EZETIMIBE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-20
description: "Ezetimibe: nuova indicazione prevista, Carenza di proteina di trasferimento degli esteri del colesterolo (livello di evidenza L5). Indicazione originale: Iperlipidemia e forme correlate"
---

# Ezetimibe
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

## Ezetimibe: dall'ipercolesterolemia alla carenza di proteina di trasferimento degli esteri del colesterolo
{: .text-alpha }

## Sintesi in una frase

Ezetimibe è un inibitore dell'assorbimento intestinale del colesterolo, utilizzato nelle dislipidemie (iperlipidemia, ipercolesterolemia familiare omozigote, sitosterolemia secondo le relazioni registrate nel knowledge graph). Il modello TxGNN ne prevede un possibile utilizzo nella **carenza di proteina di trasferimento degli esteri del colesterolo (CETP)**, ma al momento sono disponibili **0 studi clinici** e **nessuna pubblicazione che studi direttamente questa malattia**: la previsione si basa solo sul modello.

## Quadro d'insieme

| Voce | Contenuto |
|------|------|
| Indicazione originale | Iperlipidemia e forme correlate (relazioni registrate nel knowledge graph; i testi autorizzativi AIFA non riportano l'indicazione) |
| Nuova indicazione prevista | Carenza di proteina di trasferimento degli esteri del colesterolo |
| Punteggio di previsione TxGNN | 0,9909 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: almeno 20) |
| Numero di autorizzazioni | almeno 20 |
| Decisione raccomandata | Hold |

## Perché questa previsione potrebbe essere ragionevole?

Secondo la sezione «Mechanism of Action» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Ezetimibe (traduzione non ufficiale): «Ezetimibe riduce il colesterolo ematico inibendo l'assorbimento del colesterolo a livello dell'intestino tenue. È stato dimostrato che il bersaglio molecolare di ezetimibe è il trasportatore degli steroli Niemann-Pick C1-Like 1 (NPC1L1), coinvolto nella captazione intestinale del colesterolo e dei fitosteroli.» Testo originale in inglese: "Ezetimibe reduces blood cholesterol by inhibiting the absorption of cholesterol by the small intestine. The molecular target of ezetimibe has been shown to be the sterol transporter, Niemann-Pick C1-Like 1 (NPC1L1), which is involved in the intestinal uptake of cholesterol and phytosterols." ([DailyMed: ezetimibe prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c37c695b-fb40-423c-9b73-d1aa58a34db9), versione del 2026-10-08; consultato il 2026-11-19). In base alle conoscenze generali, ezetimibe inibisce il trasportatore NPC1L1 e riduce l'assorbimento intestinale del colesterolo, abbassando il colesterolo LDL.

La carenza di CETP è caratterizzata da HDL-C elevato e da un ridotto trasferimento di esteri del colesterolo dalle HDL alle lipoproteine contenenti apoB. I due ambiti condividono vie del metabolismo lipidico, e questo probabilmente spiega il punteggio elevato del modello.

Tuttavia non esistono evidenze meccanicistiche o cliniche dirette che colleghino ezetimibe al trattamento di questa condizione. La carenza di CETP è inoltre un tratto genetico con HDL-C elevato, non una malattia con un bisogno consolidato di terapia ipolipemizzante. Il legame resta una previsione basata sulla rete di relazioni.

## Evidenze da studi clinici

Attualmente non sono registrati studi clinici correlati.

## Evidenze dalla letteratura

Le due pubblicazioni raccolte non studiano direttamente la carenza di CETP, e sono riportate solo come contesto.

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [40911366](https://pubmed.ncbi.nlm.nih.gov/40911366/) | 2025 | Revisione | European Heart Journal | Panoramica dei bersagli terapeutici per la riduzione dei lipidi, dalle basi molecolari alle implicazioni traslazionali |
| [31779098](https://pubmed.ncbi.nlm.nih.gov/31779098/) | 2019 | Studio animale | International Journal of Molecular Sciences | Modello di criceto con deficit eterozigote di Ldlr per valutare un anticorpo anti-PCSK9 in iperlipidemia e aterosclerosi |

## Informazioni sul mercato italiano

L'elenco può essere parziale (almeno 20 autorizzazioni; sono riportate le prime 5). Nei dati compilati non sono presenti testi dell'indicazione approvata né la forma farmaceutica (le denominazioni indicano compresse da 10 mg).

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 045314162 | EZETIMIBE*30 cpr 10 mg | Accord Healthcare SLU | Valida |
| 044521033 | EZETIMIBE*50 cpr 10 mg | Laboratori Alter Srl | Valida |
| 045008137 | EZETIMIBE*50 cpr 10 mg | Zentiva Italia Srl | Valida |
| 036017147 | ZETIA*30 cpr 10 mg | Neopharmed Gentili SpA | Valida |
| 042752461 | EZETIMIBE*30 cpr 10 mg | Mylan SpA | Valida |

## Considerazioni sulla sicurezza

- **Controindicazioni registrate nel knowledge graph** (non derivate dal testo dell'etichetta): pancreatite, malattie del fegato, malattie della colecisti, miopatia, malattie muscolari, malattie del muscolo scheletrico, paralisi periodica familiare, abuso/dipendenza da sostanze, rabdomiolisi, fascite nodulare.
- **Interazioni farmacologiche**: sono state rilevate 100 interazioni. Quelle di livello moderato includono acido chenodesossicolico, eluxadolina, rosuvastatina e simvastatina. Altre interazioni, di livello non classificato, riguardano ad esempio calcitriolo, pantoprazolo, glimepiride, mesalazina, doxiciclina, metformina, omeprazolo e vancomicina.

Per le avvertenze e le controindicazioni ufficiali fare riferimento al foglio illustrativo.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si fonda esclusivamente sul modello (livello L5): non vi sono studi clinici né pubblicazioni che studino direttamente la carenza di CETP. Inoltre, trattandosi di un tratto con HDL-C elevato, la necessità clinica di una terapia ipolipemizzante non è stabilita.

**Per procedere, sono necessari:**
- Dati sul meccanismo d'azione (MOA) da fonti dedicate
- Avvertenze e controindicazioni dal foglio illustrativo AIFA
- Evidenze precliniche o cliniche che colleghino direttamente ezetimibe alla carenza di CETP
- Una valutazione del reale bisogno clinico di una terapia in questa condizione

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale); le predizioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti.

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: ezetimibe prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c37c695b-fb40-423c-9b73-d1aa58a34db9) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

