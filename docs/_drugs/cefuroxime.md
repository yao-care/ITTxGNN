---
layout: default
title: Cefuroxime
parent: Solo previsione del modello (L5)
nav_order: 99
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cefuroxime: nuova indicazione prevista, Sindrome da iperviscosità policlonale (livello di evidenza L5). Indicazione originale: Infezioni batteriche (otite media infettiva…"
monitor_inn: "Cefuroxime"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "Peptostreptococcus infectious disease", "blood group incompatibility", "urinary tract infection (disease)", "premalignant hematological system disease", "monoclonal gammopathy", "suppurative otitis media", "hematological disease associated with an acquired peripheral neuropathy"]
---

# Cefuroxime
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

# Cefuroxima: dalle infezioni batteriche all'infezione delle vie urinarie

## Sintesi in una frase

La cefuroxima è una cefalosporina di seconda generazione, utilizzata originariamente per infezioni batteriche come otite media, polmonite batterica, meningite batterica, gonorrea e malattia di Lyme.
Il modello TxGNN prevede che possa essere efficace per la **sindrome da iperviscosità policlonale** (indicazione con il punteggio più alto), ma per questa previsione **non esistono studi clinici né pubblicazioni** a supporto.
L'indicazione predetta con le evidenze più solide è l'**infezione delle vie urinarie** (**5 studi clinici** e **20 pubblicazioni**), che però è una naturale estensione dell'uso antibatterico già noto e non un vero riposizionamento.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezioni batteriche (otite media infettiva, infezioni da streptococco e stafilococco, polmonite batterica, meningite batterica, gonorrea, malattia di Lyme, ecc.). Il testo delle indicazioni approvate AIFA non è disponibile; l'elenco deriva dal grafo di conoscenza |
| Nuova indicazione predetta (rank 1) | Sindrome da iperviscosità policlonale |
| Punteggio di predizione TxGNN | 99,76% |
| Livello di evidenza | L5 (solo predizione del modello) |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 14 (tutte cancellate) |
| Decisione raccomandata | Hold |

**Nota sulle altre predizioni.** Oltre al rank 1, due candidati hanno evidenze rilevanti:

