---
layout: default
title: Raloxifene
parent: Solo previsione del modello (L5)
nav_order: 372
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Raloxifene: nuova indicazione prevista, Ulcera duodenale (livello di evidenza L5). Indicazione originale: Osteoporosi post-menopausale / osteoporosi"
---

# Raloxifene
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

# Raloxifene: dall'osteoporosi post-menopausale all'ulcera duodenale

## Sintesi in una frase

Il raloxifene è un modulatore selettivo dei recettori degli estrogeni (SERM), utilizzato originariamente per il trattamento dell'osteoporosi post-menopausale.
Il modello TxGNN ne prevede una possibile efficacia nell'**ulcera duodenale** (punteggio molto alto, 99,72%), ma finora **non risultano studi clinici né pubblicazioni** a sostegno di questa ipotesi: si tratta di una predizione puramente computazionale.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Osteoporosi post-menopausale / osteoporosi |
| Nuova indicazione prevista | Ulcera duodenale |
| Punteggio di predizione TxGNN | 99,72% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 4 (tutte cancellate) |
| Decisione raccomandata | Hold |

Nota: l'indicazione originale deriva dagli archi delle indicazioni del grafo di conoscenza; i testi delle indicazioni autorizzate AIFA non sono disponibili nei dati compilati.

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. Sulla base delle conoscenze generali, il raloxifene è un SERM con attività agonista estrogenica sull'osso e antagonista a livello di mammella e utero. La sua efficacia nell'osteoporosi post-menopausale è consolidata.

Non esiste un meccanismo stabilito che colleghi il raloxifene alla fisiopatologia dell'ulcera peptica (infezione da *H. pylori*, secrezione acida, difesa della mucosa). Un eventuale legame resta speculativo, ad esempio attraverso effetti dei recettori estrogenici sulla protezione della mucosa gastrica o sull'infiammazione. L'assenza dei dati sul meccanismo d'azione limita ulteriormente la valutazione.

Il punteggio elevato è quindi, allo stato attuale, l'unico elemento a favore e va interpretato con grande cautela.

### Altre predizioni del modello (tutte di livello L5, decisione Hold)

| Rango | Indicazione prevista | Punteggio TxGNN | Considerazioni |
|------|------|------|------|
| 2 | Ipoalfalipoproteinemia | 99,65% | Il raloxifene riduce modestamente LDL-C e fibrinogeno nelle donne in post-menopausa, ma gli effetti sull'HDL-C sono in genere piccoli o neutri; il beneficio non è supportato. |
| 3 | Ostruzione duodenale | 99,64% | Condizione prevalentemente meccanica/strutturale, gestita per via chirurgica o endoscopica; la predizione è probabilmente un artefatto di prossimità nella rete. |
| 4 | Reflusso duodeno-gastrico | 99,59% | Disturbo di motilità e funzione pilorica; il raloxifene non ha azione procinetica, chelante dei sali biliari o di protezione mucosale nota. |

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

Attualmente non risulta alcuna letteratura correlata.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 034154017 | OPTRUMA 14 compresse rivestite 60 mg | Eli Lilly Nederland BV | Cancellata |
| 040742025 | RALOXIFENE 28 compresse rivestite 60 mg | Sandoz SpA | Cancellata |
| 034153027 | EVISTA 28 compresse rivestite 60 mg | Substipharm | Cancellata |
| 034154029 | OPTRUMA 28 compresse rivestite 60 mg | Eli Lilly Nederland BV | Cancellata |

Tutte e quattro le autorizzazioni sono monocomponente e risultano cancellate: al momento non vi sono autorizzazioni valide in Italia.

## Considerazioni sulla sicurezza

I dati sulle controindicazioni derivano dal grafo di conoscenza (non dal testo del foglio illustrativo). Il raloxifene risulta associato alle seguenti condizioni:

- **Cardiovascolari e tromboembolici**: ipertensione/disturbo ipertensivo, fibrillazione atriale, tromboflebite, embolia polmonare, trombofilia, sindrome da anticorpi antifosfolipidi, occlusione dell'arteria retinica, coronaropatia
- **Cerebrovascolari**: ictus, disturbo cerebrovascolare, infarto cerebrale, attacco ischemico transitorio, insufficienza vertebro-basilare, suscettibilità all'ictus ischemico
- **Epatiche e biliari**: epatopatia, malattia della colecisti
- **Metaboliche e renali**: ipertrigliceridemia, compromissione della funzione renale

**Interazioni farmacologiche**: la ricerca ha individuato 100 interazioni potenziali (fonte DDInter), tutte con livello di gravità non classificato ("Unknown"). Tra quelle elencate figurano calcitriolo, pantoprazolo, glimepiride, mesalazina, doxiciclina, clotrimazolo, morfina, metformina, omeprazolo, lansoprazolo, sucralfato, rosiglitazone, vancomicina, lattulosio, triamcinolone, simvastatina, nistatina, nateglinide, scopolamina e tetraciclina. La rilevanza clinica di queste interazioni va verificata.

Per avvertenze e controindicazioni ufficiali, consultare il foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa unicamente su un punteggio computazionale elevato, senza studi clinici, letteratura o un meccanismo plausibile che colleghi il raloxifene all'ulcera duodenale. Inoltre, in Italia non vi sono autorizzazioni valide e il profilo di sicurezza (rischio tromboembolico e cerebrovascolare) è rilevante.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) del raloxifene
- Il foglio illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Una revisione sistematica della letteratura su raloxifene e patologie gastroduodenali (e, per il rango 2, sul profilo lipidico/HDL)
- Una valutazione del rapporto beneficio-rischio, considerando il rischio tromboembolico e cerebrovascolare
- Una verifica della possibilità di commercializzazione, dato che tutte le autorizzazioni italiane sono cancellate
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

