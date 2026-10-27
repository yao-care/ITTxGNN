---
layout: default
title: Clindamycin
parent: Solo previsione del modello (L5)
nav_order: 113
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Clindamycin: nuova indicazione prevista, Cheratocongiuntivite epiteliale puntata (livello di evidenza L5). Indicazione originale: Infezioni da stafilococco e streptococco, acne, vaginosi batterica…"
monitor_inn: "Clindamycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "neurotrophic keratopathy", "epidemic keratoconjunctivitis", "postmenopausal atrophic vaginitis"]
---

# Clindamycin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **6** 
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

## Clindamicina: dalle infezioni batteriche alla cheratocongiuntivite epiteliale puntata
{: .text-alpha }

## Riepilogo in una frase

La clindamicina è un antibiotico impiegato per infezioni da batteri Gram-positivi e anaerobi (ad esempio infezioni da stafilococco e streptococco, acne, vaginosi batterica, polmonite da aspirazione).
Il modello TxGNN prevede un possibile effetto nella **cheratocongiuntivite epiteliale puntata**, con un punteggio molto alto (99,97%).
Tuttavia, per questa indicazione **non risultano studi clinici né pubblicazioni**: la previsione si basa solo sul modello computazionale.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezioni da stafilococco e streptococco, acne, vaginosi batterica, infezioni da anaerobi (dalle indicazioni del grafo di conoscenza; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Cheratocongiuntivite epiteliale puntata |
| Punteggio di predizione TxGNN | 99,97% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 3 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile (o no)?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrati per questo farmaco. In base alle conoscenze generali, la clindamicina inibisce la sintesi proteica batterica legandosi alla subunità ribosomiale 50S, ed è efficace contro molti batteri Gram-positivi e anaerobi.

Il collegamento con la nuova indicazione è debole. La cheratite epiteliale puntata è spesso di origine virale o tossico/infiammatoria, quindi un antibatterico non ha una chiara motivazione meccanicistica, a meno che non vi sia una componente batterica (ad esempio blefarocheratocongiuntivite stafilococcica). Il punteggio elevato resta quindi una predizione computazionale, senza supporto clinico.

Anche le altre indicazioni previste dal modello non risultano convincenti:
- **Cheratite da esposizione** (punteggio 99,80%, livello L4): possibile solo come trattamento di un'infezione batterica secondaria; la letteratura trovata riguarda cheratiti batteriche in generale, non la clindamicina. La via oftalmica topica non è una via consolidata per questo farmaco.
- **Cheratopatia neurotrofica** (99,49%) e **vaginite atrofica postmenopausale** (99,03%): non sono condizioni primariamente infettive, e non sono stati trovati studi.
- **Cheratocongiuntivite epidemica** (99,49%): di origine adenovirale, contro cui la clindamicina non ha attività; gli articoli trovati riguardano una malattia veterinaria bovina.
- **Malattia animale non umana** (99,69%): categoria non specifica e non utilizzabile per il riposizionamento; la clindamicina è anzi un fattore di rischio per l'infezione da *C. difficile*.

## Evidenze dagli studi clinici

Attualmente non risultano studi clinici registrati correlati.

## Evidenze dalla letteratura

Per l'indicazione principale (cheratocongiuntivite epiteliale puntata) non è disponibile letteratura correlata. Per la seconda indicazione prevista (cheratite da esposizione) sono stati trovati solo lavori indiretti:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [24244625](https://pubmed.ncbi.nlm.nih.gov/24244625/) | 2013 | Studio di coorte retrospettivo | PloS one | Caratteristiche cliniche, sensibilità agli antibiotici ed esiti della cheratite da *S. aureus* (MRSA vs MSSA) |
| [22880135](https://pubmed.ncbi.nlm.nih.gov/22880135/) | 2012 | Studio di coorte retrospettivo | PloS one | Prevalenza e sensibilità antibiotica delle infezioni oculari da *S. aureus* resistente alla meticillina |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Caso clinico | Ophthalmology | Cheratite da *Bacillus cereus* associata all'uso di lenti a contatto |
| [42763505](https://pubmed.ncbi.nlm.nih.gov/42763505/) | 2026 | Caso clinico | IDCases | Toxoplasmosi oculare con coinvolgimento foveale diagnosticata con mNGS |

Nessuno di questi lavori valuta la clindamicina per la cheratite da esposizione.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 023868021 | DALACIN C FOSFATO 1 fiala IM EV 600 mg 4 ml (Pfizer Italia) | Fiala (IM/EV) | Non disponibile (autorizzazione cancellata) |
| 022633059 | DALACIN C 12 cps 150 mg (Pfizer Italia) | Capsule | Non disponibile (autorizzazione cancellata) |
| 035388026 | CLINDAMICINA FOSFATO 5 fiale 600 mg 4 ml (Hikma Italia) | Fiala | Non disponibile (autorizzazione cancellata) |

## Considerazioni di sicurezza

- **Controindicazioni segnalate nel grafo di conoscenza** (non derivate dal foglio illustrativo): insufficienza epatica, malattia di Crohn, malattie infiammatorie intestinali, colite ulcerosa, colite da *Clostridium difficile*, malattie diarroiche, enterocolite necrotizzante perinatale, dermatite atopica, dermatite esfoliativa, dermatite, scottatura solare, candidosi vulvovaginale.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni; tra quelle di livello moderato figurano balsalazide, claritromicina, acido picosolfurico, attapulgite e caolino. Per molte altre (ad esempio amoxicillina, vancomicina, doxiciclina, morfina, metformina, omeprazolo) il livello di gravità non è classificato.

Per le avvertenze e le controindicazioni ufficiali si rimanda al foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione ha solo supporto computazionale (livello L5), senza studi clinici né letteratura diretta, e il razionale meccanicistico è debole. Inoltre, in Italia tutte le autorizzazioni registrate risultano cancellate.

**Per procedere sarebbe necessario:**
- Scaricare e analizzare il foglio illustrativo AIFA per avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Ottenere i dati sul meccanismo d'azione da DrugBank
- Verificare un'eziologia batterica sensibile alla clindamicina nell'indicazione oculare
- Valutare la fattibilità di una via di somministrazione oftalmica, oggi non consolidata
- Condurre una ricerca di letteratura mirata e, se giustificato, studi preclinici o pilota
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

