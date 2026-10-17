---
layout: default
title: Pantoprazole
parent: Prove elevate (L1-L2)
nav_order: 339
evidence_level: L1
indication_count: 6
last_modified_at: 2026-10-15
description: "Pantoprazole: nuova indicazione prevista, Ulcera peptica attiva (livello di evidenza L1). Indicazione originale: Ulcera peptica, malattia da reflusso gastroesofageo, esofagite…"
monitor_inn: "pantoprazole"
predicted_indications: ["duodenal obstruction"]
---

# Pantoprazole
{: .fs-9 }

Livello di evidenza: **L1** | Indicazioni previste: **6** 
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

# Pantoprazolo: dall'ulcera peptica all'ulcera peptica attiva (uso già in etichetta)

## Riepilogo in breve

Il pantoprazolo è un inibitore della pompa protonica, originariamente usato per ulcera peptica, malattia da reflusso gastroesofageo ed esofagite, oltre che per la sindrome di Zollinger-Ellison.
Il modello TxGNN lo indica come potenzialmente efficace per l'**ulcera peptica attiva**, con **1 studio clinico** registrato per questa indicazione (Fase 3, completato) e **18 pubblicazioni**. Va però precisato che questa è un'indicazione già coperta dall'uso originale: non si tratta di un vero riposizionamento. Il punteggio molto alto riflette questa coincidenza.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ulcera peptica, malattia da reflusso gastroesofageo, esofagite, sindrome di Zollinger-Ellison (dal grafo di conoscenza; il testo autorizzato AIFA non è disponibile) |
| Nuova indicazione prevista | Ulcera peptica attiva |
| Punteggio di predizione TxGNN | 99,69% |
| Livello di evidenza | L1 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Proceed with Guardrails (procedere con cautele) |

---

## Perché questa predizione è ragionevole?

Il pantoprazolo inibisce in modo irreversibile la pompa protonica H+/K+ ATPasi delle cellule parietali gastriche, riducendo la secrezione acida e consentendo la guarigione dell'ulcera. I dati dettagliati sul meccanismo d'azione non sono disponibili nei dati compilati per questo report; la descrizione sopra deriva dalla letteratura recuperata.

L'ulcera peptica attiva coincide con l'indicazione originale: la predizione è quindi coerente, ma non rappresenta una nuova indicazione. Il punteggio elevato è in linea con questa sovrapposizione.

Anche le altre predizioni del modello riguardano condizioni legate all'acidità gastrica. Per quelle con evidenza più debole (ulcera gastrodigiunale, perforazione ulcerosa, reflusso duodenogastrico) il legame è indiretto; per l'ostruzione duodenale non emerge alcun legame meccanicistico credibile e la raccomandazione è Hold.

---

## Evidenze dagli studi clinici

Per l'ulcera peptica attiva:

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Fase 3 | Completato | 323 | Studio multicentrico, randomizzato, in doppio cieco, con controllo attivo: ilaprazolo vs pantoprazolo in triplice terapia di 7 giorni per l'eradicazione di H. pylori in pazienti con ulcera gastrica e/o duodenale. Comparatore e braccio di trattamento da verificare, perché il titolo è troncato |

