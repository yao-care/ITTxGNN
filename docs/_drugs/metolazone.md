---
layout: default
title: Metolazone
parent: Solo previsione del modello (L5)
nav_order: 146
evidence_level: L5
indication_count: 5
---

# Metolazone
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **5** 
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

# Metolazone: dall'Ipertensione e dall'Edema alla Malattia Renale Ipertensiva Maligna

## Sintesi di una Frase

Metolazone è un diuretico simil-tiazidico tradizionalmente utilizzato per gestire l'ipertensione e l'edema, incluso il sovraccarico di volume resistente ai diuretici in combinazione con diuretici dell'ansa. Il modello TxGNN predice che potrebbe avere un ruolo nella **Malattia Renale Ipertensiva Maligna**, tuttavia attualmente non ci sono **0 studi clinici** e **0 pubblicazioni specifiche della malattia** che supportino questa direzione — la previsione si basa interamente sulla modellazione del grafo conoscitivo.

---

## Panoramica Rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione Originale | Ipertensione e edema (diuretico simil-tiazidico per classe farmacologica; nessun record di autorizzazione italiana disponibile) |
| Indicazione Nuova Prevista | Malattia Renale Ipertensiva Maligna |
| Punteggio di Previsione TxGNN | 99.84% |
| Livello di Prova | L5 |
| Stato del Mercato Italiano | ✗ Non Commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | In attesa |

---

## Perché Questa Previsione è Ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili dal dossier normativo. In base alla classificazione farmacologica nota, Metolazone appartiene alla classe dei diuretici chinazolina solfonamide (simil-tiazidici). Inibisce il riassorbimento di sodio nel tubulo contorto distale, riducendo il volume intravascolare e conseguentemente abbassando la pressione arteriosa sistemica. In particolare, Metolazone mantiene l'attività diuretica a livelli di GFR inferiori rispetto ai tiazidi convenzionali, il che spiega il suo frequente uso off-label nei pazienti con compromissione renale moderata insieme ai diuretici dell'ansa.

La malattia renale ipertensiva maligna (ipertensione in fase accelerata con danno renale acuto) è caratterizzata da pressione arteriosa gravemente elevata che causa ischemia glomerulare progressiva e necrosi fibrinoide arteriolosa. In questo contesto, un agente che riduce il volume e abbassa la pressione arteriosa potrebbe teoricamente alleviare lo stress emodinamico sul glomerulo. Questa costituisce la razionale meccanicistica indiretta che il grafo conoscitivo TxGNN probabilmente ha catturato: il nodo antiipertensivo di Metolazone è ben collegato ai nodi di malattia renale correlata all'ipertensione nel grafo.

Tuttavia, la plausibilità meccanicistica è bassa o moderata nella pratica. L'ipertensione maligna richiede una riduzione della pressione arteriosa rapida e controllata ed è principalmente gestita con inibitori del RAAS, bloccanti dei canali del calcio o agenti endovenosi come terapia di prima linea. I diuretici simil-tiazidici non sono considerati standard di cura per questo fenotipo acuto e ad alta gravità, e la loro efficacia diminuisce sostanzialmente quando la GFR cala significativamente — un reperto comune proprio nella nefrosclerosi ipertensiva maligna. L'alto punteggio TxGNN quindi molto probabilmente riflette la connettività ampia della topologia del grafo piuttosto che un meccanismo mirato di modifica della malattia.

---

## Evidenza da Studi Clinici

Attualmente non ci sono studi clinici correlati registrati.

---

## Evidenza dalla Letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Considerazioni di Sicurezza

Consultare il foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusioni e Prossimi Passi

**Decisione: In attesa**

**Razionale:**
Sebbene TxGNN assegni un punteggio numerico elevato (99.84%), non c'è alcuna prova clinica o letteraria specifica della malattia, il collegamento meccanicistico è indiretto e in parte contraddetto dalla fisiopatologia dell'ipertensione maligna, e non esiste autorizzazione commerciale italiana. Questa previsione non soddisfa la soglia minima per avanzare oltre la fase di output del modello.

**Per procedere, è necessario:**
- Recuperare e analizzare il foglio illustrativo completo (SmPC/仿單) per ottenere il meccanismo d'azione confermato, avvisi in riquadri, controindicazioni e restrizioni per popolazioni speciali
- Condurre una ricerca mirata della letteratura per determinare se dati osservazionali, retrospettivi o di serie di casi supportano specificamente i diuretici simil-tiazidici nell'ipertensione maligna con coinvolgimento renale
- Chiarire la soglia di GFR al di sotto della quale l'efficacia antiipertensiva e diuretica di Metolazone diventa clinicamente insufficiente
- Valutare se il segnale TxGNN è un artefatto della prossimità del grafo tra i nodi "antiipertensivo" e "malattia renale ipertensiva", o riflette un genuino divario di esigenza insoddisfatta
- Se il recupero di evidenze produce ≥1 studio di supporto, riclassificare come L4 e ripetere la valutazione decisionale

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

