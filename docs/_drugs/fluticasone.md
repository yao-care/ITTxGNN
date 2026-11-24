---
layout: default
title: Fluticasone
parent: Solo previsione del modello (L5)
nav_order: 208
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "FLUTICASONE"
drugbank_id: DB13867
predicted_indications: ["migraine disorder", "Prinzmetal angina", "migraine with brainstem aura"]
description: "Fluticasone: nuova indicazione prevista, Emicrania (migraine disorder) (livello di evidenza L5). In Italia, confezioni AIFA: 20 (autorizzate: 20)"
---

# Fluticasone
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **3** 
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

## Fluticasone: Emicrania (migraine disorder)
{: .text-alpha }

## Sintesi in una frase

Il fluticasone è un corticosteroide glucocorticoide, di cui nei dati compilati per questo report non risulta però un'indicazione originale approvata in Italia (il testo delle indicazioni nelle autorizzazioni AIFA è vuoto). Il modello TxGNN ne prevede un possibile impiego nell'**emicrania (migraine disorder)**, ma a sostegno di questa direzione ci sono **0 studi clinici** e **1 pubblicazione**, che peraltro riguarda eventi avversi neuropsichiatrici e non un beneficio terapeutico.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Emicrania (migraine disorder) |
| Punteggio di previsione TxGNN | 0.9920 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 20 su 20) |
| Numero di autorizzazioni | 20 (valide: 20) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione potrebbe essere ragionevole?

Secondo la sezione «Mechanism of Action» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Fluticasone (traduzione non ufficiale): «Fluticasone propionato è un corticosteroide sintetico trifluorurato con attività antinfiammatoria. È stato dimostrato in vitro che fluticasone propionato presenta un'affinità di legame per il recettore umano dei glucocorticoidi pari a 18 volte quella del desametasone, quasi il doppio di quella del beclometasone-17-monopropionato (BMP), il metabolita attivo del beclometasone dipropionato, e oltre 3 volte quella della budesonide.» Testo originale in inglese: "Fluticasone propionate is a synthetic trifluorinated corticosteroid with anti-inflammatory activity. Fluticasone propionate has been shown in vitro to exhibit a binding affinity for the human glucocorticoid receptor that is 18 times that of dexamethasone, almost twice that of beclomethasone-17-monopropionate (BMP), the active metabolite of beclomethasone dipropionate, and over 3 times that of budesonide." ([DailyMed: Xhance (fluticasone propionate) prescribing information, Paratek Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=44fcea33-8cfa-3a5c-e063-6394a90aafb2), versione del 2026-10-23; consultato il 2026-11-19). In base alle conoscenze generali, il fluticasone è un glucocorticoide con attività antinfiammatoria, e la neuroinflammazione e l'infiammazione neurogena sono ritenute possibili contributori alla fisiopatologia dell'emicrania. Questo è però un collegamento solo ipotetico.

L'unica pubblicazione recuperata è una revisione sui corticosteroidi intranasali e sui disturbi neuropsichiatrici (PMID 18681087). Essa riguarda effetti avversi (inclusi cefalea e disturbi dell'umore/comportamento), non un beneficio terapeutico, e non supporta l'efficacia nell'emicrania: se mai, segnala un possibile problema di sicurezza.

Il punteggio elevato di TxGNN (0,992) va quindi interpretato con cautela: in assenza di studi clinici e di un meccanismo dimostrato, il legame meccanicistico resta non accertato.

### Altre previsioni del modello (per completezza)

- **Angina di Prinzmetal** (punteggio 0,9919, livello L5): nessuno studio clinico né pubblicazione. L'angina vasospastica è guidata da vasospasmo coronarico, disfunzione endoteliale e iperreattività della muscolatura liscia; non è stato identificato alcun meccanismo plausibile che colleghi il fluticasone al controllo del vasospasmo. Il punteggio deriva dal modello TxGNN (deep learning) e può riflettere somiglianze apprese dal modello tra malattie correlate, non evidenze biologiche.
- **Emicrania con aura del tronco encefalico** (punteggio 0,9909, livello L5): nessuno studio clinico né pubblicazione. Il punteggio riflette probabilmente la vicinanza ontologica al termine genitore "emicrania" e non un'evidenza indipendente.

---

## Evidenze da studi clinici