Per l'ulcera duodenale (predizione di rango 6), sono stati registrati ulteriori studi rilevanti:

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00374101](https://clinicaltrials.gov/study/NCT00374101) | Fase 3 | Completato | 450 | PPI ad alte dosi vs dosi standard con terapia endoscopica nell'ulcera peptica sanguinante |
| [NCT00843063](https://clinicaltrials.gov/study/NCT00843063) | Fase 4 | Completato | 161 | Famotidina vs pantoprazolo nella prevenzione delle recidive di ulcera/erosione da aspirina |
| [NCT02551744](https://clinicaltrials.gov/study/NCT02551744) | N/D | Completato | 101 | Pantoprazolo vs famotidina nella prevenzione delle recidive di ulcera in chi usa tienopiridine |
| [NCT00261300](https://clinicaltrials.gov/study/NCT00261300) | Fase 3 | Completato | 100 | Studio a lungo termine con pantoprazolo in disturbi acido-peptici cronici |
| [NCT02467621](https://clinicaltrials.gov/study/NCT02467621) | Fase 4 | Completato | 3350 | SUP-ICU: profilassi dell'ulcera da stress in terapia intensiva (quesito clinico diverso) |
| [NCT01182597](https://clinicaltrials.gov/study/NCT01182597) | Fase 3 | Stato sconosciuto | 190 | PPI orale vs endovenoso nelle ulcere sanguinanti ad alto rischio dopo emostasi |
| [NCT00161096](https://clinicaltrials.gov/study/NCT00161096) | Fase 3 | Stato sconosciuto | 276 | Pantoprazolo 20 mg al bisogno vs giornaliero dopo sollievo dei sintomi |
| [NCT00001191](https://clinicaltrials.gov/study/NCT00001191) | Fase 2 | Completato | N/D | Omeprazolo orale e pantoprazolo EV nell'ipersecrezione acida (Zollinger-Ellison) |
| [NCT00839488](https://clinicaltrials.gov/study/NCT00839488) | Fase 4 | Terminato | 6 | Pantoprazolo EV vs famotidina nella profilassi dell'ulcera da stress (arruolamento troppo basso) |
| [NCT00881413](https://clinicaltrials.gov/study/NCT00881413) | Fase 4 | Ritirato | 0 | Esomeprazolo EV vs pantoprazolo nella prevenzione del risanguinamento (nessun dato) |

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [7569755](https://pubmed.ncbi.nlm.nih.gov/7569755/) | 1995 | RCT | Scand J Gastroenterol | Pantoprazolo vs ranitidina nell'ulcera duodenale acuta (studio multicentrico) |
| [7614102](https://pubmed.ncbi.nlm.nih.gov/7614102/) | 1995 | RCT | Eur J Gastroenterol Hepatol | Confronto in doppio cieco pantoprazolo 40 mg vs omeprazolo 20 mg nell'ulcera duodenale acuta |
| [31054846](https://pubmed.ncbi.nlm.nih.gov/31054846/) | 2019 | RCT | Gastroenterology | Pantoprazolo vs placebo per prevenire eventi gastroduodenali con rivaroxaban e/o aspirina |
| [19837071](https://pubmed.ncbi.nlm.nih.gov/19837071/) | 2010 | RCT | Gastroenterology | Famotidina inferiore al pantoprazolo nel prevenire recidive di ulcere da aspirina |
| [30354950](https://pubmed.ncbi.nlm.nih.gov/30354950/) | 2018 | RCT | N Engl J Med | Pantoprazolo in pazienti ICU a rischio di sanguinamento gastrointestinale |
| [38252210](https://pubmed.ncbi.nlm.nih.gov/38252210/) | 2024 | RCT/Meta-analisi | Dig Dis Sci | Pantoprazolo e vonoprazan efficaci nel prevenire la recidiva di ulcera in chi usa aspirina a basse dosi |
| [8882382](https://pubmed.ncbi.nlm.nih.gov/8882382/) | 1996 | Revisione | Drugs | Il pantoprazolo 40 mg è superiore alla ranitidina ed equivalente all'omeprazolo nel trattamento a breve termine di ulcera peptica ed esofagite da reflusso |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Revisione | Clin Drug Investig | Profilo del pantoprazolo come PPI; nessuna interazione farmacologica identificata in numerosi studi |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Revisione sistematica/network meta-analisi | Am J Gastroenterol | Confronto tra P-CAB e PPI nell'esofagite di grado C/D |
| [8180294](https://pubmed.ncbi.nlm.nih.gov/8180294/) | 1994 | Analisi aggregata | Aliment Pharmacol Ther | Nell'ulcera duodenale, guarigione migliore con pantoprazolo 40 mg che con ranitidina a 2 e 4 settimane |

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano **cancellate**; non ne è attiva alcuna. I testi delle indicazioni approvate e le forme farmaceutiche non sono disponibili. Principali prodotti:

| N. autorizzazione | Nome prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 042953063 | PANTORC 14 cpr gastroresistenti 20 mg | GMM FARMA Srl | Cancellata |
| 038730053 | PANTOPRAZOLO 28 cpr gastroresistenti 20 mg | ALMUS Srl | Cancellata |
| 039015134 | PANTOPRAZOLO 14 cpr gastroresistenti 40 mg | SUN PHARMACEUTICAL IND. EU B.V. | Cancellata |
| 041979028 | INIPANT 14 cpr gastroresistenti 40 mg | SO.SE.PHARM Srl | Cancellata |
| 038253264 | GASTROLOC 14 cpr gastroresistenti 40 mg | HALEON ITALY Srl | Cancellata |

---

## Considerazioni sulla sicurezza

- **Controindicazioni suggerite dal grafo di conoscenza** (non derivano dal foglio illustrativo): osteoporosi, osteoporosi postmenopausale, frattura ossea, anemia perniciosa.
- **Interazioni farmacologiche**: sono state rilevate 597 interazioni. Tra quelle di livello **maggiore** figurano acalabrutinib e atazanavir. Tra quelle di livello moderato: idroclorotiazide, alpelisib, anfotericina B, amikacina, anfetamina, fenofibrato, apalutamide, armodafinil, atorvastatina, bosutinib e bumetanide. Tra quelle minori: acido acetilsalicilico, assitinib, bortezomib, brivaracetam e cianocobalamina.

Per avvertenze e controindicazioni ufficiali, consultare il foglio illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Proceed with Guardrails**

**Motivazione:**
Esistono studi di Fase 3 completati e RCT storici che supportano l'efficacia del pantoprazolo nell'ulcera peptica e duodenale. Si tratta però di un uso già in etichetta, non di un riposizionamento, e tutte le autorizzazioni italiane risultano cancellate.

**Per procedere sono necessari:**
- Verifica dello stato commerciale effettivo in Italia, dato che tutte le autorizzazioni sono cancellate
- Acquisizione del foglio illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Dati sul meccanismo d'azione da DrugBank
- Verifica di comparatore e braccio di trattamento in NCT02084420 (titolo troncato)
- Per le predizioni davvero nuove (ulcera gastrodigiunale, perforazione, reflusso duodenogastrico), studi mirati: l'evidenza attuale è indiretta o limitata. Per l'ostruzione duodenale, nessun legame meccanicistico: Hold.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

