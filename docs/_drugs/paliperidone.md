---
layout: default
title: Paliperidone
parent: Solo previsione del modello (L5)
nav_order: 159
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidone: Dalla schizofrenia alla distrofia retinica con o senza anomalie extraoculari

## Riassunto in una frase

La paliperidone è un antipsicotico di seconda generazione (atipico) — il metabolita attivo della risperidone — con uso globalmente consolidato nella schizofrenia e nel disturbo schizoaffettivo.
La più alta previsione classificata del modello TxGNN è **Distrofia retinica con o senza anomalie extraoculari** (punteggio: **99.92%**),
tuttavia **nessuna sperimentazione clinica** esiste e tutti i 15 articoli recuperati affrontano l'area della malattia oftalmologica in generale piuttosto che l'efficacia della paliperidone, collocando questa al livello di evidenza **L5**.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originale | Schizofrenia / Disturbo schizoaffettivo (globalmente consolidato; non registrato in Italia) |
| Nuova indicazione prevista | Distrofia retinica con o senza anomalie extraoculari |
| Punteggio di previsione TxGNN | 99.92% |
| Livello di evidenza | L5 |
| Stato del mercato in Italia | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Rinviare |

---

## Perché questa previsione è ragionevole?

I dati dettagliati sul meccanismo d'azione non sono disponibili in questo Evidence Pack. Sulla base della farmacologia nota, la paliperidone è un antagonista multi-recettoriale D2/5-HT2A/α1-adrenergico/H1. Modula la neurotrasmissione dopaminergica e serotoninergica centrale, che sottende la sua efficacia consolidata nella schizofrenia e nel disturbo schizoaffettivo. Il suo profilo farmacologico è strettamente correlato alla risperidone, della quale è il metabolita attivo.

La distrofia retinica con o senza anomalie extraoculari è una classe di malattia fondamentalmente diversa — una condizione degenerativa ereditaria in cui le mutazioni in geni come *RPGR* o *CRB1* causano la morte progressiva delle cellule fotorecettoriali e il deterioramento strutturale della retina. Il meccanismo patologico è genetico e strutturale, senza un componente dopaminergico o serotoninergico consolidato che guida la progressione della malattia.

Il razionale meccanicistico per questa previsione di TxGNN non è considerato credibile. Anche se i recettori della dopamina esistono in tracce all'interno del tessuto retinico, non ci sono prove pubblicate che l'antagonismo D2/5-HT2A possa arrestare o invertire la degenerazione geneticamente determinata dei fotorecettori. L'elevato punteggio di previsione molto probabilmente riflette un **falso positivo dell'embedding del grafo** — un artefatto della vicinanza dei nodi di malattia nel grafo della conoscenza piuttosto che una relazione biologica genuina.

---

## Evidenza da studi clinici

Attualmente nessuno studio clinico correlato è registrato.

---

## Evidenza da letteratura

Sono stati recuperati quindici articoli per la ricerca che combina paliperidone e distrofia retinica con o senza anomalie extraoculari. Tuttavia, dopo l'ispezione, **nessuno di questi articoli documenta l'uso di paliperidone in questa indicazione**. Gli articoli affrontano argomenti oftalmologici generali — infezioni orbitali, anomalie congenite della lente e delle palpebre, disturbi della fibrosi del muscolo extraoculare, patologia del disco ottico e sindromi di disinnervazione cranica. Sembra che siano stati recuperati attraverso l'abbinamento di parole chiave sulla malattia "anomalie extraoculari" piuttosto che qualsiasi co-occorrenza farmaco-malattia. Elencarli come evidenza a supporto misrepresentirebbe lo stato effettivo della conoscenza.

Attualmente nessuna letteratura a supporto dell'uso di paliperidone nella distrofia retinica è disponibile.

---

## Informazioni sul mercato italiano

Paliperidone **non ha autorizzazioni all'immissione in commercio in Italia**. Il farmaco non è attualmente registrato o commercializzato in questa giurisdizione. Nessun record di autorizzazione è disponibile per la tabulazione.

---

## Considerazioni sulla sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusioni e prossimi passi

**Decisione: Rinviare**

**Razionale:**
Non esiste un collegamento meccanicistico credibile tra l'antagonismo dei recettori dopaminergici/serotoninergici della paliperidone e la distrofia retinica ereditaria, e zero evidenza clinica e letteraria specifica del farmaco supporta questa indicazione. Questa previsione di TxGNN è coerente con un falso positivo dell'embedding del grafo e non dovrebbe progredire a ulteriore valutazione senza evidenza meccanicistica sostanziale e nuova.

**Per procedere, sono necessari i seguenti elementi:**
- Un'ipotesi meccanicistica sottoposta a revisione paritaria che colleghi la modulazione D2/5-HT2A ai percorsi di sopravvivenza dei fotorecettori o di degenerazione retinica
- Almeno uno studio preclinico (in vitro o modello animale) che dimostri l'attività della paliperidone in un contesto di distrofia retinica
- Recupero dei dati MOA completi da DrugBank (in sospeso al gap di dati DG002) prima di qualsiasi rivalutazione meccanicistica
- Dati del foglio illustrativo AIFA (in sospeso al gap di dati DG001) per consentire lo screening completo della sicurezza prima di qualsiasi valutazione di fattibilità clinica

---

> ### ⚠️ Nota supplementare: Previsione TxGNN più attuabile
>
> Tra tutte le 10 previsioni classificate in questo Evidence Pack, **Grado 10 — Schizofrenia resistente al trattamento** (punteggio TxGNN: **99.80%**) è di gran lunga il risultato più clinicamente significativo e attuabile. Indicatori chiave:
>
> | Elemento | Dettaglio |
> |----------|-----------|
> | Livello di evidenza | **L3** (studi osservazionali + revisioni di esperti) |
> | Studi clinici | 4 identificati (incluso 1 Phase 4 completato) |
> | Letteratura | 2 articoli a supporto |
> | Collegamento meccanicistico | Diretto e ben compreso — l'antagonismo D2/5-HT2A affronta gli squilibri neurotrasmettitoriali centrali della schizofrenia |
> | Fase della decisione | **Domanda di ricerca** — merita ulteriori indagini |
>
> La paliperidone nella schizofrenia resistente al trattamento (TRS) occupa una nicchia clinica definita: come opzione di second-line dopo il fallimento di ≥2 antagonisti D2 standard, prima di o insieme all'escalation della clozapina. Un **rapporto di valutazione dedicato a questa indicazione è consigliato** come output prioritario da questa esecuzione della pipeline.

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

