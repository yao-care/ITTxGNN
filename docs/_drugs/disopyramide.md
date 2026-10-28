---
layout: default
title: Disopyramide
parent: Solo previsione del modello (L5)
nav_order: 148
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Disopyramide: nuova indicazione prevista, Sindrome di Tourette (livello di evidenza L5). Indicazione originale: Non disponibile nei dati compilati (nessun testo di indicazione nelle…"
monitor_inn: "disopyramide"
predicted_indications: ["Tourette syndrome", "attention deficit-hyperactivity disorder", "trichotillomania", "attention deficit hyperactivity disorder, inattentive type", "faciodigitogenital syndrome", "specific developmental disorder", "idiopathic neonatal atrial flutter", "chondromyxoid fibroma", "multifocal atrial tachycardia (disease)", "trigeminal nerve neoplasm"]
---

# Disopyramide
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
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

## Disopyramide: Dalle aritmie cardiache alla sindrome di Tourette
{: .text-alpha }

## Sintesi

Disopyramide è un antiaritmico di classe Ia (bloccante dei canali del sodio con attività anticolinergica). Il modello TxGNN predice una possibile efficacia nella **sindrome di Tourette**, ma attualmente **non risultano studi clinici né pubblicazioni** a supporto di questa indicazione: la previsione si basa solo sul modello.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile nei dati compilati (nessun testo di indicazione nelle autorizzazioni AIFA) |
| Nuova indicazione prevista | Sindrome di Tourette |
| Punteggio di predizione TxGNN | 0,9986 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 2 su 2) |
| Numero di autorizzazioni | 2 (valide: 2) |
| Decisione raccomandata | Hold |

## Perché questa previsione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrati per questo farmaco. In base alle conoscenze generali, disopyramide è un antiaritmico di classe Ia che blocca i canali del sodio cardiaci ed esercita un'azione anticolinergica.

**Per la sindrome di Tourette non emerge alcun legame meccanicistico consolidato.** La fisiopatologia di questa condizione è legata soprattutto alla disfunzione dei circuiti dopaminergici cortico-striatali, che non sono un bersaglio riconosciuto di disopyramide. L'alto punteggio deriva dal modello TxGNN (deep learning) e può riflettere somiglianze apprese dal modello tra malattie correlate, non evidenze biologiche; la predizione non è sostenuta da studi.

Anche le altre indicazioni predette di rango elevato presentano la stessa debolezza:
- **ADHD (e sottotipo inattentivo)**, **tricotillomania**, **disturbo specifico dello sviluppo**: nessun legame plausibile; i punteggi derivano dal modello TxGNN (deep learning) e possono riflettere somiglianze apprese dal modello tra malattie neuroevolutive correlate, non evidenze biologiche. Gli effetti anticolinergici e cardiaci potrebbero anzi aggiungere eventi avversi.
- **Sindrome facio-digito-genitale**, **fibroma condromixoide**, **neoplasia del nervo trigemino**: nessun razionale biologico.
- **Flutter atriale neonatale idiopatico** e **tachicardia atriale multifocale**: esiste una plausibilità indiretta, trattandosi di aritmie, ma mancano dati specifici. La sicurezza neonatale è una forte preoccupazione, e la tachicardia atriale multifocale si tratta di norma con correzione della patologia polmonare di base, calcio-antagonisti o beta-bloccanti.

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

Per la sindrome di Tourette attualmente non è disponibile alcuna letteratura correlata.

Per completezza, tra le indicazioni predette di rango inferiore, l'unica pubblicazione disponibile (tachicardia atriale multifocale) è la seguente:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [7418495](https://pubmed.ncbi.nlm.nih.gov/7418495/) | 1980 | Caso clinico/coorte | Chest | Aritmie ventricolari resistenti trattate con lorcainide; disopyramide, insieme ad altri antiaritmici, non aveva soppresso le aritmie. Lo studio riguarda un altro farmaco e non supporta direttamente disopyramide. |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 021894035 | RITMODAN*40 cps 100 mg | Non disponibile | Non disponibile (autorizzazione valida) |
| 027218015 | RITMODAN RETARD*20 cpr 250 mg | Non disponibile | Non disponibile (autorizzazione valida) |

Titolare: CHEPLAPHARM ARZNEIMITTEL GMBH. Entrambe le autorizzazioni risultano cancellate.

## Considerazioni sulla sicurezza

- **Controindicazioni suggerite dal grafo di conoscenza** (relazioni farmaco-malattia del modello, non testo di scheda tecnica): sindrome del QT lungo (anche familiare), nefropatie, epatopatie, malattie della colecisti, carenza di potassio, ipertrofia prostatica benigna, glaucoma ad angolo chiuso, miastenia gravis e malattie della giunzione neuromuscolare, ipoglicemia, ipotensione, blocco atrioventricolare, cardiomiopatie (inclusa ipertrofica), fibrosi endomiocardica, miocardite, fibrillazione e flutter atriale.
- **Interazioni farmacologiche**: sono state rilevate 258 interazioni. Tra quelle di gravità **maggiore**: potassio citrato, claritromicina e acido picosolfurico. Tra quelle di gravità **moderata**: famotidina, idrocortisone, amfotericina B, ioscina, loperamide, aprepitant, atropina, desametasone, betametasone, bisacodile, budesonide, glicopirronio, clidinio, clorpropamide, triamcinolone. Cimetidina: gravità minore.

Per avvertenze e controindicazioni ufficiali consultare il foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per la sindrome di Tourette (livello L5) si fonda solo sul modello, senza studi, senza legame meccanicistico plausibile e con un profilo di sicurezza (effetti anticolinergici, rischio proaritmico, numerose controindicazioni) poco favorevole. Inoltre, in Italia tutte le autorizzazioni sono cancellate.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione e una giustificazione biologica per l'indicazione neurologica
- Scheda tecnica AIFA con avvertenze e controindicazioni, per lo screening di sicurezza
- Evidenze precliniche e cliniche specifiche (studi o letteratura) sulla sindrome di Tourette
- Valutazione della fattibilità regolatoria e commerciale, dato lo stato di autorizzazioni cancellate
- In alternativa, valutare le indicazioni cardiologiche affini (aritmie atriali) con dati dedicati
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

