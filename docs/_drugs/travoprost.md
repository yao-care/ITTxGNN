---
layout: default
title: Travoprost
parent: Solo previsione del modello (L5)
nav_order: 205
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: Dal glaucoma ad angolo aperto alla calcifiassi viscerale

## Riassunto in una frase

Travoprost è un analogo sintetico della prostaglandina F2α (agonista del recettore FP) somministrato come soluzione oftalmologica, utilizzato principalmente per ridurre la pressione intraoculare in pazienti con glaucoma ad angolo aperto e ipertensione oculare.
Il modello TxGNN prevede che potrebbe essere efficace per **calcifiassi viscerale** con un punteggio di confidenza del modello quasi perfetto,
tuttavia attualmente non ci sono **0 trial clinici** e **0 pubblicazioni** che affrontano specificamente questa indicazione — rendendo questa una previsione puramente guidata dal modello senza supporto empirico.

---

## Panoramica rapida

| Voce | Contenuto |
|------|---------|
| Indicazione originale | Glaucoma ad angolo aperto / Ipertensione oculare (desunto da evidenze cliniche; nessuna registrazione in Italia) |
| Indicazione nuova prevista | Calcifiassi viscerale |
| Punteggio di previsione TxGNN | 99.9998% |
| Livello di evidenza | L5 |
| Stato del mercato italiano | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Sospensione |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili in questo fascicolo probatorio. Sulla base delle conoscenze farmacologiche consolidate, travoprost è un agonista selettivo del recettore prostanoide FP. La sua efficacia comprovata nel glaucoma deriva dal miglioramento del deflusso dell'umor acqueo attraverso la via uveosclerale tramite il rilassamento della muscolatura liscia ciliare — un effetto mediato dalla stimolazione del recettore PGF2α. Questo meccanismo è ben documentato nei 15 trial clinici recuperati in questo fascicolo probatorio, tutti i quali confermano il ruolo di travoprost come agente ipotonizzante oculare.

La calcifiassi viscerale è una sindrome rara e pericolosa per la vita vista predominantemente in pazienti con malattia renale in stadio terminale, caratterizzata da calcificazione progressiva e trombosi dei piccoli vasi sanguigni dermici e sottocutanei che portano a necrosi ischemica. Il collegamento meccanicistico teorico proposto da TxGNN si basa su due pilastri: (1) le prostaglandine generalmente possiedono proprietà vasodilatatorie che potrebbero teoricamente migliorare la perfusione microvascolare nel tessuto ischemico, e (2) PGF2α è stato dimostrato modulare il comportamento delle cellule della muscolatura liscia vascolare. Uno studio clinico nel fascicolo probatorio (NCT00308945) ha misurato direttamente l'effetto di travoprost sul diametro vascolare retinico e sul flusso sanguigno coroideale in pazienti glaucomatosi, confermando che il farmaco esercita effetti vascolari misurabili — almeno a livello oculare.

Tuttavia, il salto dalla vasodilatazione oculare al trattamento sistemico della calcifiassi viscerale rimane speculativo e meccanicisticamente debole. La fisiopatologia della calcifiassi è dominata dalla deposizione calcio-fosfato, citochine pro-infiammatorie e disregolazione della coagulazione — nessuna delle quali è un bersaglio noto della via del recettore FP. Inoltre, travoprost esiste solo come formulazione oftalmologica topica; la biodisponibilità sistemica è trascurabile. L'altissimo punteggio TxGNN molto probabilmente riflette la prossimità a livello di grafo all'interno della rete di nodi delle malattie vascolari piuttosto che un collegamento biologico convalidato specifico per la calcifiassi.

---

## Evidenza da trial clinici

Attualmente nessun trial clinico correlato registrato.

---

## Evidenza della letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Considerazioni di sicurezza

Si prega di fare riferimento al foglio illustrativo per informazioni sulla sicurezza.

---

## Conclusioni e prossimi passi

**Decisione: Sospensione**

**Razionale:**
Questa previsione è interamente guidata dal modello (L5) con zero trial clinici, studi osservazionali o letteratura preclinica a supporto dell'uso di travoprost nella calcifiassi viscerale; il collegamento meccanicistico tra l'agonismo del recettore FP e la patobiologia della calcifiassi è altamente speculativo, e attualmente non esiste una via di somministrazione sistemica praticabile.

**Per procedere, è necessario quanto segue:**
- **Evidenza preclinica**: Studi in vitro o su animali che esaminano l'espressione e la funzione del recettore FP nella vasculatura calcificata o nei modelli di calcifiassi stabiliti
- **Dati MOA**: Recupero del meccanismo d'azione completo da DrugBank (DG002) per valutare qualsiasi attività bersaglio secondaria rilevante per la calcificazione vascolare
- **Dati di sicurezza**: Scaricamento e analisi del foglio illustrativo (DG001) per valutare l'assorbimento sistemico, gli avvertimenti cardiovascolari e le controindicazioni prima di qualsiasi discussione sulla riproposizione terapeutica
- **Fattibilità della formulazione**: Valutazione se una formulazione sistemica (endovenosa o sottocutanea) di travoprost potrebbe essere sviluppata a dosi farmacologicamente attive, dato che la via oftalmologica attuale fornisce un'esposizione sistemica trascurabile
- **Diagnosi differenziale del segnale TxGNN**: Valutare se l'altissimo punteggio riflette la vera biologia della calcifiassi o è un artefatto della prossimità del grafo delle conoscenze al raggruppamento più ampio delle malattie vascolari (i ranghi 2–9 predicono tutti sottocondizioni vascolari con punteggi simili, suggerendo un effetto di grafo a livello di classe)

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

