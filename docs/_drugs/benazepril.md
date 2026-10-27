---
layout: default
title: Benazepril
parent: Solo previsione del modello (L5)
nav_order: 64
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Benazepril: nuova indicazione prevista, Ipertensione renovascolare maligna (livello di evidenza L5). Indicazione originale: Ipertensione arteriosa (disturbo ipertensivo)…"
monitor_inn: "BENAZEPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Benazepril
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **5** 
{: .fs-6 .fw-300 }

---

## Indice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relazione di valutazione farmaceutica

</div>

## Benazepril: dall'ipertensione all'ipertensione renovascolare maligna
{: .text-alpha }

## Sintesi in una frase

Il benazepril è un inibitore dell'ACE, originariamente impiegato per il trattamento dell'ipertensione arteriosa.
Il modello TxGNN ne prevede una possibile efficacia nell'**ipertensione renovascolare maligna**, ma i dati compilati per questo report non includono **nessuno studio clinico** né **alcuna pubblicazione** a supporto diretto di questa indicazione: la previsione si basa unicamente sul modello.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione arteriosa (disturbo ipertensivo), secondo gli archi di indicazione del grafo di conoscenza TxGNN; i testi autorizzativi AIFA non riportano l'indicazione |
| Nuova indicazione prevista | Ipertensione renovascolare maligna |
| Punteggio di previsione TxGNN | 99,65% |
| Livello di evidenza | L4 (valutazione assegnata nei dati compilati; nessuno studio clinico o letteratura diretta disponibile) |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 6 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è ragionevole?

Al momento i dati dettagliati sul meccanismo d'azione non sono disponibili. Sulla base delle conoscenze generali, il benazepril appartiene alla classe degli inibitori dell'enzima di conversione dell'angiotensina (ACE), la cui efficacia nell'ipertensione è consolidata, e potrebbe essere applicabile, a livello meccanicistico, anche all'ipertensione renovascolare maligna.

L'ipertensione renovascolare maligna è sostenuta da una marcata attivazione del sistema renina-angiotensina (RAS), per cui l'inibizione dell'ACE è meccanicisticamente plausibile. Il punteggio TxGNN molto elevato riflette probabilmente la stretta vicinanza ontologica con l'indicazione già approvata (ipertensione) più che nuove evidenze.

Esiste però un rilevante problema di sicurezza: gli ACE-inibitori possono precipitare un'insufficienza renale acuta in caso di stenosi bilaterale dell'arteria renale o di stenosi in rene unico, scenari tipici della patologia renovascolare.

Altre previsioni nei dati compilati (tutte con raccomandazione Hold):
- **Ipertensione maligna con nefropatia ipertensiva** (punteggio 99,65%, L4): razionale renoprotettivo indiretto degli ACE-inibitori, ma senza studi o letteratura.
- **Ipertensione polmonare da malattia polmonare e/o ipossia** (99,60%, L5): non esiste un'evidenza a favore degli ACE-inibitori; i vasodilatatori sistemici possono peggiorare il rapporto ventilazione-perfusione. Le tre pubblicazioni recuperate riguardano formule di medicina tradizionale cinese in modelli preclinici di fibrosi e non forniscono evidenza diretta sul benazepril.
- **Ipertensione polmonare a meccanismo multifattoriale non chiaro** (99,60%, L5): solo previsione computazionale.
- **Sindrome di Braddock** (99,44%, L5): nessun legame meccanicistico individuabile; probabile artefatto del grafo di conoscenza.

## Evidenze dagli studi clinici

Al momento non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

Al momento non è disponibile letteratura correlata direttamente al benazepril per l'ipertensione renovascolare maligna.

## Informazioni sul mercato italiano

Tutte le autorizzazioni risultano cancellate; non ci sono prodotti attualmente in commercio. Il testo dell'indicazione approvata non è riportato nei dati.

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 027573029 | ZINADRIL 14 compresse rivestite 10 mg | Errekappa Euroterapici SpA | Cancellata |
| 037465034 | BENAZEPRIL 28 compresse rivestite 5 mg | Sandoz SpA | Cancellata |
| 027573031 | ZINADRIL 28 compresse rivestite 5 mg | Errekappa Euroterapici SpA | Cancellata |
| 027516020 | CIBACEN 14 compresse rivestite 10 mg | Viatris Healthcare Limited | Cancellata |
| 037507213 | BENAZEPRIL 14 compresse rivestite 10 mg | EG SpA | Cancellata |

(Una sesta autorizzazione cancellata, 037507035, BENAZEPRIL 28 compresse rivestite 5 mg, EG SpA, completa l'elenco.)

## Considerazioni sulla sicurezza

- **Controindicazioni (dal grafo di conoscenza, non dal foglietto illustrativo)**: il grafo di conoscenza segnala come controindicate, tra le altre, le seguenti condizioni: angioedema (incluso ereditario, acquisito e indotto da bloccanti del RAS), insufficienza epatica ed encefalopatia epatica, malattia renale, anuria, ipotensione, pancreatite, lupus eritematoso sistemico, diabete mellito e chetoacidosi diabetica, carenza di potassio, neutropenia/agranulocitosi, iperparatiroidismo, malattie del tessuto connettivo, malattie della colecisti, ittero neonatale e malattie ossee/cartilaginee.
- **Interazioni farmacologiche**: sono state rilevate 100 interazioni, di cui nell'elenco disponibile risultano di livello moderato quelle con idrocortisone, antidiabetici (alogliptin, acetoesamide, clorpropamide, dapagliflozin, exenatide, glimepiride, glipizide, gliburide) e numerose insuline (umana, aspart, degludec, detemir, glargine, glulisina, lispro), oltre alla glicerina. Il rischio principale è l'alterazione del controllo glicemico.
- Per avvertenze e controindicazioni ufficiali, consultare il foglietto illustrativo: il testo AIFA non è presente nei dati compilati.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si fonda solo sul punteggio del modello e sulla vicinanza all'indicazione già nota (ipertensione), senza studi clinici né letteratura diretta. A ciò si aggiunge il rischio di insufficienza renale acuta nella stenosi dell'arteria renale e l'assenza di prodotti autorizzati attualmente in commercio in Italia.

**Per procedere sono necessari:**
- Recupero e analisi del foglietto illustrativo AIFA (avvertenze e controindicazioni), attualmente un blocco per lo screening di sicurezza
- Dati sul meccanismo d'azione (ad es. da DrugBank)
- Ricerca mirata di letteratura e studi su ACE-inibitori nell'ipertensione renovascolare maligna
- Piano di monitoraggio di funzione renale e potassiemia
- Verifica della fattibilità regolatoria, dato che tutte le autorizzazioni italiane sono cancellate
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

