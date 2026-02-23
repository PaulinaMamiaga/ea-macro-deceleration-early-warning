
# Data Dictionary  
Project: EA Macro Deceleration Early Warning  

---
## Cleaned Dataset Name: ea_ml_ready_deceleration_flag_tplus1

Processed data, ready for ml project.

File:  
data/processed/ea_ml_ready_deceleration_flag_tplus1.csv  

Shape:  
737 rows × 13 columns  

Panel structure:  
Country × Year  

---
## Dataset Description

This dataset contains annual macroeconomic indicators for selected European economies.  
It is structured as a country-year panel dataset prepared for a classification model that predicts whether a growth deceleration will occur in year t+1.

Each row represents one country in one year (t).

---

## Identifiers

### REF_AREA  
Country ISO code (e.g., AUT, DEU, ESP).  
Type: Categorical (string)

### TIME_PERIOD  
Calendar year corresponding to feature values (year t).  
Type: Integer

---

## Target Variable

### Decel_flag_tplus1  
Binary indicator equal to:

- 1 → GDP growth decelerates in year t+1 (relative to year t)  
- 0 → No deceleration in year t+1  

Definition:  
Deceleration is defined as:

GDP_accel_tplus1 < 0  

Where:  
GDP_accel_tplus1 = GDP_growth(t+1) − GDP_growth(t)

Type: Integer (0/1)

---

## Auxiliary Variable (for interpretation only)

### GDP_accel_tplus1  
Continuous measure of GDP growth acceleration between t and t+1.

Positive → acceleration  
Negative → deceleration  

This variable is not intended to be used as a feature in classification models.

Type: Float

---

## Feature Variables (X)

All features correspond to year t and are expressed in percentage terms or GDP ratios.

### IMF_WEO_LUR  
Unemployment rate (% of labor force)

### IMF_WEO_LP  
Labor productivity level

### IMF_WEO_PCPIPCH  
Inflation rate (percent change in consumer prices)

### IMF_WEO_TM_RPCH  
Imports growth (real percent change)

### IMF_WEO_TX_RPCH  
Exports growth (real percent change)

### IMF_WEO_BCA_NGDPD  
Current account balance (% of GDP)

### IMF_WEO_NGSD_NGDP  
Government structural balance (% of GDP)

### IMF_WEO_NGAP_NPGDP  
Output gap (% of potential GDP)

### IMF_WEO_NGDP_RPCH  
Real GDP growth rate (%)

---

## Dataset Properties

Observations: 737  
Countries: Selected European economies  
Years: 1980–2021  
Missing values: None (features and target)  
Duplicates: None  

All features correspond strictly to year t.  
The target corresponds to year t+1.  
No future information leakage is present.

---
## Dataset Source

International Monetary Fund (IMF)

Downloaded from the World Bank Group website: https://data360.worldbank.org/en/dataset/IMF_WEO

---
## Raw Data Name & Info

World Economic Outlook (WEO)
44 Indicators | 1980-2029 |196 Economies
Source: International Monetary Fund (IMF)



