# REDBUS_PROJECT
# REDBUS ONLINE BOOKING APP

## Overview
RedBus Online Booking App is a web application built using Streamlit and MySQL that allows users to filter and view bus details based on various parameters such as state, route, bus type, price range, and ratings.

---

## Features
- Fetches real-time bus data from a MySQL database
- Filters buses based on **state, route, bus type, price range, and ratings**
- Sorting options: **Departure Time, Arrival Time, Duration, Price, and Ratings**
- **Download filtered results as a CSV file**
- Interactive and user-friendly interface with Streamlit

---

## Project Structure
```
📂 redbus-app
│── 📄 app.py              # Streamlit app main file
│── 📄 requirements.txt     # Python dependencies
│── 📄 README.docx          # Documentation (Word format)
│── 📂 data                 # Dataset (if needed)
│── 📂 images               # Screenshots of the app
```

---

## Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/redbus-app.git
cd redbus-app
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up MySQL Database
#### Create a Database
```sql
CREATE DATABASE REDBUS;
```
#### Create `bus_details` Table
```sql
CREATE TABLE bus_details (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Bus_name VARCHAR(255) NOT NULL,
    Bus_type VARCHAR(255) NOT NULL,
    Start_time TIME NOT NULL,
    End_time TIME NOT NULL,
    Total_duration VARCHAR(255) NOT NULL,
    Price FLOAT NOT NULL,
    Seats_Available INT NOT NULL,
    Ratings FLOAT NOT NULL,
    routelink TEXT NOT NULL,
    route VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL
);
```
#### Insert Sample Data
```sql
INSERT INTO bus_details (Bus_name, Bus_type, Start_time, End_time, Total_duration, Price, Seats_Available, Ratings, routelink, route, state)
VALUES
('APSRTC - 9603', 'NON AC Seater', '06:00:00', '12:20:00', '6h 20m', 296, 41, 3.4, 'https://www.redbus.in/', 'Bangalore to Tirupati', 'Karnataka');
```

---

## Running the Application
```bash
streamlit run app.py
```

---

## Configuration
Edit **database connection settings** in `app.py`:
```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="REDBUS"
)
```

---

## Screenshots
| Home Page | Filters |
|-----------|---------|
| ![Home](your_home_screenshot_url) | ![Filters](your_filter_screenshot_url) |

---

## Contributing
✅ Fork the repository  
✅ Create a new branch (`git checkout -b feature-name`)  
✅ Commit changes (`git commit -m "Added new feature"`)  
✅ Push to GitHub (`git push origin feature-name`)  
✅ Open a **Pull Request**  

---

## License
This project is **open-source** under the **MIT License**.

---

## Connect with Me
🔹 **GitHub:** [yourusername](https://github.com/DEEPTHIKA-10)  

🚀 **Happy Coding!** 🚌✨

