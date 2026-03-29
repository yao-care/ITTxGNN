"""疾病映射模組 - 葡萄牙語適應症/治療類別映射至 TxGNN 疾病本體"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# 葡萄牙語-英語疾病/症狀對照表
DISEASE_DICT = {
    # === Sistema cardiovascolare ===
    "ipertensione": "hypertension",
    "ipertensione arteriosa": "hypertension",
    "pressione alta": "hypertension",
    "ipotensione": "hypotension",
    "infarto miocardico": "myocardial infarction",
    "infarto": "myocardial infarction",
    "angina pectoris": "angina",
    "aritmia": "arrhythmia",
    "fibrillazione atriale": "atrial fibrillation",
    "insufficienza cardiaca": "heart failure",
    "scompenso cardiaco": "heart failure",
    "malattia coronarica": "coronary artery disease",
    "trombosi venosa profonda": "deep vein thrombosis",
    "embolia polmonare": "pulmonary embolism",
    "ipercolesterolemia": "hypercholesterolemia",
    "dislipidemia": "dyslipidemia",
    "aterosclerosi": "atherosclerosis",
    # === Sistema respiratorio ===
    "broncopneumopatia cronica ostruttiva": "chronic obstructive pulmonary disease",
    "bpco": "chronic obstructive pulmonary disease",
    "asma": "asthma",
    "asma bronchiale": "asthma",
    "polmonite": "pneumonia",
    "bronchite": "bronchitis",
    "influenza": "influenza",
    "tubercolosi": "tuberculosis",
    "fibrosi cistica": "cystic fibrosis",
    "apnea del sonno": "obstructive sleep apnea",
    "dispnea": "dyspnea",
    "enfisema": "emphysema",
    "sinusite": "sinusitis",
    "rinite allergica": "allergic rhinitis",
    # === Sistema digerente ===
    "reflusso gastroesofageo": "gastroesophageal reflux disease",
    "ulcera gastrica": "gastric ulcer",
    "ulcera duodenale": "duodenal ulcer",
    "gastrite": "gastritis",
    "sindrome dell'intestino irritabile": "irritable bowel syndrome",
    "malattia infiammatoria intestinale": "inflammatory bowel disease",
    "morbo di crohn": "crohn disease",
    "colite ulcerosa": "ulcerative colitis",
    "stitichezza": "constipation",
    "diarrea": "diarrhea",
    "nausea": "nausea",
    "vomito": "vomiting",
    "steatosi epatica": "hepatic steatosis",
    "cirrosi epatica": "liver cirrhosis",
    "epatite": "hepatitis",
    "epatite b": "hepatitis b",
    "epatite c": "hepatitis c",
    "pancreatite": "pancreatitis",
    "calcoli biliari": "cholelithiasis",
    # === Sistema nervoso ===
    "malattia di alzheimer": "alzheimer disease",
    "alzheimer": "alzheimer disease",
    "morbo di parkinson": "parkinson disease",
    "parkinson": "parkinson disease",
    "epilessia": "epilepsy",
    "sclerosi multipla": "multiple sclerosis",
    "emicrania": "migraine",
    "cefalea": "headache",
    "mal di testa": "headache",
    "ictus": "stroke",
    "ictus cerebrale": "stroke",
    "neuropatia": "neuropathy",
    "neuropatia periferica": "peripheral neuropathy",
    "meningite": "meningitis",
    "encefalite": "encephalitis",
    # === Disturbi psichiatrici ===
    "depressione": "depression",
    "disturbo depressivo maggiore": "major depressive disorder",
    "ansia": "anxiety disorder",
    "disturbo d'ansia generalizzato": "generalized anxiety disorder",
    "disturbo bipolare": "bipolar disorder",
    "schizofrenia": "schizophrenia",
    "disturbo ossessivo-compulsivo": "obsessive-compulsive disorder",
    "doc": "obsessive-compulsive disorder",
    "disturbo da stress post-traumatico": "post-traumatic stress disorder",
    "insonnia": "insomnia",
    "disturbo da deficit di attenzione": "attention deficit hyperactivity disorder",
    "adhd": "attention deficit hyperactivity disorder",
    # === Sistema endocrino ===
    "diabete mellito": "diabetes mellitus",
    "diabete": "diabetes mellitus",
    "diabete di tipo 1": "type 1 diabetes mellitus",
    "diabete di tipo 2": "type 2 diabetes mellitus",
    "ipotiroidismo": "hypothyroidism",
    "ipertiroidismo": "hyperthyroidism",
    "gozzo": "goiter",
    "sindrome di cushing": "cushing syndrome",
    "morbo di addison": "addison disease",
    "obesità": "obesity",
    "sindrome metabolica": "metabolic syndrome",
    "gotta": "gout",
    "iperuricemia": "hyperuricemia",
    # === Sistema muscoloscheletrico ===
    "artrite": "arthritis",
    "artrite reumatoide": "rheumatoid arthritis",
    "artrosi": "osteoarthritis",
    "osteoporosi": "osteoporosis",
    "lupus eritematoso sistemico": "systemic lupus erythematosus",
    "lupus": "systemic lupus erythematosus",
    "fibromialgia": "fibromyalgia",
    "spondilite anchilosante": "ankylosing spondylitis",
    "tendinite": "tendinitis",
    "lombalgia": "low back pain",
    # === Malattie della pelle ===
    "psoriasi": "psoriasis",
    "eczema": "eczema",
    "dermatite atopica": "atopic dermatitis",
    "orticaria": "urticaria",
    "acne": "acne",
    "rosacea": "rosacea",
    "vitiligine": "vitiligo",
    "alopecia": "alopecia",
    "herpes zoster": "herpes zoster",
    "herpes labiale": "herpes simplex",
    "micosi": "fungal infection",
    # === Sistema urinario ===
    "infezione delle vie urinarie": "urinary tract infection",
    "cistite": "cystitis",
    "nefrite": "nephritis",
    "insufficienza renale": "renal failure",
    "malattia renale cronica": "chronic kidney disease",
    "calcoli renali": "nephrolithiasis",
    "ipertrofia prostatica benigna": "benign prostatic hyperplasia",
    "incontinenza urinaria": "urinary incontinence",
    # === Oftalmologia ===
    "glaucoma": "glaucoma",
    "cataratta": "cataract",
    "degenerazione maculare": "macular degeneration",
    "congiuntivite": "conjunctivitis",
    "retinopatia diabetica": "diabetic retinopathy",
    "occhio secco": "dry eye syndrome",
    # === ORL ===
    "otite media": "otitis media",
    "faringite": "pharyngitis",
    "tonsillite": "tonsillitis",
    "laringite": "laryngitis",
    "vertigine": "vertigo",
    # === Malattie infettive ===
    "infezione da hiv": "hiv infection",
    "aids": "acquired immunodeficiency syndrome",
    "malaria": "malaria",
    "covid-19": "covid-19",
    "sepsi": "sepsis",
    "candidosi": "candidiasis",
    "toxoplasmosi": "toxoplasmosis",
    # === Allergie ===
    "allergia": "allergy",
    "anafilassi": "anaphylaxis",
    "asma allergico": "allergic asthma",
    "rinite": "rhinitis",
    "dermatite da contatto": "contact dermatitis",
    "allergia alimentare": "food allergy",
    # === Ginecologia ===
    "endometriosi": "endometriosis",
    "sindrome dell'ovaio policistico": "polycystic ovary syndrome",
    "menopausa": "menopause",
    "dismenorrea": "dysmenorrhea",
    "amenorrea": "amenorrhea",
    "vaginite": "vaginitis",
    "fibroma uterino": "uterine fibroid",
    "preeclampsia": "preeclampsia",
    # === Cancro ===
    "cancro": "cancer",
    "tumore": "cancer",
    "cancro al seno": "breast cancer",
    "tumore al seno": "breast cancer",
    "cancro ai polmoni": "lung cancer",
    "cancro del colon-retto": "colorectal cancer",
    "cancro alla prostata": "prostate cancer",
    "cancro al fegato": "liver cancer",
    "cancro allo stomaco": "stomach cancer",
    "cancro al pancreas": "pancreatic cancer",
    "leucemia": "leukemia",
    "linfoma": "lymphoma",
    "melanoma": "melanoma",
    # === Sintomi generali ===
    "febbre": "fever",
    "dolore": "pain",
    "dolore cronico": "chronic pain",
    "infiammazione": "inflammation",
    "edema": "edema",
    "stanchezza": "fatigue",
    "anemia": "anemia",
}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 疾病詞彙表"""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """建立疾病名稱索引（關鍵詞 -> (disease_id, disease_name)）"""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # 完整名稱
        index[name_upper] = (disease_id, disease_name)

        # 提取關鍵詞（按空格和逗號分割）
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:  # 只保留較長的關鍵詞
                index[kw] = (disease_id, disease_name)

    return index


