---
layout: default
title: Tamsulosin
parent: Solo previsione del modello (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tamsulosin: nuova indicazione prevista, Ipertricosi universale congenita di tipo Ambras (livello di evidenza L5). Indicazione originale: Iperplasia prostatica benigna (da grafo di conoscenza"
monitor_inn: "tamsulosin"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine with brainstem aura"]
---

# Tamsulosin
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

# Tamsulosina: dall'iperplasia prostatica benigna all'ipertricosi universale congenita di tipo Ambras

## Riepilogo in una frase

La tamsulosina è un antagonista dei recettori alfa-1 adrenergici, utilizzato originariamente per il trattamento dell'iperplasia prostatica benigna.
Il modello TxGNN ne prevede una possibile efficacia per l'**ipertricosi universale congenita di tipo Ambras**, ma per questa direzione non risulta **nessuno studio clinico** né **alcuna pubblicazione** a supporto: si tratta di una predizione puramente computazionale.

---

## Quadro di sintesi

| Voce | Contenuto |
|------|------|
| Indicazione originale | Iperplasia prostatica benigna (da grafo di conoscenza; il testo delle indicazioni approvate AIFA non è disponibile) |
| Nuova indicazione prevista | Ipertricosi universale congenita di tipo Ambras |
| Punteggio di predizione TxGNN | 99,996% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate; 0 valide) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è ragionevole?

Allo stato attuale, i dati dettagliati sul meccanismo d'azione non sono disponibili. In base alle informazioni note, la tamsulosina è un antagonista dei recettori adrenergici alfa-1A/1D, la cui efficacia nell'iperplasia prostatica benigna è consolidata.

Per l'indicazione prevista **non emerge un razionale meccanicistico plausibile**. La sindrome di Ambras deriva da riarrangiamenti genomici che alterano la regolazione di TRPS1, e non esiste alcuna via nota che colleghi il blocco alfa-1 adrenergico alla crescita eccessiva dei peli. L'elevato punteggio TxGNN (0,99996) riflette verosimilmente la vicinanza nel grafo di conoscenza a fenotipi legati ai peli, e non un legame biologico reale.

Anche le altre predizioni di rango elevato (ipertricosi, anomalie del fusto del pelo, ipotricosi, alopecia areata diffusa, alopecia, emicrania con aura del tronco encefalico, sindromi malformative congenite) sono prive di evidenze e di meccanismi plausibili.

---

## Evidenze da studi clinici

Attualmente non risulta registrato alcuno studio clinico correlato.

---

## Evidenze dalla letteratura

Per l'indicazione principale (ipertricosi di tipo Ambras) attualmente non è disponibile letteratura correlata.

Per la predizione di rango 9 (alopecia) sono state recuperate due pubblicazioni, che però **non** valutano la tamsulosina per l'alopecia:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [33175100](https://pubmed.ncbi.nlm.nih.gov/33175100/) | 2021 | Studio di coorte/sicurezza | JAMA Dermatology | Suicidalità ed eventi avversi psicologici associati alla finasteride (non alla tamsulosina) |
| [32826647](https://pubmed.ncbi.nlm.nih.gov/32826647/) | 2021 | Osservazionale | Cornea | Modificazioni morfologiche delle ghiandole di Meibomio in uomini con iperplasia prostatica benigna |

Entrambi gli studi riflettono associazioni legate all'iperplasia prostatica benigna e non costituiscono prova di beneficio.

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate. Il testo delle indicazioni approvate e la forma farmaceutica non sono presenti nei dati compilati. Le prime 5 autorizzazioni:

| N. autorizzazione | Nome prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 036908010 | ANTUNES 20 cps 0,4 mg rilascio modificato | SO.SE.PHARM Srl | Cancellata |
| 037004037 | TAMSULOSIN 20 cps 0,4 mg rilascio modificato | MYLAN SpA | Cancellata |
| 037010055 | TAMSULOSINA 30 cps 0,4 mg rilascio modificato | SANDOZ SpA | Cancellata |
| 050808017 | OMNIC 20 cps 0,4 mg rilascio modificato | FARMA 1000 Srl | Cancellata |
| 040917104 | TAMSULOSINA 30 cps 400 mcg rilascio prolungato | AUROBINDO PHARMA ITALIA Srl | Cancellata |

---

## Considerazioni sulla sicurezza

- **Controindicazioni (da grafo di conoscenza, non da scheda tecnica)**: atrofia multisistemica, sindrome da tachicardia posturale ortostatica, ipotensione ortostatica, epatopatia, malattia della colecisti, priapismo, sindrome dell'iride flaccida intraoperatoria.
- **Interazioni farmacologiche**: sono state identificate 202 interazioni. Tra quelle di gravità **maggiore** figura la **claritromicina**. Tra le interazioni di gravità **moderata** figurano bupropione, aprepitant, morfina, lorcaserina, cimetidina, miconazolo, clotrimazolo, eliglustat, dronabinolo, nabilone, oppio e gli inibitori di SGLT2 (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin).
- Per l'emicrania, va ricordato che la tamsulosina può causare ipotensione ortostatica e capogiri.

Per le avvertenze complete fare riferimento al foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa unicamente sul modello (livello L5): non esistono studi clinici o pubblicazioni, né un razionale meccanicistico plausibile. Inoltre, in Italia tutte le autorizzazioni sono cancellate.

**Per procedere sarebbero necessari:**
- Dati sul meccanismo d'azione (MOA) della tamsulosina e un'analisi del possibile legame con i disturbi del pelo
- Dati di sicurezza dal foglio illustrativo AIFA (avvertenze e controindicazioni)
- Dati preclinici o di studi osservazionali che colleghino il blocco alfa-1 adrenergico alla crescita o alla struttura del pelo
- Verifica dello stato regolatorio e della disponibilità commerciale in Italia, dato che non vi sono autorizzazioni valide
- Rivalutazione delle altre predizioni con maggiore plausibilità biologica, poiché nessuna di quelle attuali mostra evidenze di supporto
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

