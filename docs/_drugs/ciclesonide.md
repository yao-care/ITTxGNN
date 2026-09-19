---
layout: default
title: Ciclesonide
parent: Solo previsione del modello (L5)
nav_order: 51
evidence_level: L5
indication_count: 6
---

# Ciclesonide
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **6** 
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

# Ciclesonide: Dall'asma all'eczema atopico

## Riassunto in una frase

Ciclesonide è un corticosteroide inalatorio (ICS) approvato per l'asma, agisce come agonista del recettore dei glucocorticoidi (GR) che sopprime l'infiammazione delle vie aeree tramite l'attivazione enzimatica polmonare nel suo metabolita attivo, des-ciclesonide.
Il modello TxGNN prevede che potrebbe essere efficace per l'**eczema atopico**, ma attualmente con **nessun trial clinico** e **nessuna letteratura pubblicata** che supporti questa specifica direzione.
Esiste una barriera critica: ciclesonide è un profarmaco polmonare senza alcuna formulazione topica dermatologica, rendendo la compatibilità della via di somministrazione una sfida fondamentale non ancora risolta per le indicazioni cutanee.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originaria | Asma (corticosteroide inalatorio) |
| Indicazione nuova prevista | Eczema atopico |
| Punteggio di previsione TxGNN | 99.96% |
| Livello di evidenza | L5 |
| Stato del mercato di Taiwan | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Sospendere |

---

## Perché questa previsione è ragionevole?

Ciclesonide è un agonista del recettore dei glucocorticoidi (GR) progettato specificamente come profarmaco inalatorio. Dopo l'inalazione, le esterasi polmonari lo convertono nel suo metabolita attivo, des-ciclesonide, che inibisce l'attivazione di NF-κB nelle cellule epiteliali delle vie aeree e sopprime le citochine pro-infiammatorie incluse IL-6, IL-8 e TNF-α. Questo meccanismo di attivazione polmonare altamente mirato è una caratteristica di design deliberata destinata a ridurre gli effetti collaterali sistemici dei corticosteroidi.

L'eczema atopico è guidato principalmente dalla disregolazione immunitaria mediata da Th2, caratterizzata dall'iperattivazione dei percorsi IL-4, IL-13 e IgE che portano a disfunzione della barriera cutanea cronica e infiammazione. A livello di classe, gli agonisti GR sono centrali nella gestione dell'eczema atopico — i corticosteroidi topici rimangono uno standard di prima linea di cura. Il modello TxGNN probabilmente cattura questo ampio sovrapposizione meccanicistica della classe corticosteroidi, che spiega l'alto punteggio di previsione.

Tuttavia, esiste una **barriera fondamentale di compatibilità della via di somministrazione**: ciclesonide è farmacologicamente progettato per essere attivato da esterasi specifiche dei polmoni, non da enzimi cutanei. Attualmente non esiste alcuna formulazione topica o transdermale di ciclesonide, e non è chiaro se le esterasi cutanee possono convertire sufficientemente ciclesonide in des-ciclesonide a concentrazioni terapeuticamente rilevanti. Senza una via di somministrazione praticabile, la logica meccanicistica non può tradursi in applicazione clinica senza uno sviluppo farmaceutico significativo. Il punteggio TxGNN 99.96% dovrebbe quindi essere interpretato come riflettente **plausibilità a livello di classe**, non evidenza specifica di ciclesonide.

---

## Prove da trial clinici

Attualmente nessun trial clinico correlato registrato.

---

## Prove dalla letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Informazioni sul mercato di Taiwan

Ciclesonide non ha alcuna licenza di farmaco approvato registrata a Taiwan (0 autorizzazioni). Nessuna tabella di autorizzazione è disponibile.

---

## Considerazioni sulla sicurezza

Consultare il foglio illustrativo per informazioni sulla sicurezza.

---

## Conclusione e fasi successive

**Decisione: Sospendere**

**Logica:**
Nonostante un alto punteggio di previsione TxGNN (99.96%), l'evidenza per ciclesonide nell'eczema atopico è L5 (solo previsione del modello) con zero trial clinici di supporto o letteratura, e — più criticamente — la farmacologia del profarmaco di ciclesonide pone una barriera fondamentale di compatibilità della via di somministrazione che non può essere risolta senza lo sviluppo di una nuova formulazione.

**Per procedere, è necessario quanto segue:**

- **Studio di fattibilità della formulazione**: determinare se una formulazione topica o transdermale di ciclesonide può fornire des-ciclesonide terapeuticamente attivo alla pelle (richiede investimento in R&D farmaceutica prima di qualsiasi fase clinica)
- **Valutazione dell'esterasi cutanea**: caratterizzare se le esterasi cutanee umane possono attivare ciclesonide in des-ciclesonide a concentrazioni tissutali rilevanti — questo singolo punto dati cambierebbe drasticamente la plausibilità delle indicazioni cutanee
- **Prova di concetto preclinica**: modelli di cheratinociti in vitro e modelli murini di dermatite atopica in vivo utilizzando ciclesonide per stabilire un segnale di efficacia di base prima di qualsiasi studio umano
- **Conferma dei dati di MOA**: ottenere dati meccanismo completo di DrugBank per rafforzare la documentazione della logica meccanicistica

> **Nota strategica — considerare di riprioritizzare a Bronchite (Rank 4):** tra tutte e sei le indicazioni previste, bronchite/BPCO presenta la questione di ricerca più immediatamente attuabile. Ciclesonide è già un ICS con azione anti-infiammatoria delle vie aeree consolidata; le linee guida GOLD supportano l'uso di ICS in BPCO; e le linee guida finlandesi per il trattamento della BPCO ([PMID 25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/)) citano la farmacoterapia ICS in questo contesto. Non è necessario alcuno sviluppo di nuova formulazione, e la via di somministrazione è identica all'indicazione approvata.

> **Avvertenza — Dermatite da contatto (Rank 5) contiene contro-evidenza:** l'unica letteratura disponibile per questa indicazione ([PMID 22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/)) è un rapporto di caso che documenta ciclesonide come **allergene reattivo incrociato** nella dermatite allergica sistemica causata dal budesonide inalato — non come agente terapeutico. Questa indicazione non dovrebbe essere perseguita.

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

