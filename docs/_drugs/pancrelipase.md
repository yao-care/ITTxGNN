---
layout: default
title: Pancrelipase
parent: Solo previsione del modello (L5)
nav_order: 338
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pancrelipase: nuova indicazione prevista, Disturbo della fosforilazione ossidativa mitocondriale dovuto ad anomalie del DNA nucleare (livello di evidenza L5). Indicazione originale: Insufficienza pancreatica esocrina"
monitor_inn: "pancrelipase"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "pituitary dwarfism", "cytochrome-c oxidase deficiency disease", "primary bone dysplasia", "squamous cell lung carcinoma", "esophageal varices with bleeding", "esophageal varices without bleeding", "leishmaniasis, diffuse cutaneous", "thymic large cell neuroendocrine carcinoma", "pancreatic large cell neuroendocrine carcinoma"]
---

# Pancrelipase
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

## Pancrelipase: Dall'insufficienza pancreatica esocrina al Disturbo della fosforilazione ossidativa mitocondriale dovuto ad anomalie del DNA nucleare
{: .text-alpha }

## Riepilogo in una frase

La pancrelipase è una miscela di enzimi pancreatici (lipasi, proteasi, amilasi) usata per trattare l'insufficienza pancreatica esocrina. Il modello TxGNN la indica come possibile candidata per il **disturbo della fosforilazione ossidativa mitocondriale dovuto ad anomalie del DNA nucleare**, ma **non risultano sperimentazioni cliniche né pubblicazioni** a sostegno di questa ipotesi: la previsione si basa solo sul modello.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Insufficienza pancreatica esocrina |
| Nuova indicazione prevista | Disturbo della fosforilazione ossidativa mitocondriale dovuto ad anomalie del DNA nucleare |
| Punteggio di previsione TxGNN | 0,9999 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 2 su 2) |
| Numero di autorizzazioni | 2 (valide: 2) |
| Decisione raccomandata | Hold |

## Perché questa previsione è (poco) ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. Si sa che la pancrelipase è una miscela di enzimi digestivi somministrata per via orale, che agisce localmente nel lume intestinale con assorbimento sistemico trascurabile.

Le malattie della fosforilazione ossidativa mitocondriale da difetti genici nucleari compromettono la catena respiratoria all'interno della cellula. Un enzima digestivo non assorbito non può plausibilmente agire su questo bersaglio. L'unico beneficio concepibile sarebbe un supporto nutrizionale in caso di malassorbimento, che non modifica il decorso della malattia.

Il punteggio molto alto (0.9999) proviene dal modello TxGNN (deep learning) e può riflettere somiglianze apprese dal modello tra malattie correlate, non una reale evidenza biologica.

Anche le altre previsioni di rango elevato non hanno un legame meccanicistico credibile e restano tutte a livello L5 senza sperimentazioni né letteratura:

| Rango | Malattia prevista | Punteggio TxGNN | Considerazione |
|---|---|---|---|
| 2 | Nanismo ipofisario | 0,9961 | Nessun effetto sull'asse dell'ormone della crescita |
| 3 | Deficit di citocromo-c ossidasi | 0,9959 | Difetto intramitocondriale; stesso artefatto dei disturbi mitocondriali |
| 4 | Displasia ossea primaria | 0,9953 | Difetto genetico strutturale, nessun meccanismo noto |
| 5 | Carcinoma polmonare a cellule squamose | 0,9946 | Nessuna attività antitumorale documentata |
| 6 | Varici esofagee con sanguinamento | 0,9932 | Nessun effetto sull'ipertensione portale; possibile irritazione mucosa |
| 7 | Varici esofagee senza sanguinamento | 0,9932 | Punteggio identico al precedente, previsione duplicata |
| 8 | Leishmaniosi cutanea diffusa | 0,9928 | Nessuna attività antiparassitaria |
| 9 | Carcinoma neuroendocrino a grandi cellule del timo | 0,9927 | Nessun meccanismo antitumorale |
| 10 | Carcinoma neuroendocrino a grandi cellule del pancreas | 0,9914 | Solo supporto sintomatico per l'insufficienza esocrina, non effetto antitumorale |

## Evidenze da sperimentazioni cliniche

Attualmente non risultano sperimentazioni cliniche correlate registrate.

## Evidenze dalla letteratura

Attualmente non risulta letteratura correlata disponibile.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 029018064 | CREON 10.000UI*100 cps gastrores 150 mg rilascio modificato | VIATRIS ITALIA Srl | Valida |
| 047002098 | CREONIPE*100 cps gastrores 420 mg 35.000 U flacone | VIATRIS HEALTHCARE LIMITED | Valida |

## Considerazioni sulla sicurezza

**Interazioni farmacologiche** (18 interazioni di livello moderato registrate):

- **Inibitori delle alfa-glucosidasi** (antidiabetici): acarbosio, miglitolo
- **Folati**: acido folico, levomefolato, levomefolato di calcio, leucovorin
- **Sali di ferro**: ferro, fumarato ferroso, gluconato ferroso, solfato ferroso anidro, ferro proteina succinilato
- **Antiacidi**: idrossido di alluminio, carbonato di calcio, magaldrato, idrossido di magnesio, bicarbonato di sodio
- **Altri**: gliceril fenilbutirrato, chinapril

Per avvertenze e controindicazioni si rimanda al foglietto illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si fonda solo sul modello (L5), senza studi clinici né letteratura, e non esiste alcun legame meccanicistico plausibile tra un enzima digestivo non assorbito e un difetto mitocondriale intracellulare. Inoltre, le autorizzazioni italiane risultano tutte cancellate.

**Per procedere sarebbe necessario:**
- Dati sul meccanismo d'azione (MOA) da DrugBank
- Avvertenze e controindicazioni dal foglietto illustrativo AIFA
- Evidenze precliniche o cliniche che giustifichino un legame biologico con la nuova indicazione
- Chiarimento della situazione autorizzativa in Italia (tutte le licenze sono cancellate)
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

