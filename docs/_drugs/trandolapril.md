---
layout: default
title: Trandolapril
parent: Solo previsione del modello (L5)
nav_order: 204
evidence_level: L5
indication_count: 6
---

# Trandolapril
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

# Trandolapril: Dall'ipertensione all'ipertensione renovascolare maligna

## Riassunto in una frase

Trandolapril è un inibitore dell'ACE (enzima di conversione dell'angiotensina) consolidato per il trattamento dell'ipertensione e della disfunzione ventricolare sinistra in seguito a infarto del miocardio. Il modello TxGNN predice che potrebbe essere efficace per l'**ipertensione renovascolare maligna**, con **0 studi clinici** e **0 pubblicazioni** che supportano direttamente questa direzione. Criticamente, il meccanismo d'azione del farmaco pone un paradosso di sicurezza fondamentale per questa indicazione — gli inibitori dell'ACE sono controindicati nella stenosi bilaterale dell'arteria renale, l'eziologia più comune dell'ipertensione renovascolare, rendendo inappropriato l'avanzamento clinico immediato senza un ulteriore profilo di sicurezza.

---

## Panoramica rapida

| Voce | Contenuto |
|------|-----------|
| Indicazione originale | Ipertensione e disfunzione ventricolare sinistra post-IM (nessun record di autorizzazione in Italia in questo dataset) |
| Indicazione prevista | Ipertensione renovascolare maligna |
| Punteggio predittivo di TxGNN | 99.92% |
| Livello di evidenza | L5 |
| Stato del mercato italiano | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Mantenere in sospeso |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili in questo Evidence Pack. Basandosi sulla farmacologia consolidata, trandolapril appartiene alla classe degli inibitori dell'ACE — agisce bloccando l'enzima che converte l'angiotensina I in angiotensina II, riducendo così la vasocostrizione, diminuendo la secrezione di aldosterone e abbassando sia la resistenza vascolare sistemica che la pressione arteriosa. Queste proprietà sostengono la sua efficacia provata nell'ipertensione essenziale e nel rimodellamento cardiaco post-IM.

La logica biologica che connette trandolapril all'**ipertensione renovascolare maligna** passa direttamente attraverso il sistema renina-angiotensina-aldosterone (RAAS). Nella malattia renovascolare, la stenosi dell'arteria renale induce il rilascio eccessivo di renina, guidando la vasocostrizione mediata dall'angiotensina II e un'ipertensione grave, spesso refrattaria. L'inibizione dell'ACE può, in linea di principio, interrompere questa cascata patologica alla fonte — il che spiega perché il modello della rete della knowledge-graph di TxGNN assegna un punteggio predittivo estremamente elevato (99.92%).

Tuttavia, lo stesso meccanismo crea un paradosso clinico critico. Nella stenosi **bilaterale** dell'arteria renale — la causa più comune di ipertensione renovascolare — la pressione di filtrazione glomerulare è mantenuta quasi interamente dalla vasocostrizione dell'arteriola efferente mediata dall'angiotensina II. Rimuovere questo supporto compensatorio con un inibitore dell'ACE rischia una perdita precipitosa della perfusione renale e insufficienza renale acuta. Questa è una controindicazione clinica ben riconosciuta. L'alto punteggio di TxGNN probabilmente riflette la prossimità a livello di rete tra la modulazione del RAAS e la patologia renovascolare, ma il modello non codifica questa controindicazione. Qualsiasi esplorazione clinica di questa previsione deve essere ristretta a una sottopopolazione attentamente definita — ad esempio, RAS unilaterale con un rene controlaterale confermato normale — e richiede una revisione obbligatoria della nefrologia prima di procedere.

---

## Evidenza da studi clinici

Attualmente nessuno studio clinico correlato registrato per trandolapril nell'ipertensione renovascolare maligna.

---

## Evidenza dalla letteratura