def extract_indications(indication_str: str) -> List[str]:
    """從適應症/治療類別文字提取個別適應症

    使用葡萄牙語常見分隔符分割
    """
    if not indication_str:
        return []

    # 正規化
    text = indication_str.strip().lower()

    # 使用分隔符分割
    parts = re.split(r"[.;]", text)

    indications = []
    for part in parts:
        # 再用逗號細分
        sub_parts = re.split(r"[,/]", part)
        for sub in sub_parts:
            sub = sub.strip()
            # 移除常見前綴
            sub = re.sub(r"^(para |tratamento de |indicado para |usado para )", "", sub)
            # 移除常見後綴
            sub = re.sub(r"( e outros| etc\.?)$", "", sub)
            sub = sub.strip()
            if sub and len(sub) >= 2:
                indications.append(sub)

    return indications


def translate_indication(indication: str) -> List[str]:
    """將葡萄牙語適應症翻譯為英文關鍵詞"""
    keywords = []
    indication_lower = indication.lower()

    for pt, en in DISEASE_DICT.items():
        if pt in indication_lower:
            keywords.append(en.upper())

    return keywords


def map_indication_to_disease(
    indication: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """將單一適應症映射到 TxGNN 疾病

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # 翻譯為英文關鍵詞
    keywords = translate_indication(indication)

    for kw in keywords:
        # 完全匹配
        if kw in disease_index:
            disease_id, disease_name = disease_index[kw]
            results.append((disease_id, disease_name, 1.0))
            continue

        # 部分匹配
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if kw in index_kw or index_kw in kw:
                results.append((disease_id, disease_name, 0.8))

    # 去重並按信心度排序
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:5]  # 最多返回 5 個匹配


def map_fda_indications_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """將巴西 ANVISA 藥品治療類別映射到 TxGNN 疾病"""
    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []

    for _, row in fda_df.iterrows():
        # ANVISA 使用 CLASSE_TERAPEUTICA 而非適應症
        indication_str = row.get("CLASSE_TERAPEUTICA", "")
        if not indication_str:
            continue

        # 提取個別適應症
        indications = extract_indications(indication_str)

        for ind in indications:
            # 翻譯並映射
            matches = map_indication_to_disease(ind, disease_index)

            if matches:
                for disease_id, disease_name, confidence in matches:
                    results.append({
                        "NUMERO_REGISTRO_PRODUTO": row.get("NUMERO_REGISTRO_PRODUTO", ""),
                        "NOME_PRODUTO": row.get("NOME_PRODUTO", ""),
                        "CLASSE_TERAPEUTICA": indication_str[:100],
                        "extracted_indication": ind,
                        "disease_id": disease_id,
                        "disease_name": disease_name,
                        "confidence": confidence,
                    })
            else:
                results.append({
                    "NUMERO_REGISTRO_PRODUTO": row.get("NUMERO_REGISTRO_PRODUTO", ""),
                    "NOME_PRODUTO": row.get("NOME_PRODUTO", ""),
                    "CLASSE_TERAPEUTICA": indication_str[:100],
                    "extracted_indication": ind,
                    "disease_id": None,
                    "disease_name": None,
                    "confidence": 0,
                })

    return pd.DataFrame(results)


def get_indication_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算適應症映射統計"""
    total = len(mapping_df)
    mapped = mapping_df["disease_id"].notna().sum()
    unique_indications = mapping_df["extracted_indication"].nunique()
    unique_diseases = mapping_df[mapping_df["disease_id"].notna()]["disease_id"].nunique()

    return {
        "total_indications": total,
        "mapped_indications": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_indications": unique_indications,
        "unique_diseases": unique_diseases,
    }
