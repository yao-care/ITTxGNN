---
layout: default
title: Benazepril
parent: Prove moderate (L3-L4)
nav_order: 34
evidence_level: L4
indication_count: 5
---

# Benazepril
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

# BENAZEPRIL: dall'Ipertensione all'Ipertensione Renovascolare Maligna

## Riassunto in Una Frase

Benazepril è un inibitore dell'enzima di conversione dell'angiotensina (ACE), consolidato nella pratica clinica per il trattamento dell'ipertensione e dell'insufficienza cardiaca attraverso il blocco della via RAAS.
Il modello TxGNN prevede che possa essere efficace per **l'Ipertensione Renovascolare Maligna** con un punteggio di **99.65%**,
tuttavia **nessuno studio clinico** e **nessuna pubblicazione diretta** specifica per questa combinazione sono attualmente disponibili — e una controindicazione seria ben nota si applica nella stenosi bilaterale dell'arteria renale.

---

## Panoramica Rapida

| Voce | Contenuto |
|------|-----------|
| Indicazione Originale | Ipertensione (nessun record di registrazione formale trovato in Italia) |
| Indicazione Prevista | Ipertensione Renovascolare Maligna |
| Punteggio di Previsione TxGNN | 99.65% |
| Livello di Evidenza | L4 |
| Stato del Mercato Italiano | Non commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | In Sospeso |

---

## Perché Questa Previsione è Ragionevole?

Attualmente, i dati dettagliati del meccanismo di azione non sono disponibili dalla fonte DrugBank consultata. Sulla base della conoscenza farmacologica consolidata, benazepril è un inibitore dell'ACE — inibisce competitivamente l'enzima di conversione dell'angiotensina, bloccando la conversione dell'angiotensina I in angiotensina II. Ciò sopprime la vasocostrizione e la secrezione di aldosterone, determinando la riduzione della pressione arteriosa sistemica e la diminuzione del postcarico cardiaco.

L'ipertensione renovascolare maligna condivide la via RAAS come suo fattore determinante: la stenosi dell'arteria renale scatena l'ipersecrezione di renina, portando alla sovrapproduzione incontrollata di angiotensina II e all'ipertensione grave, resistente al trattamento. Poiché benazepril agisce direttamente sull'effettore centrale di questa cascata, la razionalità meccanicistica è coerente — e spiega perché TxGNN ha assegnato un punteggio di riposizionamento del 99.65%. La malattia e il meccanismo di azione del farmaco puntano verso lo stesso asse biologico.

Tuttavia, questo apparente allineamento meccanicistico è compromesso da un vincolo di sicurezza critico. Nella **stenosi bilaterale dell'arteria renale** — una variante anatomica comune nell'ipertensione renovascolare maligna — gli inibitori dell'ACE rimuovono il tono dell'arteriola efferente mediato dall'angiotensina II che mantiene la pressione di filtrazione glomerulare. La conseguenza è un calo abrupto e grave del GFR e potenzialmente un danno renale acuto (AKI) irreversibile. Questa è una controindicazione seria e ben riconosciuta che limita fondamentalmente l'applicabilità clinica di benazepril in questa indicazione. Non è un rischio teorico; è un pericolo clinico documentato.

---

## Evidenza da Studi Clinici

Attualmente nessuno studio clinico correlato registrato.

---

## Evidenza dalla Letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Considerazioni di Sicurezza

Consultare il foglio illustrativo per le informazioni di sicurezza.

> **Nota per i revisori:** Sebbene i dati formali di sicurezza non potessero essere recuperati da questa esecuzione della pipeline, l'analisi meccanicistica identifica un problema clinicamente critico — gli inibitori dell'ACE sono controindicati nella stenosi bilaterale dell'arteria renale a causa del rischio di danno renale acuto. Questo dovrebbe essere confermato rispetto all'etichettatura completa approvata dall'AIFA prima di qualsiasi ulteriore valutazione.

---

## Conclusioni e Prossimi Passi

**Decisione: In Sospeso**

**Razionale:**
Nonostante il collegamento meccanicistico RAAS teoricamente convincente, non esiste alcuna evidenza da studi clinici o letteratura che supporti specificamente benazepril nell'ipertensione renovascolare maligna, e una controindicazione nota che rappresenta un pericolo per la vita (AKI nella stenosi bilaterale dell'arteria renale) crea un ostacolo critico di sicurezza che non può essere risolto senza ulteriori dati.

**Per procedere, è necessario quanto segue:**

- **Documentazione formale del MOA** — recuperare il record completo di DrugBank (DB00542) per completare l'analisi meccanicistica e consentire il calcolo del punteggio di similarità
- **Completamento del profilo di sicurezza** — ottenere il foglio illustrativo dell'AIFA (Italia) per documentare formalmente le controindicazioni e gli avvertimenti; la controindicazione della stenosi bilaterale dell'arteria renale deve essere esplicitamente valutata
- **Stratificazione per Sottogruppi di Pazienti** — distinguere la stenosi renale unilaterale da quella bilaterale: gli inibitori dell'ACE potrebbero presentare un profilo di beneficio-rischio più gestibile nella stenosi unilaterale, il che richiede un'analisi secondaria separata
- **Revisione della Letteratura sull'Effetto di Classe** — raccogliere evidenze su inibitori dell'ACE correlati (ad es. Ramipril, Enalapril) nell'ipertensione renovascolare maligna; l'evidenza a livello di classe potrebbe indirettamente informare un caso di riposizionamento di benazepril
- **Considerare il Rank 2** — La Malattia Renale Ipertensiva Maligna (stesso punteggio TxGNN, L4, raccomandazione: Domanda di ricerca) potrebbe rappresentare un'opportunità di riposizionamento più trattabile dato il supporto meccanicistico disponibile dallo studio REIN con Ramipril; considerare di porla come la domanda di ricerca primaria

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

