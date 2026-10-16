---
layout: default
title: Bupropion
parent: Solo previsione del modello (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bupropion: nuova indicazione prevista, Disturbo da deficit di attenzione e iperattività (ADHD) (livello di evidenza L5). Indicazione originale: Depressione maggiore e dipendenza da nicotina (tra le a…"
monitor_inn: "bupropion"
predicted_indications: ["attention deficit-hyperactivity disorder", "attention deficit hyperactivity disorder, inattentive type", "faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "proximal 16p11.2 microdeletion syndrome", "hypervitaminosis", "benign paroxysmal torticollis of infancy", "trigeminal nerve neoplasm", "obsolete hypertelorism (disease)"]
---

# Bupropion
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

# Bupropione: dalla depressione al disturbo da deficit di attenzione e iperattività (ADHD)

## Sintesi in una frase

Il bupropione è un antidepressivo utilizzato originariamente per il disturbo depressivo maggiore e per la dipendenza da nicotina.
Il modello TxGNN prevede che possa essere efficace per il **disturbo da deficit di attenzione e iperattività (ADHD)**,
con **6 studi clinici** e **19 pubblicazioni** raccolti nei dati compilati per questo report, tra cui uno studio di fase 3 randomizzato in doppio cieco contro placebo e una revisione Cochrane dedicata.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Depressione maggiore e dipendenza da nicotina (tra le altre: disturbi d'ansia, disturbo distimico; indicazioni derivate dal grafo di conoscenza TxGNN, poiché il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Disturbo da deficit di attenzione e iperattività (ADHD) |
| Punteggio di predizione TxGNN | 99,99% |
| Livello di evidenza | L1 (ma vedi nota sotto) |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 10 (tutte cancellate) |
| Decisione raccomandata | Proceed with Guardrails (procedere con cautele) |

*Nota sul livello di evidenza:* il livello L1 richiederebbe almeno due studi di fase 3 randomizzati completati. Tra i dati compilati risulta un solo studio di fase 3 completato (NCT00048360) e uno di fase 2/3 (NCT00061087). Il livello L1 è quello assegnato nei dati, ma una lettura rigorosa dei criteri porterebbe a L2.

---

## Perché questa predizione è plausibile?

Il bupropione inibisce la ricaptazione di noradrenalina e dopamina (NDRI). Non ha attività serotoninergica significativa. Il dato formale sul meccanismo d'azione non è presente nei dati compilati, ma questa descrizione emerge dalla letteratura raccolta (ad esempio PMID 37405312 e 17136226).

I sistemi catecolaminergici sono il bersaglio principale dei farmaci per l'ADHD: stimolanti come il metilfenidato e le anfetamine, e non stimolanti come l'atomoxetina, agiscono su dopamina e noradrenalina. Per questo il bupropione ha una logica farmacologica per migliorare attenzione e impulsività, e viene considerato un'alternativa per gli adulti che non rispondono agli stimolanti o non li tollerano (PMID 38915262).

Anche il sottotipo "prevalentemente inattentivo" (rank 2) condivide lo stesso meccanismo, ma per esso non esistono studi specifici. Le altre predizioni (sindromi rare, tumori, ipervitaminosi) non hanno alcun razionale farmacologico e restano solo previsioni del modello, quindi non vengono approfondite.

---

## Evidenze da studi clinici

| Numero studio | Fase | Stato | Arruolamento | Risultati chiave |
|---------|------|------|------|---------|
| [NCT00048360](https://clinicaltrials.gov/study/NCT00048360) | Fase 3 | Completato | 162 | Studio di 8 settimane, randomizzato, in doppio cieco, controllato con placebo, bupropione a rilascio prolungato 300-450 mg/die in adulti con ADHD |
| [NCT00061087](https://clinicaltrials.gov/study/NCT00061087) | Fase 2/3 | Completato | 115 | Trattamento dell'ADHD dell'adulto in pazienti in terapia con metadone |
| [NCT00936299](https://clinicaltrials.gov/study/NCT00936299) | Fase 4 | Completato | 105 | Bupropione per l'ADHD in adolescenti con disturbo da uso di sostanze |
| [NCT01270555](https://clinicaltrials.gov/study/NCT01270555) | N/D | Completato | 32 | Studio in aperto sul bupropione SR in adulti con ADHD e disturbi da uso di sostanze recenti o in corso |
| [NCT00000268](https://clinicaltrials.gov/study/NCT00000268) | N/D | Completato | 32 | Abuso di cocaina e disturbo da deficit di attenzione; evidenza solo indiretta |
| [NCT04553263](https://clinicaltrials.gov/study/NCT04553263) | Fase 1 precoce | Ritirato | 0 | Prevenzione delle ricadute nel disturbo da uso di stimolanti; nessun paziente arruolato, non incentrato sull'ADHD |

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati chiave |
|------|-----|------|------|---------|
| [28965364](https://pubmed.ncbi.nlm.nih.gov/28965364/) | 2017 | Revisione sistematica (Cochrane) | Cochrane Database Syst Rev | Bupropione per l'ADHD negli adulti, come alternativa quando gli stimolanti non sono efficaci o tollerati |
| [30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/) | 2018 | Revisione sistematica / network meta-analisi | Lancet Psychiatry | Efficacia e tollerabilità comparative dei farmaci per l'ADHD in bambini, adolescenti e adulti |
| [33085721](https://pubmed.ncbi.nlm.nih.gov/33085721/) | 2020 | Revisione sistematica / network meta-analisi | PLoS One | Confronto dei trattamenti farmacologici per l'ADHD negli adulti |
| [40203844](https://pubmed.ncbi.nlm.nih.gov/40203844/) | 2025 | Network meta-analisi (sicurezza) | Lancet Psychiatry | Sicurezza cardiovascolare dei farmaci per l'ADHD (parametri emodinamici ed ECG) |
| [38915262](https://pubmed.ncbi.nlm.nih.gov/38915262/) | 2024 | Revisione | Expert Rev Neurother | Farmaci non stimolanti per l'ADHD negli adulti |
| [37405312](https://pubmed.ncbi.nlm.nih.gov/37405312/) | 2023 | Revisione | Health Psychol Res | Farmacocinetica, farmacodinamica e meccanismi del bupropione in depressione, ADHD e cessazione del fumo |
| [39172673](https://pubmed.ncbi.nlm.nih.gov/39172673/) | 2024 | Revisione | Am Fam Physician | Panoramica sull'ADHD negli adulti |
| [26601963](https://pubmed.ncbi.nlm.nih.gov/26601963/) | 2016 | Revisione | Curr Pharm Des | Effetti ed effetti collaterali dei farmaci per l'ADHD, compreso il bupropione |
| [17136226](https://pubmed.ncbi.nlm.nih.gov/17136226/) | 2006 | Revisione | Drugs Today (Barc) | Profilo del bupropione: inibizione della ricaptazione di dopamina e noradrenalina |
| [24259638](https://pubmed.ncbi.nlm.nih.gov/24259638/) | 2014 | Revisione | Ann Pharmacother | Fisiopatologia, eziologia e trattamento dell'ADHD |

---

## Informazioni sul mercato italiano

Tutte le 10 autorizzazioni risultano cancellate. Il testo dell'indicazione approvata e la forma farmaceutica non sono disponibili nei dati compilati. Sono elencate le prime 5 autorizzazioni.

| Numero di autorizzazione | Nome prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 037685029 | Wellbutrin 30 cpr 150 mg a rilascio modificato | GlaxoSmithKline SpA | Cancellata |
| 043095013 | Bupropione 30 cpr 150 mg a rilascio modificato | Sandoz SpA | Cancellata |
| 037697024 | Elontril 30 cpr 150 mg a rilascio modificato | GlaxoSmithKline SpA | Cancellata |
| 049922026 | Bupropione 30 cpr 300 mg a rilascio modificato | Zentiva Italia Srl | Cancellata |
| 037685056 | Wellbutrin 30 cpr 300 mg a rilascio modificato | GlaxoSmithKline SpA | Cancellata |

---

## Considerazioni di sicurezza

Il bupropione non è un farmaco antineoplastico, pertanto la sezione sulla citotossicità non è applicabile.

I dati su avvertenze e controindicazioni dal foglio illustrativo AIFA non sono disponibili. Le seguenti informazioni derivano dal grafo di conoscenza TxGNN e dalle banche dati sulle interazioni, non dal testo autorizzativo:

- **Possibili controindicazioni (dal grafo di conoscenza):** epilessia, ipertensione, malattie epatiche (insufficienza epatica, cirrosi), malattie renali, disturbi bipolari maniacali, disturbi psicotici (schizoaffettivo, schizofreniforme), anoressia e bulimia nervosa, dipendenza da oppioidi/morfina, abuso di sostanze, infarto del miocardio, neoplasie del sistema nervoso centrale, malattie della colecisti, emoglobinopatie.
- **Interazioni farmacologiche:** sono state rilevate 665 interazioni, un carico molto elevato (include l'inibizione del CYP2D6). Tra quelle di grado maggiore figurano fentanil, alfentanil, codeina, diidrocodeina, tramadolo, metilfenidato, lidocaina, idrocortisone, aldesleuchina e amantadina. Tra quelle di grado moderato: alprazolam, nifedipina, idroclorotiazide, cetirizina, clorfenamina, alfuzosina, acebutololo, alpelisib, abametapir (topico) ed etanolo.
- **Aspetti da tenere presenti per l'ADHD:** rischio di convulsioni (abbassamento della soglia), effetti sulla pressione arteriosa e cautela in pazienti con disturbi da uso di sostanze o disturbi alimentari.

Per le informazioni complete di sicurezza fare riferimento al foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Proceed with Guardrails**

**Motivazione:**
Esistono uno studio di fase 3 randomizzato controllato con placebo, uno studio di fase 2/3, una revisione Cochrane specifica sul bupropione nell'ADHD dell'adulto e varie meta-analisi, con un meccanismo catecolaminergico coerente. Tuttavia, in Italia tutte le autorizzazioni sono cancellate, i dati di sicurezza ufficiali mancano e il profilo di interazioni e rischio convulsivo è impegnativo; da qui la raccomandazione di procedere con cautele.

**Per procedere sono necessari:**
- Foglio illustrativo AIFA (avvertenze e controindicazioni), attualmente un blocco per lo screening di sicurezza
- Dati formali sul meccanismo d'azione (ad esempio da DrugBank)
- Verifica dei risultati effettivi dello studio NCT00048360 e valutazione critica della revisione Cochrane
- Chiarimento della situazione regolatoria in Italia, dato che tutte le autorizzazioni sono cancellate
- Piano di monitoraggio per rischio convulsivo, pressione arteriosa e interazioni (in particolare CYP2D6) e per popolazioni con uso di sostanze o disturbi alimentari
- Valutazione di un'eventuale analisi stratificata per il sottotipo inattentivo dell'ADHD, per il quale non esistono studi dedicati
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

