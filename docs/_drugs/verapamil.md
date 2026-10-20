---
layout: default
title: Verapamil
parent: Solo previsione del modello (L5)
nav_order: 462
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Verapamil: nuova indicazione prevista, Blocco di branca (termine obsoleto) (livello di evidenza L5). Indicazione originale: Ipertensione, fibrillazione atriale, sindrome coronarica acuta…"
monitor_inn: "VERAPAMIL"
predicted_indications: ["obsolete bundle branch block", "malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "periodic paralysis with transient compartment-like syndrome"]
---

# Verapamil
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

# Verapamil: Dall'ipertensione e dalle aritmie al blocco di branca (termine obsoleto)

## Sintesi

Il verapamil è un calcio-antagonista di tipo non diidropiridinico, usato originariamente per ipertensione, fibrillazione atriale, sindrome coronarica acuta, angina di Prinzmetal e tachicardia ventricolare.
Il modello TxGNN predice che possa essere efficace per l'**"obsolete bundle branch block"** (blocco di branca, termine classificato come obsoleto) con un punteggio molto alto, ma **senza alcuno studio clinico né pubblicazione** a supporto: la previsione è basata esclusivamente sul modello.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione, fibrillazione atriale, sindrome coronarica acuta, angina di Prinzmetal, tachicardia ventricolare (dal grafo di conoscenza; il testo delle indicazioni AIFA non è disponibile) |
| Nuova indicazione predetta | Blocco di branca (termine obsoleto) |
| Punteggio di predizione TxGNN | 99,62% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 12 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è (poco) ragionevole?

Il verapamil blocca i canali del calcio di tipo L e rallenta la conduzione del nodo atrioventricolare. I dati compilati per questo report non contengono una descrizione dettagliata del meccanismo d'azione; quanto segue si basa sulla conoscenza farmacologica generale.

Il blocco di branca è un difetto di conduzione del sistema His-Purkinje. Rallentare la conduzione non dovrebbe aiutare e potrebbe peggiorare una malattia della conduzione. Inoltre il termine di malattia è contrassegnato come obsoleto: il punteggio elevato è con ogni probabilità un artefatto del grafo di conoscenza e non un segnale biologico reale.

### Altre indicazioni predette (per contesto)

| Indicazione predetta | Punteggio | Livello | Valutazione sintetica |
|------|------|------|------|
| Ipertensione renovascolare maligna | 99,27% | L4 | Link indiretto plausibile (vasodilatazione), ma la patologia dipende dall'asse renina-angiotensina-aldosterone; le due pubblicazioni trovate sono solo tangenziali |
| Nefropatia ipertensiva maligna | 99,27% | L5 | Solo similarità nel grafo; effetto nefroprotettivo non dimostrato |
| Ipertensione polmonare a meccanismo multifattoriale incerto | 99,26% | L5 | Utile solo nel piccolo sottogruppo vasoreattivo; preferiti altri calcio-antagonisti; l'inotropismo negativo preoccupa in caso di disfunzione ventricolare destra |
| Ipertensione polmonare da malattia polmonare/ipossia | 99,26% | L4 | Supporto solo preclinico e indiretto; rischio di peggiorare lo scambio gassioso |
| Sindrome di Braddock | 99,15% | L5 | Nessun legame meccanicistico dimostrato |
| Paralisi periodica con sindrome compartimentale transitoria | 99,08% | L5 | Link teorico (canalopatia), nessuna evidenza; possibile effetto dannoso |

## Evidenze da studi clinici

Attualmente non risultano studi clinici registrati correlati al blocco di branca.

## Evidenze dalla letteratura

Attualmente non è disponibile alcuna letteratura correlata al blocco di branca.

## Informazioni sul mercato italiano

Tutte le 12 autorizzazioni risultano cancellate; non vi sono autorizzazioni valide. Il testo dell'indicazione approvata e la forma farmaceutica non sono riportati nei dati. Si elencano le prime 5:

| Numero di autorizzazione | Prodotto | Titolare | Stato |
|------|------|------|------|
| 034255048 | Verapamil 240 mg, 30 capsule a rilascio prolungato | DOC Generici Srl | Cancellata |
| 032100036 | Verapamil 240 mg, 30 compresse a rilascio modificato | EG SpA | Cancellata |
| 020609071 | Isoptin, 5 fiale EV 5 mg/2 ml | Viatris Italia Srl | Cancellata |
| 032100024 | Verapamil 120 mg, 30 compresse a rilascio modificato | EG SpA | Cancellata |
| 020609044 | Isoptin 120 mg, 30 compresse a rilascio prolungato | Viatris Italia Srl | Cancellata |

## Considerazioni sulla sicurezza

I dati di sicurezza tratti dal foglio illustrativo AIFA non sono disponibili. Di seguito le informazioni disponibili da altre fonti.

- **Condizioni associate a controindicazione (dal grafo di conoscenza, non dal foglio illustrativo)**: blocco atrioventricolare, scompenso cardiaco, ipotensione, stenosi aortica, cardiomiopatia ipertrofica, tachicardia ventricolare, miastenia gravis, malattie renali ed epatiche, neutropenia/agranulocitosi, angioedema, malattie del tessuto connettivo, delle ossa e della cartilagine, ostruzione dell'arteria renale. Nel caso del blocco di branca, il rischio di peggiorare la conduzione è particolarmente rilevante.
- **Interazioni farmacologiche** (100 interazioni totali; esempi):
  - **Maggiore**: loperamide.
  - **Moderata**: cimetidina, claritromicina, metformina, bupropione, aprepitant, acido acetilsalicilico, canagliflozin, corticosteroidi (idrocortisone, desametasone, betametasone, triamcinolone, budesonide) e sali di calcio.
  - **Minore**: morfina.

Per le informazioni complete fare riferimento al foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per il blocco di branca non ha alcun supporto clinico o bibliografico (L5), il meccanismo del verapamil è potenzialmente sfavorevole per i difetti di conduzione e il termine di malattia è obsoleto. Inoltre, in Italia non esistono autorizzazioni valide.

**Per procedere sarebbe necessario:**
- Verificare se il termine obsoleto corrisponda a una malattia attuale e rivalutare la previsione su di essa
- Acquisire i dati di meccanismo d'azione e il foglio illustrativo AIFA (avvertenze e controindicazioni)
- Valutare in alternativa le indicazioni con link più plausibile (ipertensione renovascolare maligna, ipertensione polmonare vasoreattiva) tramite ricerca bibliografica mirata
- Chiarire lo stato regolatorio attuale del verapamil in Italia (autorizzazioni tutte cancellate)
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

