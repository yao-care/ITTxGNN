---
layout: default
title: Amlodipine
parent: Solo previsione del modello (L5)
nav_order: 44
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Amlodipine: nuova indicazione prevista, Emorragia intracerebrale (indicazione con le evidenze più forti (livello di evidenza L5). Indicazione originale: Ipertensione, angina di Prinzmetal…"
---

# Amlodipine
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
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

# Amlodipina: dall'ipertensione all'ictus emorragico (emorragia intracerebrale)

## Sintesi

L'amlodipina è un calcio-antagonista diidropiridinico, usato originariamente per ipertensione e angina di Prinzmetal, con indicazioni correlate al rischio cerebrovascolare (ictus, infarto cerebrale). Il modello TxGNN la indica come possibile candidata per diverse nuove indicazioni; quella con il supporto più solido è l'**emorragia intracerebrale** (punteggio 99,79%), sostenuta da **4 studi clinici** e **9 pubblicazioni** nei dati compilati. Il beneficio è però legato a una combinazione a basso dosaggio di tre antipertensivi e non all'amlodipina da sola.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione, angina di Prinzmetal, ictus/infarto cerebrale (da archi di indicazione del grafo di conoscenza; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Emorragia intracerebrale (indicazione con le evidenze più forti; la prima per punteggio è l'infarto del tronco encefalico, solo predizione) |
| Punteggio di predizione TxGNN | 99,79% (emorragia intracerebrale); 99,94% per l'infarto del tronco encefalico |
| Livello di evidenza | L2 (emorragia intracerebrale) |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 20 (tutte revocate) |
| Decisione raccomandata | Proceed with Guardrails (procedere con cautele) |

Nota: i dati compilati classificano la prima indicazione in graduatoria (infarto del tronco encefalico) come solo predizione (L5, Hold). Il report si concentra sull'emorragia intracerebrale perché è l'unica con uno studio di fase 3 completato.

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle informazioni note, l'amlodipina agisce come modulatore dei canali del calcio di tipo L (Cav1.2 e Cav1.3), con conseguente vasodilatazione arteriosa e riduzione della pressione arteriosa. Il suo effetto antipertensivo è consolidato.

Il controllo pressorio è il principale fattore modificabile per prevenire la recidiva di emorragia intracerebrale. L'amlodipina è uno dei componenti della "triple pill" a basse dosi testata nello studio TRIDENT. Per questo la predizione appare coerente con le indicazioni originali, anche se si tratta in sostanza di un'estensione dell'uso antipertensivo e non di un meccanismo nuovo.

Per l'indicazione "occlusione dell'arteria cerebrale" esistono inoltre studi preclinici (modelli animali) in cui l'amlodipina, da sola o con atorvastatina, riduce il danno neuronale con effetti antiossidanti e antiapoptotici. Si tratta di evidenza indiretta (livello L3, lettura generosa; L4 è difendibile).

## Evidenze dagli studi clinici

| Studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Fase 3 | Completato | 1671 | TRIDENT: pillola con tre antipertensivi a basse dosi vs placebo per prevenire l'ictus ricorrente dopo emorragia intracerebrale; è la fonte principale, ma l'effetto è a livello di combinazione |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | Non applicabile | In reclutamento | 140 | Terapia antipertensiva tripla dopo emorragia intracerebrale; piccolo, in corso, senza risultati |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | Non applicabile | Terminato | 4 | Sotto-studio MRI di TRIDENT; non informativo |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Fase 3 | Terminato | 1 | Sotto-studio cognitivo di TRIDENT; non informativo |

