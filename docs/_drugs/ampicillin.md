---
layout: default
title: Ampicillin
parent: Solo previsione del modello (L5)
nav_order: 46
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-04
monitor_inn: "ampicillin"
predicted_indications: ["laryngitis", "Ureaplasma urethritis", "chronic rhinosinusitis", "chronic ethmoidal sinusitis", "gingivitis", "paranasal sinus neoplasm (disease)", "bacterial arthritis", "conjunctivitis", "pericoronitis"]
description: "Ampicillin: nuova indicazione prevista, Laringite (laryngitis) (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Ampicillin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **9** 
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

## Ampicillin: Laringite (laryngitis)
{: .text-alpha }

## Sintesi

L'ampicillina è un antibiotico beta-lattamico che inibisce la sintesi della parete cellulare batterica. Il modello TxGNN la indica come possibile candidata per la **laringite (laryngitis)**, ma nei dati compilati per questo report **nessuno studio clinico** e **nessuna pubblicazione** testa l'ampicillina nella laringite: la letteratura riguarda soprattutto l'epiglottite acuta, la malattia di Whipple e l'otite media. Il livello di evidenza è quindi **L5**.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Laringite (laryngitis) |
| Punteggio di predizione TxGNN | 0.9997 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 2 su 2) |
| Numero di autorizzazioni | 2 (valide: 2) |
| Decisione raccomandata | Hold (sospendere) |

## Perché questa predizione può essere ragionevole?

I dati dettagliati sul meccanismo d'azione non sono al momento disponibili. L'ampicillina appartiene alla classe delle penicilline ad ampio spettro e agisce bloccando la sintesi della parete batterica. Sul piano meccanicistico potrebbe essere rilevante per le forme batteriche delle patologie laringee, come l'epiglottite da *Haemophilus influenzae* di tipo b o gli ascessi laringei e del collo.

Ci sono però forti limiti. La maggior parte delle laringiti è di origine virale, quindi il razionale antibatterico riguarda solo un piccolo sottogruppo. Inoltre, la resistenza dovuta alle beta-lattamasi prodotte da *H. influenzae* limita l'uso dell'ampicillina da sola. L'alto punteggio del modello va quindi interpretato con cautela.

## Evidenze dagli studi clinici

Attualmente non risulta alcuno studio clinico registrato correlato.

## Evidenze dalla letteratura

Nessuna delle pubblicazioni raccolte valuta l'ampicillina nella laringite. Le più vicine sono elencate qui sotto, a titolo di contesto.

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [3026014](https://pubmed.ncbi.nlm.nih.gov/3026014/) | 1986 | Non classificato | Reviews of Infectious Diseases | Sulbactam/ampicillina nell'epiglottite acuta del bambino |
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | Revisione | Anaesthesia and Intensive Care | 161 bambini con epiglottite acuta: complicanze e gestione delle vie aeree |
| [3322611](https://pubmed.ncbi.nlm.nih.gov/3322611/) | 1987 | Non classificato | Clinical Otolaryngology | Batteriologia e principi terapeutici dell'epiglottite acuta dell'adulto |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | Caso clinico/Revisione | Ann Otol Rhinol Laryngol | Ascesso laringeo spontaneo: caso e revisione storica |
| [25944348](https://pubmed.ncbi.nlm.nih.gov/25944348/) | 2015 | Coorte | Otolaryngol Head Neck Surg | Complicanze della laringectomia e scelta dell'antibiotico perioperatorio |
| [1712371](https://pubmed.ncbi.nlm.nih.gov/1712371/) | 1991 | Non classificato | J Clin Gastroenterol | Trattamento antibiotico breve nella malattia di Whipple (non pertinente) |
| [7487676](https://pubmed.ncbi.nlm.nih.gov/7487676/) | 1995 | Preclinico | Auris Nasus Larynx | Ibuprofene più ampicillina nell'otite media sperimentale (chinchilla) |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 036624029 | Ampicillina e sulbactam, 1 fiala IM/EV 500 mg + 250 mg + 1 fiala solvente 1,6 ml (I.B.I. Giovanni Lorenzini SpA) | Non indicata | Non indicata (autorizzazione valida) |
| 036624017 | Ampicillina e sulbactam, 1 fiala IM 1 g + 500 mg + 1 fiala solvente 3,2 ml (I.B.I. Giovanni Lorenzini SpA) | Non indicata | Non indicata (autorizzazione valida) |

Entrambe le autorizzazioni risultano valide.

## Considerazioni sulla sicurezza

**Interazioni farmacologiche:** sono state rilevate 61 interazioni. Tra quelle di livello moderato figurano doxiciclina, minociclina, tetraciclina, balsalazide, kanamicina, lansoprazolo, dexlansoprazolo e acido picosolfurico. Claritromicina è di livello minore. Per altri farmaci, come omeprazolo, pantoprazolo, vancomicina e prednisone, il livello non è classificato.

Per avvertenze e controindicazioni si rimanda al foglio illustrativo.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
- Nessuno studio clinico o pubblicazione testa direttamente l'ampicillina nella laringite, quindi il livello di evidenza è L5. L'alto punteggio TxGNN (0,9997) non basta, e la maggior parte delle laringiti è virale.

**Per procedere sono necessari:**
- Studi che valutino l'ampicillina, o l'associazione ampicillina/sulbactam, specificamente nella laringite batterica
- Definizione del sottogruppo di pazienti con laringite batterica, tenendo conto della resistenza da beta-lattamasi
- Dati sul meccanismo d'azione e sulle avvertenze e controindicazioni del foglio illustrativo AIFA

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

