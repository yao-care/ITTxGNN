---
layout: default
title: Diltiazem
parent: Solo previsione del modello (L5)
nav_order: 147
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
monitor_inn: "DILTIAZEM"
predicted_indications: ["obsolete susceptibility to ischemic stroke"]
description: "Diltiazem: nuova indicazione prevista, Suscettibilità all'ictus ischemico (termine obsoleto) (livello di evidenza L5). Indicazione originale: Ipertensione, fibrillazione atriale, angina di Prinzmetal"
---

# Diltiazem
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **1** 
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

# Diltiazem: Dall'ipertensione alla suscettibilità all'ictus ischemico (indicazione obsoleta)

## Sintesi in una frase

Il diltiazem è un calcio-antagonista usato originariamente per ipertensione, fibrillazione atriale, angina di Prinzmetal e tachicardia ventricolare.
Il modello TxGNN ne prevede un possibile utilizzo per la **suscettibilità all'ictus ischemico** (termine classificato come obsoleto nell'ontologia di riferimento), ma al momento **non risultano studi clinici né pubblicazioni** a sostegno: si tratta di una predizione puramente computazionale.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione, fibrillazione atriale, angina di Prinzmetal, tachicardia ventricolare (dal grafo di conoscenza; il testo delle indicazioni autorizzate AIFA non è disponibile) |
| Nuova indicazione prevista | Suscettibilità all'ictus ischemico (termine obsoleto) |
| Punteggio di predizione TxGNN | 99,08% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa predizione è plausibile?

Per questo farmaco i dati compilati non riportano il meccanismo d'azione. In base alle conoscenze farmacologiche generali (non verificate con i dati di questo report), il diltiazem è un calcio-antagonista non diidropiridinico che agisce sui canali del calcio di tipo L, con effetti vasodilatatori e di controllo della frequenza cardiaca.

Un possibile legame con il rischio di ictus ischemico potrebbe passare per la riduzione della pressione arteriosa, una minore vasocostrizione cerebrovascolare e il controllo della frequenza nella fibrillazione atriale, importante fattore di rischio per l'ictus cardioembolico. L'ipertensione e la fibrillazione atriale, indicazioni originali, sono infatti fattori di rischio riconosciuti per l'ictus.

Va però sottolineato che il punteggio elevato è solo una predizione del modello e non costituisce evidenza clinica. Inoltre, l'indicazione prevista è un termine obsoleto e la sua definizione clinica è vaga: la prevenzione del rischio non equivale al trattamento di una malattia definita.

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

Attualmente non risulta letteratura correlata disponibile.

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; nessuna è attualmente valida. Il testo delle indicazioni approvate e la forma farmaceutica non sono disponibili nei dati. Principali autorizzazioni (prime 5):

| Numero di autorizzazione | Prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 025275049 | DILADEL 36 cps 200 mg rilascio prolungato | Zentiva Italia Srl | Cancellata |
| 026675049 | Diltiazem 14 cpr 300 mg rilascio prolungato | Mylan SpA | Cancellata |
| 025275025 | DILADEL 24 cpr 120 mg rilascio prolungato | Zentiva Italia Srl | Cancellata |
| 025277070 | DILZENE 14 cps 300 mg rilascio prolungato | Alfasigma SpA | Cancellata |
| 032808091 | Diltiazem 24 cps 120 mg rilascio modificato | EG SpA | Cancellata |

## Considerazioni sulla sicurezza

Dal grafo di conoscenza TxGNN (non dal testo del foglio illustrativo) emergono associazioni di controindicazione con le seguenti condizioni:

- **Cardiache e di conduzione**: blocco atrioventricolare, malattia del nodo del seno (anche familiare), sindrome di Wolff-Parkinson-White, sindrome di Lown-Ganong-Levine, tachicardia ventricolare (incluse forme catecolaminergiche e infantili), cardiomiopatia ipertrofica, stenosi aortica e valvulopatie aortiche, ipotensione, ostruzione dell'arteria renale.
- **Epatiche, renali e biliari**: malattia renale, malattia epatica, malattia della colecisti, piouretere.
- **Ematologiche**: neutropenia, agranulocitosi.
- **Angioedema**: forme acquisite, ereditarie e indotte da bloccanti del sistema renina-angiotensina-aldosterone.
- **Altre**: malattie del tessuto connettivo, delle ossa e della cartilagine.

**Interazioni farmacologiche** (100 interazioni totali; sono elencate le principali tra quelle disponibili):
- **Maggiore**: loperamide.
- **Moderate**: corticosteroidi (idrocortisone, desametasone, betametasone, triamcinolone, budesonide), pioglitazone, bupropione, aprepitant, morfina, acido acetilsalicilico, canagliflozin e vari sali di calcio (fosfato, acetato, carbonato, cloruro, citrato, glubionato, glucoeptonato).

Per le avvertenze e le controindicazioni ufficiali si rimanda al foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa solo sul modello (livello L5), senza studi clinici né letteratura. L'indicazione prevista è un termine obsoleto e poco definito, e in Italia non esistono autorizzazioni valide.

**Per procedere sono necessari:**
- Una definizione clinica precisa dell'indicazione (ad esempio prevenzione dell'ictus nei pazienti ipertesi o con fibrillazione atriale) al posto del termine obsoleto
- Una revisione sistematica della letteratura e la ricerca di studi clinici su diltiazem e prevenzione dell'ictus
- I dati sul meccanismo d'azione (DrugBank)
- Il foglio illustrativo AIFA con avvertenze e controindicazioni, indispensabile per la valutazione della sicurezza
- La verifica dello stato regolatorio: con tutte le autorizzazioni cancellate, occorre chiarire se esistano formulazioni ancora disponibili in Italia
- Una valutazione di compatibilità delle vie di somministrazione
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

