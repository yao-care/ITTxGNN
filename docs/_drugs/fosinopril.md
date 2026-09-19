---
layout: default
title: Fosinopril
parent: Solo previsione del modello (L5)
nav_order: 112
evidence_level: L5
indication_count: 5
---

# Fosinopril
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

# Fosinopril: Dall'ipertensione all'ipertensione renovascolare maligna

## Riassunto in una frase

Fosinopril è un inibitore dell'ACE (inibitore dell'enzima di conversione dell'angiotensina) classicamente utilizzato nella gestione dell'ipertensione e dell'insufficienza cardiaca. Il modello TxGNN prevede che potrebbe essere efficace per l'**Ipertensione Renovascolare Maligna**, senza **alcuna sperimentazione clinica** e **alcuna pubblicazione di supporto diretto** attualmente trovata per questa specifica indicazione. L'intera base di prove si situa al livello L5 — solo previsione del modello — e una preoccupazione di sicurezza critica per questo meccanismo nella malattia renovascolare giustifica una decisione di Rinvio.

---

## Panoramica rapida

| Elemento | Contenuto |
|------|---------|
| Indicazione Originale | Ipertensione / Insufficienza cardiaca (classe inibitore dell'ACE; nessun record regolatorio italiano in archivio) |
| Indicazione Nuova Prevista | Ipertensione Renovascolare Maligna |
| Punteggio di Previsione TxGNN | 99.87% |
| Livello di Evidenza | L5 |
| Stato di Commercializzazione Italia | ✗ Non commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | Rinvio |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili in questo dataset. Basandoci sulla farmacologia nota, fosinopril è un inibitore dell'ACE di classe acido fosfinico. Blocca la conversione dell'Angiotensina I in Angiotensina II, riducendo la resistenza vascolare sistemica e abbassando la pressione arteriosa. La sua efficacia nel trattamento dell'ipertensione essenziale e nella riduzione del rischio cardiovascolare nei pazienti con insufficienza cardiaca è ben consolidata in molteplici linee guida terapeutiche.

L'ipertensione renovascolare maligna è una forma grave e potenzialmente letale di ipertensione secondaria guidata da una stenosi critica dell'arteria renale. Il sistema renina-angiotensina-aldosterone (SRAA) è patologicamente iperattivato in questa condizione, che è esattamente il percorso che fosinopril colpisce — rendendo la previsione di TxGNN meccanicamente plausibile in superficie. Il modello ha probabilmente identificato questo sovrapporsi di SRAA come un segnale forte.

Tuttavia, esiste un pericolo ben riconosciuto: nella malattia renovascolare, la vasocostrizione dell'arteriola efferente guidata dall'Angiotensina II è il *meccanismo compensatorio* da cui il rene ischemico dipende per mantenere la pressione di filtrazione glomerulare. L'inibizione dell'ACE elimina questo supporto compensatorio, potenzialmente precipitando lesioni renali acute o perdita completa della funzione renale nel rene colpito. Questo profilo meccanicistico bidirezionale — beneficio antipertensivo da un lato, rischio di precipitare insufficienza renale dall'altro — è una cautela clinica nota per gli inibitori dell'ACE come classe in questo specifico contesto di malattia, e limita significativamente il potenziale di riposizionamento di questa previsione.

---

## Evidenza da sperimentazioni cliniche

Attualmente nessuna sperimentazione clinica correlata registrata.

---

## Evidenza da letteratura

Attualmente nessuna letteratura correlata disponibile.

> **Nota:** Una ricerca su PubMed per fosinopril in questa indicazione ha restituito 0 risultati. Una ricerca separata per l'indicazione di rango 3 (ipertensione polmonare dovuta a malattia polmonare/ipossia) ha recuperato 20 pubblicazioni, ma queste affrontano la biologia generale dell'ipossia e non sono specifiche al ruolo di fosinopril in questa malattia — la loro rilevanza non è confermata e non sono presentate qui.

---

## Considerazioni di sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni di sicurezza.

> I dati di sicurezza (avvertenze principali, controindicazioni, interazioni farmacologiche) non erano recuperabili dalle attuali fonti di dati. Per la valutazione dell'uso clinico, il foglio illustrativo e una ricerca di interazione farmacologica con un elenco completo dei farmaci del paziente sono prerequisiti essenziali.

---

## Conclusione e fasi successive

**Decisione: Rinvio**

**Razionale:**
Nonostante un punteggio di previsione di TxGNN molto alto (99.87%), l'evidenza di supporto è interamente al livello L5 senza alcuna sperimentazione clinica o letteratura diretta — e più criticamente, il meccanismo di inibitore dell'ACE di fosinopril è un pericolo noto a livello di classe nella malattia renovascolare, dove inibire l'Angiotensina II può precipitare insufficienza renale acuta invece di fornire beneficio.

**Per procedere, è necessario quanto segue:**

- **Dati MOA da DrugBank** (remediation DG002) per documentare formalmente il collegamento meccanicistico e il profilo di controindicazione
- **Revisione del foglio illustrativo** (remediation DG001): il testo della controindicazione formale per stenosi bilaterale dell'arteria renale / malattia renovascolare deve essere confermato prima di qualsiasi ulteriore valutazione
- **Stratificazione del rischio della funzione renale**: un quadro di sicurezza che distingua malattia renovascolare unilaterale da bilaterale, dove il profilo rischio-beneficio differisce sostanzialmente
- **Ampliamento della ricerca letteraria**: espandere la ricerca agli inibitori dell'ACE come classe (non specifici di fosinopril) nell'ipertensione maligna con eziologia renovascolare
- **Consulenza di esperti clinici**: revisione di specialisti in nefrologia o ipertensione sulla questione se questa previsione di TxGNN rappresenta un'opportunità genuina di riposizionamento o un uso controindicato che viene identificato dal segnale di percorso SRAA del modello

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

