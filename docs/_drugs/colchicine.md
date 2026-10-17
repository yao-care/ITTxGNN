---
layout: default
title: Colchicine
parent: Solo previsione del modello (L5)
nav_order: 127
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Colchicine: nuova indicazione prevista, Malaria da Plasmodium falciparum (livello di evidenza L5). Indicazione originale: Gotta, febbre mediterranea familiare (da base di conoscenza TxGNN"
monitor_inn: "Colchicine"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans"]
---

# Colchicine
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **3** 
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

# Colchicina: da gotta e febbre mediterranea familiare a malaria da Plasmodium falciparum

## Riepilogo in una frase

La colchicina è un farmaco originariamente usato per la gotta e per la febbre mediterranea familiare (FMF). Il modello TxGNN prevede che possa essere efficace contro la **malaria da Plasmodium falciparum**, ma non esistono studi clinici registrati e le due pubblicazioni raccolte sono studi preclinici indiretti, quindi il supporto è **solo predittivo (L5)**.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Gotta, febbre mediterranea familiare (da base di conoscenza TxGNN; nelle autorizzazioni AIFA il testo dell'indicazione non è riportato) |
| Nuova indicazione prevista | Malaria da Plasmodium falciparum |
| Punteggio di previsione TxGNN | 99,60% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 2 (0 valide, 2 cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione nel database. Dalle conoscenze generali, la colchicina si lega alla tubulina e interrompe la polimerizzazione dei microtubuli. Dai dati compilati emergono come bersagli anche la tubulina beta di classe I (TUBB), i recettori della glicina, BRD4 e alcuni recettori del gusto amaro (TAS2R4, TAS2R46).

Il legame con la malaria è plausibile ma indiretto. Uno studio preclinico sulla curcumina suggerisce che i microtubuli di P. falciparum possano essere un bersaglio farmacologico. Un secondo lavoro mostra che il gene plasmodiale pfmdr1 (omologo della glicoproteina P) modifica la suscettibilità delle cellule di mammifero ai farmaci. Nessuna evidenza dimostra però un'efficacia antimalarica della colchicina nei pazienti.

A ciò si aggiunge l'indice terapeutico ristretto della colchicina, che ne limita l'utilità pratica come antimalarico, data la disponibilità di farmaci efficaci già approvati.

Altre previsioni emerse per il farmaco:
- **Febbre mediterranea familiare autosomica dominante** (punteggio 99,38%, L4): è sostanzialmente un'estensione di un'indicazione già esistente. La colchicina è la terapia di prima linea per la FMF, ma le prove raccolte sono revisioni, senza studi specifici sul sottotipo dominante.
- **Dermatofibrosarcoma protuberans** (punteggio 99,37%, L5): nessuno studio o pubblicazione. La malattia è guidata dalla fusione COL1A1-PDGFB e trattata con chirurgia e imatinib; il supporto è solo il punteggio del modello.

## Evidenze da studi clinici

Attualmente non risultano studi clinici registrati correlati.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | Preclinico (in vitro) | PloS one | La curcumina altera i microtubuli di P. falciparum, suggerendo che siano un bersaglio farmacologico |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | Preclinico (in vitro) | Molecular and cellular biology | L'espressione di pfmdr1 in cellule di mammifero è associata a maggiore suscettibilità alla clorochina |

Nessuna delle due pubblicazioni testa direttamente la colchicina contro la malaria.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 009964038 | COLCHICINA LIRCA*2x30 cpr div 1 mg | Non riportata | Non riportata (autorizzazione cancellata) |
| 009964040 | COLCHICINA LIRCA*60 cpr 0,5 mg | Non riportata | Non riportata (autorizzazione cancellata) |

## Citotossicità

La colchicina è un agente antimitotico (inibitore dei microtubuli), ma il suo uso originale riguarda gotta e FMF, non patologie oncologiche. Non essendo classificabile come farmaco antineoplastico nei dati compilati, la sezione non è applicabile. Va comunque ricordato che a dosi antimitotiche la tossicità è rilevante.

## Considerazioni sulla sicurezza

**Controindicazioni e condizioni a rischio (dal grafo di conoscenza TxGNN, non dal foglio illustrativo):**
- Epatiche e renali: insufficienza epatica, funzionalità renale compromessa, nefropatia acuta da urati
- Ematologiche: malattie ematologiche, trombocitopenia, leucopenia, agranulocitosi, neutropenia (incluse forme congenite e idiopatiche dell'adulto), anemia aplastica
- Muscolari: miopatia, malattie muscolari e del muscolo scheletrico, rabdomiolisi, paralisi periodica familiare
- Gastrointestinali: ulcera peptica, malattie diarroiche
- Altre: fascite nodulare

**Interazioni e farmacologia:** i dati compilati riportano interazioni farmacologiche sui bersagli (recettori della glicina α1/α2, TAS2R4, TAS2R46, BRD4, tubulina beta di classe I), ma non interazioni farmaco-farmaco cliniche con livello di gravità.

Per avvertenze e controindicazioni ufficiali consultare il foglio illustrativo AIFA, attualmente non disponibile.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
- Per la malaria da P. falciparum non esistono studi clinici né evidenze dirette; il supporto è solo il punteggio del modello e due studi preclinici indiretti. L'indice terapeutico ristretto e la disponibilità di antimalarici efficaci riducono ulteriormente l'interesse pratico. Entrambe le autorizzazioni italiane sono cancellate.

**Per procedere sarebbe necessario:**
- Dati sul meccanismo d'azione dal database (DrugBank)
- Foglio illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Studi in vitro e in vivo che testino direttamente la colchicina su P. falciparum, con margini di sicurezza rispetto alle concentrazioni attive
- Per la FMF autosomica dominante: valutare come estensione di un'indicazione esistente, con dati specifici sul sottotipo
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

