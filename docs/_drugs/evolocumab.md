---
layout: default
title: Evolocumab
parent: Solo previsione del modello (L5)
nav_order: 100
evidence_level: L5
indication_count: 6
---

# Evolocumab
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **6** 
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

# Evolocumab: Da ipercolesterolemia a emofilia sintomatica nei portatori donne

## Sintesi in una frase

Evolocumab è un anticorpo monoclonale inibitore della PCSK9, originariamente sviluppato per ridurre il colesterolo LDL nei pazienti con ipercolesterolemia e malattia cardiovascolare aterosclerotica.
Il modello TxGNN prevede che possa essere efficace per **forma sintomatica di emofilia nei portatori donne**, con un punteggio di confidenza del modello di **99,82%**.
Tuttavia, **attualmente non esistono studi clinici e nessuna letteratura di supporto** per questa indicazione, e la razionalità meccanicistica è valutata come un probabile artefatto topologico della rete di conoscenze piuttosto che un'autentica ipotesi biologica.

---

## Panoramica rapida

| Elemento | Contenuto |
|---------|-----------|
| Indicazione originale | Nessuna indicazione approvata in archivio in Italia (0 autorizzazioni AIFA registrate) |
| Indicazione predetta | Forma sintomatica di emofilia nei portatori donne |
| Punteggio previsione TxGNN | 99,82% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | **Hold** |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili nell'Evidence Pack. In base alla farmacologia consolidata, evolocumab è un anticorpo monoclonale IgG2 completamente umano che si lega selettivamente e inibisce la PCSK9 (proprotein convertase subtilisin/kexin tipo 9), una serina proteasi secreta dal fegato che etichetta i recettori LDL per la degradazione lisosomiale. Neutralizzando la PCSK9 circolante, evolocumab previene la degradazione del recettore LDL, aumenta la densità dei recettori negli epatociti e quindi riduce sostanzialmente il colesterolo LDL plasmatico — di circa il 55–75% come monoterapia o in aggiunta alla terapia con statine.

L'indicazione predetta — emofilia sintomatica nei portatori donne — opera attraverso un percorso completamente indipendente. Questa condizione nasce dall'inattivazione asimmetrica del cromosoma X, che determina attività subnormale del Fattore VIII (emofilia A) o del Fattore IX (emofilia B) nonostante l'eterozigosità del portatore. La carenza del cascata coagulativa e il metabolismo del colesterolo mediato da PCSK9 sono sistemi biologicamente indipendenti senza alcuna intersezione farmacologica nota.

La razionalità meccanicistica incorporata nell'Evidence Pack caratterizza esplicitamente questa previsione come un **artefatto topologico**: il grafo di conoscenze TxGNN probabilmente raggruppa strutturalmente i "nodi di malattia ematologica", generando elevati punteggi di co-occorrenza che non hanno alcuna base biologica causale. Un elevato punteggio di confidenza TxGNN (99,82%) in assenza di alcuna prova di trial o pubblicazione è una bandiera rossa per questa categoria di artefatto, non un segnale di promessa clinica. Questa previsione non dovrebbe avanzare oltre l'attuale fase Hold senza un'ipotesi meccanicistica formale supportata da prove di laboratorio umido o osservazionali.

---

## Evidenza da studi clinici

Attualmente nessuno studio clinico correlato registrato.

---

## Evidenza dalla letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Informazioni di mercato Italia

Nessuna autorizzazione commerciale AIFA è attualmente in archivio per evolocumab (0 licenze registrate). Il farmaco è pertanto classificato come **non commercializzato** in Italia secondo questo dataset. È consigliata una verifica indipendente rispetto al registro online AIFA, poiché evolocumab (Repatha®) detiene un'autorizzazione centralizzata EMA e potrebbe essere commercialmente disponibile in Italia attraverso tale canale.

---

## Considerazioni di sicurezza

Si rimanda al foglio illustrativo per informazioni sulla sicurezza.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Razionale:**
Tutte e sei le indicazioni previste in questo Evidence Pack condividono lo stesso livello di evidenza L5 (sola previsione del modello) e una raccomandazione Hold. La previsione con il ranking più alto — emofilia sintomatica nei portatori donne — non ha base meccanicistica che colleghi l'inibizione di PCSK9 alla carenza di fattori della coagulazione, e sono stati identificati zero studi clinici o letteratura di supporto in tutte le query di evidenza. Gli elevati punteggi TxGNN in questo set di candidati sono coerenti con il raggruppamento topologico della rete di conoscenze piuttosto che con la plausibilità biologica.

**Per procedere, è necessario quanto segue:**

- **Verifica formale del MOA**: Confermare i dati del percorso inibitore della PCSK9 da DrugBank e dalla letteratura primaria per completare la valutazione del divario meccanicistico.
- **Generazione di ipotesi meccanicistica**: Prima che qualsiasi indicazione in questo pacchetto possa avanzare, deve essere articolato un collegamento biologico credibile tra l'inibizione della PCSK9 e la malattia target — idealmente supportato da evidenze in vitro, in vivo o genetiche umane (randomizzazione mendeliana).
- **Baseline normativa Italia**: Verificare lo stato di approvazione AIFA / EMA di evolocumab e l'etichettatura approvata direttamente dai registri ufficiali per stabilire il contesto normativo per qualsiasi discussione di repurposing.
- **Audit della rete di conoscenze**: Contrassegnare questo cluster di candidati per revisione del modello TxGNN, poiché la concentrazione di nodi di malattia ematologica con elevati punteggi e zero razionalità biologica suggerisce un problema sistematico di topologia del grafo che potrebbe interessare altri candidati nello stesso vicinato dei nodi.
- **Recupero dati di sicurezza**: Ottenere i dati del foglio illustrativo TFDA/AIFA, avvertenze, controindicazioni e informazioni su interazioni farmacologiche (attualmente tutti contrassegnati come Data Gap) prima che possa iniziare qualsiasi valutazione di fattibilità clinica.

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

