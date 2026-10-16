---
layout: default
title: Ebastine
parent: Solo previsione del modello (L5)
nav_order: 163
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Ebastine: nuova indicazione prevista, Malattia coronarica (livello di evidenza L5). Indicazione originale: Rinite allergica, rinite vasomotoria…"
---

# Ebastine
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **2** 
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

# Ebastina: Dall'allergia alla malattia coronarica

## Sintesi in una frase

L'ebastina è un antistaminico H1 di seconda generazione, utilizzato originariamente per la rinite allergica, la rinite vasomotoria e l'orticaria idiopatica.
Il modello TxGNN prevede una possibile efficacia nella **malattia coronarica** (e, in seconda posizione, nell'**ischemia miocardica**),
ma al momento **non risultano studi clinici né pubblicazioni** a supporto di questa direzione: la previsione è puramente computazionale.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Rinite allergica, rinite vasomotoria, orticaria idiopatica (dal grafo di conoscenza; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Malattia coronarica |
| Punteggio di previsione TxGNN | 99,18% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 10 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione potrebbe avere senso?

I dati compilati per questo report non contengono informazioni dettagliate sul meccanismo d'azione dell'ebastina. Sulla base delle conoscenze generali, l'ebastina è un antagonista del recettore H1 di seconda generazione, la cui efficacia nelle patologie allergiche è consolidata.

Il legame con la malattia coronarica è solo un'ipotesi: istamina e attività dei mastociti sono state proposte come fattori coinvolti nel vasospasmo coronarico e nell'instabilità della placca aterosclerotica. Il blocco del recettore H1 potrebbe quindi modulare la vasocostrizione coronarica mediata dall'istamina. Nessuna evidenza fornita in questa sede sostiene tale ipotesi.

Il punteggio elevato di TxGNN (0,992) è una previsione basata su un grafo di conoscenza e non costituisce evidenza clinica. La seconda previsione, l'**ischemia miocardica** (punteggio 99,10%), è strettamente correlata alla malattia coronarica: le due previsioni probabilmente non sono indipendenti. Anche per essa non esistono studi o pubblicazioni a supporto.

---

## Evidenze da studi clinici

Al momento non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

Al momento non è disponibile letteratura correlata.

---

## Informazioni sul mercato italiano

Tutte le 10 autorizzazioni sono cancellate; nessuna è attualmente valida. Il testo dell'indicazione approvata non è disponibile. Si elencano le prime 5:

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 047251032 | Ebastina 30 cpr orodispersibili 10 mg (Aurobindo Pharma Italia) | Aurobindo Pharma Italia Srl | Cancellata |
| 034930014 | Kestine 30 cpr rivestite 10 mg | Almirall S.A. | Cancellata |
| 034930141 | Kestine orale 30 dosi liofilizzato 10 mg | Almirall S.A. | Cancellata |
| 044598035 | Ebastina 30 cpr orodispersibili 10 mg | Aristo Pharma GmbH | Cancellata |
| 043728029 | Ebastina 30 cpr orodispersibili 10 mg | EG SpA | Cancellata |

---

## Considerazioni di sicurezza

Per l'ebastina non sono disponibili dati di sicurezza verificati (avvertenze e controindicazioni del foglio illustrativo AIFA non acquisiti; nessuna interazione farmacologica registrata nei dati compilati).

Un punto di attenzione per l'indicazione cardiaca proposta: per alcuni antistaminici H1 (ad es. terfenadina e astemizolo) sono state descritte preoccupazioni relative al prolungamento dell'intervallo QT. Il profilo di sicurezza dell'ebastina nei pazienti con cardiopatia ischemica non è stato valutato in questo report e richiede una verifica specifica.

Per le informazioni complete di sicurezza si rimanda al foglio illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si basa esclusivamente sul modello TxGNN (livello di evidenza L5), senza studi clinici, letteratura o meccanismo documentato. Inoltre, tutte le autorizzazioni italiane sono cancellate e permangono dubbi di sicurezza cardiaca (QT) in un contesto di cardiopatia ischemica.

**Per procedere sono necessari:**
- Acquisizione e analisi del foglio illustrativo AIFA (avvertenze e controindicazioni), lacuna bloccante per lo screening di sicurezza
- Dati sul meccanismo d'azione (ad es. tramite DrugBank)
- Revisione sistematica della letteratura preclinica e clinica su antistaminici H1 e malattia coronarica/ischemia miocardica
- Valutazione della sicurezza cardiaca, in particolare QT e uso in pazienti con cardiopatia ischemica
- Verifica della disponibilità del prodotto e delle vie di somministrazione, dato che non esistono autorizzazioni valide in Italia
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

