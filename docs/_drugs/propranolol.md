---
layout: default
title: Propranolol
parent: Solo previsione del modello (L5)
nav_order: 366
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "propranolol"
predicted_indications: ["distal myopathy, Tateyama type", "congenital myopathy with excess of thin filaments", "chondroma", "cirrhotic cardiomyopathy"]
description: "Propranolol: nuova indicazione prevista, Distal myopathy, Tateyama type (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Propranolol
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

## Propranolol: Distal myopathy, Tateyama type
{: .text-alpha }

## Sintesi in una frase

Il propranololo è un beta-bloccante non selettivo, originariamente usato per ipertensione, aritmie, cardiomiopatia ipertrofica ed emangioma infantile.
Il modello TxGNN predice una possibile efficacia nella **miopatia distale di tipo Tateyama**, ma per questa indicazione **non risultano studi clinici né pubblicazioni** a supporto: la predizione è puramente computazionale.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione predetta | Distal myopathy, Tateyama type |
| Punteggio di predizione TxGNN | 0.9940 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 2 su 2) |
| Numero di autorizzazioni | 2 (valide: 2) |
| Decisione raccomandata | Hold (sospendere) |

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle informazioni note, il propranololo è un beta-bloccante non selettivo, la cui efficacia è consolidata in ambito cardiovascolare, ma non esiste un razionale farmacologico chiaro per la sua applicabilità a questa malattia.

L'analisi dei dati compilati indica che **non è stato stabilito alcun legame meccanicistico**. La miopatia distale di tipo Tateyama è una rara malattia del muscolo scheletrico, senza un coinvolgimento noto delle vie beta-adrenergiche su cui agirebbe il propranololo. Il punteggio elevato proviene dal modello TxGNN (deep learning) e può riflettere somiglianze apprese dal modello tra malattie correlate, come altre miopatie e cardiomiopatie, non evidenze biologiche.

Altre predizioni del modello presentano un razionale più solido (vedi sezione conclusiva), in particolare la cardiomiopatia in generale e la cardiomiopatia cirrotica.

## Evidenze da studi clinici

Attualmente non risultano studi clinici registrati correlati.

## Evidenze dalla letteratura

Attualmente non risulta alcuna letteratura correlata a questa indicazione.

## Informazioni sul mercato italiano

| N. autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 043368012 | HEMANGIOL soluzione orale, flacone 120 ml 3,75 mg/ml + siringa (Pierre Fabre Médicament) | Non indicata | Non indicata (autorizzazione valida) |
| 020854028 | INDERAL 30 cpr 40 mg (Atnahs Pharma Netherlands BV) | Non indicata | Non indicata (autorizzazione valida) |

## Considerazioni sulla sicurezza

- **Controindicazioni (da grafo di conoscenza, non da scheda tecnica)**: il grafo associa al propranololo controindicazioni in diverse condizioni, tra cui bronchite, malattie renali, epatiche e della colecisti, pancreatite, diabete mellito e chetoacidosi diabetica, lupus eritematoso sistemico, miastenia gravis, miopatie e malattie del muscolo scheletrico, paralisi periodica familiare, gotta, iperparatiroidismo, ipercalcemia, encefalopatia epatica, anuria e disturbi d'ansia. Va sottolineato che la **miastenia gravis e le miopatie** compaiono tra queste condizioni, un elemento di particolare rilievo per l'indicazione predetta.
- **Interazioni farmacologiche**: individuate 307 interazioni. Tra quelle di livello **maggiore** figura l'**epinefrina**. Tra quelle di livello moderato: corticosteroidi (idrocortisone, desametasone, betametasone, budesonide, triamcinolone), anticolinergici (atropina, iosciamina, metscopolamina), bupropione, morfina, lorcaserina, cimetidina, canagliflozin, clorpropamide e sali di calcio. Livello minore: acido ascorbico, acido acetilsalicilico, ossido di magnesio.

Per le avvertenze complete fare riferimento al foglietto illustrativo, non disponibile tra i dati compilati.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Per la miopatia distale di tipo Tateyama non esistono studi né pubblicazioni e non è identificabile un legame meccanicistico; inoltre, il grafo segnala le miopatie come condizione di controindicazione. Il punteggio elevato non è sufficiente a giustificare un avanzamento.

**Per procedere sarebbe necessario:**
- Dati sul meccanismo d'azione e un razionale biologico specifico per questa miopatia
- Avvertenze e controindicazioni dal foglietto illustrativo AIFA (attualmente mancanti, un blocco per la valutazione di sicurezza)
- Dati preclinici o di casistica che colleghino la modulazione beta-adrenergica al muscolo scheletrico affetto

**Nota su indicazioni alternative nello stesso elenco di predizioni:**
- **Cardiomiopatia** (punteggio 0,9912, livello L3): razionale solido per la sottoclasse ipertrofica, con studi emodinamici datati (1980–1983); per altre sottoclassi serve una valutazione specifica. Stato: domanda di ricerca.
- **Cardiomiopatia cirrotica** (punteggio 0,9912, livello L4): evidenze contrastanti, con un possibile beneficio sull'intervallo QT (2024) ma segnali di rischio emodinamico e renale nella malattia avanzata (2020, 2022). Stato: domanda di ricerca.
- **Cardiomiopatia ipertrofica da allenamento atletico, condroma e miopatia congenita con eccesso di filamenti sottili**: livello L5, nessuna evidenza, da sospendere.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

