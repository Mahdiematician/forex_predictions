# Forex Prediction Project

## Overview
This is a work in progress. This project aims to predict forex prices using Taylor approximations and possibly other methods to evaluate the prediction accuracy compared to a naive constant price assumption.

## Data
Historical forex data was obtained from the European Central Bank.

## Methodology
1. **Data Preprocessing**: Data is loaded, parsed, and converted into a Pandas DataFrame.
2. **Taylor Approximation**: Calculate expected rates using Taylor approximations.
3. **Delta Calculation**: Evaluate the prediction accuracy by calculating deviations delta for different values of ensemble sizes N.
4. **Naive Model**: Compare the model against a naive assumption of constant price.
5. **Visualization**: Plot the currency rate over time.

## Results
- Comparison of deviation for different values of N.
- Best N value identified for Taylor approximation.
- Evaluation of naive model.

## How to Run
1. Clone the repository.
2. Ensure you have the required libraries: `pip install -r requirements.txt`
3. Run the script: `python your_script.py`

## Conclusion
- The Taylor approximation did not outperform the naive model in this case.
- Further improvements and more sophisticated models may yield better results.

## Contact
For any questions, feel free to reach out to me at Mahdie.Hamdan@outlook.com.
