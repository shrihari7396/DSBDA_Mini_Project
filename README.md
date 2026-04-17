# DSBDA Mini Project: COVID-19 Vaccination Analysis

## Project Overview
This project analyzes COVID-19 vaccination data in India using `Untitled1.ipynb`.
It includes data cleaning, summary analysis, and visualization of first dose, second dose, and gender-wise vaccination.

## Notebook File
- `Untitled1.ipynb`

## Dataset Columns Used
The notebook logic is based on these columns:
- `Updated On`
- `State`
- `Total Doses Administered` (present in dataset schema)
- `First Dose Administered`
- `Second Dose Administered`
- `Male (Doses Administered)`
- `Female (Doses Administered)`

Sample format:
```csv
Updated On,State,Total Doses Administered,First Dose Administered,Second Dose Administered
16/01/2021,India,48276,48276,0
17/01/2021,India,58604,58604,0
```

## Verified Notebook Workflow (What `ipynb` Does)
1. Reads CSV: `covid_vaccine_statewise.csv`.
2. Displays:
   - statistical summary (`describe`)
   - dataset structure (`info`)
   - column list
   - first 5 rows (`head`)
3. Cleans data:
   - removes `India` row (`State != 'India'`)
   - strips extra spaces from column names
   - checks null values
   - fills null values with `0`
   - removes duplicates
4. Computes and visualizes:
   - state-wise first dose (bar chart)
   - state-wise second dose (bar chart)
   - gender-wise distribution (donut/pie)
5. Prints total male and female doses.

## Output Images (Extracted from Notebook)
These are direct images from executed notebook outputs:

### First Dose Administered by State
![First Dose Chart](images/cell_16_output_1.png)

### Second Dose Administered by State
![Second Dose Chart](images/cell_17_output_1.png)

### Gender-wise Vaccination Distribution
![Gender-wise Chart](images/cell_21_output_1.png)

## Tech Stack
- Python
- Pandas
- Matplotlib
- Jupyter Notebook

## Run Instructions
1. Install dependencies:
```bash
pip install pandas matplotlib jupyter kagglehub
```

2. Keep dataset file in project folder:
- `covid_vaccine_statewise.csv`

3. Run notebook:
```bash
jupyter notebook Untitled1.ipynb
```

## Important Notes
- Current logic excludes national aggregate (`State == 'India'`) to focus on state-level comparison.
- `Updated On` is sorted as text in current notebook; converting it to datetime would improve date accuracy.

## License
Educational use only.
