---
layout: default
title: Labetalol
parent: Solo previsione del modello (L5)
nav_order: 251
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Labetalol: nuova indicazione prevista, Ipertensione renovascolare maligna (livello di evidenza L5). Indicazione originale: Disturbi ipertensivi / ipertensione (dal grafo di conoscenza TxGNN"
monitor_inn: "labetalol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Labetalol
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **4** 
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

# Labetalolo: dall'ipertensione all'ipertensione renovascolare maligna

## Riepilogo in una frase

Il labetalolo è un farmaco bloccante alfa-1 e beta-adrenergico non selettivo, originariamente usato per i disturbi ipertensivi e l'ipertensione.
Il modello TxGNN prevede che possa essere efficace per l'**ipertensione renovascolare maligna**, ma il supporto è molto debole: **nessuno studio clinico** registrato e **una sola pubblicazione** (un caso clinico, non diretto sull'indicazione).

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Disturbi ipertensivi / ipertensione (dal grafo di conoscenza TxGNN; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Ipertensione renovascolare maligna |
| Punteggio di previsione TxGNN | 99,08% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 2 |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

Il labetalolo combina il blocco dei recettori alfa-1 e beta non selettivo. Riduce le resistenze vascolari sistemiche e, tramite il blocco beta, può ridurre l'attività reninica. Questo offre una base farmacologica per l'ipertensione maligna di origine renovascolare. Nei dati compilati per questo report i dettagli sul meccanismo d'azione non sono disponibili.

Va sottolineato che si tratta sostanzialmente di un'estensione dell'indicazione ipertensiva già esistente, più che di un vero riposizionamento. L'unica pubblicazione collegata descrive un caso di ipertensione maligna indotta da allucinogeni con vasculite, in cui labetalolo e minoxidil sono stati usati per il controllo iniziale della pressione. Non fornisce prove dirette sull'efficacia del labetalolo in questa condizione. Il punteggio elevato di TxGNN è solo una previsione computazionale.

Anche per le altre tre previsioni a punteggio simile il supporto è debole:
- **Ipertensione maligna con malattia renale ipertensiva** (99,08%): plausibile per la riduzione pressoria, ma senza studi né letteratura; andrebbero valutati gli esiti renali.
- **Ipertensione polmonare da malattia polmonare e/o ipossia** (99,08%): legame meccanicistico debole. Il blocco beta non selettivo può peggiorare il broncospasmo e l'ipossia. Le 10 pubblicazioni recuperate riguardano soprattutto ipertensione sistemica o gestazionale, intossicazione da beta-bloccanti e modelli animali; nessuna valuta il labetalolo nell'ipertensione polmonare.
- **Ipertensione polmonare ad aspetto multifattoriale non chiaro** (99,08%): nessuna base meccanicistica diretta, poiché il labetalolo agisce sul tono vascolare sistemico e non sul rimodellamento vascolare polmonare; i beta-bloccanti sono usati con cautela per il possibile effetto negativo sul ventricolo destro.

## Evidenze da studi clinici

Al momento nessuno studio clinico correlato risulta registrato.

## Evidenze dalla letteratura

Per la previsione principale (ipertensione renovascolare maligna):

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Caso clinico | The Medical Journal of Australia | Ipertensione maligna in un giovane di 20 anni con vasculite indotta da allucinogeni; risposta al prednisone; labetalolo e minoxidil utili nel controllo iniziale della pressione |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 023578014 | TRANDATE*30 cpr 100 mg | Non disponibile | Non disponibile (autorizzazione revocata) |
| 023578038 | TRANDATE*30 cpr 200 mg | Non disponibile | Non disponibile (autorizzazione revocata) |

Entrambe le autorizzazioni, intestate a TEOFARMA Srl, risultano revocate.

## Considerazioni sulla sicurezza

I dati su avvertenze e controindicazioni dal foglietto illustrativo non sono disponibili; si rimanda al foglietto illustrativo.

- **Controindicazioni dal grafo di conoscenza (non da testo di etichetta)**: tra le condizioni associate figurano insufficienza epatica, encefalopatia epatica, malattia renale, anuria, diabete mellito e chetoacidosi diabetica, blocco atrioventricolare, enfisema polmonare e malattie bronchiali, lupus eritematoso sistemico, pancreatite, gotta, ipotensione e disturbi d'ansia/nevrotici.
- **Interazioni farmacologiche**: sono state rilevate 241 interazioni. Tra quelle mostrate:
  - **Maggiori**: epinefrina, dolasetron.
  - **Moderate**: corticosteroidi (idrocortisone, desametasone, betametasone, triamcinolone, budesonide), anticolinergici (atropina, ioscimamina, metscopolamina, diciclomina), morfina, cimetidina, canagliflozin, dapagliflozin, clorpropamide, sali di calcio.
  - **Minori**: acido acetilsalicilico, ossido di magnesio.

Nell'ipertensione polmonare da malattia polmonare il blocco beta non selettivo pone un potenziale problema di sicurezza.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
Tutte le previsioni sono a livello di evidenza L5, senza studi clinici e con letteratura non pertinente. L'ipertensione maligna renovascolare e renale è in gran parte un'estensione dell'indicazione ipertensiva già nota, mentre per l'ipertensione polmonare il legame meccanicistico è debole e il profilo di sicurezza preoccupante. Tutte le autorizzazioni italiane risultano inoltre revocate.

**Per procedere sono necessari:**
- Foglietto illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Dati sul meccanismo d'azione (ad esempio da DrugBank)
- Verifica dello stato regolatorio e della disponibilità commerciale attuale del labetalolo in Italia
- Revisione mirata della letteratura sull'uso del labetalolo nell'ipertensione maligna e renovascolare, con valutazione degli esiti renali
- Esclusione dell'ipertensione polmonare dalle priorità, salvo nuove evidenze dirette
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

