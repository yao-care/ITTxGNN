---
layout: default
title: Degarelix
parent: Solo previsione del modello (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Degarelix: nuova indicazione prevista, Ipertricosi (malattia) (livello di evidenza L5). Indicazione originale: Non riportata nei dati compilati per questo report (le autorizzazioni…"
monitor_inn: "DEGARELIX"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "syndrome with a Dandy-Walker malformation as major feature", "malformation syndrome with odontal and/or periodontal component", "isolated genetic hair shaft abnormality", "allergic urticaria", "cold urticaria", "familial male-limited precocious puberty", "centra precocious puberty 1", "familial isolated trichomegaly"]
---

# Degarelix
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

# Degarelix: Dal carcinoma prostatico all'ipertricosi (predizione computazionale)

## Sintesi in una frase

Degarelix è un antagonista del recettore del GnRH, noto nella pratica clinica per il trattamento del carcinoma prostatico avanzato ormono-dipendente. Il modello TxGNN predice un possibile effetto su **ipertricosi**, ma **non risultano sperimentazioni cliniche né pubblicazioni** a supporto: la predizione è puramente computazionale.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati compilati per questo report (le autorizzazioni AIFA non contengono il testo dell'indicazione) |
| Nuova indicazione predetta | Ipertricosi (malattia) |
| Punteggio di predizione TxGNN | 99,99% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 2 |
| Decisione raccomandata | Hold |

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle conoscenze generali, degarelix è un antagonista del recettore del GnRH: sopprime LH e FSH e riduce testosterone e androgeni a valle.

Il legame con l'ipertricosi è **debole e speculativo**. L'ipertricosi, a differenza dell'irsutismo, in genere non è guidata dagli androgeni, quindi non c'è una chiara ragione per cui la soppressione androgenica possa essere utile. Il punteggio elevato riflette probabilmente la vicinanza nel grafo di conoscenza (fenotipi legati ai peli), non un'evidenza biologica o clinica.

Anche le altre predizioni ad alto punteggio mostrano un quadro simile:

- **Ipertricosi congenita di tipo Ambras, sindromi malformative (Dandy-Walker, componente dentale/parodontale), anomalie genetiche del fusto del pelo, tricomegalia familiare isolata**: condizioni genetiche/strutturali senza razionale ormonale (livello L5).
- **Orticaria allergica e da freddo**: mediate dai mastociti; degarelix può causare reazioni al sito di iniezione mediate dall'istamina, quindi l'uso sarebbe controintuitivo e problematico per la sicurezza (L5).
- **Pubertà precoce maschile familiare limitata (testotossicosi) e pubertà precoce centrale**: le uniche con plausibilità biologica indiretta (livello L4, "domanda di ricerca"). Nella pubertà precoce centrale l'antagonismo del GnRH è coerente con il meccanismo, ma mancano dati pediatrici, di dosaggio e di sicurezza, e degarelix è approvato solo per adulti con carcinoma prostatico. Nella testotossicosi il difetto (mutazione attivante di LHCGR) è a valle dell'asse GnRH, quindi l'efficacia come monoterapia è improbabile.

## Evidenze da sperimentazioni cliniche

Attualmente non risultano sperimentazioni cliniche correlate registrate.

## Evidenze dalla letteratura

Attualmente non risulta letteratura correlata disponibile.

## Informazioni sul mercato italiano

| N. autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 039232020 | FIRMAGON 2 flaconcini polv 120 mg + 2 siringhe solv 3 ml (Ferring Pharmaceuticals A/S) | Non indicata | Non indicata (autorizzazione cancellata) |
| 039232018 | FIRMAGON 1 flaconcino 80 mg polv + 1 siringa solv 4,2 ml (Ferring Pharmaceuticals A/S) | Non indicata | Non indicata (autorizzazione cancellata) |

## Citotossicità

Degarelix è utilizzato in oncologia (carcinoma prostatico), ma è una terapia ormonale e non un citotossico convenzionale; i dati compilati non contengono informazioni di citotossicità. Si rimanda alle avvertenze e precauzioni del foglio illustrativo.

## Considerazioni di sicurezza

**Controindicazioni derivate dal grafo di conoscenza** (associazioni farmaco-malattia di PrimeKG, non testo di scheda tecnica): sindrome del QT lungo (anche familiare), torsione di punta, malattie epatiche, malattie della cistifellea e carenza di potassio.

**Interazioni farmacologiche** (100 interazioni individuate; principali esempi):

- **Maggiori**: cisapride, dolasetron.
- **Moderate**: claritromicina, levofloxacina, ondansetron, granisetron, palonosetron, famotidina, loperamide, nonché vari lassativi e preparati per la pulizia intestinale (bisacodile, acido picosolfurico, polietilenglicole con elettroliti, lattulosio, lattitolo, citrato e idrossido di magnesio, olio di ricino, glicerina, olio minerale).
- **Minori**: metronidazolo.

Molte di queste interazioni sono verosimilmente legate al rischio di prolungamento del QT e agli squilibri elettrolitici, coerentemente con le controindicazioni sopra riportate.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione per l'ipertricosi si basa solo sul modello (L5), senza sperimentazioni né pubblicazioni, con un razionale meccanicistico debole. Inoltre le autorizzazioni italiane sono tutte cancellate e mancano i dati di sicurezza dalla scheda tecnica.

**Per procedere sono necessari:**
- Scheda tecnica AIFA (avvertenze e controindicazioni) per completare lo screening di sicurezza
- Dati dettagliati sul meccanismo d'azione (ad esempio da DrugBank)
- Indicazione approvata originale documentata
- Per eventuali approfondimenti, valutare piuttosto la pubertà precoce centrale (L4): servirebbero dati pediatrici di efficacia, dosaggio e sicurezza
- Verifica della compatibilità di via di somministrazione e formulazione
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

