---
layout: default
title: Perindopril
parent: Solo previsione del modello (L5)
nav_order: 346
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Perindopril: nuova indicazione prevista, Ipertensione renovascolare maligna (livello di evidenza L5). Indicazione originale: Ipertensione (disturbo ipertensivo)"
monitor_inn: "PERINDOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
---

# Perindopril
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

# Perindopril: dall'ipertensione all'ipertensione renovascolare maligna

## Sintesi in una frase

Perindopril è un inibitore dell'enzima di conversione dell'angiotensina (ACE), originariamente utilizzato per il trattamento dell'ipertensione.
Il modello TxGNN prevede che possa essere efficace per l'**ipertensione renovascolare maligna**, ma per questa indicazione i dati compilati non contengono **alcuno studio clinico** né **alcuna pubblicazione** a supporto: la previsione si basa solo sul modello.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione (disturbo ipertensivo) |
| Nuova indicazione prevista | Ipertensione renovascolare maligna |
| Punteggio di previsione TxGNN | 99,77% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione è plausibile?

I dati compilati non includono una descrizione dettagliata del meccanismo d'azione. Sulla base delle conoscenze generali, perindopril è un inibitore dell'ACE: riduce la produzione di angiotensina II e quindi la pressione arteriosa. La sua efficacia nell'ipertensione è consolidata.

L'ipertensione renovascolare maligna è sostenuta da una marcata attivazione del sistema renina-angiotensina-aldosterone (RAAS), per cui il meccanismo è biologicamente plausibile.

Vi sono però due limiti importanti. Primo, la previsione è molto vicina all'indicazione originale (ipertensione), quindi apporta poco valore di riposizionamento. Secondo, gli ACE-inibitori comportano un rischio significativo di insufficienza renale acuta in caso di stenosi bilaterale delle arterie renali o di rene singolo stenotico: questo è un serio problema di sicurezza proprio in questo contesto clinico.

Altre previsioni nell'elenco (non analizzate in dettaglio sotto): ipertensione renale maligna (99,77%), ipertensione polmonare di origine multifattoriale non chiara e ipertensione polmonare da malattia polmonare/ipossia (99,75%), sindrome di Braddock (99,66%). Per l'ipertensione polmonare da malattia polmonare/ipossia esiste solo evidenza precliniche indiretta (studi su ratto, ad es. PMID 11282121 e 10602319), che la rende, tra le previsioni, l'unica formulabile come ipotesi di ricerca (livello L4).

---

## Evidenze da studi clinici

Al momento non risultano studi clinici registrati correlati.

---

## Evidenze dalla letteratura

Per l'ipertensione renovascolare maligna non è disponibile alcuna letteratura correlata.

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; nessuna è attualmente valida. Il testo dell'indicazione approvata non è riportato nei dati compilati. Esempi tra le principali:

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 051109015 | COVERSYL 30 cpr rivestite 5 mg | NEW PHARMASHOP Srl | Cancellata |
| 038764078 | PERINDOPRIL 30 cpr 4 mg | SANDOZ SpA | Cancellata |
| 041788112 | PERINDOPRIL 30 cpr rivestite 10 mg | TEVA ITALIA Srl | Cancellata |
| 027286210 | COVERSYL 30 cpr rivestite 5 mg | LES LABORATOIRES SERVIER | Cancellata |
| 027469319 | PROCAPTAN 30 cpr rivestite 10 mg | STRODER Srl | Cancellata |

---

## Considerazioni di sicurezza

- **Controindicazioni (da grafo di conoscenza, non dal foglietto illustrativo)**: malattie renali, ostruzione dell'arteria renale, malattie epatiche, malattie della colecisti, angioedema (incluso quello ereditario, acquisito e indotto da bloccanti del RAAS), neutropenia, agranulocitosi, disturbi ipotensivi, malattie del tessuto connettivo, malattie ossee e cartilaginee, piouretere.
- **Interazioni farmacologiche**: sono state rilevate 100 interazioni; tra quelle di gravità **maggiore** figurano citrato di potassio e bicarbonato di potassio (rischio di iperkaliemia). Tra le interazioni di gravità **moderata**: corticosteroidi (idrocortisone, desametasone, betametasone, budesonide, triamcinolone), antidiabetici (metformina, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, clorpropamide), bupropione, morfina, acido acetilsalicilico, dronabinolo, acido picosolfurico e polietilenglicole con elettroliti.
- Un caso clinico presente nella letteratura recuperata (PMID 37678466) segnala angioedema ad insorgenza tardiva da ACE-inibitore con rischio per le vie aeree.

Per le avvertenze complete fare riferimento al foglietto illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione ha un punteggio elevato ma nessun supporto da studi clinici o letteratura pertinente (livello L5), è molto vicina all'indicazione già nota e comporta un rilevante rischio renale nel contesto specifico. Inoltre, tutte le autorizzazioni italiane sono cancellate.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione
- Avvertenze e controindicazioni dal foglietto illustrativo AIFA (attualmente non disponibili, impediscono la valutazione di sicurezza)
- Una revisione sistematica della letteratura specifica sull'uso degli ACE-inibitori nell'ipertensione renovascolare maligna
- Una valutazione del rischio renale (stenosi bilaterale dell'arteria renale/rene singolo) e un piano di monitoraggio
- Verifica della possibilità di riammissione in commercio di prodotti a base di perindopril in Italia
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

