---
layout: default
title: Cyclosporine
parent: Prove moderate (L3-L4)
nav_order: 131
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-15
description: "Cyclosporine: nuova indicazione prevista, Malattia granulomatosa cronica, autosomica recessiva (livello di evidenza L4). Indicazione originale: Artrite reumatoide, sindrome dell'occhio secco, xerofta…"
monitor_inn: "Cyclosporine"
predicted_indications: ["granulomatous disease, chronic, autosomal recessive", "brain aneurysm", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "congenital ichthyosiform erythroderma", "fetal erythroblastosis", "brachydactyly-syndactyly syndrome", "prolapse of lacrimal gland"]
---

# Cyclosporine
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **7** 
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

# Ciclosporina: Dalla secchezza oculare/artrite reumatoide alla malattia granulomatosa cronica autosomica recessiva

## Sintesi in una frase

La ciclosporina è un immunosoppressore inibitore della calcineurina, originariamente impiegato per artrite reumatoide, sindrome dell'occhio secco, xeroftalmia e sindrome di Sjögren.
Il modello TxGNN prevede una possibile efficacia nella **malattia granulomatosa cronica autosomica recessiva**, ma i dati compilati per questo report non includono **nessuno studio clinico** e solo **1 pubblicazione**, che riguarda il trapianto di cellule staminali e non l'efficacia della ciclosporina.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Artrite reumatoide, sindrome dell'occhio secco, xeroftalmia, sindrome di Sjögren (da grafo di conoscenza; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Malattia granulomatosa cronica, autosomica recessiva |
| Punteggio di predizione TxGNN | 99,68% |
| Livello di evidenza | L4 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 15 (tutte cancellate; 0 valide) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione può essere ragionevole?

Al momento i dati dettagliati sul meccanismo d'azione non sono disponibili nei dati compilati. In base alle conoscenze generali, la ciclosporina inibisce la calcineurina e quindi l'attivazione dei linfociti T. Nella malattia granulomatosa cronica le complicanze infiammatorie e granulomatose sono mediate dal sistema immunitario, quindi un'immunosoppressione potrebbe in teoria avere un ruolo.

Tuttavia il collegamento è debole. L'unica pubblicazione disponibile riguarda gli esiti del trapianto di cellule staminali emopoietiche nella malattia granulomatosa cronica, contesto in cui la ciclosporina potrebbe al massimo far parte della profilassi della malattia del trapianto contro l'ospite. Non dimostra alcuna efficacia terapeutica della ciclosporina per la malattia in sé. Il punteggio molto elevato del modello non è supportato da dati clinici.

---

## Evidenze da studi clinici

Al momento non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [22078471](https://pubmed.ncbi.nlm.nih.gov/22078471/) | 2012 | Coorte | The Journal of Allergy and Clinical Immunology | Ottima sopravvivenza dopo trapianto di cellule staminali da donatore fratello o non consanguineo nella malattia granulomatosa cronica; non valuta la ciclosporina come terapia |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 029453040 | Sandimmun Neoral soluzione orale 50 ml 100 mg/ml (Novartis) | Soluzione orale | Non disponibile |
| 029453053 | Sandimmun Neoral 50 capsule molli 10 mg (Novartis) | Capsule molli | Non disponibile |
| 042787275 | Ciqorin 50 capsule molli 50 mg (Teva Italia) | Capsule molli | Non disponibile |
| 046918049 | Verkazia collirio emulsione 1 mg/ml (Santen) | Collirio in emulsione | Non disponibile |
| 044013011 | Ikervis collirio emulsione 1 mg/ml (Santen) | Collirio in emulsione | Non disponibile |

Tutte le 15 autorizzazioni risultano cancellate; di queste sono elencate le 5 principali.

---

## Considerazioni di sicurezza

- **Controindicazioni da grafo di conoscenza (non da scheda tecnica)**: il grafo TxGNN associa la ciclosporina a malattie quali ipertensione, epilessia, malattie renali ed epatiche, malattie infettive (anche oculari), ipertrigliceridemia, iperbilirubinemia, sindrome di Gilbert, porpora trombocitopenica, ipertensione intracranica/pseudotumor cerebri, neoplasie, linfomi (incluso il linfoma primitivo del sistema nervoso centrale) e malattie cerebrali. Si tratta di associazioni del grafo e non del testo ufficiale di scheda tecnica.
- **Interazioni e target farmacologici**: sono stati identificati 7 target/trasportatori con cui la ciclosporina interagisce: FPR1, ABCG2, SLC10A1 (cotrasportatore sodio/acidi biliari), OATP1B1, OATP1B3, peptidilprolil isomerasi A (PPIA) e peptidilprolil isomerasi D (PPID). Non sono disponibili livelli di gravità.

Per le avvertenze e le controindicazioni ufficiali si rimanda alla scheda tecnica.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Non esistono studi clinici né letteratura che colleghino direttamente la ciclosporina alla malattia granulomatosa cronica; l'elevato punteggio TxGNN rimane una predizione computazionale. Inoltre, in Italia tutte le autorizzazioni sono attualmente cancellate e i dati di sicurezza ufficiali mancano.

**Per procedere è necessario:**
- Acquisire il foglio illustrativo AIFA (avvertenze e controindicazioni) per consentire lo screening di sicurezza
- Ottenere i dati sul meccanismo d'azione (MOA) da DrugBank
- Reperire evidenze cliniche o precliniche specifiche sull'uso della ciclosporina nella malattia granulomatosa cronica
- Chiarire la situazione autorizzativa in Italia (tutte le licenze risultano cancellate)
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

