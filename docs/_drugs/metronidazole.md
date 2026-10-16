---
layout: default
title: Metronidazole
parent: Solo previsione del modello (L5)
nav_order: 297
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Metronidazole: nuova indicazione prevista, Pneumocistosi (livello di evidenza L5). Indicazione originale: Infezioni da batteri anaerobi, peritonite, giardiasi…"
monitor_inn: "metronidazole"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis", "ulcerative proctosigmoiditis", "nocardiosis", "postmenopausal atrophic vaginitis", "Cryptococcal meningitis", "papillary conjunctivitis", "myiasis", "cap polyposis", "ulceration of vulva"]
---

# Metronidazole
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

# Metronidazolo: dalle infezioni anaerobiche e protozoarie alla pneumocistosi

## Sintesi in una frase

Il metronidazolo è un antibiotico/antiprotozoario utilizzato originariamente per infezioni da batteri anaerobi, giardiasi, vaginosi batterica e altre infezioni. Il modello TxGNN prevede che possa essere efficace per la **pneumocistosi**, ma attualmente **non risultano studi clinici registrati** e la letteratura recuperata (10 pubblicazioni) è costituita da revisioni generali e case report che non dimostrano alcuna efficacia del farmaco su questa malattia.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezioni da batteri anaerobi, peritonite, giardiasi, vaginosi batterica, ascesso intracranico e altre (dal grafo di conoscenza; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Pneumocistosi |
| Punteggio di predizione TxGNN | 99,99% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 5 (tutte cancellate) |
| Decisione raccomandata | Hold (sospendere) |

---

## Perché questa predizione è ragionevole (o no)?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle conoscenze generali, il metronidazolo è attivo contro batteri anaerobi e protozoi, grazie a una via di attivazione mediata da nitroriduttasi.

Per la pneumocistosi il collegamento meccanicistico appare debole: *Pneumocystis* è un fungo e non possiede la via di attivazione da cui dipende il metronidazolo. L'elevato punteggio TxGNN è verosimilmente dovuto alla prossimità, nella rete di conoscenza, con farmaci antiparassitari e antinfettivi. La letteratura recuperata comprende revisioni generali sugli antiparassitari e articoli sulle infezioni opportunistiche in corso di AIDS, senza prove di efficacia del metronidazolo contro *Pneumocystis*.

### Altre indicazioni previste con segnali più coerenti

Tra le altre candidate emerse dall'analisi, alcune hanno un razionale più plausibile, anche se basato su evidenze deboli:

| Indicazione | Punteggio TxGNN | Livello | Note |
|------|------|------|------|
| Poliposi a cappuccio (cap polyposis) | 99,73% | L3 | Segnale più coerente: case report di remissione con regimi antibiotici contenenti metronidazolo; ipotesi di azione antinfiammatoria. Nessuno studio controllato; alcuni casi refrattari |
| Ulcerazione della vulva | 99,72% | L3 | Utilizzo nella malattia di Crohn vulvare e nelle ulcere amebiche; effetto specifico per eziologia, non generalizzabile |
| Proctosigmoidite ulcerosa | 99,87% | L4 | Evidenza indiretta (revisioni su IBD, pouchite); nessuno studio controllato |
| Miasi | 99,75% | L4 | Ruolo solo adiuvante (controllo dell'odore nelle ferite maligne); le larve si trattano con ivermectina |
| Nocardiosi, meningite criptococcica, cheratocongiuntivite epiteliale puntata, congiuntivite papillare, vaginite atrofica postmenopausale | — | L4–L5 | Nessun razionale meccanicistico evidente |

---

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

Per la pneumocistosi (10 pubblicazioni; nessuna dimostra l'efficacia del metronidazolo):

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Revisione | Mayo Clin Proc | Panoramica generale sugli antiparassitari |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Revisione | Am Fam Physician | Il metronidazolo è indicato per amebiasi e tricomoniasi; per la polmonite da Pneumocystis è indicato trimetoprim-sulfametossazolo |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Revisione | Clin Pharmacokinet | Terapia antiprotozoaria e razionale farmacocinetico |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Revisione | Clin Pharm | Trattamento delle complicanze infettive dell'AIDS |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Revisione | Top Antivir Med | Infezioni opportunistiche correlate all'HIV ancora rilevanti |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Revisione | Rev Infect Dis | Critica degli studi sulla profilassi antimicrobica |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case report | Am Rev Respir Dis | Polmonite da P. carinii e CMV in adulto precedentemente trattato con metronidazolo per diarrea; nessun effetto dimostrato |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case report | Kansenshogaku Zasshi | Due pazienti con AIDS; amebiasi trattata con metronidazolo, poi polmonite da Pneumocystis |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case report | J Formos Med Assoc | Perforazione del colon in paziente con AIDS, CMV e colite amebica |
| [42178576](https://pubmed.ncbi.nlm.nih.gov/42178576/) | 2026 | Case report | J Med Case Rep | Ascesso cerebellare da *S. intermedius* come prima manifestazione di sarcoidosi |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 018505038 | FLAGYL*20 cpr 250 mg (TEOFARMA Srl) | — | Stato: cancellata |
| 020689028 | VAGILEN*20 cps 250 mg (DYMALIFE PHARMACEUTICAL Srl) | — | Stato: cancellata |
| 048155016 | METRONIDAZOLO*20 cpr 250 mg (AUROBINDO PHARMA ITALIA Srl) | — | Stato: cancellata |
| 021299033 | DEFLAMON*1 flacone EV 500 mg 100 ml (SPA) | — | Stato: cancellata |
| 041527019 | PYLERA*120 cps 140 mg + 125 mg + 125 mg flacone (LAB. JUVISE' PHARMACEUTICALS) | — | Stato: cancellata |

Tutte e 5 le autorizzazioni risultano cancellate; non vi sono autorizzazioni valide nei dati compilati.

---

## Considerazioni sulla sicurezza

**Controindicazioni/condizioni a rischio (dal grafo di conoscenza, non dal foglietto illustrativo):** insufficienza epatica, epilessia, malattie renali, malattie ematologiche (neutropenia, agranulocitosi, leucopenia), malattie epatiche e della colecisti, insufficienza cardiaca congestizia, diabete e chetoacidosi diabetica, gotta, neuropatia periferica e malattie del sistema nervoso periferico, abuso/dipendenza da sostanze, disturbi della coagulazione, dermatite, malattie cerebrali, meningite non infettiva, malattie del nervo ottico e delle vie visive.

**Interazioni farmacologiche:** sono state identificate 620 interazioni. Tra quelle elencate:
- **Maggiore:** etanolo
- **Moderata:** paclitaxel, adalimumab, trastuzumab emtansine, etinilestradiolo, estradiolo, butalbital, amiodarone, celecoxib, amobarbital, loperamide
- **Minore:** abiraterone, tramadolo, famotidina, salbutamolo, alfuzosina, amisulpride, amitriptilina, anagrelide, propofol

Per avvertenze e controindicazioni ufficiali si rimanda al foglietto illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Hold (sospendere)**

**Motivazione:**
- Per la pneumocistosi non esistono studi clinici né letteratura a supporto; il meccanismo è implausibile (*Pneumocystis* è un fungo) e il punteggio elevato sembra derivare da prossimità di rete. Evidenza di livello L5. Inoltre, in Italia tutte le autorizzazioni del prodotto risultano cancellate.

**Per procedere sarebbe necessario:**
- Dati sul meccanismo d'azione (MOA) del metronidazolo.
- Testo autorizzativo AIFA e avvertenze/controindicazioni dal foglietto illustrativo, attualmente mancanti.
- Riorientare la valutazione verso candidate più plausibili, in particolare la **poliposi a cappuccio** e l'**ulcerazione vulvare** (ad es. da malattia di Crohn), con revisione sistematica della letteratura ed eventuale studio pilota controllato.
- Chiarire lo stato regolatorio e la disponibilità in commercio del metronidazolo in Italia.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

