# LaunchLyft — AI Startup Success Predictor

**LaunchLyft** is an intelligent web application that predicts the success probability of early-stage startups using machine learning. Built with Streamlit, it provides an intuitive interface for entrepreneurs and investors to evaluate startup potential based on key factors like funding, team, market, and product.

## Live Demo
Try the deployed application:  
[https://startupsuccessprediction-9emvyabh3jyxjucnigipnq.streamlit.app/](https://startupsuccessprediction-9emvyabh3jyxjucnigipnq.streamlit.app/)

## Dataset Link
[https://www.kaggle.com/datasets/manishkc06/startup-success-prediction](https://www.kaggle.com/datasets/manishkc06/startup-success-prediction)

## Features
- **Interactive Prediction Form**: Input startup details (funding, team size, market, etc.) to get success probability
- **Multi-Page Interface**: Clean navigation between welcome screen and prediction tool
- **Visual Feedback**: Results displayed with confidence metrics and actionable insights
- **Model Caching**: Efficient loading of ML model for faster predictions

## Technologies Used
- **Frontend**: Streamlit (Python framework for web apps)
- **Machine Learning**: Scikit-learn, joblib (for model serialization)
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Handling Imbalanced Data**: Imbalanced-learn

## Installation & Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Startup_Success_Prediction.git
   cd Startup_Success_Prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Open your browser to `http://localhost:8501`

## Project Structure
```
Startup_Success_Prediction/
├── app.py                 # Main Streamlit application
├── predictor.py           # Prediction logic and UI
├── welcome.py             # Welcome page content
├── sidebar.py             # Navigation sidebar
├── styles.py              # Custom CSS styling
├── launchlyft_model.pkl   # Trained ML model
├── requirements.txt       # Python dependencies
```

## Model Information
The prediction model is a machine learning classifier trained on startup dataset features including:
- Funding amount and rounds
- Team size and experience
- Market category and size
- Product development stage
- Business model metrics
