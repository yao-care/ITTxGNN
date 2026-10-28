---
layout: default
title: Mirtazapine
parent: Solo previsione del modello (L5)
nav_order: 304
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
monitor_inn: "Mirtazapine"
predicted_indications: ["Ohdo syndrome and variants", "blepharophimosis - intellectual disability syndrome, Ohdo type", "benign paroxysmal torticollis of infancy"]
description: "Mirtazapine: nuova indicazione prevista, Sindrome di Ohdo e varianti (Ohdo syndrome and variants) (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Mirtazapine
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

## Mirtazapine: Sindrome di Ohdo e varianti (Ohdo syndrome and variants)
{: .text-alpha }

## Sintesi in una frase

La mirtazapina è un antidepressivo originariamente utilizzato per il trattamento della depressione (unipolare, endogena e disturbo depressivo maggiore) e dei disturbi d'ansia.
Il modello TxGNN ne predice una possibile efficacia nella **sindrome di Ohdo e varianti**, ma al momento non risultano **né studi clinici né pubblicazioni** a supporto: si tratta di una predizione puramente basata sul modello.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione predetta | Sindrome di Ohdo e varianti (Ohdo syndrome and variants) |
| Punteggio di predizione TxGNN | 0.9942 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 17 su 17) |
| Numero di autorizzazioni | 17 (valide: 17) |
| Decisione raccomandata | Hold |

## Perché questa predizione può (o non può) essere ragionevole?

Allo stato attuale i dati dettagliati sul meccanismo d'azione non sono disponibili nei dati compilati per questo report. In base alle informazioni farmacologiche note, la mirtazapina ha la maggiore affinità misurabile per i recettori alfa-2 adrenergici (2A > 2C > 2B) e per i recettori serotoninergici 5-HT2A e 5-HT2C. È un antidepressivo noradrenergico e serotoninergico specifico, con attività antagonista anche su recettori 5-HT3 e H1.

La sindrome di Ohdo (comprese le varianti correlate a KAT6B) è una rara malattia genetica della regolazione della cromatina, caratterizzata da disabilità intellettiva e tratti craniofacciali. Non emerge alcun collegamento meccanicistico tra l'attività recettoriale della mirtazapina e la patologia di base. Il punteggio TxGNN è molto alto, ma deriva dal modello TxGNN (deep learning) e può riflettere somiglianze apprese dal modello tra malattie correlate, non evidenze biologiche. Un eventuale beneficio sarebbe al massimo sintomatico (sonno, appetito, umore) e non modificante la malattia.

Altre predizioni nell'elenco hanno la stessa debolezza:
- **Sindrome blefarofimosi – disabilità intellettiva, tipo Ohdo** (punteggio 0,9911): molto probabilmente si sovrappone alla predizione principale, trattandosi di un sottotipo della stessa famiglia di malattie. Non ci sono studi clinici né pubblicazioni.
- **Torcicollo parossistico benigno dell'infanzia** (punteggio 0,9911): esiste solo un legame speculativo, perché la condizione è considerata un equivalente emicranico o una canalopatia (associazione con CACNA1A) e la modulazione serotoninergica e antistaminica è rilevante per i disturbi dello spettro emicranico. È un'ipotesi indiretta, senza evidenze di supporto. In età infantile la sicurezza è un problema importante: la mirtazapina non è approvata in ambito pediatrico e comporta un avvertimento per il rischio di suicidalità nei pazienti giovani.

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

Attualmente non risulta alcuna letteratura correlata.

## Informazioni sul mercato italiano

Il farmaco è in commercio: tutte le 17 autorizzazioni risultano valide (17 su 17). Di seguito le principali 5 (il testo dell'indicazione approvata non è disponibile).

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|------|
| 037988211 | MIRTAZAPINA 30 cpr orosolubili 30 mg | ALMUS Srl | Valida |
| 038514030 | MIRTAZAPINA 30 cpr orodispersibili 30 mg | TEVA ITALIA Srl | Valida |
| 037885249 | MIRTAZAPINA 30 cpr orodispersibili 30 mg | SANDOZ GMBH | Valida |
| 050628015 | ZAPIN 30 cpr rivestite 30 mg | ECUPHARMA Srl | Valida |
| 029444181 | REMERON 30 cpr orodispersibili 30 mg | ORGANON ITALIA Srl | Valida |

## Considerazioni sulla sicurezza

**Controindicazioni derivate dal grafo di conoscenza** (relazioni farmaco-malattia del grafo, non testo del foglio illustrativo):
- Neurologiche e psichiatriche: epilessia, disturbo bipolare in fase maniacale, atrofia multisistemica, acatisia indotta da farmaci, sindrome serotoninergica
- Cardiovascolari: ipotensione, ipotensione ortostatica, sindrome da tachicardia posturale ortostatica, infarto del miocardio, trombosi coronarica, ictus, disturbi cerebrovascolari, infarto cerebrale
- Ematologiche: neutropenia, agranulocitosi, emoglobinopatie
- Metaboliche ed epatorenali: ipertrigliceridemia, obesità (compresa la forma monogenica), epatopatie, malattie della colecisti, insufficienza renale

**Interazioni e target farmacologici**: la mirtazapina interagisce con i recettori 5-HT2A, 5-HT2C e con gli adrenocettori alfa-2A, alfa-2B e alfa-2C. In ambito clinico viene talvolta associata a un SSRI o a un SNRI nella depressione grave.

Per le avvertenze e le controindicazioni ufficiali si rimanda al foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa solo sul modello (livello L5), senza studi clinici né letteratura e senza un legame meccanicistico plausibile. A ciò si aggiungono lo stato di mercato "solo autorizzazioni revocate" e le preoccupazioni di sicurezza, soprattutto in ambito pediatrico.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) per verificare l'eventuale collegamento con la patologia
- Foglio illustrativo AIFA con avvertenze e controindicazioni, per lo screening di sicurezza
- Evidenze precliniche o cliniche che colleghino la farmacologia della mirtazapina alla sindrome di Ohdo
- Valutazione dell'accesso al farmaco, dato che in Italia non risultano autorizzazioni valide
- Piano di sicurezza specifico per popolazioni pediatriche
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

