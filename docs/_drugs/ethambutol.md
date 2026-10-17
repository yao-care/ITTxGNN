---
layout: default
title: Ethambutol
parent: Prove moderate (L3-L4)
nav_order: 182
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-15
description: "Ethambutol: nuova indicazione prevista, Epiglottite (livello di evidenza L4). Indicazione originale: Tubercolosi polmonare (da archi di indicazione del grafo di conoscenza"
monitor_inn: "ethambutol"
predicted_indications: ["epiglottitis", "laryngitis", "meningococcal infection", "peritonitis", "infectious otitis media"]
---

# Ethambutol
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **5** 
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

# Etambutolo: dalla tubercolosi polmonare all'epiglottite

## Sintesi in una frase

L'etambutolo è un farmaco antimicobatterico, originariamente usato per il trattamento della tubercolosi polmonare. Il modello TxGNN ne predice una possibile efficacia nell'**epiglottite**, ma per questa indicazione non risultano **sperimentazioni cliniche** e la letteratura si limita a **1 pubblicazione** (una serie di casi di tubercolosi laringea), per cui il segnale va considerato solo come ipotesi computazionale.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Tubercolosi polmonare (da archi di indicazione del grafo di conoscenza; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione predetta | Epiglottite |
| Punteggio di predizione TxGNN | 99,90% |
| Livello di evidenza | L4 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 1 |
| Decisione raccomandata | Hold (sospendere) |

## Perché questa predizione può essere ragionevole (o no)?

I dati compilati per questo report non includono una descrizione dettagliata del meccanismo d'azione. In base alle conoscenze generali, l'etambutolo inibisce le arabinosil-transferasi dei micobatteri e quindi la sintesi della parete cellulare micobatterica. Fa parte dei regimi standard multifarmaco antitubercolari.

Questo meccanismo non è attivo contro i patogeni tipici dell'epiglottite batterica (*Haemophilus influenzae* tipo b, streptococchi, *Staphylococcus aureus*). L'unico collegamento con la letteratura è la tubercolosi laringea, in cui l'epiglottide può essere coinvolta e l'etambutolo è usato come parte della terapia antitubercolare. Il punteggio elevato di TxGNN riflette probabilmente un'associazione anatomica e legata alla tubercolosi, non una vera indicazione per l'epiglottite batterica. Si tratta, in sostanza, dell'indicazione tubercolare originaria applicata a un sito diverso, non di un vero riposizionamento.

### Altre predizioni analizzate

| Rango | Malattia predetta | Punteggio | Livello | Valutazione |
|------|------|------|------|------|
| 2 | Laringite | 99,71% | L4 | Rilevante solo per la laringite tubercolare/da micobatteri non tubercolari; letteratura costituita da case report ed epidemiologia, nessuno studio |
| 3 | Infezione meningococcica | 99,63% | L5 | Nessuna base meccanicistica (le arabinosil-transferasi sono assenti in *Neisseria meningitidis*); nessuna evidenza |
| 4 | Peritonite | 99,20% | L3 | Segnale più solido, limitato alla peritonite tubercolare (revisione sistematica, report sulla terapia dell'TB addominale); estensione dell'indicazione TB, non utile per peritoniti non micobatteriche |
| 5 | Otite media infettiva | 99,06% | L5 | Nessuna attività sui patogeni abituali; nessuna evidenza |

## Evidenza dalle sperimentazioni cliniche

Attualmente non risultano sperimentazioni cliniche correlate registrate.

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | Serie di casi | Eur Respir J | 41 casi di tubercolosi laringea (1975-1985); sedi colpite per frequenza: corde vocali vere, epiglottide, corde false. Trattamento abituale con isoniazide, rifampicina ed etambutolo |

## Informazioni sul mercato italiano

| N. autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 021257023 | ETAPIAM*50 cpr rivestite 400 mg (PIAM FARMACEUTICI SpA) | Compresse rivestite | Non disponibile (autorizzazione cancellata) |

L'unica autorizzazione registrata risulta cancellata; non vi sono autorizzazioni valide.

## Considerazioni di sicurezza

- **Controindicazioni (dal grafo di conoscenza TxGNN, non dal foglio illustrativo)**: malattia renale, piureter, gotta, retinopatia diabetica, cataratta diabetica, neurite ottica.
- **Interazioni farmacologiche**: sono state identificate 112 interazioni. Quelle di livello moderato includono metronidazolo, acido picosolfurico, naltrexone, rosuvastatina, simvastatina, tinidazolo e idrossido di alluminio. Per altri farmaci (ad es. clotrimazolo, pantoprazolo, morfina, omeprazolo, lansoprazolo, vancomicina, prednisone, idrocortisone, sulfasalazina, prednisolone, ranitidina) il livello è non classificato.

Per avvertenze e controindicazioni ufficiali, consultare il foglio illustrativo.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
Il punteggio TxGNN è molto alto, ma non è supportato da alcuna sperimentazione né da una base meccanicistica per l'epiglottite batterica; la sola letteratura riguarda la tubercolosi laringea, dove l'etambutolo è già parte della terapia TB standard. Inoltre l'unica autorizzazione italiana è cancellata.

**Per procedere sarebbe necessario:**
- Ottenere le avvertenze e controindicazioni dal foglio illustrativo AIFA (lacuna bloccante per lo screening di sicurezza)
- Reperire i dati sul meccanismo d'azione (ad es. da DrugBank)
- Se di interesse, concentrare la ricerca sui sottotipi tubercolari (laringite e peritonite tubercolari, il segnale più solido, L3) anziché sull'epiglottite batterica
- Valutare il rischio oculare (neurite ottica) e renale, in particolare nei pazienti con diabete o nefropatia
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

