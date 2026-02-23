# ML Handoff Document  
Project: EA Macro Deceleration Early Warning  

## Objective

Build a classification model to predict whether a macroeconomic growth deceleration will occur in year t+1 using macroeconomic indicators from year t.

Target: Decel_flag_tplus1 (binary)

---

## Dataset

File:  
data/processed/ea_ml_ready_deceleration_flag_tplus1.csv  

Shape:  
737 rows × 13 columns  

Panel structure:  
Country × Year  

No missing values in features or target.  
No duplicated country-year observations.

---

## Feature Set

9 macroeconomic features:

- IMF_WEO_LUR  
- IMF_WEO_LP  
- IMF_WEO_PCPIPCH  
- IMF_WEO_TM_RPCH  
- IMF_WEO_TX_RPCH  
- IMF_WEO_BCA_NGDPD  
- IMF_WEO_NGSD_NGDP  
- IMF_WEO_NGAP_NPGDP  
- IMF_WEO_NGDP_RPCH  

All features are measured at time t.

---

## Target Definition

Decel_flag_tplus1 = 1 if GDP_accel_tplus1 < 0  
Else 0.

GDP_accel_tplus1 = GDP_growth(t+1) − GDP_growth(t)

Balanced distribution:
Approximately 48% positive class.

---

## Time Structure Recommendation

Use time-based split.

Suggested:

1) Post COVID

Train: ≤ 2020  
Test: 2021  

Or alternatively:

2) Before COVID 

Train: ≤ 2016  
Test: 2017–2019  

Do NOT use random split.

---

## Baseline Recommendation

Start with:

- Logistic Regression (baseline)
- Time-based split
- AUC as primary metric
- F1 and Recall as secondary metrics

---

## Next Modeling Steps
