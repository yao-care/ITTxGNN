---
layout: default
title: Ambrisentan
parent: Solo previsione del modello (L5)
nav_order: 25
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan: Valutazione del Riposizionamento del Farmaco

## Riassunto in una frase

Ambrisentan (DrugBank: DB06403) è un antagonista selettivo del recettore dell'endotelina di tipo A (ETA), indicato principalmente per il trattamento dell'ipertensione arteriosa polmonare (IAP). Il modello TxGNN **non ha generato alcuna indicazione nuova prevista** per questo farmaco al momento, e il pacchetto di evidenze contiene importanti lacune nei dati che impediscono una valutazione completa.

---

## Panoramica Rapida

| Elemento | Contenuto |
|------|------|
| Farmaco (DCI) | Ambrisentan |
| ID DrugBank | DB06403 |
| Indicazione Originale | Non elencata nel pacchetto di evidenze (uso noto: Ipertensione Arteriosa Polmonare) |
| Indicazione Nuova Prevista | — Nessuna prevista — |
| Punteggio di Previsione TxGNN | N/A |
| Livello di Evidenza | L5 (Nessuna previsione o studi di supporto disponibili) |
| Stato del Mercato Taiwan | Non commercializzato (Non commercializzato) |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | **Sospensione** |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non erano disponibili nel pacchetto di evidenze. In base alle informazioni pubblicamente disponibili, Ambrisentan è un antagonista selettivo del recettore dell'endotelina di tipo A (ETA). L'endotelina-1 (ET-1) è un potente vasocostrittore e mitogeno della muscolatura liscia, e bloccando selettivamente il recettore ETA, Ambrisentan promuove la vasodilatazione e riduce la resistenza vascolare polmonare. È approvato in più mercati (ad es., negli Stati Uniti come Letairis®, nell'UE come Volibris®) per l'ipertensione arteriosa polmonare (IAP) di Gruppo WHO 1.

Poiché nessuna indicazione prevista è stata generata dal modello TxGNN, non è attualmente disponibile alcuna analisi del collegamento meccanicistico da eseguire. Ciò potrebbe essere dovuto all'assenza del farmaco dal mercato taiwanese e alla limitata rappresentazione nella rete di conoscenza utilizzata dal modello. Ulteriore arricchimento dei dati — inclusi i dettagli sul meccanismo d'azione, i profili di sicurezza completi e la mappatura più ampia delle indicazioni — sarebbe necessario prima che il modello possa generare previsioni praticabili.

---

## Evidenze da Studi Clinici

Attualmente nessuna indicazione prevista disponibile — la ricerca di studi clinici non è stata eseguita.

---

## Evidenze dalla Letteratura

Attualmente nessuna indicazione prevista disponibile — la ricerca della letteratura non è stata eseguita.

---

## Informazioni sul Mercato Taiwan

Ambrisentan **non è attualmente commercializzato a Taiwan** (Non commercializzato). Nessuna autorizzazione TFDA è stata trovata.

| Numero di Autorizzazione | Nome del Prodotto | Forma Farmaceutica | Indicazione Approvata |
|---------|------|------|-----------|
| — | — | — | Nessuna autorizzazione registrata |

---

## Considerazioni di Sicurezza

> Si prega di fare riferimento al foglio illustrativo per le informazioni di sicurezza.
>
> Nota: Nel pacchetto di evidenze non erano disponibili avvertenze dal foglio illustrativo TFDA, controindicazioni o dati sulle interazioni farmacologiche. Per riferimento, i problemi di sicurezza noti a livello internazionale per Ambrisentan includono:
> - **Rischio di epatotossicità** (richiede il monitoraggio della funzionalità epatica)
> - **Teratogenicità** (Categoria di Gravidanza X — controindicato rigorosamente in gravidanza; richiede test di gravidanza e contraccezione nelle donne in età fertile)
> - **Ritenzione di liquidi e edema periferico**
> - **Diminuzione dell'emoglobina / ematocrito**
>
> I prescrittori devono consultare l'etichettatura approvata del prodotto nella giurisdizione pertinente (ad es., foglio illustrativo FDA Letairis® negli USA, SmPC Volibris® dell'EMA).

---

## Conclusione e Prossimi Passi

**Decisione: Sospensione**

**Razionale:**
Il modello TxGNN non ha generato alcuna indicazione nuova prevista per Ambrisentan. Inoltre, il farmaco non è commercializzato a Taiwan e il pacchetto di evidenze ha lacune critiche nei dati (meccanismo d'azione, avvertenze di sicurezza, controindicazioni). Senza una indicazione prevista, nessuna valutazione del riposizionamento può procedere.

**Per procedere, è necessario quanto segue:**

1. **Risolvere la Lacuna Critica nei Dati (DG001):** Ottenere le avvertenze del foglio illustrativo TFDA e le controindicazioni (o etichettatura internazionale equivalente) per consentire lo screening di sicurezza di Fase 1.
2. **Risolvere la Lacuna ad Alta Priorità nei Dati (DG002):** Recuperare i dati dettagliati del meccanismo d'azione dall'API di DrugBank per supportare l'analisi del collegamento meccanicistico.
3. **Arricchimento della Rete di Conoscenza:** Assicurare che Ambrisentan e la sua classe di antagonisti del recettore dell'endotelina siano adeguatamente rappresentati nella rete di conoscenza TxGNN, quindi rieseguire le previsioni.
4. **Rivalutazione:** Una volta colmate le lacune nei dati e disponibili le previsioni, rigenerare il pacchetto di evidenze e rivalutare.

---

*Rapporto generato: 2026-04-03 | Versione del pacchetto di evidenze: v4 | ID del Candidato: TW-DB06403-multi*

*⚠️ Questo rapporto è solo per scopi di ricerca e non costituisce consulenza medica. Qualsiasi candidato di riposizionamento del farmaco richiede validazione clinica prima dell'applicazione.*

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

