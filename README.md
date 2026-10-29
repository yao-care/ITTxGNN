# ITTxGNN - Italia: Riposizionamento dei Farmaci

> 本專案由 **藥提醒科技有限公司**（[yao.care](https://www.yao.care)）開發與維運。
> ITTxGNN 站台：<https://ittxgnn.yao.care/>｜產品總覽：<https://www.yao.care/medical/txgnn/>

[![Website](https://img.shields.io/badge/Website-ittxgnn.yao.care-blue)](https://ittxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Previsioni di riposizionamento di farmaci per farmaci approvati da AIFA (Italy) utilizzando il modello TxGNN.

## Avvertenza

- I risultati di questo progetto sono solo a scopo di ricerca e non costituiscono consulenza medica.
- I candidati al riposizionamento dei farmaci richiedono una validazione clinica prima dell'applicazione.

## Panoramica del progetto

### Statistiche dei rapporti

| Elemento | Quantita |
|------|------|
| **Rapporti sui farmaci** | 436 |
| **Previsioni totali** | 7,794,696 |
| **Farmaci unici** | 407 |
| **Indicazioni uniche** | 16,985 |
| **Dati DDI** | 302,516 |
| **Dati DFI** | 857 |
| **Dati DHI** | 35 |
| **Dati DDSI** | 8,359 |
| **Risorse FHIR** | 333 MK / 1,860 CUD |

### Distribuzione dei livelli di evidenza

| Livello di evidenza | Numero di rapporti | Descrizione |
|---------|-------|------|
| **L1** | 0 | Multipli RCT di Fase 3 |
| **L2** | 0 | RCT singolo o multipli Fase 2 |
| **L3** | 0 | Studi osservazionali |
| **L4** | 0 | Studi preclinici / meccanicistici |
| **L5** | 333 | Solo previsione computazionale |

### Per fonte

| Fonte | Previsioni |
|------|------|
| DL | 7,792,836 |
| KG + DL | 1,617 |
| KG | 243 |

### Per fiducia

| Fiducia | Previsioni |
|------|------|
| very_high | 1,263 |
| high | 381,100 |
| medium | 722,747 |
| low | 6,689,586 |

---

## Metodi di previsione

| Metodo | Velocita | Precisione | Requisiti |
|------|------|--------|----------|
| Grafo di conoscenza | Veloce (secondi) | Inferiore | Nessun requisito speciale |
| Deep Learning | Lento (ore) | Superiore | Conda + PyTorch + DGL |

### Metodo del grafo di conoscenza

```bash
uv run python scripts/run_kg_prediction.py
```

| Metrica | Valore |
|------|------|
| AIFA Totale farmaci | 10,545 |
| Mappati a DrugBank | 5,481 (52.0%) |
| Candidati al riposizionamento | 1,860 |

### Metodo di deep learning

```bash
conda activate txgnn
PYTHONPATH=src python -m ittxgnn.predict.txgnn_model
```

| Metrica | Valore |
|------|------|
| Previsioni DL totali | 689,135 |
| Farmaci unici | 407 |
| Indicazioni uniche | 16,985 |

### Interpretazione dei punteggi

Il punteggio TxGNN rappresenta la fiducia del modello in una coppia farmaco-malattia, con un range da 0 a 1.

| Soglia | Significato |
|-----|------|
| >= 0.9 | Fiducia molto alta |
| >= 0.7 | Fiducia alta |
| >= 0.5 | Fiducia moderata |

#### Distribuzione dei punteggi

| Soglia | Significato |
|-----|------|
| ≥ 0.9999 | Confidenza estremamente alta, previsioni piu sicure del modello |
| ≥ 0.99 | Confidenza molto alta, da prioritizzare per la validazione |
| ≥ 0.9 | Confidenza alta |
| ≥ 0.5 | Confidenza moderata (confine decisionale sigmoide) |

#### Definizioni dei livelli di evidenza

| Livello | Definizione | Significato clinico |
|-----|------|---------|
| L1 | RCT di fase 3 o revisione sistematica | Puo supportare l'uso clinico |
| L2 | RCT di fase 2 | Puo essere considerato per l'uso |
| L3 | Fase 1 o studio osservazionale | Richiede ulteriore valutazione |
| L4 | Report di caso o ricerca preclinica | Non ancora raccomandato |
| L5 | Solo previsione computazionale, nessuna evidenza clinica | Richiede ulteriore ricerca |

#### Promemoria importanti

1. **Punteggi alti non garantiscono efficacia clinica: i punteggi TxGNN sono previsioni basate su grafi di conoscenza che richiedono validazione tramite studi clinici.**
2. **Punteggi bassi non significano inefficacia: il modello potrebbe non aver appreso certe associazioni.**
3. **Si consiglia l'uso con la pipeline di validazione: utilizzare gli strumenti di questo progetto per esaminare studi clinici, letteratura e altre prove.**

### Pipeline di validazione

```mermaid
flowchart TD
    A["Risultati di previsione TxGNN"] --> B
    subgraph B["Step 1: DrugBundle Collector"]
        B1["Livello farmaco: AIFA, DDI, DrugBank"]
        B2["Livello indicazione: ClinicalTrials, PubMed, ICTRP"]
    end
    B --> |"drug_bundle.json"| C
    subgraph C["Step 2: Evidence Pack Generator"]
        C1["Trasferimento dati programmatico (100%)"]
        C2["+ LLM Analisi (L1-L5)"]
    end
    C --> |"drug_evidence_pack.json/md"| D
    subgraph D["Step 3: Notes Writer"]
        D1["drug_pharmacist_notes.md"]
        D2["drug_sponsor_notes.md"]
    end
```

---

## Avvio rapido

### Passo 1: Scaricare i dati

| File | Download |
|------|------|
| AIFA Dati | [AIFA - Liste Farmaci Classe A e H](https://www.aifa.gov.it/en/liste-farmaci-a-h) |
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) |
| model_ckpt.zip | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) |

### Passo 2: Installare le dipendenze

```bash
uv sync
```

### Passo 3: Elaborare i dati sui farmaci

```bash
uv run python scripts/process_fda_data.py
```

### Passo 4: Preparare i dati del vocabolario

```bash
uv run python scripts/prepare_external_data.py
```

### Passo 5: Eseguire la previsione del grafo di conoscenza

```bash
uv run python scripts/run_kg_prediction.py
```

### Passo 6: Configurare l'ambiente di deep learning

```bash
conda create -n txgnn python=3.11 -y
conda activate txgnn
pip install torch==2.2.2 torchvision==0.17.2
pip install dgl==1.1.3
pip install git+https://github.com/mims-harvard/TxGNN.git
pip install pandas tqdm pyyaml pydantic ogb
```

### Passo 7: Eseguire la previsione di deep learning

```bash
conda activate txgnn
PYTHONPATH=src python -m ittxgnn.predict.txgnn_model
```

---

## Risorse

### TxGNN Nucleo

- [TxGNN Paper](https://www.nature.com/articles/s41591-024-03233-x) - Nature Medicine, 2024
- [TxGNN GitHub](https://github.com/mims-harvard/TxGNN)
- [TxGNN Explorer](http://txgnn.org)

### Fonti di dati

| Categoria | Dati | Fonte | Nota |
|------|------|------|------|
| **Dati sui farmaci** | AIFA | [AIFA - Liste Farmaci Classe A e H](https://www.aifa.gov.it/en/liste-farmaci-a-h) | Italy |
| **Grafo di conoscenza** | TxGNN KG | [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM) | 17,080 diseases, 7,957 drugs |
| **Database dei farmaci** | DrugBank | [DrugBank](https://go.drugbank.com/) | Mappatura ingredienti farmaci |
| **Interazioni farmacologiche** | DDInter 2.0 | [DDInter](https://ddinter2.scbdd.com/) | Coppie DDI |
| **Interazioni farmacologiche** | Guide to PHARMACOLOGY | [IUPHAR/BPS](https://www.guidetopharmacology.org/) | Interazioni farmaci approvati |
| **Sperimentazioni cliniche** | ClinicalTrials.gov | [CT.gov API v2](https://clinicaltrials.gov/data-api/api) | Registro sperimentazioni cliniche |
| **Sperimentazioni cliniche** | WHO ICTRP | [ICTRP API](https://apps.who.int/trialsearch/api/v1/search) | Piattaforma internazionale sperimentazioni cliniche |
| **Letteratura** | PubMed | [NCBI E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/) | Ricerca letteratura medica |
| **Mappatura dei nomi** | RxNorm | [RxNav API](https://rxnav.nlm.nih.gov/REST) | Standardizzazione nomi farmaci |
| **Mappatura dei nomi** | PubChem | [PUG-REST API](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) | Ricerca sinonimi chimici |
| **Mappatura dei nomi** | ChEMBL | [ChEMBL API](https://www.ebi.ac.uk/chembl/api/data) | Database bioattivita |
| **Standard** | FHIR R4 | [HL7 FHIR](http://hl7.org/fhir/) | MedicationKnowledge, ClinicalUseDefinition |
| **Standard** | SMART on FHIR | [SMART Health IT](https://smarthealthit.org/) | Integrazione EHR, OAuth 2.0 + PKCE |

### Download dei modelli

| File | Download | Nota |
|------|------|------|
| Modello pre-addestrato | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) | model_ckpt.zip |
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) | Dati nodi |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) | Dati grafo di conoscenza |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) | Dati archi (DL) |

## Introduzione al progetto

### Struttura delle directory

```
ITTxGNN/
├── README.md
├── CLAUDE.md
├── pyproject.toml
│
├── config/
│   └── fields.yaml
│
├── data/
│   ├── kg.csv
│   ├── node.csv
│   ├── edges.csv
│   ├── raw/
│   ├── external/
│   ├── processed/
│   │   ├── drug_mapping.csv
│   │   ├── repurposing_candidates.csv
│   │   ├── txgnn_dl_predictions.csv.gz
│   │   └── integration_stats.json
│   ├── bundles/
│   └── collected/
│
├── src/ittxgnn/
│   ├── data/
│   │   └── loader.py
│   ├── mapping/
│   │   ├── normalizer.py
│   │   ├── drugbank_mapper.py
│   │   └── disease_mapper.py
│   ├── predict/
│   │   ├── repurposing.py
│   │   └── txgnn_model.py
│   ├── collectors/
│   └── paths.py
│
├── scripts/
│   ├── process_fda_data.py
│   ├── prepare_external_data.py
│   ├── run_kg_prediction.py
│   └── integrate_predictions.py
│
├── docs/
│   ├── _drugs/
│   ├── fhir/
│   │   ├── MedicationKnowledge/
│   │   └── ClinicalUseDefinition/
│   └── smart/
│
├── model_ckpt/
└── tests/
```

**Legenda**: 🔵 Sviluppo progetto | 🟢 Dati locali | 🟡 Dati TxGNN | 🟠 Pipeline di validazione

### Flusso di dati

```mermaid
flowchart TD
    FDA["AIFA Dati"] --> proc["process_fda_data.py"]
    TxGNN["TxGNN Dati"] --> prep["prepare_external_data.py"]

    proc --> json["it_fda_drugs.json"]
    prep --> ext["data/external/"]

    json --> norm["normalizer.py"]
    ext --> norm

    norm --> drug_map["drug_mapping.csv"]
    drug_map --> ind_map["indication_mapping.csv"]

    ind_map --> KG["Grafo di conoscenza"]
    ind_map --> DL["Deep Learning"]

    KG --> kg_out["repurposing_candidates.csv"]
    DL --> dl_out["txgnn_dl_predictions.csv"]
```

---

## Citazione

Se si utilizza questo set di dati o software, si prega di citare:

```bibtex
@software{ittxgnn2026,
  author       = {Yao.Care},
  title        = {ITTxGNN: Drug Repurposing Validation Reports for Italy AIFA Drugs},
  year         = 2026,
  publisher    = {GitHub},
  url          = {https://github.com/yao-care/ITTxGNN}
}
```

Citare anche l'articolo originale TxGNN:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and Chandak, Payal and Wang, Qianwen and Haber, Shreyas and Zitnik, Marinka},
  journal={Nature Medicine},
  year={2024},
  doi={10.1038/s41591-024-03233-x}
}
```

<!-- txgnn-ops:start -->
## 維運：資料還原與許可證更新

### 完整還原

git 只放程式碼與網站頁面；許可證原始資料、證據包、藥師報告原稿、預測結果放在本 repo 的 Release。

```bash
git clone https://github.com/yao-care/ittxgnn.git && cd ittxgnn
uv sync                                  # Python 相依套件
bash scripts/restore_data.sh             # 取最新的 data-* Release，還原 data/（含校驗）
bash scripts/restore_data.sh --with-kg   # 另加共用知識圖譜與預測模型（只有重跑預測才需要）
```

需要 [GitHub CLI](https://cli.github.com/)（`gh auth login`）與 [uv](https://docs.astral.sh/uv/)。

### 改頁工具鏈

事實層、checker、許可證狀態計算等放在 `tools/txgnn/.claude/`，是母 repo `yao-care/txgnn` 的 `.claude/` 複本（版本見 `tools/txgnn/VERSION`）。
規則要改請改母 repo，再用 `python3 .claude/sync_site_tools.py ITTxGNN` 同步過來，不要直接改這裡的複本。
在本 repo 單獨使用時，先組工作目錄：

```bash
WS=$(bash scripts/txgnn_ws.sh)
cd "$WS"
python3 .claude/dump_license_facts_20261021.py ITTxGNN       # 依證據包算市場狀態（checker 要用）
python3 .claude/checker_trend.py --no-append ITTxGNN           # 全部藥物頁 checker，必須「非 0 0」
```

### 許可證排程更新（GitHub Actions）

`.github/workflows/license-refresh.yml` 每週一 UTC 03:17 自動執行，也可以在 Actions 頁手動觸發（可選只試跑）：

1. 從 Release 還原 `data/`（`scripts/restore_data.sh`）
2. 從主管機關下載最新許可證資料（`scripts/license_adapter.py`），檢查筆數與格式
3. 更新證據包的許可證狀態 → 重算市場狀態 → 同步許可證表 → 事實層改頁 → checker 全量必須 0 → 衍生檔 → gate
4. 全部通過才推上 `main` 並觸發部署；更新後的 `data/` 另存成新的 `data-YYYYMMDD` Release

以下情況一律不推、自動開 issue（label `license-refresh`）：下載失敗或格式改變、狀態變動超過兩成、
改到的藥物頁超過 min(200, 5%)、checker／gate／h1 沒過、有人工查核紀錄的頁會被改到。全程不使用 AI。
<!-- txgnn-ops:end -->
