---
layout: default
title: Clavulanic Acid
parent: Solo previsione del modello (L5)
nav_order: 112
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Clavulanic Acid: nuova indicazione prevista, Uretrite da Ureaplasma (livello di evidenza L5). Indicazione originale: Infezioni delle vie urinarie, polmonite batterica…"
---

# Clavulanic Acid
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

# Acido clavulanico: dalle infezioni batteriche all'uretrite gonococcica

## Sintesi in una frase

L'acido clavulanico è un inibitore delle beta-lattamasi, usato in associazione con l'amoxicillina per trattare infezioni batteriche come quelle delle vie urinarie e le polmoniti batteriche.
Il modello TxGNN lo indica come potenzialmente utile per l'**uretrite da Ureaplasma** (primo nella classifica del modello), ma questa predizione non è supportata da dati reali. L'indicazione con il supporto più concreto è l'**uretrite gonococcica**, con **0 studi clinici registrati** e **9 pubblicazioni**, in gran parte studi clinici degli anni '80.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezioni delle vie urinarie, polmonite batterica, infezioni da *Staphylococcus aureus*, *Escherichia coli* e *Klebsiella* (dal grafo di conoscenza; nei dati compilati non è riportato il testo dell'indicazione approvata) |
| Nuova indicazione predetta (rank 1) | Uretrite da Ureaplasma |
| Punteggio di predizione TxGNN | 99,93% |
| Livello di evidenza | L5 (solo predizione del modello) |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 20 (tutte revocate) |
| Decisione raccomandata | Hold |

> **Nota:** la prima indicazione predetta (uretrite da Ureaplasma) ha lo stesso punteggio di quella gonococcica (99,93%). Quest'ultima è l'unica con evidenza clinica reale (livello L3) ed è discussa più avanti come candidata più rilevante.

---

## Perché questa predizione è ragionevole (o no)?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle conoscenze generali, l'acido clavulanico è un inibitore delle beta-lattamasi: non ha un'attività antibatterica significativa da solo, ma protegge l'amoxicillina dalla degradazione enzimatica, ripristinandone l'efficacia contro i ceppi produttori di beta-lattamasi.

**Uretrite da Ureaplasma (rank 1):** la predizione appare poco solida dal punto di vista farmacologico. L'Ureaplasma non possiede parete cellulare ed è intrinsecamente resistente ai beta-lattamici, quindi un inibitore delle beta-lattamasi non ha un razionale biologico. Il punteggio elevato è probabilmente dovuto alla vicinanza nella rete di conoscenza ad altre indicazioni di uretrite. La letteratura recuperata riguarda l'uretrite in generale (*Pasteurella bettyae*, revisioni diagnostiche, terapia empirica, anaerobi nella prostatite) e non contiene dati clinici specifici su Ureaplasma.

**Uretrite gonococcica (rank 2):** qui il razionale è chiaro. L'acido clavulanico inibisce la penicillinasi prodotta da *Neisseria gonorrhoeae*, ripristinando l'attività dell'amoxicillina sui ceppi produttori. Si tratta però di un uso storico già studiato, non di una vera novità di riposizionamento. Le resistenze attuali e le terapie preferite dalle linee guida a base di ceftriaxone ne limitano la rilevanza contemporanea.

**Altre predizioni:** per malattia infiammatoria uterina e tubercolosi urogenitale esiste solo un razionale indiretto o teorico (inibizione della beta-lattamasi BlaC di *M. tuberculosis*, attività *in vitro*), senza evidenza clinica. Per le restanti (pielonefrite xantogranulomatosa, sindrome da compressione del tronco celiaco, gravidanza ectopica addominale, linfangioma cistico addominale, miofibroblastoma palizzata dei linfonodi, malattia del legamento largo dell'utero) il razionale è assente o speculativo e probabilmente frutto di artefatti del grafo.

---

## Evidenze da studi clinici

Al momento non risultano studi clinici correlati registrati per l'indicazione di primo rango (uretrite da Ureaplasma), né per le altre indicazioni predette.

---

## Evidenze dalla letteratura

**Uretrite da Ureaplasma (rank 1)**: nessuna pubblicazione riguarda specificamente l'indicazione o l'acido clavulanico.

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [34366085](https://pubmed.ncbi.nlm.nih.gov/34366085/) | 2021 | Caso clinico | Infectious Diseases Now | Prima associazione di *Pasteurella bettyae* con uretrite e balanite in uomini che hanno rapporti con uomini |
| [19544099](https://pubmed.ncbi.nlm.nih.gov/19544099/) | 2009 | Revisione | Rev Esp Quimioter | Prevalenza e tendenza dei microrganismi responsabili di uretrite nell'uomo (Madrid) |
| [21947096](https://pubmed.ncbi.nlm.nih.gov/21947096/) | 2011 | Revisione | Rev Esp Quimioter | Migliore terapia empirica dell'uretrite |
| [9669200](https://pubmed.ncbi.nlm.nih.gov/9669200/) | 1998 | Revisione | Int J Androl | Possibile ruolo dei batteri anaerobi nella prostatite cronica |

**Uretrite gonococcica (rank 2)**: l'evidenza più pertinente.

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [3533755](https://pubmed.ncbi.nlm.nih.gov/3533755/) | 1986 | Studio randomizzato comparativo | Genitourin Med | Cefuroxima axetil vs amoxicillina + acido clavulanico (con probenecid) in 500 pazienti con gonorrea non complicata |
| [6365235](https://pubmed.ncbi.nlm.nih.gov/6365235/) | 1984 | Studio clinico comparativo | Br J Vener Dis | In 121 uomini, amoxicillina 3 g + clavulanato 250 mg: 9,4% ancora positivi alla coltura a 7 giorni, vs 26,3% con penicillina procaina i.m. |
| [6428699](https://pubmed.ncbi.nlm.nih.gov/6428699/) | 1984 | Studio clinico | Br J Vener Dis | Due dosi di Augmentin: guarigione 95,9% vs 87,4% con kanamicina (192 uomini) |
| [4007860](https://pubmed.ncbi.nlm.nih.gov/4007860/) | 1985 | Studio clinico (confronto di dosi) | Genitourin Med | Amoxicillina 3 g + clavulanato 125 mg: guarigione di 97 su 100 pazienti valutabili; 85% di guarigione nei ceppi PPNG |
| [3004176](https://pubmed.ncbi.nlm.nih.gov/3004176/) | 1985 | Studio clinico (dose singola) | Afr J Med Med Sci | Augmentin in dose singola a Ibadan, dove circa l'80% dei ceppi è produttore di penicillinasi |
| [6757686](https://pubmed.ncbi.nlm.nih.gov/6757686/) | 1982 | Studio clinico (braccio singolo) | Med J Malaysia | Amoxicillina + acido clavulanico orale in dose singola nell'uretrite gonococcica maschile |
| [3147528](https://pubmed.ncbi.nlm.nih.gov/3147528/) | 1988 | Studio clinico/Revisione | Sex Transm Dis | Opzioni terapeutiche per gonorrea resistente agli antibiotici, incluso l'acido clavulanico aggiunto ad amoxicillina |
| [3132029](https://pubmed.ncbi.nlm.nih.gov/3132029/) | 1988 | Studio di laboratorio | Hinyokika Kiyo | Rilevamento di *N. gonorrhoeae* produttore di penicillinasi in 89 isolati di uomini con uretrite e sensibilità a vari antibiotici |
| [21947096](https://pubmed.ncbi.nlm.nih.gov/21947096/) | 2011 | Revisione | Rev Esp Quimioter | Migliore terapia empirica dell'uretrite |

**Altre indicazioni** (evidenza solo indiretta):

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [30890463](https://pubmed.ncbi.nlm.nih.gov/30890463/) | 2019 | Linee guida | Gynecol Obstet Fertil Senol | Linee guida CNGOF/SPILF sull'endometrite post-partum (malattia infiammatoria uterina) |
| [7811001](https://pubmed.ncbi.nlm.nih.gov/7811001/) | 1994 | Modello animale | Antimicrob Agents Chemother | Infezione genitale murina da *Chlamydia trachomatis* trattata con tetracicline, amoxicillina-clavulanato o azitromicina |
| [26847806](https://pubmed.ncbi.nlm.nih.gov/26847806/) | 2016 | Caso clinico | BMJ Case Reports | Epididimo-orchite tubercolare scambiata per scroto acuto; l'amoxicillina/clavulanato non ha valutato l'efficacia sulla tubercolosi |

Per la malattia infiammatoria uterina gli altri studi recuperati sono veterinari (cavalle, vacche, cani) o non pertinenti (un caso di actinomicosi) e non sono riportati.

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano revocate; nessuna è attualmente valida. Nei dati compilati non sono presenti la forma farmaceutica né il testo dell'indicazione approvata. Le principali autorizzazioni:

| N. autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 048462067 | Amoxicillina e acido clavulanico, sospensione orale granulare 140 ml 400 mg/5 ml + 57 mg/5 ml | Zentiva Italia Srl | Revocata |
| 036944015 | Amoxicillina e acido clavulanico, 12 bustine 875 mg + 125 mg | Laboratori Alter Srl | Revocata |
| 036815025 | Amoxicillina e acido clavulanico, 12 compresse rivestite 875 mg + 125 mg | Pharmacare Srl | Revocata |
| 040488049 | Augmentin, 12 compresse rivestite 875 mg + 125 mg | Farma 1000 Srl | Revocata |
| 026138228 | Clavulin, sospensione orale 140 ml 400 mg/5 ml + 57 mg/5 ml con siringa dosatrice | GlaxoSmithKline SpA | Revocata |

---

## Considerazioni di sicurezza

Dati disponibili per questo farmaco (le informazioni dal grafo di conoscenza non derivano dal foglietto illustrativo):

- **Condizioni associate a controindicazione nel grafo di conoscenza**: malattia renale, malattia epatica, malattia della colecisti, colestasi (incluse colestasi intraepatica ricorrente benigna e familiare), colite da *Clostridium difficile*, enterocolite necrotizzante perinatale, piureterere, mononucleosi infettiva e sindrome da infezione cronica da virus di Epstein-Barr.
- **Interazioni farmacologiche**: 16 interazioni segnalate, di cui 2 di livello **maggiore**: **leflunomide** e **teriflunomide**. Le altre 14 sono di livello moderato (ad esempio metotrexato, naltrexone, balsalazide, epirubicina, tioguanina, trabectedina, idelalisib, clofarabina, brentuximab vedotin, asparaginasi, pegaspargase e gli interferoni beta).

Per avvertenze e controindicazioni ufficiali, consultare il foglietto illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione di primo rango (uretrite da Ureaplasma) non ha base farmacologica (l'Ureaplasma è privo di parete cellulare e quindi intrinsecamente resistente ai beta-lattamici) né evidenza clinica, ed è classificata L5. L'uretrite gonococcica ha studi clinici più concreti (L3), ma si tratta di un uso storico degli anni '80, limitato dalle resistenze attuali e dalle terapie a base di ceftriaxone raccomandate dalle linee guida; tutte le autorizzazioni italiane sono inoltre revocate.

**Per procedere è necessario:**
- Acquisire le avvertenze e le controindicazioni dal foglietto illustrativo AIFA (lacuna bloccante per lo screening di sicurezza)
- Recuperare i dati sul meccanismo d'azione da DrugBank
- Verificare la sensibilità attuale di *N. gonorrhoeae* e le linee guida correnti prima di considerare l'uretrite gonococcica
- Confermare lo stato regolatorio attuale in Italia, poiché non risultano autorizzazioni valide
- Escludere l'indicazione da Ureaplasma salvo comparsa di dati specifici, e considerare le predizioni prive di razionale (rank 6-10) probabili artefatti del grafo
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

