---
layout: default
title: Balsalazide
parent: Solo previsione del modello (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Balsalazide
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

# Balsalazide: Dalla colite ulcerosa alla gotta

## Riepilogo in una frase

Balsalazide è un profarmaco dell'acido 5-aminosalicilico (5-ASA), progettato per rilasciare l'agente antinfiammatorio attivo direttamente sulla mucosa colonica nel trattamento della **colite ulcerosa**.
Il modello TxGNN prevede che potrebbe essere efficace nella **gotta**, con **0 studi clinici** e **0 pubblicazioni** che attualmente supportano questa direzione.
Le evidenze si limitano esclusivamente alla previsione del modello, rappresentando il livello di fiducia più basso (Livello 5).

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originale | Colite ulcerosa |
| Nuova indicazione prevista | Gotta |
| Punteggio di previsione TxGNN | 99.75% |
| Livello di evidenza | L5 — Previsione del modello solo; nessuno studio clinico o preclinico di supporto |
| Stato del mercato italiano | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Tenere in sospeso |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati del meccanismo d'azione non sono disponibili dalle nostre fonti di dati. In base alla farmacologia consolidata, Balsalazide è un profarmaco mirato al colon: dopo somministrazione orale, i batteri intestinali scindono il legame azo per rilasciare 5-ASA ad alte concentrazioni locali nel colon distale. 5-ASA esercita i suoi effetti antinfiammatori principalmente attraverso l'inibizione di NF-κB, la soppressione della sintesi delle prostaglandine e lo scavenging delle specie reattive dell'ossigeno — tutti agendo localmente all'interno della mucosa colonica per controllare la colite ulcerosa.

La gotta, tuttavia, è guidata da un meccanismo fondamentalmente diverso. La deposizione di cristalli di urato monosodico negli spazi articolari attiva l'infiammosoma NLRP3, portando alla scissione mediata da caspasi-1 e al rilascio di IL-1β — una cascata di citochine che orchestra l'artrite gottosa acuta. Mentre 5-ASA possiede proprietà antinfiammatorie ampie, non ci sono prove pubblicate che inibisca direttamente l'assemblaggio di NLRP3 o la maturazione di IL-1β, che sono i fattori trainanti della patologia gottosa.

Una barriera farmacocinetica critica sottomine inoltre questa previsione. Balsalazide è intenzionalmente progettato per l'assorbimento sistemico minimo: le concentrazioni plasmatiche di 5-ASA sono molto basse dopo la somministrazione orale, il che è clinicamente desiderabile per le IBD ma significa che livelli di farmaco terapeuticamente significativi difficilmente saranno raggiunti nelle cavità articolari periferiche. La combinazione di una mancanza di corrispondenza meccanicistica e di una biodisponibilità sistemica inadeguata rende questa direzione di riposizionamento biologicamente implausibile con la formulazione attuale. Questa previsione probabilmente riflette il rumore strutturale nella rete di conoscenza sottostante il modello TxGNN.

---

## Evidenza da studi clinici

Attualmente nessuno studio clinico correlato è registrato.

---

## Evidenza dalla letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Informazioni sul mercato italiano

Balsalazide **non è attualmente commercializzato in Italia**. Nessuna autorizzazione di prodotto è stata identificata nel database normativo. Qualsiasi futuro programma di riposizionamento rivolto al mercato italiano richiederebbe una domanda di autorizzazione all'immissione in commercio completa fin dall'inizio.

---

## Considerazioni sulla sicurezza

Si rimanda al foglio illustrativo per le informazioni sulla sicurezza.

> **Nota:** I dati del foglio illustrativo (avvertenze, controindicazioni) per questo medicinale non hanno potuto essere recuperati durante l'attuale ciclo di raccolta delle evidenze e sono contrassegnati come una lacuna critica nei dati (DG001). Queste informazioni sono necessarie prima di qualsiasi valutazione in fase clinica.

---

## Conclusione e prossimi passi

**Decisione: Tenere in sospeso**

**Razionale:**
Il modello TxGNN assegna un punteggio di previsione elevato (99.75%), ma questa fiducia numerica non è supportata da studi clinici, letteratura pubblicata o evidenza meccanicistica. La farmacocinetica mirata al colon di Balsalazide e la patologia della gotta incentrata su NLRP3/IL-1β rappresentano una mancanza di corrispondenza fondamentale che non può essere colmata senza una significativa rielaborazione della formulazione. Inoltre, il medicinale non è attualmente autorizzato in Italia, il che significa che il percorso normativo dovrebbe anche iniziare da zero.

**Per procedere, è necessario quanto segue:**

- **Verifica MOA:** Recuperare i dati meccanicistici completi di DrugBank (DG002) per confermare o confutare qualsiasi attività di 5-ASA sui percorsi NLRP3, IL-1β o trasporto dell'acido urico
- **Dossier di sicurezza:** Scaricare e analizzare il foglio illustrativo ufficiale (DG001 — attualmente bloccante) per stabilire controindicazioni e avvertenze chiave
- **Ricerca bibliografica di collegamento:** Condurre una ricerca mirata su PubMed per mesalazina/5-ASA + gotta o iperuricemia per identificare qualsiasi evidenza di supporto indiretta
- **Modellazione PK:** Valutare se formulazioni a rilascio modificato o 5-ASA sistemico potrebbero raggiungere concentrazioni articolari terapeutiche, come prerequisito per qualsiasi ulteriore generazione di ipotesi
- **Considerare previsioni alternative:** I ranghi 3 (Spondilite anchilosante), 4 (Artrite reumatoide), 7 (Spondiolopatia infiammatoria) e 10 (Malattia dell'ano) offrono razionali meccanicistici più forti attraverso l'analogia NF-κB/sulfasalazina o la sovrapposizione della distribuzione colonica, e possono essere vie più produttive per la valutazione della fase successiva

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