Per l'occlusione dell'arteria cerebrale, lo studio [NCT00805311](https://clinicaltrials.gov/study/NCT00805311) (fase 4, terminato, 400 partecipanti) confronta endoarterectomia carotidea e terapia medica ottimale, senza isolare l'amlodipina.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/) | 2026 | RCT (rapporto primario) | N Engl J Med | Tre antipertensivi a basse dosi in un'unica pillola dopo emorragia intracerebrale, per ridurre la pressione e il rischio di ictus ricorrente |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Protocollo/disegno | Int J Stroke | Razionale e disegno dello studio TRIDENT |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Revisione (indiretta) | Cardiovasc Drugs Ther | Uso e efficacia comparativa dei calcio-antagonisti nell'ipertensione |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Caso clinico | Ann Pharmacother | Probabile angioedema da amlodipina in un paziente con ictus emorragico talamico |

Per l'occlusione dell'arteria cerebrale, le evidenze preclinica (ratti e topi) includono [21538457](https://pubmed.ncbi.nlm.nih.gov/21538457/), [17070425](https://pubmed.ncbi.nlm.nih.gov/17070425/), [20971084](https://pubmed.ncbi.nlm.nih.gov/20971084/) e [21276424](https://pubmed.ncbi.nlm.nih.gov/21276424/), con riduzione dell'area di infarto.

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano revocate. Il testo delle indicazioni approvate e la forma farmaceutica non sono disponibili nei dati compilati. Le principali:

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 044428035 | NORVASC 14 cpr 10 mg | Compresse | Non disponibile |
| 038092021 | AMLODIPINA 14 cpr 10 mg (DOC Generici) | Compresse | Non disponibile |
| 038056014 | LOSEDIN 28 cpr 5 mg | Compresse | Non disponibile |
| 027428010 | NORVASC 28 cpr 5 mg (Viatris Pharma) | Compresse | Non disponibile |
| 037479060 | AMLODIPINA 28 cpr 5 mg (EG) | Compresse | Non disponibile |

## Considerazioni sulla sicurezza

Il foglietto illustrativo AIFA non è stato reperito; si rimanda quindi al foglietto illustrativo per avvertenze e controindicazioni ufficiali.

- **Controindicazioni (dal grafo di conoscenza, non dal testo del foglietto)**: insufficienza epatica e malattie epatiche, malattie renali, pancreatite, malattie della colecisti, ipotiroidismo, angioedema (incluso quello ereditario e da bloccanti del sistema renina-angiotensina-aldosterone), lupus eritematoso sistemico, miopatie, paralisi periodica familiare, diabete e chetoacidosi diabetica, neutropenia e agranulocitosi, disturbi ipotensivi, iperparatiroidismo.
- **Segnali dalla letteratura**: un caso di angioedema probabilmente da amlodipina (PMID 19299323); un caso di edema polmonare non cardiogenico ed emorragia alveolare dopo sovradosaggio (PMID 35261597).
- **Interazioni**: nei dati compilati compaiono solo interazioni farmacologiche con bersagli (P2X4, Cav1.2, Cav1.3), non interazioni con altri farmaci.

## Conclusione e prossimi passi

**Decisione: Proceed with Guardrails**

**Motivazione:**
Esiste uno studio di fase 3 completato (TRIDENT, n=1671) con risultati pubblicati nel 2026, ma l'intervento è una combinazione di tre farmaci, quindi il contributo dell'amlodipina non è separabile; inoltre il beneficio passa dalla riduzione pressoria e non da un meccanismo nuovo. Per questo il livello è L2 e non L1. Le altre indicazioni previste sono per lo più solo predizioni (L5, Hold).

**Per procedere sono necessari:**
- Verifica degli esiti di TRIDENT (risultato positivo e attribuibile a un regime contenente amlodipina) per valutare un eventuale livello L1
- Dati dettagliati sul meccanismo d'azione (MOA)
- Scarico e analisi del foglietto illustrativo AIFA per avvertenze e controindicazioni
- Chiarimento della situazione regolatoria: tutte le autorizzazioni italiane risultano revocate
- Piano di monitoraggio della sicurezza (ipotensione, angioedema, funzione epatica e renale)
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

