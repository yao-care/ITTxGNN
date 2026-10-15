---
layout: default
title: Tiaprofenic Acid
parent: Solo previsione del modello (L5)
nav_order: 436
evidence_level: L5
indication_count: 10
---

# Tiaprofenic Acid
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

# Acido tiaprofenico: dall'artrite reumatoide alla sindrome brachidattilia-sindattilia

## Sintesi in una frase

L'acido tiaprofenico è un farmaco antinfiammatorio non steroideo (FANS), originariamente utilizzato per artrite reumatoide, osteoartrosi e artropatie.
Il modello TxGNN lo indica come potenzialmente efficace per la **sindrome brachidattilia-sindattilia**, ma **non risulta alcuna sperimentazione clinica né alcuna pubblicazione** a supporto: la previsione è puramente computazionale.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Artrite reumatoide, osteoartrosi, artropatia (da indicazioni del grafo di conoscenza; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Sindrome brachidattilia-sindattilia |
| Punteggio di previsione TxGNN | 99,99% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 2 (nessuna valida) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione potrebbe essere ragionevole?

I dati compilati per questo report non contengono informazioni dettagliate sul meccanismo d'azione. In base alle conoscenze generali (non presenti nei dati), l'acido tiaprofenico appartiene ai FANS della classe degli acidi propionici e agisce come inibitore non selettivo della cicloossigenasi (COX). Per questo la sua efficacia sintomatica nelle patologie articolari infiammatorie è ben compresa.

La sindrome brachidattilia-sindattilia è invece una malformazione scheletrica congenita. L'inibizione della COX non può correggere un difetto genetico o dello sviluppo, quindi **non emerge alcun legame meccanicistico** con la nuova indicazione. L'elevato punteggio TxGNN riflette verosimilmente associazioni di fenotipo muscolo-scheletrico condivise nel grafo di conoscenza, e non un'effettiva plausibilità terapeutica.

### Altre previsioni del modello

Tra le prime 10 previsioni, tutte senza sperimentazioni o letteratura a supporto, la più plausibile dal punto di vista biologico è la **suscettibilità alla spondiloartropatia** (punteggio 99,99%, livello L4, classificata come "domanda di ricerca"). I FANS sono una terapia sintomatica standard per le spondiloartropatie e la condizione è affine alle indicazioni originali. Si tratta però di un'evidenza indiretta, per classe di farmaci e similarità delle indicazioni.

Le altre previsioni (sindromi displasiche scheletriche, miosclerosi, disturbi della coagulazione come l'eccesso di fattore V e il deficit di cofattore eparinico II, pseudoacondroplasia) non hanno un legame meccanicistico supportato dai dati. Per i disturbi trombotici il profilo rischio-beneficio dei FANS risulterebbe addirittura sfavorevole.

---

## Evidenze da sperimentazioni cliniche

Attualmente non risulta alcuna sperimentazione clinica correlata registrata.

---

## Evidenze dalla letteratura

Attualmente non è disponibile alcuna letteratura correlata.

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Stato | Indicazione approvata |
|---------|------|------|------|-----------|
| 025195052 | SURGAMYL*orale grat 30 bust 300 mg (SCHARPER SpA) | Non indicata | Cancellata | Non disponibile |
| 025195025 | SURGAMYL*30 cpr 300 mg (SCHARPER SpA) | Non indicata | Cancellata | Non disponibile |

---

## Considerazioni sulla sicurezza

Per le informazioni di sicurezza si rimanda al foglio illustrativo; i dati compilati per questo report non includono avvertenze o controindicazioni. Non sono state trovate interazioni farmacologiche nei dati disponibili.

Si segnala inoltre che, secondo le valutazioni di contesto, il farmaco non è più in commercio e presenta problemi di sicurezza noti non coperti dai dati (ad esempio la cistite). Qualsiasi ulteriore sviluppo dovrebbe affrontare prima la sicurezza e un confronto con i FANS attualmente in commercio.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per la sindrome brachidattilia-sindattilia si basa solo sul modello (livello L5), senza sperimentazioni, letteratura o un plausibile legame meccanicistico. Il farmaco non è inoltre più autorizzato in Italia.

**Per procedere sarebbe necessario:**
- Recuperare le avvertenze e le controindicazioni dal foglio illustrativo AIFA (lacuna bloccante per lo screening di sicurezza)
- Ottenere i dati sul meccanismo d'azione da DrugBank
- Se si intende proseguire, concentrarsi sulla **suscettibilità alla spondiloartropatia**, valutando il profilo di sicurezza (inclusa la cistite) e il confronto con i FANS attualmente commercializzati
- Verificare la compatibilità delle vie di somministrazione con l'indicazione prevista
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

