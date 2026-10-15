---
layout: default
title: Riluzole
parent: Solo previsione del modello (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
---

# Riluzole
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

# Riluzolo: dalla sclerosi laterale amiotrofica alla polimicrogiria parieto-occipitale parasagittale bilaterale

## Sintesi in una frase

Il riluzolo è stato sviluppato e utilizzato per il trattamento della sclerosi laterale amiotrofica (SLA).
Il modello TxGNN prevede una possibile efficacia nella **polimicrogiria parieto-occipitale parasagittale bilaterale** (punteggio molto alto, ma solo computazionale), con **0 sperimentazioni cliniche** e **0 pubblicazioni** a supporto di questa specifica indicazione.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Sclerosi laterale amiotrofica (SLA) |
| Nuova indicazione prevista | Polimicrogiria parieto-occipitale parasagittale bilaterale |
| Punteggio di predizione TxGNN | 99,99% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 6 |
| Decisione raccomandata | Hold |

## Perché questa predizione è ragionevole?

I dati compilati per questo report non riportano un meccanismo d'azione dettagliato. In base alle conoscenze generali, il riluzolo modula la trasmissione glutammatergica, ed è su questa base che si spiega la sua azione nella SLA.

Per la polimicrogiria, una malformazione corticale dello sviluppo, non esiste alcun legame meccanicistico supportato dai dati disponibili. Il punteggio TxGNN elevato (0,9999) è una predizione puramente computazionale, senza studi clinici né letteratura a sostegno. La predizione va quindi considerata con molta cautela.

### Altre indicazioni previste (contesto)

Tra le prime 10 predizioni, alcune riguardano patologie vicine alla SLA e biologicamente più plausibili per analogia, ma senza evidenze dirette:

| Posizione | Malattia prevista | Punteggio TxGNN | Livello di evidenza | Nota |
|------|------|------|------|------|
| 3 | Sindrome del motoneurone inferiore ad esordio nell'adulto tardivo | 99,99% | L5 | Plausibile per analogia con la SLA; nessuno studio specifico |
| 6 | Amiotrofia monomelica | 99,99% | L5 | Di solito autolimitante; beneficio incerto |
| 7 | Sindrome di Mills | 99,98% | L5 | Variante rara dello spettro dei motoneuroni; solo predizione |
| 8 | SLA, suscettibilità | 99,98% | L4 | Sovrapposta all'indicazione originale, non un vero riposizionamento |
| 10 | SLA di tipo 22 | 99,98% | L5 | Sottotipo genetico; nessuno studio specifico |

Le altre predizioni (displasia spondilometafisaria assiale, sindrome tricomegalia-degenerazione pigmentaria retinica-nanismo, sindrome artrogriposi letale-malattia delle corna anteriori, miopatia mitocondriale autosomica dominante) non hanno un legame meccanicistico evidente con il riluzolo.

## Evidenze dagli studi clinici

Attualmente non risultano studi clinici registrati correlati a questa indicazione prevista.

## Evidenze dalla letteratura

Per la polimicrogiria parieto-occipitale parasagittale bilaterale non è disponibile alcuna letteratura correlata.

Per completezza, la letteratura raccolta per la predizione di rango 8 (SLA, suscettibilità) è costituita in prevalenza da revisioni e studi meccanicistici o genetici, ed è quindi sovrapposta all'indicazione originale. Esempi:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [9178165](https://pubmed.ncbi.nlm.nih.gov/9178165/) | 1997 | Revisione | Journal of Neurology | Ipotesi del glutammato ed eccitotossicità nella SLA |
| [21128691](https://pubmed.ncbi.nlm.nih.gov/21128691/) | 2011 | Revisione | CNS Drugs | Fisiopatologia, diagnosi e gestione della SLA; il riluzolo è l'unico farmaco che prolunga modestamente la sopravvivenza |
| [16723044](https://pubmed.ncbi.nlm.nih.gov/16723044/) | 2006 | Revisione | Expert Reviews in Molecular Medicine | Meccanismi proposti e percorsi verso il trattamento della SLA |
| [42161327](https://pubmed.ncbi.nlm.nih.gov/42161327/) | 2026 | Studio di associazione genetica | Brain | Varianti di CYP2D6 nella SLA: rischio e sopravvivenza |
| [32040174](https://pubmed.ncbi.nlm.nih.gov/32040174/) | 2020 | Modellistica (DILIsym) | Toxicological Sciences | Effetti di una formulazione sublinguale e del riluzolo 50 mg orale sui parametri epatici |
| [20942785](https://pubmed.ncbi.nlm.nih.gov/20942785/) | 2010 | Revisione | CNS & Neurological Disorders Drug Targets | Determinanti genetici della SLA come bersagli terapeutici; il riluzolo prolunga la sopravvivenza di 2-3 mesi |

## Informazioni sul mercato italiano

Tutte le 6 autorizzazioni risultano cancellate; non vi sono autorizzazioni attualmente valide. Il testo delle indicazioni approvate non è disponibile.

| Numero di autorizzazione | Nome del prodotto | Titolare |
|---------|------|-----------|
| 050382035 | EMYLIF, 56 bustine orodispersibili 50 mg | Zambon SpA |
| 042018010 | TEGLUTIK, sospensione orale 300 ml 5 mg/ml | Italfarmaco SpA |
| 040541070 | Riluzolo, 56 compresse rivestite 50 mg | Aurobindo Pharma Italia Srl |
| 040801019 | Riluzolo, 56 compresse rivestite 50 mg | Sun Pharma France |
| 032887010 | RILUTEK, 56 compresse rivestite 50 mg | Sanofi Winthrop Industrie |

È presente anche una sesta autorizzazione (041946031, Riluzolo 56 compresse rivestite 50 mg, Sandoz SpA), anch'essa cancellata.

## Considerazioni sulla sicurezza

- **Controindicazioni derivate dal grafo di conoscenza (non dal foglietto illustrativo)**: neutropenia, agranulocitosi, abuso/dipendenza da sostanze, iperbilirubinemia (anche ereditaria), sindrome di Gilbert, malattia polmonare interstiziale, danno epatico indotto da farmaci.
- **Interazioni farmacologiche**: individuate 44 interazioni. Tra quelle di livello moderato: acido obeticolico, naltrexone, deferasirox, osilodrostat, anagrelide, asparaginasi (E. coli), brentuximab vedotin, clofarabina, metotrexato, epirubicina. Di livello lieve: omeprazolo, caffeina, teofillina, aminofillina. Per metformina, simvastatina, ranitidina, cianocobalamina, salbutamolo e ibuprofene il livello non è classificato.
- **Segnali epatici**: la letteratura segnala che circa il 50% dei pazienti con SLA in terapia con riluzolo orale presenta ALT sopra il limite superiore della norma, quindi è necessario il monitoraggio della funzione epatica.

Per avvertenze e controindicazioni ufficiali si rimanda al foglietto illustrativo.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione principale (polimicrogiria) si basa solo sul punteggio computazionale (L5), senza studi clinici, letteratura o legame meccanicistico. Inoltre, in Italia tutte le autorizzazioni risultano cancellate e i dati di sicurezza ufficiali non sono disponibili.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) del riluzolo
- Avvertenze e controindicazioni ufficiali dal foglietto illustrativo AIFA
- Verifica dello stato regolatorio attuale e della disponibilità del prodotto in Italia
- Evidenze precliniche o cliniche specifiche per la malattia prevista
- Valutazione, in via separata, delle indicazioni più plausibili (malattie del motoneurone inferiore, sindrome di Mills, sottotipi di SLA) come ipotesi di ricerca
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

