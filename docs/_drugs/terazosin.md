---
layout: default
title: Terazosin
parent: Solo previsione del modello (L5)
nav_order: 428
evidence_level: L5
indication_count: 10
---

# Terazosin
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

# Terazosina: dall'ipertensione e iperplasia prostatica benigna alla perdita di capelli (ipotricosi semplice del cuoio capelluto)

## Sintesi in una frase

La terazosina è un alfa-1 bloccante adrenergico, utilizzato in origine per il trattamento dell'ipertensione e dell'iperplasia prostatica benigna.
Il modello TxGNN prevede una possibile efficacia per l'**ipotricosi semplice del cuoio capelluto**, ma **non risultano studi clinici né pubblicazioni** a sostegno di questa indicazione: si tratta di una previsione puramente computazionale.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione e iperplasia prostatica benigna (dal grafo di conoscenza; i testi autorizzativi AIFA non riportano l'indicazione) |
| Nuova indicazione prevista | Ipotricosi semplice del cuoio capelluto |
| Punteggio di previsione TxGNN | 99,97% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni annullate |
| Numero di autorizzazioni | 20 (tutte annullate) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione potrebbe essere ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle conoscenze generali, la terazosina è un alfa-1 bloccante: riduce la vasocostrizione mediata dal sistema simpatico e il tono della muscolatura liscia, e per questo è impiegata nell'ipertensione e nei sintomi urinari da ipertrofia prostatica.

Un legame con la perdita di capelli è ipotizzabile solo in modo speculativo, ad esempio attraverso un effetto vasodilatatore sul cuoio capelluto, analogo a quanto noto per il minoxidil. Questo effetto non è dimostrato per la terazosina e i dati compilati non supportano alcun nesso meccanicistico. Il punteggio elevato del modello non è accompagnato da alcuna prova clinica o bibliografica.

### Altre previsioni del modello e relativa evidenza

Per completezza, tra le prime 10 previsioni alcune dispongono di una letteratura minima:

| Indicazione prevista | Punteggio TxGNN | Evidenza | Note |
|------|------|------|------|
| Emicrania | 99,92% | L4 | Due pubblicazioni (1994, 1997), piccole e datate; domanda di ricerca |
| Malattia di Raynaud | 99,83% | L4 | Una pubblicazione del 1997; meccanismo plausibile (riduzione della vasocostrizione simpatica); domanda di ricerca |
| Alopecia | 99,95% | L4 | Solo una revisione generale del 2022 sugli effetti extracardiaci dei farmaci cardiovascolari |
| Altre (alopecia areata diffusa, ipotricosi congenita, ecc.) | 99,5–99,97% | L5 | Solo previsione, nessuna evidenza |

---

## Evidenze da studi clinici

Al momento non risultano studi clinici registrati relativi a questa indicazione.

---

## Evidenze dalla letteratura

Per l'indicazione principale (ipotricosi semplice del cuoio capelluto) non è disponibile letteratura correlata.

Per la previsione affine **alopecia** è stata individuata una pubblicazione, di valore indiretto:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [34779371](https://pubmed.ncbi.nlm.nih.gov/34779371/) | 2022 | Revisione | Current Cardiology Reviews | Effetti extracardiaci dei farmaci cardiovascolari (ad es. minoxidil e crescita dei peli); il ruolo specifico della terazosina non è verificabile |

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano annullate; nessuna è attualmente valida. Principali prodotti:

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 035046022 | Terafluss, 14 cpr div 5 mg | Viatris Italia Srl | Annullata |
| 035295120 | Terazosina, 14 cpr 5 mg | Teva Italia Srl | Annullata |
| 028652028 | Unoprost, 14 cpr div 5 mg | Laboratori Guidotti SpA | Annullata |
| 026929036 | Itrin, 14 cpr 5 mg | Eberlife Farmaceutici SpA | Annullata |
| 035622024 | Terazosina, 14 cpr div 5 mg | DOC Generici Srl | Annullata |

---

## Considerazioni di sicurezza

- **Controindicazioni (dal grafo di conoscenza, non dal foglietto illustrativo):** atrofia multisistemica, sindrome da tachicardia posturale ortostatica, ipotensione ortostatica, priapismo, sindrome dell'iride flaccida intraoperatoria.
- **Interazioni farmacologiche:** rilevate 137 interazioni. Quelle di livello moderato comprendono corticosteroidi (idrocortisone, desametasone, betametasone, budesonide, prednisone, prednisolone, triamcinolone), bupropione, oppioidi (morfina, oppio), cannabinoidi (dronabinolo, nabilone) e inibitori di SGLT2 (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin).

Per le avvertenze complete si rimanda al foglietto illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
L'indicazione prevista si basa solo sul punteggio del modello (livello L5), senza studi clinici, letteratura né un meccanismo plausibile. Inoltre tutte le autorizzazioni italiane sono annullate, il che limita la praticabilità immediata.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (ad es. da DrugBank) e valutazione di un nesso con la biologia del follicolo pilifero
- Avvertenze e controindicazioni dal foglietto illustrativo AIFA (lacuna bloccante per la valutazione di sicurezza)
- Studi preclinici o pilota sull'alopecia/ipotricosi
- Valutazione dello stato regolatorio, dato che non esistono autorizzazioni valide in Italia
- Come alternativa più promettente, approfondire le domande di ricerca su **malattia di Raynaud** ed **emicrania**, dove esiste almeno una letteratura preliminare, previa verifica del disegno e dei risultati degli studi originali
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

