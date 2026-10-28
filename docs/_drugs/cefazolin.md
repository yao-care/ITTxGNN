---
layout: default
title: Cefazolin
parent: Solo previsione del modello (L5)
nav_order: 93
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Cefazolin: nuova indicazione prevista, Otite media infettiva (livello di evidenza L5). Indicazione originale: Infezioni batteriche (polmonite batterica, colangite, endocardite…"
monitor_inn: "Cefazolin"
predicted_indications: ["infectious otitis media", "bronchitis", "middle ear disease", "chronic otitis media", "suppurative otitis media", "otosalpingitis", "non-suppurative otitis media", "allergic otitis media"]
---

# Cefazolin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **8** 
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

## Cefazolina: dalle infezioni batteriche alle infezioni dell'orecchio medio (otite media infettiva)
{: .text-alpha }

## Sintesi in una frase

La cefazolina è una cefalosporina di prima generazione, utilizzata originariamente per infezioni batteriche come polmonite, endocardite, colangite e infezioni articolari.
Il modello TxGNN prevede che possa essere efficace per l'**otite media infettiva**, ma finora **non risultano studi clinici registrati** e la letteratura disponibile consiste in **2 pubblicazioni** poco pertinenti (una revisione e un caso clinico).
Il punteggio elevato è quindi una predizione del modello, non una conferma clinica.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezioni batteriche (polmonite batterica, colangite, endocardite, artropatia batterica); il testo delle indicazioni approvate AIFA non è disponibile |
| Nuova indicazione prevista | Otite media infettiva |
| Punteggio di predizione TxGNN | 0,9944 |
| Livello di evidenza | L5 (solo predizione del modello, nessuno studio clinico dedicato; la letteratura raccolta è costituita da una revisione e da un caso clinico) |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 5 su 5) |
| Numero di autorizzazioni | 5 (valide: 5) |
| Decisione raccomandata | Hold (sospendere) |

---

## Perché questa predizione è plausibile?

I dati dettagliati sul meccanismo d'azione non sono al momento disponibili nei dati compilati per questo report. In base alle conoscenze generali, la cefazolina è un beta-lattamico che inibisce la sintesi della parete cellulare batterica. È attiva soprattutto contro i batteri Gram-positivi come *Staphylococcus aureus* sensibile alla meticillina (MSSA) e gli streptococchi, che possono causare otite media. Esiste quindi un legame antibatterico plausibile con l'indicazione prevista.

Vi sono però limiti importanti. La cefazolina ha un'attività limitata contro patogeni tipici dell'otite media come *H. influenzae* e *M. catarrhalis*. Inoltre il punteggio TxGNN molto alto (0,9944) è solo una predizione computazionale, non una prova di efficacia.

Tra le altre indicazioni previste dal modello, alcune hanno un razionale più debole: l'otite media non suppurativa e quella allergica sono spesso non batteriche, quindi un antibiotico ha scarso fondamento meccanicistico. Le forme suppurative e croniche hanno invece un'evidenza clinica, seppur datata (vedi sotto).

---

## Evidenze da studi clinici

Al momento non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Caso clinico | Annals of Otology, Rhinology & Laryngology | Terapia empirica con ceftazidima-cefazolina in un bambino con sindrome di Gradenigo, complicanza rara di otite media acuta |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Revisione | Clinical Pharmacy | Gestione della sindrome di Stevens-Johnson; l'otite media compare solo come contesto clinico del caso, con scarsa pertinenza |

Nota: per le altre indicazioni predette, l'unico dato clinico umano diretto è un confronto del 1982 tra cefmetazolo e cefazolina nell'otite media suppurativa (PMID 6752467, 172 pazienti valutati), datato e non paragonabile a uno studio randomizzato moderno.

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 023853031 | CEFAZOLINA (1 fiala IM 1 g + 1 fiala solvente 4 ml) – TEVA ITALIA | Non indicata | Non disponibile (autorizzazione valida) |
| 033575010 | CEFAZOLINA (1 fiala IM 1 g + 1 fiala solvente 4 ml) – S.F. GROUP | Non indicata | Non disponibile (autorizzazione valida) |
| 033123011 | NEFAZOL (1 fiala IM 1 g + 1 fiala solvente 4 ml) – NEW RESEARCH | Non indicata | Non disponibile (autorizzazione valida) |
| 023916051 | CEFAZIL (1 fiala IM 1 g + 1 fiala solvente 4 ml) – ITALFARMACO | Non indicata | Non disponibile (autorizzazione valida) |
| 024127019 | CEFAZOLINA (1 fiala IM 1 g + 1 fiala solvente 4 ml) – PHARMACARE | Non indicata | Non disponibile (autorizzazione valida) |

---

## Considerazioni di sicurezza

- **Controindicazioni (da relazioni nel grafo di conoscenza, non dal foglietto illustrativo)**: disturbi della coagulazione del sangue, colite da *Clostridium difficile*, enterocolite necrotizzante perinatale, deficit congenito di protrombina.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni. Quelle di livello moderato riguardano gli aminoglicosidi **kanamicina, neomicina e streptomicina** e l'**acido picosolfurico**. Per altre (ad esempio calcitriolo, epinefrina, amfotericina B, mannitolo, acido acetilsalicilico, amoxicillina, metformina, omeprazolo) il livello di gravità non è classificato.

Per le avvertenze complete si rimanda al foglietto illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa solo sul modello, senza studi clinici registrati e con letteratura scarsa e poco pertinente. Le autorizzazioni italiane sono tutte cancellate, e la cefazolina ha un'attività limitata contro i principali patogeni dell'otite media.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione e sullo spettro di attività della cefazolina contro i patogeni tipici dell'otite media
- Avvertenze e controindicazioni dal foglietto illustrativo AIFA, non disponibili al momento
- Una valutazione più approfondita delle forme suppurative e croniche, per cui esiste almeno un confronto clinico storico (1982)
- Studi clinici moderni o dati di sensibilità batterica aggiornati
- Valutazione della compatibilità della via di somministrazione (al momento non determinata)
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

