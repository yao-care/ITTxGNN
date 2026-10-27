---
layout: default
title: Fluticasone
parent: Prove moderate (L3-L4)
nav_order: 208
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-15
description: "Fluticasone: nuova indicazione prevista, Emicrania (migraine disorder) (livello di evidenza L4). Indicazione originale: Non disponibile (testo delle indicazioni assente nelle autorizzazioni…"
monitor_inn: "FLUTICASONE"
predicted_indications: ["migraine disorder", "Prinzmetal angina", "migraine with brainstem aura"]
---

# Fluticasone
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **3** 
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

## Fluticasone: Dall'indicazione originale non documentata all'emicrania (migraine disorder)
{: .text-alpha }

## Sintesi in una frase

Il fluticasone è un corticosteroide glucocorticoide, di cui nei dati compilati per questo report non risulta però un'indicazione originale approvata in Italia (il testo delle indicazioni nelle autorizzazioni AIFA è vuoto). Il modello TxGNN ne prevede un possibile impiego nell'**emicrania (migraine disorder)**, ma a sostegno di questa direzione ci sono **0 studi clinici** e **1 pubblicazione**, che peraltro riguarda eventi avversi neuropsichiatrici e non un beneficio terapeutico.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile (testo delle indicazioni assente nelle autorizzazioni AIFA) |
| Nuova indicazione prevista | Emicrania (migraine disorder) |
| Punteggio di previsione TxGNN | 99,20% |
| Livello di evidenza | L4 |
| Stato sul mercato italiano | Solo autorizzazioni revocate/cessate |
| Numero di autorizzazioni | 20 (0 valide, 20 cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione potrebbe essere ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle conoscenze generali, il fluticasone è un glucocorticoide con attività antinfiammatoria, e la neuroinflammazione e l'infiammazione neurogena sono ritenute possibili contributori alla fisiopatologia dell'emicrania. Questo è però un collegamento solo ipotetico.

L'unica pubblicazione recuperata è una revisione sui corticosteroidi intranasali e sui disturbi neuropsichiatrici (PMID 18681087). Essa riguarda effetti avversi (inclusi cefalea e disturbi dell'umore/comportamento), non un beneficio terapeutico, e non supporta l'efficacia nell'emicrania: se mai, segnala un possibile problema di sicurezza.

Il punteggio elevato di TxGNN (0,992) va quindi interpretato con cautela: in assenza di studi clinici e di un meccanismo dimostrato, il legame meccanicistico resta non accertato.

### Altre previsioni del modello (per completezza)

- **Angina di Prinzmetal** (punteggio 99,19%, livello L5): nessuno studio clinico né pubblicazione. L'angina vasospastica è guidata da vasospasmo coronarico, disfunzione endoteliale e iperreattività della muscolatura liscia; non è stato identificato alcun meccanismo plausibile che colleghi il fluticasone al controllo del vasospasmo. La previsione è verosimilmente un artefatto del grafo di conoscenza.
- **Emicrania con aura del tronco encefalico** (punteggio 99,09%, livello L5): nessuno studio clinico né pubblicazione. Il punteggio riflette probabilmente la vicinanza ontologica al termine genitore "emicrania" e non un'evidenza indipendente.

---

## Evidenze da studi clinici

Al momento non risulta alcuno studio clinico registrato correlato.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [18681087](https://pubmed.ncbi.nlm.nih.gov/18681087/) | 2008 | Revisione | Annals of Allergy, Asthma & Immunology | Revisione dei dati di farmacovigilanza OMS: un insieme inatteso di segnalazioni di disturbi neuropsichiatrici durante l'uso di corticosteroidi intranasali. Non fornisce evidenza di efficacia nell'emicrania. |

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; nessuna è attualmente valida. Il testo delle indicazioni approvate e la forma farmaceutica non sono riportati nei dati compilati. Di seguito le prime 5 autorizzazioni (la forma è desunta dal nome del prodotto).

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 029014014 | FLIXODERM crema derm 30 g 0,5 mg/g (GlaxoSmithKline) | Crema dermatologica | Non disponibile |
| 028667020 | FLIXOTIDE 50 sospensione inalatoria 120 erogazioni 50 mcg (GlaxoSmithKline) | Sospensione per inalazione | Non disponibile |
| 043082015 | FLUTICASONE sospensione inalatoria 120 erogazioni 125 mcg (DOC Generici) | Sospensione per inalazione | Non disponibile |
| 028675104 | FLUSPIRAL sospensione inalatoria 120 dosi 50 mcg (A. Menarini) | Sospensione per inalazione | Non disponibile |
| 028675270 | FLUSPIRAL DISKUS polvere inalatoria 60 dosi 250 mcg (A. Menarini) | Polvere per inalazione | Non disponibile |

---

## Considerazioni sulla sicurezza

- **Interazioni farmacologiche**: sono state identificate 100 interazioni complessive; tra quelle elencate:
  - **Maggiore**: claritromicina.
  - **Moderata**: aprepitant, insulina umana (inalatoria, ad azione rapida).
  - **Livello non classificato**: calcitriolo, fentermina, pantoprazolo, mesalazina, doxiciclina, clotrimazolo, morfina, omeprazolo, lansoprazolo, cimetidina, vancomicina, levocarnitina, nizatidina, triamcinolone, oxandrolone, prednisone, simvastatina.
- Per avvertenze e controindicazioni si rimanda al foglio illustrativo, non disponibile nei dati compilati.
- La revisione di farmacovigilanza (PMID 18681087) segnala possibili disturbi neuropsichiatrici con corticosteroidi intranasali.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si basa quasi esclusivamente sul punteggio del modello TxGNN. Non ci sono studi clinici, l'unica pubblicazione riguarda eventi avversi e non efficacia, il meccanismo non è dimostrato e tutte le autorizzazioni italiane sono cancellate.

**Per procedere è necessario:**
- Recuperare avvertenze e controindicazioni dal foglio illustrativo AIFA (lacuna bloccante per lo screening di sicurezza).
- Acquisire i dati sul meccanismo d'azione (ad es. tramite DrugBank).
- Individuare le indicazioni originali approvate e le forme farmaceutiche.
- Cercare evidenze precliniche o cliniche sull'uso di corticosteroidi nell'emicrania, valutando il segnale neuropsichiatrico.
- Chiarire la compatibilità della via di somministrazione, dato che nessun prodotto è oggi in commercio in Italia.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

