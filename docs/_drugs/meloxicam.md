---
layout: default
title: Meloxicam
parent: Solo previsione del modello (L5)
nav_order: 283
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Meloxicam: nuova indicazione prevista, Displasia acromesomelica, tipo Hunter-Thompson (livello di evidenza L5). Indicazione originale: Artrite reumatoide, artrosi, artropatia, artrite idiopatica giov…"
monitor_inn: "MELOXICAM"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "spondyloarthropathy, susceptibility to", "rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "WHIM syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Meloxicam
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

# Meloxicam: Dall'artrite reumatoide alla displasia acromesomelica di tipo Hunter-Thompson

## Sintesi in una frase

Il meloxicam è un farmaco antinfiammatorio non steroideo (FANS) preferenzialmente inibitore della COX-2, originariamente utilizzato per artrite reumatoide, artrosi e altre patologie articolari.
Il modello TxGNN lo prevede come potenzialmente efficace per la **displasia acromesomelica di tipo Hunter-Thompson**, ma al momento **non risulta alcuno studio clinico né alcuna pubblicazione** a supporto di questa previsione (evidenza basata solo sul modello).

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Artrite reumatoide, artrosi, artropatia, artrite idiopatica giovanile, spondiloartropatia (dal grafo di conoscenza TxGNN; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Displasia acromesomelica, tipo Hunter-Thompson |
| Punteggio di previsione TxGNN | 99,92% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 7 |
| Decisione raccomandata | Hold |

## Perché questa previsione è ragionevole?

Al momento i dati dettagliati sul meccanismo d'azione non sono disponibili. In base alle informazioni note, il meloxicam è un FANS preferenzialmente inibitore della COX-2, con effetto antinfiammatorio e analgesico sintomatico nelle patologie articolari.

Per questa specifica previsione, tuttavia, **non emerge un chiaro legame meccanicistico**. La displasia acromesomelica di tipo Hunter-Thompson è una rara displasia scheletrica causata da varianti con perdita di funzione di CDMP1/GDF5, che compromettono la condrogenesi. Il meloxicam non è in grado di modificare il difetto genetico di base. L'elevato punteggio TxGNN riflette verosimilmente la prossimità, nella rete di conoscenza, a fenotipi scheletrici e articolari, più che un reale meccanismo terapeutico.

Il quadro è simile per le altre previsioni di alto rango (sindrome brachiolmia-amelogenesi imperfetta, brachiolmia, sindrome microftalmia colobomatosa-displasia rizomelica, sindrome WHIM): si tratta di condizioni genetiche dello sviluppo o immunodeficienze primarie su cui l'inibizione della COX non ha un effetto plausibile. Per la sindrome WHIM, la terapia è l'antagonismo di CXCR4 (ad es. plerixafor, mavorixafor).

Previsioni con maggiore plausibilità biologica, ma di fatto estensioni di indicazioni già esistenti:
- **Artrite idiopatica giovanile poliarticolare fattore reumatoide-positiva** (punteggio 99,44%): buona coerenza meccanicistica, ma è sostanzialmente interna alla famiglia di indicazioni già note.
- **Spondiloartropatia (suscettibilità)** e **nodulosi reumatoide**: vicine all'artrite reumatoide e alla spondiloartropatia, ma senza nuove evidenze; i FANS possono alleviare i sintomi articolari senza trattare i noduli.
- **Pseudoacondroplasia**: i FANS potrebbero alleviare il dolore articolare dell'artrosi precoce associata, ma senza razionale di modifica della malattia.

## Evidenza da studi clinici

Attualmente non risultano studi clinici correlati registrati per la displasia acromesomelica di tipo Hunter-Thompson.

## Evidenza dalla letteratura

Attualmente non risulta alcuna letteratura correlata per questa indicazione.

(Per la previsione di rango 8, l'artrite idiopatica giovanile poliarticolare fattore reumatoide-positiva, esiste un solo lavoro indiretto: [PMID 25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/), 2014, studio di coorte/registro di fase 4 sulla sicurezza del celecoxib e dei FANS non selettivi nell'artrite idiopatica giovanile. Non riguarda specificamente il meloxicam.)

## Informazioni sul mercato italiano

Tutte le autorizzazioni risultano cancellate; nessuna è attualmente valida. Le forme farmaceutiche e il testo delle indicazioni approvate non sono presenti nei dati compilati.

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 037077221 | MELOXICAM 30 cpr 15 mg | EG SpA | Cancellata |
| 037069224 | MELOXICAM 30 cpr div 15 mg | Mylan SpA | Cancellata |
| 037069073 | MELOXICAM 30 cpr 7,5 mg | Mylan SpA | Cancellata |
| 031985157 | MOBIC 7,5 30 cpr 7,5 mg | Boehringer Ingelheim Int. GmbH | Cancellata |
| 031985068 | MOBIC 15 30 cpr 15 mg | Boehringer Ingelheim Int. GmbH | Cancellata |

Complessivamente le autorizzazioni sono 7; le altre due sono MOBIC fiale IM 15 mg/1,5 ml (Boehringer Ingelheim, n. 035464015) e MELOXICAM 30 cpr 15 mg (Zentiva Italia, n. 037322260), entrambe cancellate.

## Considerazioni di sicurezza

**Controindicazioni derivate dal grafo di conoscenza** (non dal foglietto illustrativo): il grafo di conoscenza associa al meloxicam controindicazioni in diverse aree:
- Cardiovascolari e cerebrovascolari: ipertensione, scompenso cardiaco congestizio, infarto miocardico, trombosi coronarica, ictus, infarto cerebrale, cardiopatie.
- Gastrointestinali: gastrite, ulcera peptica attiva.
- Renali: nefropatia, insufficienza renale.
- Ematologiche: disturbi della coagulazione, anemia (incluse forme macrocitiche), emoglobinopatie.
- Metaboliche: diabete mellito, chetoacidosi diabetica, iperlipidemia (anche familiare).
- Altre: abuso/dipendenza da sostanze, piouretere.

**Interazioni farmacologiche**: sono state identificate 100 interazioni; tra quelle riportate, la maggior parte è di livello moderato:
- Corticosteroidi: idrocortisone, desametasone, betametasone, triamcinolone, budesonide.
- Antidiabetici: metformina, clorpropamide, glimepiride.
- Acido acetilsalicilico, mesalazina, balsalazide.
- Aprepitant, vancomicina, kanamicina.
- Sali di potassio (citrato, bicarbonato) e lassativi/preparati intestinali (picosolfato, polietilenglicole con elettroliti, solfato di sodio).
- Linaclotide: interazione di livello minore.

Per avvertenze e controindicazioni ufficiali, consultare il foglietto illustrativo AIFA, non disponibile nei dati compilati.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione principale non ha alcun supporto clinico o bibliografico (livello L5) e manca un meccanismo plausibile: un FANS non può correggere un difetto genetico dello sviluppo scheletrico. Inoltre, tutte le autorizzazioni italiane sono cancellate e il profilo di rischio cardiovascolare, gastrointestinale e renale dei FANS è rilevante.

**Per procedere sarebbe necessario:**
- Acquisire e analizzare il foglietto illustrativo AIFA (avvertenze e controindicazioni), attualmente mancante.
- Reperire i dati sul meccanismo d'azione (ad es. da DrugBank).
- Valutare un razionale preclinico per la via GDF5/CDMP1, oppure considerare solo un uso sintomatico (gestione del dolore) con studi specifici.
- Se si desidera un'opzione più realistica, dare priorità alla previsione sull'artrite idiopatica giovanile poliarticolare fattore reumatoide-positiva (livello L4), che rappresenta però un'estensione di un'indicazione già nota e richiede dati specifici sul meloxicam.
- Chiarire la situazione regolatoria: poiché non risultano autorizzazioni valide, andrebbe verificato se esistano altri prodotti a base di meloxicam commercializzati in Italia.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

