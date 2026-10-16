---
layout: default
title: Pentamidine
parent: Solo previsione del modello (L5)
nav_order: 344
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Pentamidine: nuova indicazione prevista, Cheratocongiuntivite epiteliale puntata (livello di evidenza L5). Indicazione originale: Pneumocistosi, tripanosomiasi africana umana…"
---

# Pentamidine
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

# Pentamidina: dalla polmonite da Pneumocystis alla cheratocongiuntivite epiteliale puntata

## Sintesi

La pentamidina è un farmaco antimicrobico utilizzato originariamente per la pneumocistosi e per la tripanosomiasi (compresa la tripanosomiasi africana umana). Il modello TxGNN la indica come potenzialmente efficace per la **cheratocongiuntivite epiteliale puntata**, ma al momento **non risultano studi clinici né pubblicazioni** a sostegno di questa direzione: la previsione è solo computazionale.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Pneumocistosi, tripanosomiasi africana umana, tripanosomiasi (dal grafo di conoscenza; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Cheratocongiuntivite epiteliale puntata |
| Punteggio di predizione TxGNN | 99,73% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 1 (revocata) |
| Decisione raccomandata | Hold |

## Perché questa previsione potrebbe essere ragionevole?

I dati compilati per questo report non includono il meccanismo d'azione della pentamidina. Sulla base delle informazioni note, la pentamidina è un agente antimicrobico (antiprotozoario e antifungino) la cui efficacia è documentata nelle infezioni sopra citate. Un legame con una cheratocongiuntivite di origine infettiva potrebbe essere ipotizzato in teoria, ma si tratta di una speculazione non supportata da alcuna evidenza.

Il punteggio elevato (0,997) è una previsione basata sul grafo di conoscenza. Le altre previsioni ad alto punteggio (cheratopatia neurotrofica, cheratite da esposizione, "malattia animale non umana", analbuminemia congenita) non hanno nemmeno un plausibile collegamento meccanicistico: alcune sono probabilmente artefatti del grafo, e "malattia animale non umana" è una categoria ontologica non clinica.

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

Attualmente non è disponibile letteratura correlata.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 027625019 | PENTACARINAT*1 fiala IM EV aerosol 300 mg (SANOFI Srl), revocata | Fiala (IM/EV/aerosol) | Non disponibile |

## Considerazioni sulla sicurezza

I dati di sicurezza tratti dal foglio illustrativo non sono disponibili. Si rimanda al foglio illustrativo per le avvertenze e le controindicazioni.

- **Controindicazioni/condizioni a rischio (dal grafo di conoscenza, non da testo di etichetta)**: ipertensione e ipotensione, torsione di punta, arresto cardiaco improvviso, malattie della conduzione cardiaca, malattie renali, malattie epatiche, malattie della colecisti, pancreatite, trombocitopenia, leucopenia, anemia (inclusa la macrocitica), iperglicemia, ipoglicemia, diabete mellito, chetoacidosi diabetica, asma (anche intrinseca e allergica), ipercalcemia, nefrocalcinosi, disturbi del metabolismo del fosforo, piourete.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni; tra le principali (livello moderato) figurano:
  - antidiabetici (acarbose, metformina, pioglitazone, alogliptin, albiglutide, canagliflozin, dapagliflozin, clorpropamide);
  - amfotericina B (anche in complesso lipidico);
  - claritromicina;
  - inibitori di pompa protonica e anti-H2 (omeprazolo, rabeprazolo, famotidina);
  - lassativi e preparati intestinali (bisacodile, acido picosolfurico, polietilenglicole con elettroliti);
  - loperamide, mesalazina e balsalazide.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si basa solo sul modello (livello L5), senza studi clinici né letteratura, e senza un meccanismo plausibile. In Italia l'unica autorizzazione è revocata e il profilo di rischio (cardiaco, metabolico, renale, ematologico) è rilevante per un'eventuale nuova indicazione oftalmica.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) da DrugBank
- Avvertenze e controindicazioni dal foglio illustrativo AIFA (lacuna bloccante per la valutazione di sicurezza)
- Ricerca di evidenze preclinico-sperimentali o letteratura sull'uso oculare della pentamidina
- Valutazione della compatibilità della via di somministrazione (formulazione oftalmica topica non disponibile)
- Verifica di indicazioni più specifiche tra quelle previste, escludendo categorie non cliniche
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

