---
layout: default
title: Phenobarbital
parent: Solo previsione del modello (L5)
nav_order: 347
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Phenobarbital: nuova indicazione prevista, Neoplasma del nervo trigemino (livello di evidenza L5). Indicazione originale: Epilessia (anche con crisi tonico-cloniche generalizzate e parziale)…"
monitor_inn: "Phenobarbital"
predicted_indications: ["trigeminal nerve neoplasm", "orgasm-induced seizures", "eating seizures", "micturation-induced seizures", "thinking seizures", "audiogenic seizures", "reading seizures", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
---

# Phenobarbital
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

# Fenobarbital: dall'epilessia al neoplasma del nervo trigemino

## Sintesi

Il fenobarbital è un barbiturico utilizzato storicamente come anticonvulsivante, con indicazioni principali per epilessia (inclusa quella con crisi tonico-cloniche generalizzate e parziale), sindrome di Lennox-Gastaut ed emicrania/cefalee.
Il modello TxGNN lo propone per il **neoplasma del nervo trigemino** (punteggio molto alto), ma per questa indicazione non esistono **studi clinici** e vi è **1 sola pubblicazione**, che riguarda un'altra patologia (sindrome di Sturge-Weber).
Si tratta quindi di una predizione basata solo sul modello, con evidenza scarsa e verosimilmente dovuta alla vicinanza nel grafo a termini neurologici.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Epilessia (anche con crisi tonico-cloniche generalizzate e parziale), sindrome di Lennox-Gastaut, emicrania e cefalee (dati dal grafo di conoscenza; il testo dell'indicazione autorizzata AIFA non è disponibile) |
| Nuova indicazione predetta | Neoplasma del nervo trigemino |
| Punteggio di predizione TxGNN | 99,96% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 4 (tutte cancellate) |
| Decisione raccomandata | Hold (sospendere) |

---

## Perché questa predizione è (o non è) ragionevole?

Per questo farmaco non sono attualmente disponibili dati dettagliati sul meccanismo d'azione. Sulla base delle conoscenze generali, il fenobarbital è un modulatore allosterico positivo del recettore GABA-A, con efficacia consolidata nelle crisi epilettiche. Non è noto alcun meccanismo antitumorale.

Il punteggio elevato del modello riflette probabilmente la prossimità, nella rete di conoscenza, con epilessia e termini neurologici, più che una reale attività contro la neoplasia. L'unico articolo collegato (PMID 9157801) è una serie di casi sulla sindrome di Sturge-Weber, un disordine neurocutaneo vascolare, non un tumore del trigemino. Un eventuale beneficio sarebbe limitato al controllo sintomatico delle crisi, non al trattamento della neoplasia.

Tra le altre predizioni nella stessa lista, quelle per le epilessie riflesse (crisi indotte da alimentazione, minzione, pensiero, sorpresa, suoni, lettura, orgasmo) sono meccanisticamente più plausibili, in quanto basate sull'azione anticonvulsivante generale, ma anch'esse prive di studi specifici. Per la nevralgia del trigemino il fenobarbital non è una terapia standard (il farmaco di scelta è la carbamazepina), e la letteratura è in gran parte indiretta. La predizione per il deficit di beta-chetotiolasi non ha alcun legame meccanicistico noto.

---

## Evidenze da studi clinici

Attualmente non risulta registrato alcuno studio clinico correlato.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Serie di casi | Anales españoles de pediatría | Esperienza su 14 casi di sindrome di Sturge-Weber: caratteristiche cliniche, evoluzione e risposta terapeutica. Non riguarda un tumore del nervo trigemino |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 004556015 | GARDENALE 20 cpr 100 mg (ATNAHS PHARMA NETHERLANDS BV) | Compresse | Non disponibile (autorizzazione cancellata) |
| 002860031 | LUMINALE 20 cpr 100 mg (SUBSTIPHARM) | Compresse | Non disponibile (autorizzazione cancellata) |
| 004556027 | GARDENALE 30 cpr 50 mg (ATNAHS PHARMA NETHERLANDS BV) | Compresse | Non disponibile (autorizzazione cancellata) |
| 002860043 | LUMINALE 30 cpr 15 mg (SUBSTIPHARM) | Compresse | Non disponibile (autorizzazione cancellata) |

---

## Considerazioni di sicurezza

- **Controindicazioni (dal grafo di conoscenza, non dal foglio illustrativo)**: ipertensione, insufficienza epatica e malattie del fegato, porfiria (ereditaria e disturbi del metabolismo delle porfirine), malattie renali, broncopneumopatia cronica ostruttiva, ulcera gastrica/peptica e gastrite, insonnia, disturbi d'ansia, disturbi nevrotici e distimici, disturbi psicotici e altri disturbi mentali (schizofreniforme, schizoaffettivo), malattie della colecisti, trombocitopenia, iperglicemia, ipotiroidismo (mixedema, ipotiroidismo congenito), lupus eritematoso sistemico (anche pediatrico).
- **Interazioni**: è registrata un'interazione farmacologica con il recettore X del pregnano (PXR, gene NR1I2), di cui il fenobarbital è ligando. Questo è coerente con l'induzione degli enzimi del citocromo P450 e con il rischio di interazioni con altri farmaci (ad esempio la carbamazepina).
- **Segnali dalla letteratura collegata**: riportati rischi di teratogenicità, effetti cognitivi tardivi dopo esposizione precoce e possibili effetti sullo sviluppo neurologico neonatale.

Per avvertenze e controindicazioni ufficiali occorre consultare il foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold (sospendere)**

**Motivazione:**
- La predizione per il neoplasma del nervo trigemino si basa solo sul punteggio del modello (livello L5), senza studi clinici e con un'unica pubblicazione non pertinente. Non vi è alcuna plausibilità antitumorale.
- Tutte le autorizzazioni italiane sono cancellate, il che limita ulteriormente la praticabilità.

**Per procedere sarebbe necessario:**
- Recuperare il foglio illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per la valutazione di sicurezza).
- Ottenere i dati sul meccanismo d'azione da DrugBank.
- Individuare evidenze mirate di attività contro i tumori del nervo trigemino (precliniche o cliniche).
- Se l'interesse fosse per le epilessie riflesse, valutare queste indicazioni come candidate separate, con revisione sistematica della letteratura specifica e verifica della disponibilità del farmaco sul mercato italiano.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

