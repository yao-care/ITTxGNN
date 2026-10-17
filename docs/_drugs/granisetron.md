---
layout: default
title: Granisetron
parent: Solo previsione del modello (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Granisetron: nuova indicazione prevista, Disturbo bipolare affettivo maniacale (livello di evidenza L5). Indicazione originale: Non disponibile nei dati compilati (i testi delle indicazioni delle a…"
monitor_inn: "granisetron"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "bronchitis", "cold urticaria", "conjunctivitis"]
---

# Granisetron
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
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

# Granisetron: Dal controllo della nausea e del vomito al disturbo bipolare maniacale

## Sintesi in una frase

Il granisetron è un antagonista selettivo del recettore 5-HT3, autorizzato in Italia in diverse formulazioni (fiale endovenose, compresse rivestite, cerotto transdermico). Il modello TxGNN prevede che possa essere efficace per il **disturbo bipolare affettivo maniacale**, ma questa indicazione si basa **solo sulla previsione del modello**: nei dati compilati per questo report non risultano **né studi clinici né pubblicazioni** a supporto.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile nei dati compilati (i testi delle indicazioni delle autorizzazioni AIFA sono vuoti) |
| Nuova indicazione prevista | Disturbo bipolare affettivo maniacale |
| Punteggio di predizione TxGNN | 99,62% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 10 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrati per questo farmaco. In base alle conoscenze generali, il granisetron è un antagonista selettivo del recettore 5-HT3 della serotonina, noto per l'uso nella prevenzione della nausea e del vomito, e potrebbe in via ipotetica essere applicabile al disturbo bipolare maniacale.

Il collegamento meccanicistico proposto è indiretto: la disregolazione serotoninergica e dopaminergica è coinvolta nella mania, quindi un'azione sul sistema 5-HT3 potrebbe modularne alcuni circuiti. Si tratta tuttavia di un'ipotesi non supportata da dati clinici; il punteggio elevato (0,996) è una predizione del modello e non una prova di efficacia. La similarità con l'indicazione originale non è stata ancora valutata.

Anche le altre indicazioni previste ai primi posti hanno lo stesso livello di evidenza (L5, nessuno studio né pubblicazione): sindrome di Tourette, congiuntivite contagiosa acuta, angioedema, orticaria allergica, sindrome nefrogenica da inappropriata antidiuresi, tricotillomania, bronchite, orticaria da freddo e congiuntivite. Per diverse di esse (ad esempio congiuntivite, sindrome nefrogenica da inappropriata antidiuresi) non emerge alcun razionale biologico plausibile e il punteggio sembra riflettere associazioni del grafo di conoscenza.

## Evidenze da studi clinici

Attualmente non risultano studi clinici registrati correlati.

## Evidenze dalla letteratura

Attualmente non risulta letteratura correlata disponibile.

## Informazioni sul mercato italiano

Tutte e 10 le autorizzazioni risultano cancellate; nessuna è attualmente valida. I testi delle indicazioni approvate e le forme farmaceutiche non sono riportati nei dati compilati. Principali autorizzazioni (prime 5):

| N. autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 028093019 | KYTRIL 1 fiala EV 3 mg/3 ml | Atnahs Pharma Netherlands BV | Cancellata |
| 046096018 | PANDIOL 10 cpr rivestite 1 mg | Elleva Pharma Srl | Cancellata |
| 042924011 | SANCUSO 1 cerotto transdermico 3,1 mg/24 ore | Grunenthal GmbH | Cancellata |
| 028093021 | KYTRIL 10 cpr rivestite 1 mg | Atnahs Pharma Netherlands BV | Cancellata |
| 050350026 | GRANDISE 5 cpr rivestite 2 mg | Lanova Farmaceutici Srl | Cancellata |

## Considerazioni sulla sicurezza

- **Controindicazioni dal grafo di conoscenza (PrimeKG, non dal foglio illustrativo)**: sindrome del QT lungo, sindrome del QT lungo familiare, carenza di potassio, arresto cardiaco improvviso, malattie del sistema di conduzione cardiaco.
- **Interazioni farmacologiche**: sono state identificate 461 interazioni. Tra quelle di livello **maggiore** figurano fentanil, destrometorfano, tramadolo, alfentanil, almotriptan, sumatriptan, amiodarone, amisulpride, amitriptilina e anagrelide. Tra quelle di livello **moderato** figurano abametapir (topico), abiraterone, diidrocodeina, codeina, famotidina, formoterolo, adenosina, salbutamolo, alfuzosina e propofol. Il quadro suggerisce particolare cautela per i rischi di prolungamento del QT e di sindrome serotoninergica.

Per le avvertenze e le controindicazioni ufficiali si rimanda al foglio illustrativo, non disponibile nei dati compilati.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
L'indicazione prevista si fonda esclusivamente sul punteggio del modello (livello L5), senza studi clinici né letteratura, con un razionale meccanicistico solo ipotetico. Inoltre, tutte le autorizzazioni italiane sono cancellate e le controindicazioni cardiache segnalate richiedono cautela.

**Per procedere sono necessari:**
- Una revisione sistematica della letteratura e la ricerca di studi clinici su granisetron e disturbo bipolare maniacale
- Dati sul meccanismo d'azione (MOA) da DrugBank
- Foglio illustrativo AIFA con avvertenze e controindicazioni, per consentire lo screening di sicurezza
- Valutazione della similarità con l'indicazione originale e della compatibilità della via di somministrazione
- Una valutazione del rischio cardiaco (QT) e delle interazioni per la popolazione bipolare, spesso in terapia con farmaci interagenti
- Verifica della disponibilità commerciale del prodotto in Italia, dato lo stato di autorizzazioni cancellate
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

