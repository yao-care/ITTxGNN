---
layout: default
title: Etoricoxib
parent: Solo previsione del modello (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Etoricoxib
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

# Etoricoxib: dal dolore muscoloscheletrico al disturbo dell'emicrania

## Sommario di una riga

L'etoricoxib è un inibitore altamente selettivo di COX-2 (FANS), approvato in molti mercati per condizioni infiammatorie inclusa l'osteoartrosi, l'artrite reumatoide, la spondilite anchilosante e la gotta acuta. Il modello TxGNN predice che potrebbe essere efficace per il **disturbo dell'emicrania** con un punteggio di predizione quasi perfetto; tuttavia, attualmente vi sono **0 studi clinici** e **0 pubblicazioni** che supportano direttamente questa indicazione specifica, collocando l'evidenza al livello più basso (L5). Indicazioni strettamente correlate — disturbo cefalico e cefalgia autonomica trigeminale — hanno invece prove preliminari da serie di casi che forniscono plausibilità biologica indiretta.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originale | Nessun registro di autorizzazione in Italia disponibile; l'etoricoxib è un inibitore selettivo di COX-2 utilizzato per il dolore articolare infiammatorio |
| Indicazione nuova predetta | Disturbo dell'emicrania |
| Punteggio di predizione TxGNN | 99.90% |
| Livello di evidenza | L5 |
| Stato del mercato italiano | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Sospensione |

---

## Perché questa predizione è ragionevole?

Attualmente, i dati dettagliati del meccanismo d'azione non sono disponibili da questo dataset. Sulla base di informazioni farmacologiche note, l'etoricoxib è un inibitore altamente selettivo della cicloossigenasi-2 (COX-2), l'isoforma inducibile responsabile della sintesi delle prostaglandine durante l'infiammazione e il dolore. La sua efficacia nelle condizioni infiammatorie muscoloscheletriche è ben consolidata, e dal punto di vista meccanicistico potrebbe essere applicabile al disturbo dell'emicrania attraverso un percorso infiammatorio condiviso.

Il collegamento biologico all'emicrania si basa sull'ipotesi trigeminovascolare: l'inibizione della COX-2 riduce la sintesi della prostaglandina E₂ (PGE₂), un mediatore chiave dell'infiammazione neurogena nel sistema trigeminovascolare. Attenuando la sensibilizzazione guidata da PGE₂ delle terminazioni del nervo trigemino nella dura madre, un inibitore selettivo della COX-2 come l'etoricoxib teoricamente potrebbe interrompere o prevenire gli attacchi emicranici. Questo è coerente con il meccanismo stabilito dell'indometacina — un inibitore non selettivo di COX che è un trattamento riconosciuto per diversi sottotipi di cefalea responsive all'indometacina — e i resoconti di casi mostrano che l'etoricoxib può sostituire l'indometacina in quelle sindromi (vedi l'evidenza per l'indicazione correlata di rango 9, disturbo cefalico).

Tuttavia, deve essere notata una distinzione critica: l'emicrania comporta non solo l'infiammazione mediata dalle prostaglandine ma anche la segnalazione del CGRP, la depressione corticale diffusa, e la sensibilizzazione centrale — percorsi non direttamente colpiti dall'inibizione della COX-2. Il modello TxGNN probabilmente predice questo collegamento attraverso la prossimità della rete grafica tra il profilo target dell'etoricoxib e il nodo della malattia emicrania, informato in parte dalla letteratura più ampia sulla suscettibilità genetica condivisa epilessia-emicrania catturata sotto il rango 3 (suscettibilità all'emicrania con o senza aura). Questa prossimità della rete genetica è meccanicisticamente distante da un effetto terapeutico diretto, il che spiega perché non esiste alcuna prova clinica diretta.

---

## Evidenza da studi clinici

Attualmente nessuno studio clinico correlato registrato per l'etoricoxib nel disturbo dell'emicrania.

---

## Evidenza dalla letteratura

Attualmente nessuna letteratura correlata disponibile per l'etoricoxib nel disturbo dell'emicrania.

---

## Informazioni sul mercato italiano

L'etoricoxib attualmente non ha autorizzazioni di commercializzazione registrate in Italia in questo dataset (0 autorizzazioni, stato del mercato: Non commercializzato).

---

## Considerazioni di sicurezza

Si prega di consultare il riassunto delle caratteristiche del prodotto per informazioni sulla sicurezza.

> ⚠️ **Nota dall'Evidence Pack:** Un resoconto di caso di evento avverso (PMID [21373319](https://pubmed.ncbi.nlm.nih.gov/21373319/)) ha documentato iperkaliemia potenzialmente letale e disfunzione renale acuta con etoricoxib in un paziente in trattamento con telmisartan e una dieta povera di sodio. Un resoconto di caso separato (PMID [25229174](https://pubmed.ncbi.nlm.nih.gov/25229174/)) ha descritto una sindrome di vasocostrizione cerebrale reversibile (RCVS) possibilmente indotta da etoricoxib — particolarmente rilevante dato che i pazienti con emicrania possono avere un rischio RCVS sovrapposto. Questi segnali, sebbene derivati dalla query di evidenza del disturbo cefalico piuttosto che dalla query di emicrania direttamente, sono clinicamente importanti per qualsiasi uso neurologico dell'etoricoxib.

---

## Conclusione e prossimi passi

**Decisione: Sospensione**

**Motivazione:**
Il modello TxGNN assegna un punteggio quasi perfetto al disturbo dell'emicrania, ma la base di evidenza è interamente assente — nessuno studio clinico e nessuna pubblicazione affrontano direttamente l'etoricoxib per questa indicazione. La predizione è biologicamente plausibile a livello teorico (percorso COX-2/PGE₂/trigeminovascolare), ma la sola plausibilità biologica è insufficiente per far avanzare un candidato al riposizionamento. L'indicazione strettamente correlata del **disturbo cefalico (rango 9)** ha un caso di ricerca più forte, supportato da multiple serie di casi pubblicate che mostrano l'etoricoxib come un'alternativa efficace all'indometacina nelle sindromi di cefalea responsive all'indometacina, e dovrebbe essere considerato come l'obiettivo di ricerca a breve termine più attuabile.

**Per procedere, è necessario quanto segue:**

- **Dati MOA da DrugBank:** Recuperare la farmacologia completa, i bersagli del farmaco e il profilo di tossicità per l'etoricoxib (DB01628) per completare l'analisi del meccanismo d'azione e perfezionare il razionale del percorso dell'emicrania.
- **Riassunto delle caratteristiche del prodotto TFDA/EMA:** Ottenere il testo completo delle controindicazioni e degli avvertimenti chiave (attualmente bloccando lo screening di sicurezza preliminare alla fase S0) per valutare se l'uso neurologico/vascolare è formalmente controindicato.
- **Ricerca letteraria mirata:** Condurre una ricerca dedicata su PubMed combinando specificamente "etoricoxib" AND "migraine" (piuttosto che il termine di malattia di suscettibilità più ampio utilizzato in questo dataset) per confermare se esiste alcuna prova diretta che sia stata persa dalla strategia di interrogazione attuale.
- **Riclassificare il candidato principale:** Considerare di elevare il **disturbo cefalico** (rango 9, Livello di evidenza L4, fase S1) come il candidato principale al riposizionamento per l'investigazione a breve termine, dato che ha prova diretta di casi pubblicati dell'efficacia dell'etoricoxib e un collegamento meccanicistico chiaro attraverso il percorso indometacina-COX-2.
- **Valutazione del rischio RCVS:** Prima di perseguire qualsiasi indicazione neurologica, è richiesta una valutazione formale rischio-beneficio per RCVS (vasocostrizione indotta da etoricoxib) nei pazienti con emicrania — che già presentano sensibilità cerebrovascolare elevata.

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

