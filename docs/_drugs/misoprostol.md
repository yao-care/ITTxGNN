---
layout: default
title: Misoprostol
parent: Solo previsione del modello (L5)
nav_order: 305
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Misoprostol: nuova indicazione prevista, Amenorrea (livello di evidenza L5). Indicazione originale: Non disponibile (i testi delle indicazioni nelle autorizzazioni AIFA…"
---

# Misoprostol
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **2** 
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

# Misoprostolo: dall'indicazione originale non documentata all'amenorrea

## Sintesi in una frase

Il misoprostolo è un analogo della prostaglandina E1; nei dati compilati per questo report non risulta alcun testo di indicazione approvata associato alle autorizzazioni italiane.
Il modello TxGNN lo prevede come potenzialmente efficace per l'**amenorrea**, con un punteggio molto alto, ma sono disponibili **0 studi clinici** e **7 pubblicazioni**, nessuna delle quali valuta il misoprostolo come trattamento dell'amenorrea.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile (i testi delle indicazioni nelle autorizzazioni AIFA sono vuoti) |
| Nuova indicazione prevista | Amenorrea |
| Punteggio di predizione TxGNN | 99,64% |
| Livello di evidenza | L5 (solo predizione del modello; nessuno studio clinico che valuti il farmaco per questa indicazione) |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 4 (tutte revocate) |
| Decisione raccomandata | Hold |

Nota: la valutazione preliminare indica L4, ma le pubblicazioni recuperate non contengono studi preclinici o meccanicistici sull'amenorrea come bersaglio terapeutico. In applicazione rigorosa delle regole di livello, il caso è quindi L5.

---

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle conoscenze generali, il misoprostolo è un analogo della prostaglandina E1 che induce contrazioni uterine e maturazione cervicale. Un legame plausibile con l'amenorrea potrebbe passare dall'azione sull'endometrio e sul sanguinamento uterino.

Tuttavia, la letteratura recuperata non supporta questa ipotesi. Il misoprostolo vi compare nell'aborto farmacologico (in associazione al mifepristone) e nella gestione dell'aborto interno. In questi lavori l'amenorrea è uno stato legato alla gravidanza o alla procedura (ad esempio l'epoca gestazionale ≤35 giorni di amenorrea), non un bersaglio terapeutico.

Il punteggio elevato di TxGNN è dunque una predizione computazionale, non confermata da evidenze cliniche dirette. Anche la relazione con l'indicazione originale non è valutabile, perché questa non è disponibile.

---

## Evidenza da studi clinici

Al momento non risultano studi clinici correlati registrati.

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reprod Sci | Mifepristone a basse dosi più misoprostolo autosomministrato per l'aborto ultra-precoce (amenorrea ≤35 giorni), 744 donne: valutate efficacia, sicurezza e accettabilità. Non riguarda il trattamento dell'amenorrea |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT (dose-ranging) | Reprod Sci | 2500 donne con gravidanza ultra-precoce randomizzate a dosi decrescenti di mifepristone (150-50 mg) seguite da misoprostolo 200 µg per l'aborto completo. Non riguarda l'amenorrea come bersaglio |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Coorte | Hum Reprod | Prevenzione della gravidanza indesiderata con mifepristone a basse dosi più misoprostolo prima della mestruazione attesa |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Coorte | J Obstet Gynaecol Res | Interruzione precoce di gravidanza con mifepristone a basse dosi e misoprostolo autosomministrato: sicurezza ed efficacia |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Revisione | BMJ | Gestione medica dell'aborto interno e della gravidanza anembrionica |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Revisione | J Obstet Gynaecol Can | Ablazione endometriale nel sanguinamento uterino anomalo; relazione con il misoprostolo non evidente |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Caso clinico | Cureus | Steatosi epatica acuta della gravidanza; l'amenorrea è solo un sintomo di presentazione |

---

## Informazioni sul mercato italiano

| N. autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 026488015 | CYTOTEC*50 cpr 200 mcg (Pfizer Srl) | Non disponibile | Non disponibile (revocata) |
| 029316041 | MISOFENAC*30 cpr 75 mg + 200 mcg rilascio modificato (Pfizer Italia Srl) | Non disponibile | Non disponibile (revocata) |
| 029757010 | ARTROTEC*30 cpr 50 mg + 200 mcg (Pfizer Italia Srl) | Non disponibile | Non disponibile (revocata) |
| 029757059 | ARTROTEC*30 cpr 75 mg + 200 mcg rilascio modificato (Pfizer Italia Srl) | Non disponibile | Non disponibile (revocata) |

---

## Considerazioni di sicurezza

- **Controindicazioni derivate dal grafo di conoscenza (TxGNN/PrimeKG, non dal foglietto illustrativo)**: ipertensione, insufficienza e malattie epatiche, danno epatico da farmaci, malattie della colecisti, scompenso cardiaco congestizio, malattie cardiovascolari e cardiache, infarto del miocardio, ictus e malattie cerebrovascolari, infarto cerebrale, malattia infiammatoria intestinale, asma (incluse forme intrinseca e allergica), abuso/dipendenza da sostanze, disturbi della coagulazione, emoglobinopatie e anemie, ulcera peptica attiva, meningite non infettiva.
- **Interazioni farmacologiche**: sono state identificate 196 interazioni. Tra quelle recuperate, di rilievo:
  - **Maggiore**: dinoprostone (uso topico).
  - **Moderata**: antiacidi contenenti magnesio (ossido, carbonato, idrossido, magaldrato) e chinapril.
  - **Minore**: sodio citrato, idrossido di alluminio, carbonato di calcio, bicarbonato di sodio, naprossene.
- **Gravidanza**: per l'azione uterotonica e il rischio teratogeno, il misoprostolo richiede particolare cautela nelle donne in età fertile, rilevante per un'indicazione come l'amenorrea.

Per le avvertenze e controindicazioni ufficiali occorre consultare il foglietto illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa unicamente sul punteggio del modello. Non esistono studi clinici né letteratura che indichino il misoprostolo come trattamento dell'amenorrea; gli studi trovati lo usano per l'interruzione di gravidanza. Inoltre, tutte le autorizzazioni italiane sono revocate e mancano i dati di sicurezza ufficiali.

**Per procedere sono necessari:**
- Scaricare e analizzare il foglietto illustrativo AIFA (avvertenze e controindicazioni), lacuna bloccante per lo screening di sicurezza.
- Ottenere i dati sul meccanismo d'azione (ad esempio da DrugBank).
- Chiarire l'indicazione originale del farmaco.
- Ricerca di letteratura o dati preclinici che colleghino il misoprostolo all'amenorrea come bersaglio terapeutico.
- Valutare la fattibilità regolatoria, dato che il prodotto è revocato in Italia, e un piano di sicurezza per le donne in età fertile.

**Nota sulla seconda predizione:** la coartazione atipica dell'aorta (punteggio TxGNN 99,30%, livello L5) non ha né studi clinici né letteratura. Un'eventuale analogia con le prostaglandine E1 nel mantenere pervio il dotto arterioso riguarda l'alprostadil, non il misoprostolo, e non costituisce evidenza. Anche per questa predizione la decisione è Hold.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

