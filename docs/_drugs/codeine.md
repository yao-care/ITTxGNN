---
layout: default
title: Codeine
parent: Solo previsione del modello (L5)
nav_order: 125
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Codeine: nuova indicazione prevista, Malattia della cavità nasale (livello di evidenza L5). Indicazione originale: Rinite allergica, rinite vasomotoria, faringite, raffreddore comune…"
monitor_inn: "codeine"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "trigeminal autonomic cephalalgia", "allergic urticaria"]
---

# Codeine
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **4** 
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

# Codeina: Da cefalea e infiammazioni delle vie respiratorie superiori a malattia della cavità nasale

## Sintesi in una frase

La codeina è un oppioide con azione analgesica e antitussiva, originariamente usato per rinite, faringite, raffreddore comune e cefalea.
Il modello TxGNN prevede una possibile efficacia per **malattia della cavità nasale**, ma **non sono presenti sperimentazioni cliniche** e la sola pubblicazione disponibile è un **caso clinico** che non descrive alcun effetto terapeutico.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Rinite allergica, rinite vasomotoria, faringite, raffreddore comune, rinite, rinofaringite, cefalea (dal grafo di conoscenza TxGNN; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Malattia della cavità nasale |
| Punteggio di previsione TxGNN | 99,93% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 9 |
| Decisione raccomandata | Hold |

---

## Perché questa previsione potrebbe essere ragionevole?

Allo stato attuale non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle informazioni note, la codeina è un oppioide agonista dei recettori mu, con effetti antitussivi e analgesici lievi, ed è presente in Italia soprattutto in associazione con paracetamolo (o ibuprofene).

La previsione sembra guidata dalle indicazioni già note (rinite, raffreddore, rinofaringite), che coinvolgono sintomi nasali. Si tratta di un'associazione basata sul sollievo sintomatico, non di un'azione modificatrice della malattia a livello della cavità nasale. Non è stato stabilito alcun meccanismo a supporto.

L'unica pubblicazione disponibile descrive un caso di rinolitiasi causata da un corpo estraneo contenente codeina e oppio: un reperto accidentale o avverso, non un beneficio terapeutico.

---

## Evidenze dagli studi clinici

Attualmente non risultano sperimentazioni cliniche correlate registrate.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Caso clinico | Ear, Nose, & Throat Journal | Rinolite insolita in un uomo di 21 anni, formatasi attorno a un corpo estraneo costituito da una miscela indurita di codeina e oppio ("opioma"); nessun effetto terapeutico descritto |

---

## Informazioni sul mercato italiano

| N. autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 037021021 | CODAMOL 16 cpr rivestite 500 mg + 30 mg | n.d. | Non disponibile (autorizzazione cancellata) |
| 031825060 | TACHIDOL 16 cpr rivestite div. 500 mg + 30 mg | n.d. | Non disponibile (autorizzazione cancellata) |
| 042711010 | PARACETAMOLO E CODEINA 16 cpr 500 mg + 30 mg (DOC Generici) | n.d. | Non disponibile (autorizzazione cancellata) |
| 047824014 | PARACETAMOLO CODEINA 16 cpr rivestite 500 mg + 30 mg (Towa) | n.d. | Non disponibile (autorizzazione cancellata) |
| 042269011 | BRUFECOD 30 cpr rivestite 400 mg + 30 mg | n.d. | Non disponibile (autorizzazione cancellata) |

Tutte e 9 le autorizzazioni risultano cancellate; nessuna è attualmente valida.

---

## Considerazioni sulla sicurezza

I dati sul foglio illustrativo AIFA (avvertenze e controindicazioni) non sono disponibili; si rimanda al foglio illustrativo per le informazioni di sicurezza.

- **Controindicazioni o condizioni a rischio dal grafo di conoscenza** (non provenienti dal testo dell'etichetta): ipertensione, insufficienza epatica e malattie del fegato, epilessia, insonnia, BPCO, disturbi d'ansia e disturbi psichiatrici (inclusi psicosi e schizofrenia), porfiria, malattie renali, pancreatite, malattie della colecisti, trombocitopenia, ipotiroidismo/mixedema, ulcera peptica, malattia infiammatoria intestinale, gastrite, dermatite erpetiforme.
- **Interazioni farmacologiche**: sono state identificate 449 interazioni. Tra quelle di gravità **maggiore** figurano **alvimopan** e **bupropione**. Tra quelle di gravità moderata: atropina, cimetidina, desametasone, loperamide, glicopirronio, ioscina/iosciamina, granisetron, dolasetron, dronabinolo, eliglustat, eluxadoline, fenfluramina, caolino e altri.
- **Restrizioni pediatriche**: l'uso della codeina per condizioni respiratorie in età pediatrica è soggetto a limitazioni di sicurezza.

---

## Altre indicazioni previste (valutate nei dati compilati)

| Indicazione | Punteggio TxGNN | Livello | Osservazioni |
|------|------|------|------|
| Laringofaringite acuta | 99,92% | L5 | Solo previsione computazionale, senza studi né letteratura; sovrapposta alle indicazioni già note e limitata a sollievo sintomatico |
| Cefalea autonomica trigeminale | 99,43% | L5 | La letteratura (serie pediatrica di cefalea a grappolo, caso di abuso di cocaina) non valuta la codeina; gli oppioidi non sono raccomandati per rischio di abuso e scarsa efficacia |
| Orticaria allergica | 99,37% | L4 | La letteratura (16 voci) mostra la codeina come causa/trigger di orticaria (degranulazione diretta dei mastociti), usata come controllo positivo nei test cutanei; meccanismo orientato al danno, non terapeutico |

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Il punteggio TxGNN è molto alto (99,93%), ma non esistono sperimentazioni cliniche e l'unica pubblicazione è un caso clinico di un evento accidentale, non di un beneficio. Tutte le autorizzazioni italiane sono cancellate e i dati di sicurezza dal foglio illustrativo mancano (lacuna bloccante). Per l'orticaria allergica il meccanismo suggerisce addirittura un effetto dannoso.

**Per procedere sono necessari:**
- Acquisire e analizzare il foglio illustrativo AIFA (avvertenze e controindicazioni), lacuna bloccante per lo screening di sicurezza
- Dati dettagliati sul meccanismo d'azione (ad esempio da DrugBank)
- Evidenze cliniche o precliniche che dimostrino un beneficio terapeutico in patologie della cavità nasale
- Valutazione del rapporto rischio-beneficio, tenuto conto di dipendenza, interazioni maggiori e restrizioni pediatriche
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

