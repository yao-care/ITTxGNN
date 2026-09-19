---
layout: default
title: Safinamide
parent: Solo previsione del modello (L5)
nav_order: 185
evidence_level: L5
indication_count: 3
---

# Safinamide
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **3** 
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

# Safinamide: dalla malattia di Parkinson all'encefalite sottacuta di Rasmussen

## Riepilogo in una frase

Safinamide (nome commerciale: Xadago) è un inibitore della MAO-B con attività aggiuntiva di blocco dei canali del sodio voltaggio-dipendenti, approvato a livello internazionale come terapia aggiuntiva per la malattia di Parkinson, anche se non ha ricevuto autorizzazione al commercio in Italia.
Il modello TxGNN prevede che potrebbe essere efficace per l'**encefalite sottacuta di Rasmussen**,
tuttavia **nessuna sperimentazione clinica o letteratura pubblicata** attualmente supporta questa direzione — rendendola una predizione solo da modello (L5) al momento.

---

## Panoramica rapida

| Voce | Contenuto |
|------|-----------|
| Indicazione originale | Malattia di Parkinson (approvazione internazionale; nessuna registrazione in Italia) |
| Indicazione nuova predetta | Encefalite sottacuta di Rasmussen |
| Punteggio di predizione TxGNN | 99.63% |
| Livello di evidenza | L5 |
| Stato del mercato italiano | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | In attesa |

---

## Perché questa predizione è ragionevole?

Attualmente, i dati dettagliati del meccanismo d'azione non sono disponibili in questo pacchetto di evidenze. Sulla base delle informazioni a cui si fa riferimento nell'analisi meccanicistica, safinamide agisce attraverso due percorsi complementari: inibizione della MAO-B (riducendo il catabolismo della dopamina e lo stress ossidativo mediato da perossido di idrogeno) e blocco dei canali del sodio voltaggio-dipendenti (sopprimendo il rilascio eccessivo di glutammato). Queste proprietà sono alla base del suo uso approvato nella malattia di Parkinson e costituiscono il fondamento da cui l'algoritmo del grafo di conoscenza TxGNN ha generato questa predizione.

L'encefalite di Rasmussen (RE) è una rara condizione autoimmune inesorabilmente progressiva caratterizzata da distruzione corticale focale mediata da cellule T CD8+ ed epilessia intrattabile, con anticorpi anti-GluR3 come marchio immunologico centrale. La soppressione del rilascio di glutammato di safinamide offre un overlap concettuale ristretto con il fenotipo di iper-eccitabilità della RE, e la sua riduzione guidata dalla MAO-B dello stress ossidativo potrebbe fornire un beneficio neuroprotettivo marginale a livello tissutale. Tuttavia, il meccanismo distruttivo centrale della RE è mediato da meccanismi immunitari e non dipende dall'attività della MAO-B o dalla disregolazione primaria del glutammato.

Nella pratica clinica, la RE è gestita con agenti immunosoppressivi (immunoglobuline endovenose, micofenolato mofetil, rituximab) e il controllo delle crisi è già affrontato da farmaci antiepilettici consolidati; la chirurgia emisferica rimane l'intervento definitivo. Il punteggio TxGNN probabilmente riflette la prossimità del grafo tra i nodi della malattia di Parkinson e della RE nel grafo di conoscenza — un artefatto strutturale — piuttosto che un segnale guidato meccanicisticamente. Il collegamento meccanicistico complessivo è considerato molto debole.

---

## Evidenze da sperimentazioni cliniche

Attualmente nessuna sperimentazione clinica correlata registrata.

---

## Evidenze da letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Considerazioni sulla sicurezza

Si prega di fare riferimento al foglio illustrativo per informazioni sulla sicurezza.

---

## Conclusione e prossimi passi

**Decisione: In attesa**

**Razionale:**
Non esiste alcuna evidenza da sperimentazione clinica o letteratura pubblicata che supporti safinamide nell'encefalite sottacuta di Rasmussen, e la razionale meccanicistica è debole — la RE è una malattia immune-distruttiva che non si affida ai percorsi della MAO-B o del glutammato presi di mira da safinamide; la predizione è attribuibile alla prossimità del vicinato del grafo nel modello TxGNN piuttosto che alla plausibilità biologica.

**Per procedere, è necessario quanto segue:**

- **Dati del meccanismo d'azione**: Query API completa di DrugBank per confermare il profilo farmacologico completo
- **Revisione del foglio illustrativo**: Ottenere avvertenze e controindicazioni dello SmPC TFDA/EMA per consentire l'ingresso nella fase di sicurezza (S1)
- **Evidenze precliniche**: Studi che dimostrino l'attività di safinamide in modelli di encefalite autoimmune mediata da cellule T o modelli di crisi rilevanti per la RE
- **Valutazione del meccanismo immunologico**: Valutare se l'inibizione della MAO-B o il blocco dei canali del sodio modulano significativamente l'asse immunitario CD8+/anti-GluR3 nella RE
- **Analisi comparativa**: Benchmarking rispetto allo standard di cura attuale della RE (rituximab, MMF) per valutare se un beneficio aggiuntivo è plausibile

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

