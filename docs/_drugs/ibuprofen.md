---
layout: default
title: Ibuprofen
parent: Solo previsione del modello (L5)
nav_order: 230
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Ibuprofen: nuova indicazione prevista, Displasia acromesomelica, tipo Hunter-Thompson (livello di evidenza L5). Indicazione originale: Artrite reumatoide, cefalea, artrosi, artropatie…"
monitor_inn: "ibuprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Ibuprofen
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **7** 
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

## Ibuprofene: dall'artrite reumatoide alla displasia acromesomelica di tipo Hunter-Thompson
{: .text-alpha }

## Riepilogo in una frase

L'ibuprofene è un farmaco antinfiammatorio non steroideo (FANS), utilizzato originariamente per artrite reumatoide, artrosi, cefalea, artrite idiopatica giovanile e, in ambito neonatale, per la chiusura del dotto arterioso pervio.
Il modello TxGNN prevede che possa essere efficace per la **displasia acromesomelica di tipo Hunter-Thompson**, ma al momento **non risulta alcuno studio clinico né alcuna pubblicazione** a sostegno di questa ipotesi: la previsione si basa solo sul modello computazionale.

---

## Quadro di sintesi

| Voce | Contenuto |
|------|------|
| Indicazione originale | Artrite reumatoide, cefalea, artrosi, artropatie, artrite idiopatica giovanile, spondiloartropatie, dotto arterioso pervio (dal grafo di conoscenza; il testo delle indicazioni autorizzate AIFA non è disponibile) |
| Nuova indicazione prevista | Displasia acromesomelica, tipo Hunter-Thompson |
| Punteggio di predizione TxGNN | 99,74% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate; nessuna valida) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione può essere ragionevole (o no)?

Per i dati compilati, il meccanismo d'azione dettagliato non è disponibile. In base alle conoscenze generali, l'ibuprofene è un inibitore delle ciclossigenasi COX-1 e COX-2, con effetto antinfiammatorio e analgesico, la cui efficacia nelle patologie articolari infiammatorie e degenerative è nota.

La displasia acromesomelica di tipo Hunter-Thompson è una rara displasia scheletrica causata da varianti con perdita di funzione del gene CDMP1/GDF5, che alterano lo sviluppo della cartilagine (condrogenesi). Si tratta di un difetto strutturale dello sviluppo, che l'inibizione delle COX non può plausibilmente correggere. Nel migliore dei casi, l'ibuprofene potrebbe offrire un sollievo sintomatico dal dolore, che non equivale a una modifica della malattia.

È probabile che l'alta posizione del punteggio rifletta la vicinanza, nel grafo di conoscenza, a termini muscoloscheletrici e artropatici tra le indicazioni originali, più che un reale legame biologico.

**Altre previsioni nella lista (tutte senza studi o pubblicazioni, livello L5, decisione Hold):**

| Rango | Malattia prevista | Punteggio TxGNN | Considerazione |
|---|---|---|---|
| 2 | Sindrome brachiolmia-amelogenesi imperfetta | 99,71% | Nessun legame meccanicistico; al massimo analgesia sintomatica |
| 3 | Miosclerosi | 99,68% | Legame debole e speculativo (componente infiammatoria/dolore); la più plausibile biologicamente tra le candidate |
| 4 | Brachiolmia | 99,67% | Nessun legame meccanicistico |
| 5 | Sindrome brachidattilia-sindattilia | 99,66% | Malformazione congenita; probabile artefatto del grafo |
| 6 | Pseudoacondroplasia | 99,66% | Legame indiretto: possibile sollievo sintomatico del dolore articolare secondario |
| 7 | Sindrome microftalmia colobomatosa-displasia rizomelica | 99,60% | Nessun legame meccanicistico |

---

## Evidenza dagli studi clinici

Al momento non risultano studi clinici correlati registrati.

---

## Evidenza dalla letteratura

Al momento non risulta alcuna letteratura correlata.

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; non vi sono autorizzazioni valide. Il testo delle indicazioni approvate e la forma farmaceutica non sono disponibili nei dati compilati. Si elencano le prime 5 autorizzazioni:

| N. autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 039693066 | BRUFEN 30 cpr rivestite 600 mg | Programmi Sanit. Integrati Srl | Cancellata |
| 022593103 | BRUFEN granulato orale 30 bustine 600 mg | Viatris Italia Srl | Cancellata |
| 043890045 | BRUFEN 30 cpr rivestite 600 mg | New Pharmashop Srl | Cancellata |
| 042859064 | BRUFEN 30 cpr rivestite 600 mg | GMM Farma Srl | Cancellata |
| 026916142 | SPIDIFEN granulato orale 30 bustine 600 mg, aroma cola limone | Zambon Italia Srl | Cancellata |

---

## Considerazioni sulla sicurezza

Le informazioni del foglio illustrativo AIFA (avvertenze e controindicazioni) non sono disponibili; si rimanda al foglio illustrativo.

- **Controindicazioni/condizioni a rischio dal grafo di conoscenza** (non provengono dal testo dell'etichetta): ipertensione, insufficienza epatica e malattie epatiche, malattia renale, ulcera peptica, malattie infiammatorie intestinali, BPCO, epilessia, trombocitopenia, disturbi della coagulazione, ictus e disturbi cerebrovascolari, infarto miocardico, diabete mellito e chetoacidosi diabetica, lupus eritematoso sistemico, ipotiroidismo, ipertrofia prostatica benigna, ipotensione, deficit di potassio, malattie della colecisti, abuso/dipendenza da sostanze.
- **Interazioni farmacologiche**: sono state rilevate 687 interazioni complessive. Tra quelle visibili:
  - **Maggiore**: acido acetilsalicilico.
  - **Moderate**: corticosteroidi (betametasone, budesonide, desametasone, idrocortisone), sulfoniluree e antidiabetici (acetoesamide, clorpropamide, glimepiride, glipizide, gliburide, exenatide), balsalazide, aprepitant, fenfluramina e dexfenfluramina, kanamicina, levofloxacina.
  - **Minori**: famotidina, ranitidina, cimetidina.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si basa solo sul punteggio del modello (livello L5), senza studi clinici né pubblicazioni, e non c'è un meccanismo plausibile per cui un inibitore delle COX possa modificare una displasia scheletrica genetica. In Italia, inoltre, tutte le autorizzazioni sono cancellate.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (ad esempio da DrugBank) e un'analisi dei legami meccanicistici.
- Testo delle avvertenze e delle controindicazioni dal foglio illustrativo AIFA, indispensabile per lo screening di sicurezza.
- Studi preclinici o case report che valutino un beneficio sintomatico (dolore articolare) nelle displasie scheletriche.
- Chiarimento dello stato regolatorio attuale in Italia, dato che non vi sono autorizzazioni valide.
- Se si intende proseguire, valutare in via prioritaria candidate biologicamente più plausibili, come la miosclerosi o la pseudoacondroplasia, limitatamente alla gestione sintomatica.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

