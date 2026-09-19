---
layout: default
title: Simoctocog Alfa
parent: Solo previsione del modello (L5)
nav_order: 186
evidence_level: L5
indication_count: 10
---

# Simoctocog Alfa
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

# Simoctocog Alfa: Dall'Emofilia A alla Pseudo-Malattia di von Willebrand

## Riassunto in Una Frase

Simoctocog alfa (Nuwiq) è un prodotto ricombinante umano di Fattore VIII di 4ª generazione (rFVIII), approvato per la prevenzione e il trattamento degli episodi emorragici nei pazienti con Emofilia A.
Il modello TxGNN prevede che possa essere efficace nella **pseudo-malattia di von Willebrand**,
tuttavia attualmente vi sono **0 studi clinici** e **0 pubblicazioni** che supportano direttamente questa applicazione — rendendo questa una previsione basata esclusivamente su modello con razionale meccanicistico debole.

---

## Panoramica Rapida

| Voce | Contenuto |
|------|-----------|
| Indicazione Originaria | Emofilia A (prevenzione e trattamento degli episodi emorragici) |
| Indicazione Nuova Prevista | Pseudo-Malattia di von Willebrand |
| Punteggio di Previsione TxGNN | 99.997% |
| Livello di Evidenza | L5 |
| Stato del Mercato Italiano | ✗ Non Commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | In sospeso |

---

## Perché Questa Previsione è Ragionevole?

Simoctocog alfa è un prodotto ricombinante umano di Fattore VIII di 4ª generazione con dominio B eliminato. Nella via della coagulazione intrinseca, il FVIII funge da cofattore per il Fattore IXa nel complesso della Tenasi, che attiva il Fattore X e infine guida la generazione della trombina. Nel flusso sanguigno, il FVIII circola legato al Fattore di von Willebrand (vWF), che funge da proteina portatrice e lo protegge dalla degradazione proteolitica prematura. La sostituzione del FVIII deficiente è la pietra angolare della gestione dell'Emofilia A, e simoctocog alfa svolge questa funzione ripristinando direttamente la cascata della coagulazione intrinseca.

La pseudo-malattia di von Willebrand (vWD di tipo piastrinico) è un disturbo distinto causato da una mutazione gain-of-function nel GPIbα piastrinico, che porta al legame spontaneo delle piastrine al vWF e al consumo dei multimeri del vWF ad alto peso molecolare. Poiché il vWF è il portatore del FVIII, una riduzione secondaria del FVIII è teoricamente possibile nei casi gravi — e questo collegamento strutturale vWF–FVIII è probabilmente il motivo per cui TxGNN posiziona simoctocog alfa vicino alla pseudo-vWD nel grafo della conoscenza. Tuttavia, l'obiettivo di trattamento primario per la pseudo-vWD è la **sostituzione del vWF** (utilizzando concentrati contenenti vWF) o DDAVP a bassa dose, non l'integrazione isolata del FVIII. Il collegamento meccanicistico è indiretto e clinicamente fragile.

È importante notare che tutte le 10 indicazioni previste da TxGNN per questo farmaco sono disturbi emorragici o piastrinici — che vanno dalla trombastenia di Glanzmann alla porpora trombotica trombocitopenica — nessuna delle quali ha prove di supporto. Questo modello suggerisce fortemente una **distorsione topologica del grafo della conoscenza**: TxGNN sta raggruppando simoctocog alfa con nodi di disturbi emorragici vicini in base alla prossimità malattia-malattia, piuttosto che identificare una vera relazione farmacologica. I punteggi di previsione alti da soli non indicano validità clinica quando il razionale meccanicistico è assente o contraddetto dalla letteratura esistente.

---

## Evidenza da Studi Clinici

Attualmente non ci sono studi clinici correlati registrati.

---

## Evidenza dalla Letteratura

Attualmente non è disponibile letteratura correlata.

---

## Considerazioni di Sicurezza

Si prega di consultare il foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusione e Prossimi Passi

**Decisione: In sospeso**

**Razionale:**
Tutte le 10 indicazioni previste da TxGNN hanno un livello di evidenza L5 (previsione basata solo su modello), con zero studi clinici di supporto o pubblicazioni identificate per qualsiasi indicazione. La previsione principale — pseudo-malattia di von Willebrand — ha un collegamento meccanicistico così debole che il trattamento con il FVIII isolato potrebbe essere considerato off-target; l'intervento corretto per la pseudo-vWD è la sostituzione con prodotto contenente vWF. I punteggi elevati di TxGNN in tutto un cluster di disturbi emorragici sono coerenti con un artefatto topologico del grafo della conoscenza piuttosto che con un segnale di repurposing utilizzabile.

**Per procedere, è necessario quanto segue:**

- **Dati di sicurezza**: Ottenere il foglio illustrativo completo (TFDA o EMA/AIFA) per completare la valutazione avvertenze e controindicazioni — attualmente una lacuna critica nei dati
- **Verifica dello stato del mercato italiano/EMA**: Simoctocog alfa (Nuwiq) detiene l'approvazione EMA per l'Emofilia A; re-interrogare i registri di registrazione AIFA poiché lo stato attuale "Non Commercializzato" potrebbe essere incompleto
- **Approfondimento meccanicistico**: Condurre una revisione mirata della letteratura sull'uso di rFVIII negli stati di deficienza di FVIII secondaria (ad es. pseudo-vWD, sindrome da acquisizione vWF) per determinare se esista qualche evidenza a livello di caso
- **Revisione da esperti**: Consultare un ematologo specializzato in disturbi emorragici rari prima di avanzare una qualsiasi delle 10 indicazioni previste oltre lo stato L5
- **Investigazione distorsione KG**: Valutare se il cluster di disturbi emorragici nel grafo della conoscenza TxGNN richieda correzioni a livello topologico per ridurre i falsi positivi per i farmaci della classe FVIII

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

