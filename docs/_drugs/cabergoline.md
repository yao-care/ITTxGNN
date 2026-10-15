---
layout: default
title: Cabergoline
parent: Prove moderate (L3-L4)
nav_order: 82
evidence_level: L4
indication_count: 5
---

# Cabergoline
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **5** 
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

# Cabergolina: dall'iperprolattinemia all'adenocarcinoma ipofisario

## Sintesi in una frase

La cabergolina è un agonista dopaminergico D2 usato originariamente per l'iperprolattinemia e per i tumori ipofisari che producono prolattina. Il modello TxGNN la indica come potenzialmente efficace nell'**adenocarcinoma ipofisario**, con un punteggio molto alto. Per questa indicazione specifica **non esistono studi clinici registrati** e la letteratura è limitata a **3 case report indiretti**, quindi il supporto è solo computazionale e indiretto.

---

## Quadro di sintesi

| Voce | Contenuto |
|------|------|
| Indicazione originale | Iperprolattinemia (comprese le forme familiari e acquisite) e tumore ipofisario secernente prolattina |
| Nuova indicazione prevista | Adenocarcinoma ipofisario |
| Punteggio di predizione TxGNN | 99,06% |
| Livello di evidenza | L4 |
| Stato di mercato in Italia | Solo autorizzazioni cancellate (nessuna attualmente valida) |
| Numero di autorizzazioni | 7 (tutte cancellate) |
| Decisione raccomandata | Hold |

L'indicazione originale deriva dal grafo di conoscenza biomedico usato da TxGNN. Nei dati compilati per questo report le autorizzazioni italiane non riportano il testo dell'indicazione approvata.

---

## Perché questa predizione è ragionevole?

La cabergolina è un agonista del recettore dopaminergico D2. Molti tumori ipofisari esprimono recettori D2, quindi la stimolazione di questi recettori può ridurre la secrezione ormonale e, in alcuni casi, limitare la crescita tumorale. Il profilo farmacologico compilato mostra inoltre un'attività su numerosi recettori serotoninergici (5-HT1A, 1B, 1D, 2A, 2B, 2C), adrenergici (α1A, α2A, α2B, α2C) e dopaminergici (D1-D5). Una descrizione dettagliata del meccanismo d'azione non è però disponibile nei dati compilati.

Il legame con l'indicazione originale è plausibile: l'iperprolattinemia da tumore ipofisario e l'adenocarcinoma ipofisario riguardano lo stesso tessuto e la stessa via di segnalazione dopaminergica. Il punteggio elevato del modello riflette soprattutto la vicinanza nella rete di conoscenza alla biologia dei tumori ipofisari, non una prova clinica diretta.

La letteratura associata a questa predizione è indiretta:
- un case report su octreotide o cabergolina nella secrezione ectopica di corticotropina;
- un case report su un adenocarcinoma pancreatico non correlato alla patologia ipofisaria;
- un caso di neoplasia endocrina multipla di tipo 1 con decorso atipico.

Nessuno di questi lavori studia la cabergolina nel vero carcinoma ipofisario (malattia metastatica).

Per completezza, nei dati compilati compare anche una predizione correlata, il "cancro ipofisario", sostenuta da diversi studi di fase 3 sulla cabergolina negli adenomi ipofisari (prolattinomi, tumori corticotropi e adenomi non funzionanti). Si tratta però di tumori prevalentemente benigni e in parte sovrapposti all'indicazione originale. Quegli studi non dimostrano l'efficacia nel carcinoma e non sono stati considerati per il livello di evidenza di questa valutazione.

---

## Evidenza da studi clinici

Attualmente nessuno studio clinico correlato registrato per questa indicazione specifica.

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [20497940](https://pubmed.ncbi.nlm.nih.gov/20497940/) | 2010 | Case report | Endocrine Practice | Risposta della corticotropina a octreotide o cabergolina a lungo termine in un paziente con secrezione ectopica di corticotropina dopo surgenalectomia |
| [33569966](https://pubmed.ncbi.nlm.nih.gov/33569966/) | 2021 | Case report | Revista Española de Enfermedades Digestivas | Linfangectasie duodenali come primo segno di adenocarcinoma pancreatico in una paziente con adenoma ipofisario in terapia con cabergolina; rilevanza solo marginale |
| [41760078](https://pubmed.ncbi.nlm.nih.gov/41760078/) | 2026 | Case report | Medicine | Neoplasia endocrina multipla con decorso atipico e variante del gene MEN1 di significato incerto |

---

## Informazioni sul mercato italiano

Delle 7 autorizzazioni registrate, nessuna è attualmente valida; di seguito le prime 5. Il testo dell'indicazione approvata non è disponibile per queste autorizzazioni.

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Titolare | Stato |
|---------|------|------|------|------|
| 037576016 | Cabergolina, 2 cpr 0,5 mg | Compresse 0,5 mg | Ratiopharm GmbH | Cancellata |
| 028988032 | Dostinex, 8 cpr 0,5 mg | Compresse 0,5 mg | Pfizer Italia Srl | Cancellata |
| 028988018 | Dostinex, 2 cpr 0,5 mg | Compresse 0,5 mg | Pfizer Italia Srl | Cancellata |
| 033359035 | Actualene, 8 cpr 0,5 mg | Compresse 0,5 mg | Pfizer Italia Srl | Cancellata |
| 050868025 | Cabergolina, 8 cpr 0,5 mg | Compresse 0,5 mg | Aurobindo Pharma Italia Srl | Cancellata |

---

## Considerazioni sulla sicurezza

- **Condizioni associate a controindicazione nel grafo di conoscenza** (non derivano dal testo del foglio illustrativo): malattia epatica, malattia della colecisti, valvulopatia cardiaca, fibrosi polmonare (incluse la fibrosi polmonare post-infiammatoria e la fibrosi retroperitoneale correlata a IgG4), preeclampsia e preeclampsia grave.
- **Profilo recettoriale**: l'attività sui recettori serotoninergici, in particolare 5-HT2B, è coerente con il rischio di valvulopatia cardiaca segnalato nella letteratura sulla cabergolina. Sono stati compilati 15 bersagli recettoriali, ma non interazioni farmacologiche cliniche con altri medicinali.

Per avvertenze, controindicazioni e interazioni ufficiali si rimanda al foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
- Per l'adenocarcinoma ipofisario non esistono studi clinici né letteratura diretta: le tre pubblicazioni disponibili sono case report indiretti, e il punteggio TxGNN (99,06%) è una predizione computazionale. Il livello di evidenza è L4.
- Tutte le autorizzazioni italiane sono cancellate, il che complica un eventuale percorso di riposizionamento.

**Per procedere sono necessari:**
- Dati clinici diretti sull'uso della cabergolina nel carcinoma ipofisario (serie di casi, studi osservazionali o studi clinici).
- Valutazione dei risultati degli studi di fase 3 sugli adenomi ipofisari non funzionanti e corticotropi, per capire se possano essere estrapolati alla malattia maligna.
- Dati dettagliati sul meccanismo d'azione.
- Foglio illustrativo AIFA con avvertenze e controindicazioni, per lo screening di sicurezza.
- Chiarimento dello stato regolatorio in Italia, dato che tutte le autorizzazioni risultano cancellate.
- Un piano di monitoraggio cardiaco (valvole) per l'uso prolungato o ad alte dosi.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

