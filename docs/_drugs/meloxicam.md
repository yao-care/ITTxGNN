---
layout: default
title: Meloxicam
parent: Solo previsione del modello (L5)
nav_order: 143
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

# Meloxicam: dall'Artrite e Gestione del Dolore alla Displasia Acromesomelica (Tipo Hunter-Thompson)

## Riepilogo in Una Frase

Meloxicam è un FANS con preferenza per la COX-2 ampiamente consolidato nel trattamento di patologie muscoloscheletriche infiammatorie come l'osteoartrosi e l'artrite reumatoide.
La previsione di primo livello del modello TxGNN è la **Displasia Acromesomelica, Tipo Hunter-Thompson**, una rara displasia scheletrica genetica causata da mutazioni nel percorso GDF5/BMPR1B.
Attualmente **0 studi clinici** e **0 pubblicazioni** supportano questa direzione di repurposing specifica, collocando l'evidenza fermamente al Livello **L5**.

---

## Panoramica Rapida

| Voce | Contenuto |
|------|---------|
| Indicazione Originale | Non disponibile (nessuna autorizzazione AIFA nel dataset) |
| Nuova Indicazione Prevista | Displasia Acromesomelica, Tipo Hunter-Thompson |
| Punteggio di Previsione TxGNN | 99.92% |
| Livello di Evidenza | L5 |
| Stato di Commercializzazione in Italia | ✗ Non Commercializzato (per dataset) |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | Sospendere |

---

## Perché Questa Previsione È Ragionevole?

Attualmente, i dati dettagliati sul meccanismo di azione non sono disponibili dal dataset. Basato sulla conoscenza farmacologica consolidata, il meloxicam è un inibitore preferenziale della COX-2 appartenente alla classe degli oxicam tra gli FANS. Riduce l'infiammazione e il dolore principalmente bloccando la cicloossigenasi-2, sopprimendo così la sintesi della prostaglandina E2 (PGE2) nei siti di infiammazione e nel sistema nervoso centrale. La sua efficacia nelle artropatie infiammatorie croniche è supportata da decenni di uso clinico a livello globale.

La Displasia Acromesomelica, Tipo Hunter-Thompson (AMDH) è una rara displasia scheletrica autosomica recessiva causata da mutazioni loss-of-function nei geni GDF5 o BMPR1B, che governano la morfogenesi ossea e cartilaginea durante lo sviluppo embrionale degli arti. Il ponte meccanicistico proposto è estremamente fragile: COX-2/PGE2 è noto per modulare la segnalazione BMP a valle in alcuni modelli di differenziamento cartilagineo, il che significa che l'inibizione della COX-2 potrebbe teoricamente influenzare i percorsi condrogenici. Tuttavia, questa connessione è interamente indiretta e non è stata convalidata sperimentalmente in nessun modello AMDH, studio su animali o studio su tessuto umano.

La spiegazione più probabile per il punteggio elevato del TxGNN è la **topologia del grafo di conoscenza**: il meloxicam è densamente collegato ai nodi delle patologie muscoloscheletriche e infiammatorie, e l'AMDH si raggruppa vicino ad altre malattie scheletriche nel grafo. I modelli GNN sono noti per propagare punteggi elevati attraverso nodi di malattia topologicamente adiacenti indipendentemente dalla plausibilità biologica. Questa previsione dovrebbe essere trattata come un artefatto di grafo piuttosto che come un segnale farmacologico. In particolare, tra tutte e dieci le previsioni, gli obiettivi clinicamente più coerenti — **Spondilartropatia (rank 6)**, **Nodulosi Reumatoide (rank 7)** e **JIA Poliarticolare RF-positiva (rank 8)** — segnano un punteggio inferiore precisamente perché appaiono più lontani dal vicinato di grafo del farmaco, sebbene siano molto migliori dal punto di vista meccanicistico.

> ⚠️ **Avviso Critico sulla Qualità dei Dati — Rank 6 (Spondilartropatia):** Gli FANS incluso il meloxicam sono **terapia di prima linea secondo le linee guida cliniche EULAR e ACR** per la spondilartropatia, eppure questo dataset ha recuperato zero studi clinici e zero letteratura per questa indicazione. Questo è un gap di raccolta dati, non un'autentica assenza di evidenza. Il segnale di repurposing più forte nel mondo reale per il meloxicam in questo dataset è sistematicamente soppresso da un recupero di evidenza incompleto.

---

## Evidenza da Studi Clinici

Attualmente nessuno studio clinico correlato registrato per la Displasia Acromesomelica (Tipo Hunter-Thompson) e Meloxicam.

---

## Evidenza dalla Letteratura

Attualmente nessuna letteratura correlata disponibile per la Displasia Acromesomelica (Tipo Hunter-Thompson) e Meloxicam.

---

## Considerazioni sulla Sicurezza

Si prega di consultare il foglio illustrativo per informazioni sulla sicurezza.

---

## Conclusioni e Prossimi Passi

**Decisione: Sospendere**

**Razionale:**
La previsione di primo livello del TxGNN (Displasia Acromesomelica, Tipo Hunter-Thompson) è una rara displasia scheletrica geneticamente determinata. Non ci sono studi clinici, nessuna pubblicazione, e il collegamento meccanicistico proposto attraverso la cross-talk del percorso COX-2/BMP è altamente speculativo e completamente non convalidato. Questo non costituisce un candidato repurposing praticabile.

**Per procedere, è necessario quanto segue:**

- **Risolvere il gap di recupero delle evidenze per la Spondilartropatia (rank 6):** Re-eseguire la ricerca letteraria e da studi clinici con termini di query più ampi (ad es. "spondilite anchilosante", "SpA assiale", "FANS spondilartropatia") — le evidenze del mondo reale sono sostanziali e dovrebbero essere catturate prima di qualsiasi decisione finale
- **Risolvere il gap di dati AIFA per l'Italia:** Il meloxicam è un FANS di riferimento commercializzato a livello globale; l'assenza di qualsiasi record di autorizzazione italiana probabilmente riflette un problema di raccolta dati e dovrebbe essere verificato direttamente rispetto al registro pubblico AIFA
- **Ottenere dati MOA da DrugBank (DG002):** La documentazione formale del MOA è necessaria per la sezione di analisi del collegamento meccanicistico
- **Rivalutare formalmente i rank 6–8** (Spondilartropatia, Nodulosi Reumatoide, JIA Poliarticolare RF+) come obiettivi prioritizzati farmacologicamente — questi sono meccanicisticamente allineati con l'inibizione della COX-2 del meloxicam e meritano un'approfondita analisi di evidenza dedicata prima che la decisione di Sospensione sia considerata definitiva

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

