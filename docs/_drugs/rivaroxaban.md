---
layout: default
title: Rivaroxaban
parent: Solo previsione del modello (L5)
nav_order: 385
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Rivaroxaban: nuova indicazione prevista, Artrite reumatoide (livello di evidenza L5). Indicazione originale: Non disponibile nei dati compilati (i testi di indicazione delle auto…"
monitor_inn: "RIVAROXABAN"
predicted_indications: ["rheumatoid arthritis", "gout", "HIV infectious disease", "brachydactyly-syndactyly syndrome"]
---

# Rivaroxaban
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **4** 
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

## Rivaroxaban: Dall'uso antitrombotico all'artrite reumatoide (predizione TxGNN)
{: .text-alpha }

## Riepilogo in una frase

Il rivaroxaban è un anticoagulante orale che inibisce il fattore Xa. Nei dati compilati per questo report non è disponibile un testo di indicazione approvata.
Il modello TxGNN lo associa all'**artrite reumatoide** con un punteggio molto alto, ma **non esistono studi clinici registrati** e nessuna delle pubblicazioni recuperate valuta il rivaroxaban come trattamento di questa malattia. L'evidenza si basa quindi solo sulla predizione del modello.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile nei dati compilati (i testi di indicazione delle autorizzazioni AIFA sono vuoti) |
| Nuova indicazione predetta | Artrite reumatoide |
| Punteggio di predizione TxGNN | 99,57% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate; nessuna valida) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione potrebbe essere ragionevole?

I dati sul meccanismo d'azione non sono al momento disponibili nei dati compilati. In base alle conoscenze generali, il rivaroxaban è un inibitore diretto del fattore Xa, utilizzato come anticoagulante.

L'unico collegamento plausibile è indiretto: la via della coagulazione e l'infiammazione sono correlate. La trombina e il fattore Xa possono segnalare tramite i recettori PAR-1/PAR-2 e contribuire all'infiammazione sinoviale, e le malattie autoimmuni si associano ad alterata generazione di trombina e a un maggior rischio di tromboembolismo venoso. Si tratta **soltanto di un'ipotesi**: giustificherebbe al massimo un ruolo nella tromboprofilassi nei pazienti con artrite reumatoide, non un effetto modificante la malattia.

Va sottolineato che il punteggio TxGNN (0,996) deriva da un grafo di conoscenza e non costituisce evidenza clinica.

---

## Evidenze da studi clinici

Al momento non risultano studi clinici registrati correlati all'artrite reumatoide.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Revisione su diagnosi e trattamento del tromboembolismo venoso degli arti inferiori; non riguarda l'artrite reumatoide come bersaglio terapeutico |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de médecine interne | Il test di generazione della trombina nelle malattie autoimmuni evidenzia stati di ipercoagulabilità e rischio cardiovascolare |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Coorte | PloS one | Aderenza a rivaroxaban vs apixaban nella fibrillazione atriale non valvolare; non pertinente all'artrite reumatoide |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case report | Cureus | Infarto cerebrale tromboembolico perioperatorio in una paziente con fibrillazione atriale in terapia steroidea per artrite reumatoide; l'artrite è solo una comorbilità |

Nessuna di queste pubblicazioni studia l'efficacia del rivaroxaban nell'artrite reumatoide.

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; non ne è presente alcuna valida. Il testo dell'indicazione approvata e la forma farmaceutica non sono disponibili. Di seguito le principali (le prime 5 dell'elenco):

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 049197078 | Rivaroxaban 30 cpr rivestite 10 mg (Sandoz) | Compresse rivestite | Non disponibile |
| 050706035 | Mirebax 42 cpr rivestite 15 mg (Aurora Licensing) | Compresse rivestite | Non disponibile |
| 049197080 | Rivaroxaban 42 cpr rivestite 15 mg (Sandoz) | Compresse rivestite | Non disponibile |
| 038744138 | Xarelto 42 cpr rivestite 15 mg (Bayer) | Compresse rivestite | Non disponibile |
| 038744518 | Xarelto granuli per sospensione orale 1 mg/ml (Bayer) | Granuli per sospensione orale | Non disponibile |

---

## Considerazioni sulla sicurezza

- **Controindicazioni segnalate dal grafo di conoscenza** (archi farmaco-malattia di TxGNN, non testo del foglietto illustrativo): insufficienza epatica, malattia renale, piouretere, malattia epatica, malattia della colecisti, disturbi della coagulazione del sangue.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni; tra quelle di gravità **maggiore** figurano:
  - acido acetilsalicilico
  - cobicistat
  - deferasirox
  - ibritumomab tiuxetan
  - tositumomab (I-131)

  Tra quelle di gravità moderata: aprepitant, desametasone, cimetidina, claritromicina, miconazolo, clotrimazolo e altri.

Per avvertenze e controindicazioni ufficiali, consultare il foglietto illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
Il punteggio TxGNN è molto alto, ma non vi sono studi clinici né letteratura che supportino un effetto terapeutico del rivaroxaban nell'artrite reumatoide (livello L5). Inoltre, tutte le autorizzazioni italiane sono cancellate e le informazioni di sicurezza ufficiali non sono disponibili.

**Per procedere è necessario:**
- Scaricare e analizzare il foglietto illustrativo AIFA per avvertenze e controindicazioni
- Ottenere i dati sul meccanismo d'azione (ad esempio da DrugBank)
- Chiarire l'indicazione originale e lo stato regolatorio attuale (autorizzazioni cancellate)
- Raccogliere evidenze precliniche o cliniche dirette sul ruolo del fattore Xa/trombina nell'artrite reumatoide
- Valutare, se pertinente, un'ipotesi limitata alla tromboprofilassi nei pazienti con artrite reumatoide

**Nota sulle altre indicazioni predette:** gotta (99,5%), infezione da HIV (99,2%) e sindrome brachidattilia-sindattilia (99,1%) presentano ugualmente evidenza L5 o L4 e raccomandazione Hold. Per l'HIV la letteratura riguarda solo la gestione dell'anticoagulazione e le interazioni con gli antiretrovirali potenziati (ritonavir/cobicistat), non un effetto antivirale. L'unico studio (NCT00786422) è una coorte di fase 2 sulla trombosi venosa profonda, non uno studio sull'HIV.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

