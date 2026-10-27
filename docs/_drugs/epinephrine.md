---
layout: default
title: Epinephrine
parent: Prove elevate (L1-L2)
nav_order: 175
evidence_level: L1
indication_count: 4
last_modified_at: 2026-10-15
description: "Epinephrine: nuova indicazione prevista, Malattia polmonare ostruttiva (livello di evidenza L1). Indicazione originale: Asma, bronchite, anafilassi, enfisema…"
monitor_inn: "Epinephrine"
predicted_indications: ["obstructive lung disease", "food-dependent exercise-induced anaphylaxis", "Rienhoff syndrome", "respiratory malformation"]
---

# Epinephrine
{: .fs-9 }

Livello di evidenza: **L1** | Indicazioni previste: **4** 
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

## Epinefrina: da asma e anafilassi a malattia polmonare ostruttiva
{: .text-alpha }

## Sintesi in una frase

L'epinefrina (adrenalina) è un agonista adrenergico non selettivo, utilizzato originariamente per asma, bronchite, anafilassi, enfisema e glaucoma ad angolo aperto.
Il modello TxGNN ne prevede l'efficacia per la **malattia polmonare ostruttiva**, con **15 studi clinici** e **20 pubblicazioni** nei dati compilati per questa indicazione.
Si tratta però di un'indicazione che si sovrappone in gran parte agli usi già noti: è più una conferma di un uso esistente che un vero riposizionamento.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Asma, bronchite, anafilassi, enfisema, glaucoma ad angolo aperto (dal grafo di conoscenza; i testi delle autorizzazioni italiane non riportano indicazioni) |
| Nuova indicazione prevista | Malattia polmonare ostruttiva |
| Punteggio di predizione TxGNN | 99,71% |
| Livello di evidenza | L1 |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 4 (tutte revocate) |
| Decisione raccomandata | Proceed with Guardrails (procedere con cautele) |

## Perché questa predizione è ragionevole?

Al momento i dati dettagliati sul meccanismo d'azione non sono disponibili nei dati compilati. In base alle conoscenze generali, l'epinefrina è un agonista adrenergico non selettivo: l'attivazione dei recettori beta-2 rilassa la muscolatura liscia bronchiale e produce broncodilatazione, mentre l'attività alfa-1 riduce l'edema della mucosa delle vie aeree.

La categoria «malattia polmonare ostruttiva» comprende asma, enfisema e bronchiectasie, già tra le indicazioni originali del farmaco. La predizione conferma quindi un uso esistente più che aprire una direzione realmente nuova. Un segnale distinto e più debole riguarda la bronchiolite infantile, dove l'epinefrina inalatoria è stata studiata con risultati incerti.

