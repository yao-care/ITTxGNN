---
layout: default
title: Alfacalcidol
parent: Solo previsione del modello (L5)
nav_order: 26
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Alfacalcidol: nuova indicazione prevista, Ipoparatiroidismo isolato familiare da alterata secrezione di PTH (livello di evidenza L5). Indicazione originale: Iperparatiroidismo, osteite fibrosa, ipopa…"
monitor_inn: "alfacalcidol"
predicted_indications: ["familial isolated hypoparathyroidism due to impaired PTH secretion", "Dahlberg-Borer-Newcomer syndrome", "craniofacial conodysplasia", "acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis"]
---

# Alfacalcidol
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

# Alfacalcidolo: dall'iperparatiroidismo alla forma familiare di ipoparatiroidismo isolato da alterata secrezione di PTH

## Sintesi in una frase

L'alfacalcidolo è un analogo della vitamina D con idrossilazione in posizione 1-alfa, usato originariamente per iperparatiroidismo, osteite fibrosa, ipoparatiroidismo e osteodistrofia renale.
Il modello TxGNN prevede che possa essere efficace per la **forma familiare di ipoparatiroidismo isolato da alterata secrezione di PTH**, con un punteggio molto alto, ma **nessuno studio clinico e nessuna pubblicazione** a supporto diretto di questa specifica indicazione.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Iperparatiroidismo, osteite fibrosa, ipoparatiroidismo, osteodistrofia renale (dalle indicazioni del grafo di conoscenza; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Ipoparatiroidismo isolato familiare da alterata secrezione di PTH |
| Punteggio di predizione TxGNN | 99,61% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 10 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle informazioni note, l'alfacalcidolo è un analogo della vitamina D già idrossilato in posizione 1-alfa: aggira quindi la 1-alfa-idrossilasi renale e aumenta la calcemia indipendentemente dal PTH. Questo è biologicamente plausibile negli stati di carenza di PTH.

L'ipoparatiroidismo è già tra le indicazioni originali del farmaco. La forma familiare da alterata secrezione di PTH è quindi molto vicina a un uso già noto, più che un vero riposizionamento. L'alto punteggio TxGNN è coerente con questa vicinanza, ma non costituisce evidenza clinica diretta per questa forma specifica.

## Studi clinici

Al momento non risultano studi clinici registrati correlati.

## Evidenza dalla letteratura

Per la predizione principale non è disponibile letteratura specifica. Per completezza, il data set include evidenze sulle altre indicazioni previste, tutte di livello basso:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [22740247](https://pubmed.ncbi.nlm.nih.gov/22740247/) | 2013 | Caso clinico | Modern Rheumatology | Osteomalacia da acidosi tubulare renale associata a Sjögren: miglioramento con bicarbonato, risedronato, alfacalcidolo e prednisolone (terapia combinata) |
| [11518137](https://pubmed.ncbi.nlm.nih.gov/11518137/) | 2001 | Caso clinico | Internal Medicine | Rapido miglioramento dell'osteomalacia in un caso di Sjögren, artrite reumatoide e acidosi tubulare renale di tipo 1 |
| [33398781](https://pubmed.ncbi.nlm.nih.gov/33398781/) | 2021 | Caso clinico | CEN Case Reports | Osteomalacia da acidosi tubulare renale atipica con carenza di vitamina D |
| [28509074](https://pubmed.ncbi.nlm.nih.gov/28509074/) | 2012 | Caso clinico con revisione | CEN Case Reports | Osteomalacia secondaria ad acidosi tubulare renale in Sjögren |
| [29545131](https://pubmed.ncbi.nlm.nih.gov/29545131/) | 2018 | Revisione | Néphrologie & Thérapeutique | Uso dell'alfacalcidolo e degli analoghi attivi della vitamina D nella malattia renale cronica e nell'iperparatiroidismo secondario |
| [34431511](https://pubmed.ncbi.nlm.nih.gov/34431511/) | 2021 | Revisione sistematica | Cochrane Database Syst Rev | Supplementazione di vitamina D nelle epatopatie croniche dell'adulto |
| [41948115](https://pubmed.ncbi.nlm.nih.gov/41948115/) | 2026 | RCT | Clinical Kidney Journal | Alfacalcidolo più calcio versus colecalciferolo in bambini con sindrome nefrosica esposti a glucocorticoidi |
| [41905593](https://pubmed.ncbi.nlm.nih.gov/41905593/) | 2026 | RCT | Kidney International | Studio ADAPT: prednisolone a dose ridotta con vitamina D attivata (alfacalcidolo) nella malattia a lesioni minime dell'adulto |

## Altre indicazioni previste (sintesi)

- **Sindrome di Dahlberg-Borer-Newcomer** (punteggio 99,60%, L5, Hold): entità rara e poco caratterizzata, probabilmente associata a una tubulopatia simile alla sindrome di Fanconi-Bickel. Le pubblicazioni recuperate riguardano condizioni correlate e non studiano l'alfacalcidolo in questa malattia; il legame è indiretto.
- **Conodisplasia craniofacciale** (99,55%, L5, Hold): nessun razionale meccanicistico evidente, nessuno studio o pubblicazione.
- **Displasia acromesomelica tipo Campailla-Martinelli** (99,53%, L5, Hold): nessun collegamento diretto tra attivazione del recettore della vitamina D e il difetto genetico; predizione puramente computazionale.
- **Acidosi tubulare renale** (99,27%, L4, domanda di ricerca): razionale plausibile (osteomalacia da acidosi cronica, perdita di fosfato e ridotta attivazione della vitamina D). Le 5 pubblicazioni sono casi clinici in cui l'alfacalcidolo era somministrato insieme a terapia alcalinizzante o fosfato, per cui il suo contributo non è isolabile. Il rischio di ipercalciuria e nefrocalcinosi richiede una valutazione di sicurezza.

## Informazioni sul mercato italiano

Tutte le 10 autorizzazioni risultano cancellate; non è presente alcun prodotto attualmente in commercio. Il testo delle indicazioni approvate e la forma farmaceutica non sono riportati nei dati.

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 025487036 | DEDIOL gocce orali 10 ml 2 mcg/ml | Cheplapharm Arzneimittel GmbH | Cancellata |
| 025487024 | DEDIOL 30 capsule molli 0,25 mcg | Cheplapharm Arzneimittel GmbH | Cancellata |
| 032333027 | DISERINAL 30 capsule molli 1 mcg | S.F. Group Srl | Cancellata |
| 032936027 | OSTIDIL D3 30 capsule molli 1 mcg | SIT Laboratorio Farmac. Srl | Cancellata |
| 029008024 | ALPHA D3 30 capsule molli 1 mcg | Theramex Ireland Limited | Cancellata |

Sono presenti ulteriori 5 autorizzazioni cancellate (GENIAD, DERIL, SEFAL, DISEON 1 mcg e DISEON 0,25 mcg).

## Considerazioni di sicurezza

Per le informazioni di sicurezza si rimanda al foglio illustrativo. I dati compilati per questo report non contengono avvertenze, controindicazioni o interazioni farmacologiche rilevate. Dalla letteratura sull'acidosi tubulare renale emerge in particolare il rischio di ipercalciuria e nefrocalcinosi, e nei pazienti ipoparatiroidei in terapia con vitamina D e calcio il rischio di ipercalcemia (sindrome calcio-alcali).

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Per l'indicazione principale la predizione si basa solo sul modello (L5), senza studi né pubblicazioni dirette, ed è probabilmente vicina a un uso già esistente più che a un vero riposizionamento. Inoltre in Italia tutte le autorizzazioni sono cancellate e mancano i dati di sicurezza del foglio illustrativo, che bloccano l'avanzamento alla fase di valutazione della sicurezza.

**Per procedere sono necessari:**
- Reperimento e analisi del foglio illustrativo AIFA (avvertenze e controindicazioni)
- Dati sul meccanismo d'azione da DrugBank
- Verifica dello stato regolatorio e della disponibilità commerciale dell'alfacalcidolo in Italia
- Ricerca di letteratura e registri specifici sull'ipoparatiroidismo isolato familiare
- Per l'acidosi tubulare renale, unica indicazione con qualche evidenza (L4): valutazione del rischio di ipercalciuria e nefrocalcinosi e, se opportuno, uno studio controllato
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

