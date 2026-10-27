---
layout: default
title: Pravastatin
parent: Prove elevate (L1-L2)
nav_order: 359
evidence_level: L2
indication_count: 9
last_modified_at: 2026-10-15
description: "Pravastatin: nuova indicazione prevista, Infezione da HIV (dislipidemia e rischio cardiovascolare associati) (livello di evidenza L2). Indicazione originale: Iperlipidemie (ipertrigliceridemia, iperl…"
monitor_inn: "Pravastatin"
predicted_indications: ["HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "hypoalphalipoproteinemia", "cholesterol-ester transfer protein deficiency"]
---

# Pravastatin
{: .fs-9 }

Livello di evidenza: **L2** | Indicazioni previste: **9** 
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

## Pravastatina: dall'iperlipidemia alla HIV (dislipidemia associata all'infezione da HIV)
{: .text-alpha }

## Sintesi in una frase

La pravastatina è una statina (inibitore dell'HMG-CoA reduttasi) utilizzata per trattare le dislipidemie e ridurre il rischio cardiovascolare e cerebrovascolare.
Il modello TxGNN la indica come candidata per **infezione da HIV** (indicazione prioritaria con il supporto più solido tra le previsioni), non come antivirale ma per il controllo della dislipidemia e del rischio cardiovascolare associati all'HIV e alla terapia antiretrovirale.
A sostegno di questa direzione ci sono **12 studi clinici** e **19 pubblicazioni** nei dati compilati per questo report.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Iperlipidemie (ipertrigliceridemia, iperlipidemia familiare combinata, iperlipoproteinemia) e malattie aterosclerotiche/cerebrovascolari (ictus, infarto cerebrale, aterosclerosi), secondo gli archi di indicazione del grafo di conoscenza; il testo autorizzativo AIFA non è disponibile |
| Nuova indicazione prevista | Infezione da HIV (dislipidemia e rischio cardiovascolare associati) |
| Punteggio di previsione TxGNN | 99,74% |
| Livello di evidenza | L2 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Proceed with Guardrails (procedere con cautele) |

**Nota sulla selezione.** La prima previsione per punteggio è l'ipercolesterolemia familiare omozigote (99,95%), ma i dati la collocano a livello L4 con raccomandazione "domanda di ricerca": l'unico studio di fase 3 riguarda l'alirocumab e non la pravastatina. L'indicazione con evidenza più solida e coerente con una raccomandazione operativa è l'infezione da HIV (L2), ed è quella trattata in questo report. Le altre previsioni sono riassunte nelle conclusioni.

---

## Perché questa previsione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione nei dati compilati per questo report. In base alle informazioni note, la pravastatina inibisce l'HMG-CoA reduttasi (confermato dal dato di farmacologia sul bersaglio HMGCR), riduce la sintesi epatica di colesterolo e aumenta l'espressione dei recettori epatici per le LDL. La sua efficacia nelle dislipidemie è consolidata.

Nell'HIV il razionale **non è antivirale**. I pazienti con HIV, in particolare quelli trattati con inibitori della proteasi, sviluppano spesso dislipidemia e hanno un rischio cardiovascolare aumentato. La pravastatina agisce su questo versante, con possibili effetti pleiotropici su funzione endoteliale e infiammazione.

Un vantaggio pratico: la pravastatina è metabolizzata in modo minimo dal CYP3A4, quindi il rischio di interazioni con gli inibitori della proteasi è inferiore rispetto ad altre statine. Il trasportatore epatico OATP1B1 (SLCO1B1), identificato tra i dati di farmacologia, resta però rilevante: i dati compilati citano uno studio sulla variabilità farmacocinetica legata ai polimorfismi SLCO1B1 con darunavir/ritonavir.

---

## Evidenze da studi clinici

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00006412](https://clinicaltrials.gov/study/NCT00006412) | Fase 3 | Completato | 630 | Fenofibrato vs pravastatina in soggetti HIV con anomalie lipidiche |
| [NCT00227500](https://clinicaltrials.gov/study/NCT00227500) | Fase 4 | Completato | 40 | Pravastatina vs placebo in iperlipidemia in pazienti HIV trattati con inibitori della proteasi |
| [NCT00221754](https://clinicaltrials.gov/study/NCT00221754) | Fase 2 | Completato | 21 | Pravastatina in pazienti HIV ipercolesterolemici in HAART, randomizzato in doppio cieco |
| [NCT00117494](https://clinicaltrials.gov/study/NCT00117494) | Fase 4 | Completato | 86 | Rosuvastatina vs pravastatina in pazienti HIV dislipidemici in terapia antiretrovirale |
| [NCT00843661](https://clinicaltrials.gov/study/NCT00843661) | Fase 4 | Sconosciuto | 60 | Ezetimibe + fenofibrato vs pravastatina in monoterapia in pazienti HIV in terapia con inibitori della proteasi |
| [NCT00630734](https://clinicaltrials.gov/study/NCT00630734) | Fase 4 | Completato | 32 | Predittori genetici (SLCO1B1) della variabilità farmacocinetica nell'interazione darunavir/ritonavir–pravastatina |
| [NCT02841774](https://clinicaltrials.gov/study/NCT02841774) | Fase 2 | Completato | 10 | Pravastatina 40 mg vs rosuvastatina ad alta dose in persone con HIV e coronaropatia (HILLCLIMBER) |
| [NCT00982189](https://clinicaltrials.gov/study/NCT00982189) | Non applicabile | Completato | 37 | Studio pilota con polipillola per ridurre il rischio cardiovascolare in persone con HIV |
| [NCT00665717](https://clinicaltrials.gov/study/NCT00665717) | Fase 1 | Completato | 24 | Effetto del raltegravir sulla farmacocinetica della pravastatina in volontari sani |
| [NCT00000941](https://clinicaltrials.gov/study/NCT00000941) | Fase 1 | Completato | 56 | Interazioni farmacocinetiche tra inibitori della proteasi e ipolipemizzanti |

Sono presenti altri due studi di fase 1 nei dati compilati (NCT00017758 e NCT00039663), non riportati in tabella per il limite di 10 studi.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [25907504](https://pubmed.ncbi.nlm.nih.gov/25907504/) | 2015 | Revisione sistematica | Am J Cardiol | Utilità delle statine nei pazienti HIV, in un contesto di rischio cardiovascolare aumentato |
| [16603852](https://pubmed.ncbi.nlm.nih.gov/16603852/) | 2006 | Studio clinico randomizzato controllato con placebo | AIDS | Effetto della pravastatina su composizione corporea e marcatori cardiovascolari in uomini HIV trattati con inibitori della proteasi |
| [18991624](https://pubmed.ncbi.nlm.nih.gov/18991624/) | 2008 | Studio randomizzato in aperto | Curr HIV Res | Rosuvastatina, pravastatina e atorvastatina per l'ipercolesterolemia in pazienti HIV in terapia con inibitori della proteasi |
| [26148680](https://pubmed.ncbi.nlm.nih.gov/26148680/) | 2015 | Studio crossover randomizzato | BMC Res Notes | Pravastatina, fitosteroli e terapia combinata sul profilo lipidico in pazienti HIV |
| [28252528](https://pubmed.ncbi.nlm.nih.gov/28252528/) | 2017 | Studio clinico | AIDS | Effetti di pitavastatina e pravastatina su marcatori di attivazione immunitaria e infiammazione arteriosa in HIV |
| [22770622](https://pubmed.ncbi.nlm.nih.gov/22770622/) | 2012 | Revisione | Expert Opin Pharmacother | Sicurezza ed efficacia delle statine nella dislipidemia da HIV |
| [28364370](https://pubmed.ncbi.nlm.nih.gov/28364370/) | 2017 | Revisione/linee guida | Am J Cardiovasc Drugs | Raccomandazioni per gestire le interazioni tra statine e farmaci anti-HIV |
| [23703578](https://pubmed.ncbi.nlm.nih.gov/23703578/) | 2013 | Revisione | Clin Pharmacokinet | Interazioni tra statine e inibitori della proteasi antivirali |
| [32240298](https://pubmed.ncbi.nlm.nih.gov/32240298/) | 2020 | Studio osservazionale | J Antimicrob Chemother | Gestione nella pratica reale delle interazioni tra antiretrovirali e statine |
| [27192322](https://pubmed.ncbi.nlm.nih.gov/27192322/) | 2016 | Revisione | Expert Opin Pharmacother | Terapie farmacologiche per i disturbi metabolici correlati all'HIV |

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; non ne è attiva nessuna. Il testo dell'indicazione approvata e la forma farmaceutica non sono disponibili nei dati compilati. Di seguito le prime 5 autorizzazioni:

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 037517226 | Pravastatina 14 cpr 40 mg | Teva Italia Srl | Cancellata |
| 041337167 | Pravastatina 10 cpr 20 mg | Aurobindo Pharma Italia Srl | Cancellata |
| 039239280 | Pravastatina 14 cpr 40 mg | Sandoz GmbH | Cancellata |
| 027309032 | Pravaselect 14 cpr 40 mg | A. Menarini Ind. Farm. Riun. Srl | Cancellata |
| 027776032 | Prasterol 14 cpr 40 mg | Ist. Lusofarmaco d'Italia SpA | Cancellata |

---

## Considerazioni sulla sicurezza

Le informazioni derivano dal grafo di conoscenza e dai dati di farmacologia, non dal foglietto illustrativo.

- **Condizioni associate a controindicazione nel grafo di conoscenza** (non è testo di scheda tecnica): malattie epatiche e renali, miopatia e malattie muscolari, rabdomiolisi, trombocitopenia, gotta, nefrolitiasi, ulcera peptica, malattie della colecisti, anemia, emofilia, ipotensione, iperparatiroidismo, ipercalcemia, abuso di sostanze/dipendenza, tra le altre.
- **Interazioni**: i dati di farmacologia indicano come bersaglio l'HMG-CoA reduttasi (HMGCR) e come trasportatore l'OATP1B1 (SLCO1B1). L'interazione con OATP1B1 è rilevante in HIV: gli inibitori della proteasi possono aumentare l'esposizione alla pravastatina (es. darunavir/ritonavir). Gli studi di farmacocinetica citati (efavirenz, nelfinavir, raltegravir, darunavir/ritonavir) sono utili per definire le cautele.

Per avvertenze e controindicazioni ufficiali, consultare il foglietto illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Proceed with Guardrails**

**Motivazione:**
- Per l'HIV esistono studi randomizzati sulla pravastatina (incluso uno di fase 3 con 630 partecipanti, pravastatina vs fenofibrato, e studi di fase 2/4), insieme a una revisione sistematica e a numerosi studi di farmacocinetica. Il livello di evidenza è L2. Il razionale riguarda la dislipidemia e il rischio cardiovascolare, non un effetto antivirale.
- Il prodotto non ha autorizzazioni attive in Italia, e i dati di sicurezza dal foglietto illustrativo AIFA mancano.

**Per procedere è necessario:**
- Reperire e analizzare il foglietto illustrativo AIFA (avvertenze e controindicazioni): lacuna bloccante per lo screening di sicurezza.
- Completare i dati sul meccanismo d'azione da DrugBank.
- Verificare con le fonti originali gli esiti degli studi (NCT00006412 in particolare), non riportati in dettaglio nei dati compilati, e confermare con RCT più ampi su esiti clinici cardiovascolari; lo studio di fase 2 HILLCLIMBER è molto piccolo (n=10).
- Definire un piano di gestione delle interazioni con gli antiretrovirali (es. darunavir/ritonavir) e di monitoraggio della sicurezza muscolare, epatica e renale.
- Chiarire la situazione regolatoria, dato che tutte le autorizzazioni sono cancellate.

**Altre previsioni TxGNN (sintesi):**
- *Ipercolesterolemia familiare* (99,34%, L3): decisione "Proceed with Guardrails", con dati pediatrici specifici sulla pravastatina (PMID 12891228, 31618540); è un uso vicino all'indicazione originale più che un vero riposizionamento. Cautele: dosaggio pediatrico e monitoraggio della crescita.
- *Ipercolesterolemia familiare omozigote* (99,95%, L4): domanda di ricerca; efficacia limitata delle statine per la funzione residua del recettore LDL, nessuno studio diretto sulla pravastatina.
- *Ipoalfalipoproteinemia* (L4), *deficit di colesterolo 7α-idrossilasi*, *deficit di CETP*, *disturbo del neurosviluppo con atassia*, *infezione da virus dell'immunodeficienza delle scimmie* e *AIDS felina* (L5): Hold, senza studi di supporto o con rilevanza clinica umana limitata.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

