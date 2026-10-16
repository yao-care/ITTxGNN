---
layout: default
title: Bisoprolol
parent: Solo previsione del modello (L5)
nav_order: 73
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Bisoprolol: nuova indicazione prevista, Malattia renale ipertensiva maligna (livello di evidenza L5). Indicazione originale: Disturbo ipertensivo / ipertensione"
monitor_inn: "bisoprolol"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Bisoprolol
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

# Bisoprololo: dall'ipertensione alla malattia renale ipertensiva maligna

## Sintesi in una frase

Il bisoprololo è un beta-bloccante beta-1 selettivo, utilizzato originariamente per il trattamento dell'ipertensione.
Il modello TxGNN prevede che possa essere efficace per la **malattia renale ipertensiva maligna**,
ma per questa indicazione **non risultano né studi clinici né pubblicazioni**: la previsione si basa esclusivamente sul modello.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Disturbo ipertensivo / ipertensione (derivata dal knowledge graph TxGNN; i testi autorizzativi AIFA non riportano l'indicazione) |
| Nuova indicazione prevista | Malattia renale ipertensiva maligna |
| Punteggio di predizione TxGNN | 99,94% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate (nessuna autorizzazione valida) |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

I dati compilati per questo report non contengono informazioni dettagliate sul meccanismo d'azione. In base alle conoscenze generali, il bisoprololo è un beta-1 bloccante selettivo, la cui efficacia nell'ipertensione è consolidata. Dal punto di vista meccanicistico, potrebbe essere applicabile a una complicanza ipertensiva grave.

La malattia renale ipertensiva maligna è una complicanza severa a carico degli organi bersaglio dell'ipertensione. Il collegamento ipotizzato passa attraverso la riduzione della pressione arteriosa e la riduzione dell'attività simpatica e del sistema renina-angiotensina (il blocco beta-1 riduce il rilascio di renina). Si tratta tuttavia di un razionale teorico.

Il punteggio elevato (0,999) riflette probabilmente la vicinanza, nel grafo, all'indicazione ipertensiva già esistente, e non costituisce una prova di efficacia. L'ipertensione maligna è un'emergenza ipertensiva, di norma gestita con farmaci per via endovenosa: il bisoprololo orale non è un'opzione standard. La seconda previsione (ipertensione nefrovascolare maligna) ha lo stesso punteggio, il che suggerisce un "vicinato" comune nel grafo piuttosto che evidenze indipendenti.

## Altre indicazioni previste (per contesto)

| Indicazione prevista | Punteggio TxGNN | Evidenza | Nota |
|------|------|------|------|
| Ipertensione nefrovascolare maligna | 99,94% | L5 | Razionale teorico (riduzione della renina), nessun dato clinico |
| Ipertensione polmonare da malattia polmonare e/o ipossia | 99,93% | L4 | Solo letteratura indiretta; possibile rischio per la funzione ventricolare destra |
| Ipertensione polmonare con meccanismo multifattoriale non chiaro | 99,93% | L5 | Nessun dato; il blocco beta potrebbe essere dannoso |
| Sindrome di Braddock | 99,91% | L5 | Nessun legame meccanicistico identificabile |

## Evidenza dagli studi clinici

Attualmente non risultano studi clinici registrati correlati.

## Evidenza dalla letteratura

Per la nuova indicazione principale (malattia renale ipertensiva maligna) attualmente non è disponibile alcuna letteratura correlata.

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; non esistono autorizzazioni valide. Il testo dell'indicazione approvata e la forma farmaceutica non sono riportati nei dati compilati. Esempi delle principali autorizzazioni:

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 044048015 | CONGESCOR 28 cpr rivestite 2,5 mg | GEKOFAR Srl | Cancellata |
| 034954420 | CARDICOR 28 cpr rivestite 10 mg | RECORDATI SpA | Cancellata |
| 034953416 | CONGESCOR 28 cpr rivestite 10 mg | MERCK SERONO SpA | Cancellata |
| 034952263 | SEQUACOR 28 cpr rivestite 5 mg | DOMPÉ FARMACEUTICI SpA | Cancellata |
| 037130174 | BISOPROLOLO 28 cpr rivestite 10 mg | EG SpA | Cancellata |

## Considerazioni sulla sicurezza

- **Controindicazioni suggerite dal knowledge graph** (archi farmaco-malattia di TxGNN, non testo del foglio illustrativo): asma (anche intrinseca e allergica), diabete mellito e chetoacidosi diabetica, malattie epatiche (incluse encefalopatia e coma epatico), malattia renale, anuria, pancreatite, malattie della colecisti, lupus eritematoso sistemico, psoriasi, gotta e iperuricemia, miastenia grave, disturbi d'ansia e nevrotici, distimia, ipercalcemia, iperparatiroidismo, carenza di potassio, disturbi del metabolismo del fosforo e ittero neonatale.
- **Interazioni farmacologiche**: sono state identificate 228 interazioni. Tra quelle riportate, di livello moderato: epinefrina, idrocortisone, desametasone, betametasone, budesonide, triamcinolone, bupropione, morfina, atropina, ioscimamina, metscopolamina, acetoesamide e vari sali di calcio. Di livello minore: acido acetilsalicilico, idrossido di alluminio e attapulgite.
- **Considerazioni specifiche per le nuove indicazioni**: nell'ipertensione polmonare la funzione del ventricolo destro dipende da frequenza cardiaca e contrattilità, e nelle malattie polmonari con broncospasmo i beta-bloccanti comportano rischi. La selettività beta-1 del bisoprololo riduce ma non elimina tale rischio.

Per le avvertenze e le controindicazioni ufficiali si rimanda al foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Per la malattia renale ipertensiva maligna non esistono studi clinici né letteratura (livello L5): il punteggio elevato è solo una previsione del modello. Inoltre l'ipertensione maligna è un'emergenza trattata di norma con farmaci endovenosi, e in Italia non esiste attualmente alcuna autorizzazione valida per il bisoprololo.

**Per procedere è necessario:**
- Acquisire il foglio illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Ottenere i dati sul meccanismo d'azione (ad esempio da DrugBank)
- Verificare le ragioni della cancellazione delle autorizzazioni e la disponibilità effettiva del farmaco sul mercato italiano
- Condurre una revisione sistematica della letteratura sull'uso dei beta-bloccanti nell'ipertensione maligna e nefrovascolare
- Valutare preliminarmente la sicurezza, in particolare per le ipotesi riguardanti l'ipertensione polmonare
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

