# PROJECT: EA Macro Deceleration Early Warning  

This project constructs a macroeconomic **early warning system** aimed at predicting growth deceleration one year ahead in Euro Area countries using IMF World Economic Outlook data (1980–2021). Rather than modeling GDP levels directly, we redefine the prediction task as a classification problem identifying negative growth acceleration. This transformation increases stationarity, improves signal strength, and enhances interpretability. All features are measured strictly at time t to prevent forward-looking bias. The panel dataset is fully balanced, cleaned, and free of information leakage. The modeling framework uses time-based validation to ensure realistic out-of-sample evaluation consistent with macroeconomic forecasting practice.


---
**Project Overview**

This project develops an Early Warning System to predict macroeconomic growth deceleration in selected European economies using annual macroeconomic indicators.
>
*The objective is to anticipate whether GDP growth will decelerate in year t+1 based exclusively on macroeconomic information available in year t.*
>
*Core Question:* Can macroeconomic fundamentals help identify upcoming economic deceleration episodes in Euro Area economies?

The final modeling approach is a supervised classification framework.

--

**Target Definition**

The target variable is:

Decel_flag_tplus1

Defined as:

Decel_flag_tplus1 = 1 if GDP_accel_tplus1 < 0 Else 0

Where:

GDP_accel_tplus1 = GDP_growth(t+1) − GDP_growth(t)

This definition captures any economic deceleration, creating a broad early warning signal rather than focusing exclusively on recessions.

Target distribution is approximately balanced (48% positive class), which supports stable classification performance.

---

**Features**

Nine macroeconomic indicators measured at time t:

- Unemployment rate

- Labor productivity

- Inflation

- Imports growth

- Exports growth

- Current account balance (% GDP)

- Structural fiscal balance (% GDP)

- Output gap (% potential GDP)

- Real GDP growth (%)


All features are strictly contemporaneous (year t) to prevent information leakage.

---

**Data Structure**

Observations: 737

Countries: European economies

Years: 1980–2021

Missing values: None

Duplicates: None

Panel format: Country × Year

---

**Modeling Strategy**

Time-based train/test split

Baseline: Logistic Regression

Evaluation metrics: AUC (primary), F1 and Recall (secondary)

No random shuffling (to preserve temporal integrity)



