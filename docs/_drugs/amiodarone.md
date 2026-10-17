---
layout: default
title: Amiodarone
parent: Prove elevate (L1-L2)
nav_order: 40
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Amiodarone: nuova indicazione prevista, Tachicardia ventricolare (livello di evidenza L1). Indicazione originale: Fibrillazione ventricolare (testo approvato AIFA non disponibile)"
monitor_inn: "AMIODARONE"
predicted_indications: ["catecholaminergic polymorphic ventricular tachycardia", "incessant infant ventricular tachycardia", "ventricular tachycardia", "obsolete bundle branch block", "rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "heparin cofactor 2 deficiency", "trichotillomania", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "gout"]
---

# Amiodarone
{: .fs-9 }

Livello di evidenza: **L1** | Indicazioni previste: **10** 
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

# Amiodarone: dalla fibrillazione ventricolare alla tachicardia ventricolare

## Sintesi in una frase

L'amiodarone è un antiaritmico originariamente utilizzato per la fibrillazione ventricolare. Il modello TxGNN lo prevede efficace per la **tachicardia ventricolare**, che nei dati compilati per questo report è l'indicazione prevista con il supporto clinico più solido: **18 sperimentazioni cliniche** e **20 pubblicazioni** sostengono questa direzione, incluse due sperimentazioni di Fase 3 completate (AVID e ALPS).

Nota: la tachicardia ventricolare è di fatto vicina all'indicazione storica del farmaco. Si tratta quindi più di una conferma dell'uso già consolidato che di un vero riposizionamento. Il report si concentra su questa indicazione; le altre predizioni sono riassunte in coda.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Fibrillazione ventricolare (testo approvato AIFA non disponibile) |
| Nuova indicazione prevista | Tachicardia ventricolare |
| Punteggio di predizione TxGNN | 99,64% |
| Livello di evidenza | L1 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 8 (tutte cancellate) |
| Decisione raccomandata | Proceed with Guardrails |

*Nota sul punteggio: la prima predizione per punteggio nell'elenco è la tachicardia ventricolare polimorfa catecolaminergica (99,78%), ma con evidenza solo di livello L4 e raccomandazione Hold. La tachicardia ventricolare (rank 3) è stata scelta perché è l'indicazione con l'evidenza più forte.*

---

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione nel dossier originale. In base alle informazioni disponibili, l'amiodarone è un antiaritmico multicanale: blocca i canali del potassio, del sodio e del calcio e ha un effetto antagonista beta-adrenergico. Il suo effetto principale è il prolungamento della ripolarizzazione (classe III di Vaughan Williams).

La fibrillazione ventricolare e la tachicardia ventricolare sono aritmie ventricolari strettamente correlate: la tachicardia ventricolare può degenerare in fibrillazione ventricolare ed entrambe sono sostenute da meccanismi di rientro e attività triggerata. Il blocco multicanale sopprime questi meccanismi, per cui l'applicabilità alla tachicardia ventricolare è meccanicisticamente plausibile e supportata da studi clinici diretti.

---

## Evidenze dalle sperimentazioni cliniche

Sono elencate le sperimentazioni più rilevanti (le 18 registrate comprendono anche studi di ablazione con amiodarone come comparatore).

| Numero studio | Fase | Stato | Arruolamento | Risultati chiave |
|---------|------|------|------|---------|
| [NCT00000531](https://clinicaltrials.gov/study/NCT00000531) | Fase 3 | Completato | N/D | AVID: defibrillatori impiantabili vs terapia antiaritmica (soprattutto amiodarone) in aritmie ventricolari potenzialmente letali |
| [NCT01401647](https://clinicaltrials.gov/study/NCT01401647) | Fase 3 | Completato | 3024 | ALPS: amiodarone vs lidocaina vs placebo nell'arresto cardiaco extraospedaliero da FV/TV senza polso |
| [NCT00257959](https://clinicaltrials.gov/study/NCT00257959) | Fase 4 | Completato | 400 | OPTIC: amiodarone + beta-bloccante vs beta-bloccante vs sotalolo nella prevenzione degli shock da ICD |
| [NCT00383799](https://clinicaltrials.gov/study/NCT00383799) | Fase 4 | Terminato | 302 | PROCAMIO: amiodarone vs procainamide EV nella tachicardia a QRS largo ben tollerata |
| [NCT03299517](https://clinicaltrials.gov/study/NCT03299517) | Fase 4 | Sconosciuto | 80 | Amiodarone vs lidocaina nella TV stabile in pronto soccorso |
| [NCT02830360](https://clinicaltrials.gov/study/NCT02830360) | Fase 4 | Completato | 416 | VANISH2: ablazione vs terapia antiaritmica in TV monomorfa post-infarto |
| [NCT03734562](https://clinicaltrials.gov/study/NCT03734562) | N/A | Completato | 180 | Ablazione con radiofrequenza vs farmaci antiaritmici in cardiomiopatia ischemica con TV |
| [NCT01722942](https://clinicaltrials.gov/study/NCT01722942) | N/A | Sconosciuto | 1100 | CHAGASICS: amiodarone vs ICD nella cardiomiopatia di Chagas con TV non sostenuta |
| [NCT01097330](https://clinicaltrials.gov/study/NCT01097330) | Fase 3 | Terminato | 12 | Ablazione transcatetere vs amiodarone nei portatori di ICD con TV (arruolamento molto ridotto) |
| [NCT02303639](https://clinicaltrials.gov/study/NCT02303639) | Fase 4 | Sconosciuto | 120 | Terapia antiaritmica vs ablazione in tachiaritmie ventricolari ischemiche |

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati chiave |
|------|-----|------|------|---------|
| [27354046](https://pubmed.ncbi.nlm.nih.gov/27354046/) | 2017 | RCT | European Heart Journal | PROCAMIO: confronto randomizzato tra procainamide e amiodarone EV nella tachicardia a QRS largo tollerata |
| [41217320](https://pubmed.ncbi.nlm.nih.gov/41217320/) | 2026 | Sottostudio di RCT | J Am Coll Cardiol | Sottostudio VANISH2: ablazione vs sotalolo o amiodarone nella TV |
| [30084131](https://pubmed.ncbi.nlm.nih.gov/30084131/) | 2018 | Coorte | Emerg Med Australas | Sicurezza ed efficacia dell'amiodarone nella TV stabile in ambito preospedaliero |
| [20730062](https://pubmed.ncbi.nlm.nih.gov/20730062/) | 2010 | Revisione | Vasc Health Risk Manag | L'amiodarone come principale terapia antiaritmica per terminare e prevenire FV/TV |
| [36878200](https://pubmed.ncbi.nlm.nih.gov/36878200/) | 2023 | Revisione | Cardiology | Farmacoterapia delle aritmie ventricolari |
| [9137212](https://pubmed.ncbi.nlm.nih.gov/9137212/) | 1997 | Revisione | J Am Coll Cardiol | Amiodarone EV per aritmie ventricolari maligne e resistenti |
| [10666663](https://pubmed.ncbi.nlm.nih.gov/10666663/) | 2000 | Revisione | Curr Opin Cardiol | Studi clinici di prevenzione primaria e secondaria con amiodarone (EMIAT, CAMIAT) |
| [36293490](https://pubmed.ncbi.nlm.nih.gov/36293490/) | 2022 | Revisione | Int J Mol Sci | Terapie promettenti per fibrillazione atriale e tachicardia ventricolare |
| [37380314](https://pubmed.ncbi.nlm.nih.gov/37380314/) | 2023 | Studio clinico | JACC Clin Electrophysiol | Carico di TV e di terapie ICD con ablazione vs terapia antiaritmica intensificata |
| [8258259](https://pubmed.ncbi.nlm.nih.gov/8258259/) | 1993 | Caso clinico | Clin Pharm | Disfunzione tiroidea indotta da amiodarone in un paziente con TV ricorrente |

---

## Informazioni sul mercato italiano

Tutte le 8 autorizzazioni risultano **cancellate**; non ve ne sono di valide. Il testo dell'indicazione approvata e la forma farmaceutica non sono riportati nei dati compilati.

| Numero di autorizzazione | Nome prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 033200015 | Amiodarone 20 cpr 200 mg | Sandoz SpA | Cancellata |
| 044112023 | Amiodarone 20 cpr 200 mg | Aurobindo Pharma Italia Srl | Cancellata |
| 022033031 | Amiodar 20 cpr 200 mg | Alfasigma SpA | Cancellata |
| 040758029 | Amiodarone 20 cpr 200 mg | Mylan SpA | Cancellata |
| 025035015 | Cordarone 20 cpr 200 mg | Sanofi Srl | Cancellata |

---

## Considerazioni sulla sicurezza

- **Controindicazioni (dal grafo di conoscenza TxGNN, non dal foglio illustrativo):** sindrome del QT lungo (anche familiare), torsione di punta, blocco atrioventricolare, malattia del nodo del seno, ipotiroidismo e ipertiroidismo (incl. malattia di Graves, tireotossicosi), malattie epatiche e danno epatico da farmaci, malattia polmonare interstiziale, polmonite eosinofila, alveolite allergica estrinseca, neuropatia periferica, neurite ottica, depositi corneali, carenza di potassio.
- **Interazioni farmacologiche:** sono state identificate 100 interazioni. Tra quelle di livello **maggiore** figurano: cisapride, claritromicina, clotrimazolo, desametasone, idrocortisone, dolasetron, eliglustat, agalsidasi beta e le formulazioni di amfotericina B. Tra quelle di livello moderato: famotidina, cimetidina, aprepitant, bisacodile, budesonide e olio di ricino.
- **Segnali dalla letteratura:** tossicità tiroidea, polmonare (fibrosi, emorragia alveolare), epatica e oculare; rischio proaritmico con prolungamento del QT.

Per le avvertenze complete e le controindicazioni ufficiali occorre consultare il foglio illustrativo.

---

## Citotossicità

Sezione omessa: l'amiodarone non è un farmaco antineoplastico.

---

## Altre indicazioni previste (sintesi)

| Indicazione | Punteggio | Livello di evidenza | Decisione | Commento |
|------|------|------|------|------|
| TV polimorfa catecolaminergica | 99,78% | L4 | Hold | Solo coorti, casi clinici e revisioni; amiodarone usato come rescue, non come terapia studiata (prima linea: beta-bloccanti) |
| TV infantile incessante | 99,65% | L2 | Research Question | RCT in doppio cieco di amiodarone EV in bambini (PMID 16316969), ma popolazione mista sopraventricolare/ventricolare |
| Blocco di branca (termine obsoleto) | 99,58% | L5 | Hold | Probabile artefatto del modello; l'amiodarone può causare disturbi di conduzione |
| Artrite reumatoide | 99,40% | L5 | Hold | La letteratura riguarda solo effetti avversi, non efficacia |
| Sindrome brachidattilia-sindattilia | 99,38% | L5 | Hold | Nessuna evidenza né meccanismo plausibile |
| Deficit di cofattore 2 dell'eparina | 99,36% | L5 | Hold | Nessuna evidenza né meccanismo plausibile |
| Tricotillomania | 99,30% | L5 | Hold | Nessuna evidenza né meccanismo plausibile |
| Sindrome da microftalmia colobomatosa-displasia rizomelica | 99,26% | L5 | Hold | Nessuna evidenza né meccanismo plausibile |
| Gotta | 99,19% | L5 | Hold | La letteratura riguarda interazioni e eventi avversi, non benefici |

---

## Conclusioni e prossimi passi

**Decisione: Proceed with Guardrails**

**Motivazione:**
L'indicazione tachicardia ventricolare è sostenuta da più sperimentazioni di Fase 3 completate (AVID, ALPS) e da diversi studi di Fase 4 comparativi (OPTIC, PROCAMIO), con un'ampia letteratura. Si tratta però di un uso che coincide in sostanza con l'indicazione storica del farmaco, e le 8 autorizzazioni italiane sono tutte cancellate: non si tratta quindi di un vero riposizionamento, e la disponibilità del prodotto va verificata.

**Per procedere è necessario:**
- Verificare la disponibilità commerciale in Italia (formulazioni orali ed endovenose) e lo stato regolatorio attuale presso AIFA
- Acquisire e analizzare il foglio illustrativo AIFA (avvertenze, controindicazioni, indicazioni approvate), attualmente mancante
- Integrare i dati sul meccanismo d'azione da DrugBank
- Definire un piano di monitoraggio: funzione tiroidea, polmonare ed epatica, esame oculare, ECG (QT), con dose e durata minime efficaci
- Gestire il rischio di interazioni (100 segnalate, molte di livello maggiore), in particolare con farmaci che prolungano il QT
- Per la TV infantile incessante: valutare uno studio dedicato al sottogruppo ventricolare con salvaguardie di sicurezza pediatriche
- Per la TV polimorfa catecolaminergica: sono necessari studi specifici prima di qualsiasi considerazione oltre l'uso di salvataggio
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