Al momento non risulta alcuno studio clinico registrato correlato.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [18681087](https://pubmed.ncbi.nlm.nih.gov/18681087/) | 2008 | Revisione | Annals of Allergy, Asthma & Immunology | Revisione dei dati di farmacovigilanza OMS: un insieme inatteso di segnalazioni di disturbi neuropsichiatrici durante l'uso di corticosteroidi intranasali. Non fornisce evidenza di efficacia nell'emicrania. |

---

## Informazioni sul mercato italiano

Il testo delle indicazioni approvate e la forma farmaceutica non sono riportati nei dati compilati.

<!-- licenses:begin -->

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|------|------|------|------|
| 029014014 | FLIXODERM\*crema derm 30 g 0,5 mg/g | GLAXOSMITHKLINE SpA | Autorizzata |
| 028667020 | FLIXOTIDE 50\*sosp inal 120 erog 50 mcg | GLAXOSMITHKLINE SpA | Autorizzata |
| 043082015 | FLUTICASONE\*sosp inal 120 erog 125 mcg | DOC GENERICI Srl | Autorizzata |
| 028675104 | FLUSPIRAL\*sosp inal 120 dosi 50 mcg | A.MENARINI IND.FARM.RIUN.Srl | Autorizzata |
| 028675270 | FLUSPIRAL\*DISKUS polv inal 60 dosi 250 mcg | A.MENARINI IND.FARM.RIUN.Srl | Autorizzata |
| 028667208 | FLIXOTIDE 500\*60 dosi 500 mcg polv inal | GLAXOSMITHKLINE SpA | Autorizzata |
| 028675181 | FLUSPIRAL\*sosp inal 120 dosi 250 mcg | A.MENARINI IND.FARM.RIUN.Srl | Autorizzata |
| 028667107 | FLIXOTIDE 250\*sosp inal 120 erog 250 mcg | GLAXOSMITHKLINE SpA | Autorizzata |
| 029014038 | FLIXODERM\*ung derm 30 g 0,05 mg/g | GLAXOSMITHKLINE SpA | Autorizzata |
| 043088020 | FLUGENIX\*sosp nebul 20 contenitori monod 2 ml 500 mcg/2 ml | GENETIC SpA | Autorizzata |
| 043084021 | PAVETOD\*sosp nebul 20 contenitori monod 500 mcg 2 ml | GENETIC SpA | Autorizzata |
| 043082027 | FLUTICASONE\*sosp inal 120 erog 250 mcg | DOC GENERICI Srl | Autorizzata |
| 028675179 | FLUSPIRAL\*sosp inal 120 dosi 125 mcg | A.MENARINI IND.FARM.RIUN.Srl | Autorizzata |
| 028675282 | FLUSPIRAL\*DISKUS polv inal 60 dosi 500 mcg | A.MENARINI IND.FARM.RIUN.Srl | Autorizzata |
| 028667095 | FLIXOTIDE 125\*sosp inal 120 erog 125 mcg | GLAXOSMITHKLINE SpA | Autorizzata |
| 028675268 | FLUSPIRAL\*DISKUS polv inal 60 dosi 100 mcg | A.MENARINI IND.FARM.RIUN.Srl | Autorizzata |
| 043084045 | PAVETOD\*sosp nebul 20 contenitori monod 2 mg 2 ml | GENETIC SpA | Autorizzata |
| 039738012 | FLUTICREM\*crema derm 30 g 0,05% | DIFA COOPER SpA | Autorizzata |
| 028667184 | FLIXOTIDE 250\*polv inal 60 dosi 250 mcg | GLAXOSMITHKLINE SpA | Autorizzata |
| 043088044 | FLUGENIX\*sosp nebul 20 contenitori monod 2 ml 2 mg/2 ml | GENETIC SpA | Autorizzata |

Fonte: AIFA, elenco delle confezioni autorizzate (open data), stato amministrativo; confezioni autorizzate per prime.

<!-- licenses:end -->

---

## Considerazioni sulla sicurezza

- **Interazioni farmacologiche**: sono state identificate 100 interazioni complessive; tra quelle elencate:
  - **Maggiore**: claritromicina.
  - **Moderata**: aprepitant, insulina umana (inalatoria, ad azione rapida).
  - **Livello non classificato**: calcitriolo, fentermina, pantoprazolo, mesalazina, doxiciclina, clotrimazolo, morfina, omeprazolo, lansoprazolo, cimetidina, vancomicina, levocarnitina, nizatidina, triamcinolone, oxandrolone, prednisone, simvastatina.
- Per avvertenze e controindicazioni si rimanda al foglio illustrativo, non disponibile nei dati compilati.
- La revisione di farmacovigilanza (PMID 18681087) segnala possibili disturbi neuropsichiatrici con corticosteroidi intranasali.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si basa quasi esclusivamente sul punteggio del modello TxGNN. Non ci sono studi clinici, l'unica pubblicazione riguarda eventi avversi e non efficacia, il meccanismo non è dimostrato.

<!-- review:begin it-lic-20261106-fluticasone-1 -->

> **Correzione di verifica (2026-11-24)**: Testo originale: «Non ci sono studi clinici, l'unica pubblicazione riguarda eventi avversi e non efficacia, il meccanismo non è dimostrato e tutte le autorizzazioni italiane sono cancellate.» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). I numeri aggiornati delle autorizzazioni sono nella panoramica rapida e nella tabella delle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-fluticasone-1 -->

**Per procedere è necessario:**
- Recuperare avvertenze e controindicazioni dal foglio illustrativo AIFA (lacuna bloccante per lo screening di sicurezza).
- Acquisire i dati sul meccanismo d'azione (ad es. tramite DrugBank).
- Individuare le indicazioni originali approvate e le forme farmaceutiche.
- Cercare evidenze precliniche o cliniche sull'uso di corticosteroidi nell'emicrania, valutando il segnale neuropsichiatrico.
- Chiarire la compatibilità della via di somministrazione, dato che nessun prodotto è oggi in commercio in Italia.

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale).

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-24 | Rimosso: «e tutte le autorizzazioni italiane sono cancellate» | Corretto (rivisto il 2026-11-24; versione precedente conservata nel registro) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: Xhance (fluticasone propionate) prescribing information, Paratek Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=44fcea33-8cfa-3a5c-e063-6394a90aafb2) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

