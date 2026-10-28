---
layout: default
title: Nabumetone
parent: Solo previsione del modello (L5)
nav_order: 314
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "NABUMETONE"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "WHIM syndrome", "rheumatoid nodulosis"]
description: "Nabumetone: nuova indicazione prevista, Displasia acromesomelica, tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) (livello di evidenza L5). Indicazione originale: Non riportata n…"
---

# Nabumetone
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

## Nabumetone: Displasia acromesomelica, tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)
{: .text-alpha }

## Riepilogo in una frase

Il nabumetone è un farmaco antinfiammatorio non steroideo (FANS), originariamente utilizzato per artrite reumatoide, osteoartrosi e artropatie.
Il modello TxGNN ne prevede un possibile effetto sulla **displasia acromesomelica di tipo Hunter-Thompson**, ma al momento **non risulta alcuna sperimentazione clinica né pubblicazione** a supporto: la previsione si basa solo sul modello computazionale.

## Quadro d'insieme

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Displasia acromesomelica, tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) |
| Punteggio di previsione TxGNN | 0.9999 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 2 su 2) |
| Numero di autorizzazioni | 2 (valide: 2) |
| Decisione raccomandata | Hold |

## Perché questa previsione è ragionevole (o no)?

Il meccanismo d'azione dettagliato non è attualmente disponibile nei dati compilati. In generale il nabumetone è un inibitore della ciclo-ossigenasi (COX) con effetto antinfiammatorio e analgesico, il cui valore è consolidato nelle patologie articolari infiammatorie e degenerative.

La displasia acromesomelica di tipo Hunter-Thompson è una displasia scheletrica genetica, legata a perdita di funzione di CDMP1/GDF5, che altera la crescita di cartilagine e ossa. Il nabumetone può dare al massimo un sollievo sintomatico del dolore, ma **non agisce sul difetto di segnalazione di GDF5**. Il punteggio molto alto del modello è verosimilmente dovuto alla vicinanza nella rete di conoscenza a termini scheletrici e artropatici, più che a una reale base biologica. Non si ravvisa quindi un legame meccanicistico solido.

### Altre previsioni nella lista (prime 10)

| Rango | Malattia prevista | Punteggio | Plausibilità biologica |
|------|------|------|------|
| 1 | Displasia acromesomelica, tipo Hunter-Thompson | 0,9999 | Nessun legame; solo sintomatico |
| 2 | Sindrome brachiolmia-amelogenesi imperfetta | 0,9999 | Nessun legame plausibile |
| 3 | Miosclerosi | 0,9999 | Debole e indiretta |
| 4 | Sindrome microftalmia colobomatosa-displasia rizomelica | 0,9999 | Nessun legame |
| 5 | Brachiolmia | 0,9999 | Nessun ruolo modificante la malattia |
| 6 | Sindrome brachidattilia-sindattilia | 0,9999 | Nessun legame |
| 7 | Pseudoacondroplasia | 0,9998 | Solo gestione sintomatica del dolore articolare |
| 8 | Spondiloartropatia (suscettibilità) | 0,9994 | La più plausibile: i FANS sono terapia di prima linea |
| 9 | Sindrome WHIM | 0,9994 | Nessun legame (via CXCR4) |
| 10 | Noduli reumatoidi (nodulosi reumatoide) | 0,9993 | Plausibile solo per associazione |

Tra queste, la **spondiloartropatia** è la candidata biologicamente più coerente, perché i FANS sono la terapia di prima linea in questo ambito. Tuttavia i dati compilati non contengono studi su di essa; una ricerca bibliografica mirata potrebbe portare il livello di evidenza almeno a L4.

## Evidenze dalle sperimentazioni cliniche

Attualmente non risulta alcuna sperimentazione clinica correlata registrata.

## Evidenze dalla letteratura

Attualmente non è disponibile alcuna letteratura correlata.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 026673057 | NABUSER 30 compresse rivestite 1 g (Pharmaday Pharm. Srl Unipersonale) | Compresse rivestite | Non disponibile (autorizzazione valida) |
| 026673069 | NABUSER granulato orale 30 bustine 1 g (Pharmaday Pharm. Srl Unipersonale) | Granulato orale | Non disponibile (autorizzazione valida) |

Entrambe le autorizzazioni risultano cancellate: oggi non esiste in Italia un prodotto a base di nabumetone con autorizzazione valida, il che limita lo sviluppo pratico.

## Considerazioni sulla sicurezza

- **Controindicazioni segnalate dal grafo di conoscenza** (non derivano dal foglietto illustrativo): ipertensione/disturbi ipertensivi, malattie renali, pioureterе, malattie epatiche, malattie della colecisti, ulcera peptica (anche attiva), abuso/dipendenza da sostanze, disturbi della coagulazione, infarto miocardico, trombosi coronarica, emoglobinopatie, malattie cardiovascolari e cardiache.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni; tra quelle visualizzate:
  - Gravità moderata: acido acetilsalicilico, corticosteroidi (idrocortisone, desametasone, betametasone, budesonide, triamcinolone), metformina, glimepiride, clorpropamide, mesalazina, balsalazide, vancomicina, citrato e bicarbonato di potassio, acido picosolfurico, polietilenglicole con elettroliti, solfato di sodio.
  - Gravità lieve: ranitidina, cimetidina, linaclotide.

Per avvertenze e controindicazioni ufficiali si rimanda al foglietto illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per la displasia acromesomelica di tipo Hunter-Thompson non ha alcun supporto clinico o bibliografico e nessun legame meccanicistico con l'azione del nabumetone, che potrebbe offrire al massimo sollievo sintomatico. Inoltre, il farmaco non ha autorizzazioni valide in Italia.

**Per procedere sarebbe necessario:**
- Recuperare i dati sul meccanismo d'azione (MOA) del nabumetone.
- Acquisire avvertenze e controindicazioni dal foglietto illustrativo AIFA, indispensabili per lo screening di sicurezza.
- Valutare, con una ricerca bibliografica mirata, indicazioni più plausibili come la spondiloartropatia.
- Verificare la fattibilità regolatoria, dato che tutte le autorizzazioni italiane sono cancellate.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