Attualmente nessuna letteratura correlata disponibile per trandolapril nell'ipertensione renovascolare maligna.

---

## Informazioni sul mercato italiano

Trandolapril attualmente non detiene **nessuna autorizzazione al commercio** in Italia. Nessun prodotto autorizzato o indicazione approvata è registrato in questo dataset.

> **Nota:** Il log di interrogazione conferma che è stata eseguita una ricerca di successo nel database AIFA (2026-03-29) con zero risultati. Trandolapril è disponibile con marchi come Gopten in altri mercati europei; l'assenza di autorizzazione italiana dovrebbe essere verificata indipendentemente attraverso il registro AIFA ufficiale prima di trarre conclusioni normative.

---

## Considerazioni di sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni di sicurezza.

> **Avvertimento meccanicistico importante:** Anche se i record formali di sicurezza non sono stati recuperabili per questo dataset, l'analisi della logica di riproposto identifica una preoccupazione clinicamente significativa indipendente dal foglio illustrativo: gli inibitori dell'ACE come classe — incluso trandolapril — possono precipitare insufficienza renale acuta in pazienti con stenosi bilaterale dell'arteria renale o stenosi di un rene funzionante solitario. Poiché questa anatomia è il fattore determinante predominante dell'ipertensione renovascolare, qualsiasi decisione di prescrizione in questa indicazione richiede una precedente imaging vascolare renale e una valutazione specialistica.

---

## Conclusione e prossimi step

**Decisione: Mantenere in sospeso**

**Logica:**
La previsione di primo livello (ipertensione renovascolare maligna, 99.92%) porta zero studi clinici di supporto e zero letteratura pubblicata, e l'analisi meccanicistica rivela una probabile controindicazione nella presentazione clinica più comune della malattia — non un'opportunità di riproposto. Procedere alla valutazione clinica senza prima risolvere questo paradosso di sicurezza e definire una sottopopolazione sicura di pazienti sarebbe inappropriato.

**Per procedere, è necessario quanto segue:**

- **Recuperare il foglio illustrativo completo (SmPC) EMA/AIFA** per trandolapril al fine di documentare formalmente controindicazioni, avvertimenti e requisiti di monitoraggio renale
- **Definire la sottopopolazione di pazienti idonei:** RAS unilaterale con funzione renale controlaterale confermata normale, dove l'inibizione dell'ACE è meccanicamente più sicura
- **Ampliare la ricerca letteraria** dalle query specifiche di trandolapril agli inibitori dell'ACE come classe nell'ipertensione renovascolare, per stabilire la base di evidenza esistente
- **Valutare indicazioni alternative previste** con profili beneficio-rischio più favorevoli come potenziali priorità di sviluppo precedenti:
  - **Malattia cardiaca polmonare cronica** (Rank 6, Livello di evidenza L4) — supportata da uno studio animale ([PMID 8989645](https://pubmed.ncbi.nlm.nih.gov/8989645/)) che mostra come il trattamento prolungato con trandolapril attenua la vasocostrizione aumentata in ratti con insufficienza cardiaca cronica; la logica meccanicistica attraverso il rimodellamento del ventricolo destro mediato dal RAAS è plausibile
  - **Ipertensione polmonare dovuta a malattia polmonare/ipossia** (Rank 4, Livello di evidenza L5) — l'ipertensione polmonare di Gruppo 3 presenta preoccupazioni di pressione arteriosa sistemica inferiori rispetto al Gruppo 1 PAH, rendendo l'inibizione dell'ACE meccanicamente più sicura da esplorare; l'angiotensina II elevata in condizioni di ipossia fornisce un punto di ingresso biologico
- **Confermare lo stato del mercato italiano** tramite ricerca diretta nel registro AIFA, poiché la disponibilità commerciale nei mercati dell'UE vicini (ad es. Gopten in Germania/Regno Unito) potrebbe influenzare la pianificazione del percorso normativo

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

