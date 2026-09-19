---
layout: default
title: Nabumetone
parent: Solo previsione del modello (L5)
nav_order: 153
evidence_level: L5
indication_count: 10
---

# Nabumetone
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

# Nabumetone: da Osteoartrosi / Artrite Reumatoide a Displasia acromesomelica (tipo Hunter-Thompson)

## Riassunto in una frase

Nabumetone è un inibitore non selettivo della COX (FANS) utilizzato classicamente per alleviare il dolore e l'infiammazione nell'osteoartrosi e nell'artrite reumatoide.
Il modello TxGNN prevede che possa essere efficace per **Displasia acromesomelica, tipo Hunter-Thompson** — un raro disturbo scheletrico ereditario causato da mutazioni in GDF5/CDMP1.
Tuttavia, questa previsione è supportata da **0 studi clinici** e **0 pubblicazioni**, collocandola al livello di evidenza più basso (L5), il che significa che si basa interamente su inferenza del modello grafo senza dati di studi umani.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originale | Osteoartrosi / Artrite Reumatoide (uso noto della classe FANS; nessuna autorizzazione italiana registrata) |
| Indicazione nuova prevista | Displasia acromesomelica, tipo Hunter-Thompson |
| Punteggio di previsione TxGNN | 99.99% |
| Livello di evidenza | L5 (solo previsione del modello, nessuno studio reale) |
| Stato del mercato italiano | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Rinviare |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione di Nabumetone non sono disponibili dalle fonti di dati interrogate. Sulla base delle informazioni farmacologiche note, Nabumetone è un profarmaco FANS che viene convertito in vivo nel suo metabolita attivo acido 6-metossi-2-naftilacetico (6-MNA), che inibisce in modo non selettivo sia gli enzimi COX-1 che COX-2. Questo riduce la sintesi delle prostaglandine, sopprimendo così il dolore e l'infiammazione nelle condizioni muscoloscheletriche come l'osteoartrosi e l'artrite reumatoide.

Displasia acromesomelica, tipo Hunter-Thompson (AMDH) è una rara displasia scheletrica autosomica recessiva causata da mutazioni con perdita di funzione in *GDF5* (nota anche come *CDMP1*), che codifica una proteina morfogenetica ossea (BMP) critica per la specificazione del pattern degli arti e la formazione delle articolazioni. La patologia comporta l'interruzione della via di segnalazione dello sviluppo BMP/GDF5, risultando in accorciamento sproporzionato dei segmenti degli arti medi e distali — un'anomalia scheletrica strutturale, non infiammatoria, stabilita prenatalmente.

Non esiste un ponte meccanicistico riconosciuto tra l'inibizione della COX e l'interruzione della via GDF5/BMP che sottende l'AMDH. Nabumetone può fornire sollievo dal dolore sintomatico nei pazienti con disturbi muscoloscheletrici secondari, ma non ha capacità di modificare il difetto genetico o dello sviluppo sottostante. Il modello TxGNN probabilmente ha generato questa previsione a causa della prossimità nel grafo tra i nodi delle displasie scheletriche e i nodi delle artriti infiammatorie nel grafo della conoscenza delle malattie — una fonte nota di falsi positivi per i FANS nelle rare malattie ossee.

---

## Evidenza da studi clinici

Attualmente nessuno studio clinico correlato è registrato.

---

## Evidenza dalla letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Informazioni sul mercato italiano

Nabumetone attualmente non detiene autorizzazioni all'immissione in commercio in Italia (AIFA). Il farmaco non è commercializzato, e nessun record di licenza è stato recuperato.

---

## Considerazioni sulla sicurezza

Si prega di fare riferimento al foglio illustrativo per informazioni sulla sicurezza.

---

## Conclusioni e prossimi passi

**Decisione: Rinviare**

**Razionale:**
Non esiste evidenza clinica, meccanicistica o letteraria che supporti Nabumetone come trattamento per Displasia acromesomelica, tipo Hunter-Thompson. La malattia è guidata da un difetto ereditario della via BMP/GDF5 che è strutturalmente e biologicamente incompatibile con l'inibizione della COX. Il punteggio TxGNN da solo, senza alcuna evidenza corroborante, è insufficiente a giustificare ulteriore sviluppo.

**Per riconsiderare questa previsione, sarebbero necessari:**
- Un'ipotesi meccanicistica credibile che colleghi le vie COX/prostaglandina alla segnalazione GDF5 (ad es., studi sull'attività del recettore BMP modulata dalle prostaglandine)
- Almeno uno studio preclinico (modello animale o in vitro) che dimostri che Nabumetone o un FANS strutturalmente correlato influisce sui fenotipi correlati a GDF5
- Un esame degli spigoli del grafo TxGNN che collegano questa coppia farmaco-malattia per verificare se riflettono relazioni biologiche genuine o sono artefatti di nodi di prossimità condivisa (ad es., prossimità di spondiloartropatia o brachiolmia)

> **Nota sui candidati con rango più alto:** Rango 8 — *Spondiloartropatia* (suscettibilità) — presenta un obiettivo di reimpiego farmacologico biologicamente più plausibile. I FANS, incluso Nabumetone, sono agenti di prima linea per la spondilite anchilosante e SpA come classe farmacologica (evidenza di effetto di classe L1), anche se i dati RCT specifici per Nabumetone sono assenti (L4). Se viene perseguito un programma di reimpiego farmacologico, quell'indicazione merita la priorità rispetto alle displasie scheletriche rare con rango più alto.

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

