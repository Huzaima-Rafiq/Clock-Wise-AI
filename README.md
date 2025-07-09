# Clock Wise AI

**Clock Wise AI** is a generative AI-powered web application that allows users to create and view multiple digital or analog clocks for different time zones around the world simultaneously. Whether you're working remotely, managing a global team, or just need to stay connected with multiple time zones, this app offers a sleek and simple solution.

Built using Python and Streamlit, the app delivers a real-time, interactive experience with visualizations powered by Plotly and timezone support from pytz. Its minimal design makes it easy to use, lightweight, and fast to deploy.

---

**Features**

- Display multiple clocks for any country or timezone  
- Support for both digital and analog formats  
- Real-time synchronization  
- Interactive and responsive design using Plotly  
- Built entirely in Python using Streamlit  
- Lightweight and deployment-ready

---

**Installation & Usage**

**Prerequisites**  
- Python 3.7 or higher  
- pip (Python package manager)

**Setup Steps**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/clock-wise-ai.git
   cd clock-wise-ai
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

The app will automatically open in your default web browser.

---

**Tech Stack**

- **Language**: Python  
- **Framework**: Streamlit (v1.46.1)  
- **Visualization**: Plotly  
- **Timezone Management**: pytz  
- **Data Handling**: pandas

---

**Project Structure**

```
clock-wise-ai/
├── app.py                # Main application script
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
└── .streamlit/           # (Optional) Streamlit config files
```

---

**License**

This project is licensed under the **MIT License**.  
For more information, see the [LICENSE](LICENSE) file.
