# src/config.py

# -----------------------------
# Project configuration
# -----------------------------

SEED = 42

# Data paths (relative to repo root)
RAW_DATA_PATH = "data/raw/IMF_WEO.csv"
RAW_DICT_PATH = "data/raw/IMF_WEO_DATADICT.csv"

INTERIM_PANEL_PATH = "data/interim/IMF_WEO_A_panel.csv"
PROCESSED_ML_READY_PATH = "data/processed/ea_ml_ready_deceleration_flag_tplus1.csv"

# Panel identifiers
ID_COLS = ["REF_AREA", "TIME_PERIOD"]

# Country list (EA selected set)
EA_COUNTRIES = [
    "DEU", "FRA", "ITA", "ESP", "NLD", "BEL", "AUT", "FIN", "IRL", "PRT", "GRC",
    "SVK", "SVN", "EST", "LVA", "LTU", "LUX", "MLT", "CYP"
]

# Time range
START_YEAR = 1980
END_YEAR = 2023
LAST_USABLE_TARGET_YEAR = 2020  # if you want to avoid later years in modeling

# Target definitions
GDP_GROWTH_COL = "IMF_WEO_NGDP_RPCH"     # GDP real growth (percent)
TARGET_ACCEL_COL = "GDP_accel_tplus1"   # computed: GDP(t+1) - GDP(t)
TARGET_FLAG_COL = "Decel_flag_tplus1"   # computed binary: accel < 0

# Final feature set (X)
FEATURES = [
    "IMF_WEO_LUR",
    "IMF_WEO_LP",
    "IMF_WEO_PCPIPCH",
    "IMF_WEO_TM_RPCH",
    "IMF_WEO_TX_RPCH",
    "IMF_WEO_BCA_NGDPD",
    "IMF_WEO_NGSD_NGDP",
    "IMF_WEO_NGAP_NPGDP",
    "IMF_WEO_NGDP_RPCH",
]

# Train/test split (time-based)
TRAIN_END_YEAR = 2016
TEST_START_YEAR = 2017
TEST_END_YEAR = 2019