## Evidenze dagli studi clinici

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT01357642](https://clinicaltrials.gov/study/NCT01357642) | Fase 3 | Completato | 373 | Efficacia e sicurezza a 12 settimane di epinefrina inalatoria HFA-MDI vs placebo e Primatene Mist in asma |
| [NCT01476904](https://clinicaltrials.gov/study/NCT01476904) | Fase 3 | Completato | 208 | Estensione di sicurezza a 3 mesi, in doppio cieco, in pazienti asmatici |
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Fase 3 | Completato | 70 | E004 vs placebo per 4 settimane in bambini asmatici (4-11 anni) |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Fase 3 | Completato | 28 | Dose singola di E004 in bambini asmatici, studio crossover in doppio cieco |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Fase 4 | Completato | 49 | Epinefrina intramuscolare come terapia aggiuntiva nell'esacerbazione grave di asma pediatrica |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Fase 4 | Completato | 120 | Epinefrina, desametasone e soluzione salina ipertonica nella bronchiolite (regime combinato) |
| [NCT00817466](https://clinicaltrials.gov/study/NCT00817466) | Fase 4 | Sconosciuto | 500 | Confronto di trattamenti inalatori in lattanti con bronchiolite acuta |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | Non applicabile | Sconosciuto | 600 | Epinefrina vs albuterolo nella bronchiolite |
| [NCT00622817](https://clinicaltrials.gov/study/NCT00622817) | Non applicabile | Completato | 65 | Epinefrina inalatoria vs gocce nasali di xilometazolina nella bronchiolite |
| [NCT04207840](https://clinicaltrials.gov/study/NCT04207840) | Fase 4 | Completato | 28 | Esposizione sistemica di Primatene Mist vs epinefrina intramuscolare in volontari sani (farmacocinetica) |

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [35093318](https://pubmed.ncbi.nlm.nih.gov/35093318/) | 2022 | RCT | The Journal of Pediatrics | Corticosteroidi sistemici più epinefrina nebulizzata nella bronchiolite in terapia intensiva pediatrica |
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Revisione sistematica (Cochrane) | Cochrane Database of Systematic Reviews | Epinefrina per la bronchiolite |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Revisione sistematica (Cochrane) | Cochrane Database of Systematic Reviews | Epinefrina per la bronchiolite; i broncodilatatori mostrano benefici modesti a breve termine nelle forme lievi-moderate |
| [33893229](https://pubmed.ncbi.nlm.nih.gov/33893229/) | 2021 | Network meta-analisi | Pediatrics | Efficacia comparativa degli interventi per la bronchiolite in cure acute |
| [35953216](https://pubmed.ncbi.nlm.nih.gov/35953216/) | 2022 | Revisione | Emergency Medicine Clinics of North America | Gestione delle esacerbazioni di asma e BPCO in pronto soccorso |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Revisione | Expert Review of Respiratory Medicine | Ruolo di epinefrina racemica, corticosteroidi, soluzione ipertonica e ossigenoterapia ad alto flusso nella bronchiolite |
| [21157348](https://pubmed.ncbi.nlm.nih.gov/21157348/) | 2011 | Revisione | Current Opinion in Pediatrics | Aggiornamento sulla gestione della bronchiolite: nessun trattamento ha dimostrato di modificare il decorso |
| [23393929](https://pubmed.ncbi.nlm.nih.gov/23393929/) | 2012 | Revisione | Duodecim | Bronchiolite; inalazioni di epinefrina racemica quando necessario |
| [20876171](https://pubmed.ncbi.nlm.nih.gov/20876171/) | 2010 | Analisi di costo-efficacia | Pediatrics | Costo-efficacia di epinefrina e desametasone nella bronchiolite |
| [11940264](https://pubmed.ncbi.nlm.nih.gov/11940264/) | 2002 | Revisione clinica | Critical Care | Asma grave e stato asmatico |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 030650016 | ADRENALINA*5 fiale 0,5 mg 1 ml (SALF SpA) | Fiale | Revocata |
| 030650030 | ADRENALINA*5 fiale 1 mg 1 ml (SALF SpA) | Fiale | Revocata |
| 030780011 | ADRENALINA*5 fiale 0,5 mg 1 ml (MONICO SpA) | Fiale | Revocata |
| 030780023 | ADRENALINA*5 fiale 1 mg 1 ml (MONICO SpA) | Fiale | Revocata |

Tutte e quattro le autorizzazioni risultano revocate: non vi sono attualmente autorizzazioni valide per monocomponenti o combinazioni.

## Considerazioni sulla sicurezza

- **Controindicazioni (da relazioni nel grafo di conoscenza, non dal foglietto illustrativo)**: ipertensione, malattie cardiovascolari e cardiache (coronaropatia, infarto miocardico, fibrillazione atriale, disturbi della conduzione, arresto cardiaco improvviso), glaucoma ad angolo chiuso, ipertiroidismo, diabete mellito e chetoacidosi diabetica, epilessia, insufficienza epatica o renale, insufficienza respiratoria, iperplasia prostatica benigna, miastenia gravis e malattie della giunzione neuromuscolare, deficit di butirrilcolinesterasi, emoglobinopatie e deficit di potassio.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni. Quelle di livello **maggiore** includono amitriptilina e amoxapina (antidepressivi triciclici). Tra quelle di livello moderato figurano beta-bloccanti (acebutololo, atenololo, betaxololo), beta-agonisti (formoterolo, salbutamolo, arformoterolo), stimolanti (metilfenidato, anfetamina, atomoxetina), antidiabetici (acarbosio, acetoesamide, albiglutide, alogliptin) e antipsicotici (amisulpride, aripiprazolo, asenapina).

Per le avvertenze d'uso e le controindicazioni ufficiali, consultare il foglietto illustrativo.

## Conclusione e prossimi passi

**Decisione: Proceed with Guardrails**

**Motivazione:**
Esistono diversi studi di fase 3 completati sull'epinefrina inalatoria nell'asma (adulti e bambini), che sostengono il livello L1. Tuttavia l'indicazione coincide in larga parte con gli usi già noti. Inoltre tutte le autorizzazioni italiane sono revocate e le avvertenze ufficiali non sono disponibili.

**Per procedere sono necessari:**
- Recupero del foglietto illustrativo AIFA (avvertenze e controindicazioni), lacuna bloccante per la valutazione di sicurezza
- Dati sul meccanismo d'azione da DrugBank
- Verifica dello stato regolatorio e della disponibilità di formulazioni inalatorie in Italia
- Piano di monitoraggio cardiovascolare e delle interazioni (in particolare antidepressivi triciclici e beta-bloccanti)

## Altre indicazioni previste (sintesi)

| Indicazione | Punteggio TxGNN | Livello | Raccomandazione | Note |
|------|------|------|------|------|
| Anafilassi indotta da esercizio dipendente dal cibo | 99,57% | L4 | Research Question | Nessuno studio clinico; letteratura costituita soprattutto da revisioni. L'epinefrina è già il trattamento di prima linea dell'anafilassi, quindi il razionale è forte ma indiretto. |
| Sindrome di Rienhoff | 99,57% | L5 | Hold | Solo predizione del modello, senza studi né letteratura né un legame meccanicistico plausibile. |
| Malformazione respiratoria | 99,56% | L3 | Research Question | Un solo studio di fase 1 (NCT05006235) sulla tachipnea transitoria del neonato, che non è una vera malformazione; gran parte della letteratura è fuori tema. |
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

