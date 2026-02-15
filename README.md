🌍 GlacioTrack
Seasonal Glacier-Induced Displacement Analysis for VLBI Stations

GlacioTrack is a scientific Python toolkit for analyzing seasonal glacier-driven vertical displacement in Very Long Baseline Interferometry (VLBI) stations.

It isolates glacier-induced elastic loading signals using STL decomposition and quantifies climate coupling through statistically rigorous correlation and lag analysis.

🧊 Scientific Motivation

VLBI stations located near large glacier systems (e.g., Alaska) experience:

Seasonal snow accumulation → crustal depression

Summer melt → elastic rebound

Long-term glacier mass loss → uplift trend

These deformation signals are often entangled with tectonic and atmospheric effects.

GlacioTrack provides tools to:

Extract displacement time series

Separate trend vs seasonal components

Correlate deformation with temperature

Quantify statistical significance

Detect physical lag relationships

🚀 Features

STL time-series decomposition

Seasonal signal isolation

Trend removal (tectonic filtering)

Z-score normalization

Pearson correlation analysis

Lag correlation detection

P-value computation

95% confidence intervals (Fisher transform)

Modular and reusable architecture

📊 Example Output
STL Decomposition

Separates vertical displacement into:

Observed

Long-term trend

Seasonal glacier loading

Residual noise

(Insert your STL plot here)

Seasonal Correlation Results

Example output:

Correlation coefficient: 0.843
P-value: 1.7e-20
95% Confidence Interval: 0.75 to 0.90
Strongest seasonal correlation at lag: 1 month


Interpretation:

Seasonal vertical displacement is strongly correlated with temperature variability, consistent with glacier-driven elastic loading mechanisms.

📁 Project Structure
glaciotrack/
├── glaciotrack/
│   ├── decomposition.py
│   ├── correlation.py
│   └── utils.py
├── scripts/
│   ├── generate_data.py
│   ├── run_decomposition.py
│   └── run_correlation.py
├── data/
├── notebooks/
├── tests/
├── requirements.txt
└── README.md

⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/glaciotrack.git
cd glaciotrack


Create virtual environment:

python -m venv .venv
source .venv/bin/activate


Install dependencies:

pip install -r requirements.txt

▶️ Usage

Generate synthetic dataset:

python scripts/generate_data.py


Run STL decomposition:

python scripts/run_decomposition.py


Run seasonal correlation analysis:

python scripts/run_correlation.py

🧠 Methodology

STL Decomposition
Separates time series into:

Trend (long-term uplift)

Seasonal (glacier loading)

Residual noise

Trend Removal
Only seasonal components are used for correlation.

Normalization
Signals are standardized using z-score normalization.

Statistical Testing

Pearson correlation coefficient

Two-sided p-value

95% confidence interval (Fisher z-transform)

Lag Detection
Cross-correlation is computed across ±6 months to detect physical delay between temperature and deformation.

🔬 Scientific Applications

Cryosphere–solid Earth coupling studies

Glacier mass loading analysis

Tectonic signal filtering

Climate-driven deformation research

Earth system modeling validation

🛠 Dependencies

numpy

pandas

matplotlib

statsmodels

scipy

🧭 Future Roadmap

Real ERA5 temperature integration

Multi-station comparison

GRACE mass anomaly integration

Streamlit dashboard interface

Elastic loading model implementation

📄 License

MIT License