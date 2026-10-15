---
layout: default
title: Levodopa
parent: Solo previsione del modello (L5)
nav_order: 266
evidence_level: L5
indication_count: 1
---

# Levodopa
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **1** 
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

# Levodopa: dalla malattia di Parkinson all'encefalite subacuta di Rasmussen

## Sintesi

La levodopa è un precursore della dopamina, originariamente impiegato nel trattamento della malattia di Parkinson e delle sindromi parkinsoniane correlate.
Il modello TxGNN ne prevede una possibile efficacia per l'**encefalite subacuta di Rasmussen**, con un punteggio molto alto (**99,06%**).
Tuttavia, nei dati compilati per questo report non risulta **nessuno studio clinico** né **alcuna pubblicazione** a sostegno di questa indicazione: la previsione si basa unicamente sul modello.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Malattia di Parkinson (e sindromi parkinsoniane correlate) |
| Nuova indicazione prevista | Encefalite subacuta di Rasmussen |
| Punteggio di predizione TxGNN | 99,06% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione potrebbe essere ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrato. In termini generali, la levodopa è un precursore della dopamina che viene decarbossilato a dopamina nel sistema nervoso centrale; la sua efficacia nella malattia di Parkinson è consolidata.

L'encefalite di Rasmussen è invece una malattia infiammatoria cerebrale cronica, tipicamente unilaterale e immunomediata (guidata dai linfociti T), che causa crisi focali farmacoresistenti (spesso epilessia parziale continua) e atrofia emisferica progressiva. Un possibile legame è l'esistenza di manifestazioni dei gangli della base o di disturbi del movimento associati ad atrofia cerebrale unilaterale (ad esempio la sindrome emiparkinsonismo-emiatrofia), ma si tratta di un'associazione indiretta nella rete di conoscenza.

Non ci sono prove che la sostituzione dopaminergica agisca sull'infiammazione sottostante o sulle crisi epilettiche. È plausibile che la previsione rifletta la vicinanza nel grafo di conoscenza alle indicazioni parkinsoniane, più che un reale meccanismo terapeutico. Inoltre, gli agenti dopaminergici potrebbero abbassare la soglia convulsiva o peggiorare i sintomi neuropsichiatrici, per cui la sicurezza in questa popolazione non è stabilita.

## Evidenza da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenza dalla letteratura

Attualmente non è disponibile letteratura correlata.

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; nessuna è attualmente valida. Le principali (testo dell'indicazione approvata non disponibile):

| Numero di autorizzazione | Nome del prodotto | Titolare |
|---------|------|------|
| 023145028 | SINEMET 50 cpr 100 mg + 25 mg | Organon Italia Srl |
| 023145042 | SINEMET 50 cpr 100 mg + 25 mg rilascio modificato | Organon Italia Srl |
| 023142045 | MADOPAR 30 cps 100 mg + 25 mg rilascio prolungato | Roche SpA |
| 023142019 | MADOPAR 30 cps 100 mg + 25 mg | Roche SpA |
| 023145016 | SINEMET 50 cpr 250 mg + 25 mg | Organon Italia Srl |

## Considerazioni sulla sicurezza

- **Controindicazioni secondo il grafo di conoscenza** (relazioni farmaco-malattia di TxGNN, non testo del foglio illustrativo): atrofia multisistemica, ipotensione ortostatica, sindrome da tachicardia posturale ortostatica, discinesia indotta da farmaci, **epilessia**, ulcera gastrica e peptica, disturbi d'ansia e nevrotici, distimia, malattie renali, epatiche e della colecisti, glaucoma ad angolo aperto e ad angolo chiuso, disturbi psicotici (schizofreniformi, schizoaffettivi), disturbi mentali, diabete mellito e chetoacidosi diabetica, melanoma, infarto miocardico e trombosi coronarica, emoglobinopatie, malattie diarroiche, arresto cardiaco improvviso e malattie della conduzione cardiaca.
  - Di particolare rilievo per la nuova indicazione: l'**epilessia** compare tra le controindicazioni, e l'encefalite di Rasmussen si manifesta proprio con crisi epilettiche intrattabili.
- **Interazioni farmacologiche**: sono state identificate 104 interazioni. Tra quelle mostrate, di livello **moderato**: epinefrina, efedrina, bupropione, metronidazolo, piridossina, metoclopramide, ferro e vari anticolinergici (atropina, ioscimina, metscopolamina, glicopirronio, diciclomina, clidinio, mepenzolato). Di livello **minore**: antiacidi (idrossido di alluminio, carbonato di calcio, magaldrato e sali di magnesio).

Per avvertenze e controindicazioni ufficiali, consultare il foglio illustrativo: i dati AIFA corrispondenti non erano disponibili.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione poggia solo sul punteggio del modello (livello L5), senza studi clinici né letteratura. Il legame meccanicistico è indiretto, e l'epilessia figura tra le controindicazioni nel grafo di conoscenza, con possibili rischi in una malattia dominata dalle crisi. In Italia, inoltre, nessuna autorizzazione è attualmente valida.

**Per procedere sono necessari:**
- Una revisione sistematica della letteratura su levodopa ed encefalite di Rasmussen (inclusi case report su emiparkinsonismo-emiatrofia)
- I dati sul meccanismo d'azione della levodopa e un'analisi del legame con la patogenesi immunomediata
- Le avvertenze e controindicazioni dal foglio illustrativo AIFA, con una valutazione specifica del rischio convulsivo
- Chiarimenti sullo stato regolatorio attuale in Italia (le autorizzazioni risultano tutte cancellate)
- Una valutazione di compatibilità di via di somministrazione e di similarità con l'indicazione originale
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