| Indicazione predetta | Punteggio TxGNN | Livello di evidenza | Valutazione |
|------|------|------|------|
| Infezione delle vie urinarie | 99,62% | L3 | Domanda di ricerca (estensione dell'uso antibatterico) |
| Otite media suppurativa | 99,56% | L4 | Domanda di ricerca (evidenze indirette) |

---

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle conoscenze generali, la cefuroxima è una cefalosporina di seconda generazione che inibisce la sintesi della parete cellulare batterica; la sua efficacia nelle infezioni batteriche è consolidata.

**Per la predizione di rank 1 (sindrome da iperviscosità policlonale)** non si riscontra un collegamento meccanicistico plausibile. Si tratta di un disturbo reologico guidato da proteine/immunoglobuline, su cui un antibatterico non ha effetto noto. L'alto punteggio TxGNN deriva da associazioni nel grafo, senza supporto clinico o bibliografico. Analogamente, per iperamilasemia, analbuminemia congenita, incompatibilità di gruppo sanguigno, malattie ematologiche premaligne e neuropatie ematologiche non esiste alcun razionale meccanicistico.

**Per le predizioni con base biologica** (infezione delle vie urinarie, otite media suppurativa, infezione da *Peptostreptococcus*) il razionale è solido: la cefuroxima è attiva sui comuni uropatogeni (*E. coli*, *Klebsiella*, *Proteus*) e sui patogeni dell'otite media (*S. pneumoniae*, *H. influenzae*, *M. catarrhalis*). L'otite media infettiva è già tra le indicazioni originali, quindi si tratta di un'estensione dell'uso esistente. Per *Peptostreptococcus* l'unica fonte è uno studio in vitro del 1981, incentrato sulla ceftazidima, con copertura anaerobica della cefuroxima variabile.

---

## Evidenze da studi clinici

Per la predizione di rank 1 non risultano studi clinici registrati. Di seguito gli studi relativi all'**infezione delle vie urinarie** (predizione con evidenze più solide):

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT04616352](https://clinicaltrials.gov/study/NCT04616352) | N/D | Completato | 973 | Effetto della terapia inappropriata con cefuroxima in adulti ospedalizzati con pielonefrite (rilevanza alta, ma non RCT) |
| [NCT01507974](https://clinicaltrials.gov/study/NCT01507974) | N/D | Completato | 220 | Antibiotico-profilassi nel puerperio in donne con infezioni urinarie ricorrenti (specificità per cefuroxima non chiara) |
| [NCT05577273](https://clinicaltrials.gov/study/NCT05577273) | N/D | Sconosciuto | 1000 | Profilassi antibiotica alla rimozione del catetere urinario (agente non specificato) |
| [NCT02789579](https://clinicaltrials.gov/study/NCT02789579) | Fase 1 precoce | Sconosciuto | 150 | Prevenzione delle infezioni urinarie prima della litotrissia mininvasiva (disegno debole) |
| [NCT02009098](https://clinicaltrials.gov/study/NCT02009098) | Fase 4 | Ritirato | 0 | Profilassi delle infezioni post-partum dopo taglio cesareo (nessun dato) |

Non è presente alcuno studio di fase 3 randomizzato che dimostri direttamente l'efficacia della cefuroxima.

---

## Evidenze dalla letteratura

Pubblicazioni più rilevanti per l'**infezione delle vie urinarie** (priorità a revisioni sistematiche e studi randomizzati):

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [2689345](https://pubmed.ncbi.nlm.nih.gov/2689345/) | 1989 | Confronto randomizzato | Infection | Aztreonam vs cefuroxima nelle infezioni urinarie alte da Gram-negativi |
| [38215770](https://pubmed.ncbi.nlm.nih.gov/38215770/) | 2024 | RCT | Lancet Infect Dis | De-escalation da β-lattamici antipseudomonas in batteriemie da Enterobacterales (evidenza indiretta) |
| [41693075](https://pubmed.ncbi.nlm.nih.gov/41693075/) | 2026 | Revisione sistematica | Pharmacotherapy | β-lattamici orali nelle infezioni urinarie complicate, confronto con TMP/SMX e fluorochinoloni |
| [8799689](https://pubmed.ncbi.nlm.nih.gov/8799689/) | 1996 | Revisione | Drugs | Attività antibatterica, farmacocinetica ed efficacia terapeutica della cefuroxima axetil |
| [18611587](https://pubmed.ncbi.nlm.nih.gov/18611587/) | 1994 | Revisione | Int J Antimicrob Agents | Cefuroxima axetil: spettro e uso nelle infezioni, in particolare respiratorie |
| [6349019](https://pubmed.ncbi.nlm.nih.gov/6349019/) | 1983 | Revisione | Ther Drug Monit | Attività antimicrobica, farmacologia ed efficacia clinica della cefuroxima |
| [6344037](https://pubmed.ncbi.nlm.nih.gov/6344037/) | 1983 | Revisione | Pharmacotherapy | Meccanismo d'azione, attività, farmacocinetica e indicazioni terapeutiche della cefuroxima |
| [39005695](https://pubmed.ncbi.nlm.nih.gov/39005695/) | 2024 | Coorte/epidemiologia | Infect Dis Clin Microbiol | Microrganismi nelle infezioni urinarie comunitarie e fattori di rischio per ESBL |

Per l'**otite media suppurativa** le 20 pubblicazioni sono per lo più revisioni e indagini microbiologiche di sensibilità; l'unico studio specifico sulla cefuroxima è la diffusione nell'essudato dell'orecchio medio nell'otite purulenta cronica ([PMID 7142073](https://pubmed.ncbi.nlm.nih.gov/7142073/), 1982). Non vi sono studi controllati.

---

## Informazioni sul mercato italiano

Tutte le 14 autorizzazioni sono cancellate. Il testo delle indicazioni approvate e la forma farmaceutica non sono disponibili nei dati compilati; sono riportate le principali 5.

| Numero di autorizzazione | Nome prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 037732308 | Cefuroxima compresse rivestite 500 mg (6 cpr) | Sandoz SpA | Cancellata |
| 026915025 | Zinnat 250 mg (12 cpr rivestite) | Sandoz SpA | Cancellata |
| 027002029 | Oraxim 250 mg (12 cpr rivestite) | Malesci SpA | Cancellata |
| 026915037 | Zinnat 500 mg (6 cpr rivestite) | Sandoz SpA | Cancellata |
| 023576022 | Curoxim 500 mg IM (flacone + solvente) | Sandoz SpA | Cancellata |

---

## Considerazioni sulla sicurezza

I dati su avvertenze e controindicazioni dal foglio illustrativo non sono disponibili. Dal grafo di conoscenza risultano controindicazioni associate a: malattia renale, malattia epatica, malattia della colecisti, disturbi della coagulazione, colite da *Clostridium difficile*, enterocolite necrotizzante perinatale, deficit congenito di protrombina e piouretere (fonte: archi del grafo, non testo di etichetta).

**Interazioni farmacologiche** (100 segnalate, tutte di livello moderato nei campioni disponibili):
- Antiacidi/inibitori della secrezione acida: famotidina, ranitidina, cimetidina, nizatidina, omeprazolo, esomeprazolo, lansoprazolo, dexlansoprazolo, pantoprazolo, rabeprazolo, idrossido di alluminio, carbonato di calcio, magaldrato, sali di magnesio
- Aminoglicosidi: kanamicina, neomicina
- Altri: balsalazide

Per ulteriori informazioni sulla sicurezza consultare il foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione con il punteggio più alto (sindrome da iperviscosità policlonale) non ha alcun razionale meccanicistico né evidenze cliniche o bibliografiche (L5). Inoltre tutte le autorizzazioni italiane sono cancellate. Le uniche indicazioni con evidenze (infezione delle vie urinarie, L3; otite media suppurativa, L4) sono estensioni dell'uso antibatterico esistente, e non veri riposizionamenti, e possono essere trattate come domande di ricerca.

**Per procedere sono necessari:**
- Foglio illustrativo AIFA (avvertenze e controindicazioni) per completare la valutazione di sicurezza
- Dati sul meccanismo d'azione da DrugBank
- Verifica della disponibilità del prodotto in Italia, dato che tutte le autorizzazioni sono cancellate
- Per l'infezione delle vie urinarie: RCT o dati di resistenza locale specifici per la cefuroxima
- Per l'otite media: studi controllati specifici sulla cefuroxima
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

