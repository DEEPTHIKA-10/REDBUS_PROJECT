import streamlit as st
import mysql.connector  
import pandas as pd
import pymysql




# Create a database connection
conn = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "REDBUS"
)
# Create a cursor object
mycursor = conn.cursor()

##SETTING UP STREAMLIT PAGE

st.set_page_config(layout="wide")
st.title("RED BUS ONLINE BOOKING APP")

st.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit ")
st.image(r"C:\Users\kumar\Desktop\scraped_data\redbusimage.jpg",width=1500)
st.subheader(":REDBUS: Project  by DEEPTHIKA BASKARAN")

# Fetch data from database
mycursor.execute("SELECT * FROM bus_details")
data = pd.DataFrame(mycursor.fetchall(), columns=[desc[0] for desc in mycursor.description])

# sidebar
# Filters
st.sidebar.header("Filters")

mycursor.execute('SELECT DISTINCT state FROM bus_details')
state_list = []
for x in mycursor:
    state_list.append(x[0])
state = st.sidebar.selectbox("State",state_list)

mycursor.execute(f'SELECT DISTINCT route FROM bus_details WHERE state = "{state}"')
route_list = []
for x in mycursor:
    route_list.append(x[0])
route = st.sidebar.selectbox("Route",route_list)

mycursor.execute(f'SELECT DISTINCT Bus_type FROM bus_details WHERE route = "{route}"')
bustype_list = [x[0] for x in mycursor.fetchall()]  # Fetch all rows properly
bustype = st.sidebar.multiselect("Bus Type", bustype_list)


# departure time
st.sidebar.write("Departure Time")
col1, col2 = st.sidebar.columns(2)
with col1:
    t1 = st.time_input("Between")
with col2:
    t2 = st.time_input("And")
# Filter data based on user inputs
filtered_data = data

# p - price
p = st.sidebar.slider("Price Range", 0, 8000, (0, 8000))
p1 = float(p[0])
p2 = float(p[1])

# r - rating
r = st.sidebar.slider("Rating Range", 0.0, 5.0, (0.0, 5.0))
r1 = float(r[0])
r2 = float(r[1])


# Sortings
st.sidebar.header("Sort")
sort = st.sidebar.radio("By",(
    "Departure Time","Arrival Time","Duration",
    "Price: low to high","Price: high to low",
    "Rating"))
st.write('Filtered Data:')
st.dataframe(filtered_data)


if sort == "Departure Time":
    o = "departing_time"
elif sort == "Arrival Time":
    o = "reaching_time"
elif sort == "Duration":
    o = "Total_duration"
elif sort == "Price: low to high":
    o = "price"
elif sort == "Price: high to low":
    o = "price DESC"
else:
    o = "Ratings DESC"

if not bustype:  
    bustype_condition = "AND Bus_type LIKE '%%'"
    params = (route, t1, t2, p1, p2, r1, r2)  # No need to add bustype to parameters
else:
    bustype_tuple = tuple(bustype)
    bustype_condition = "AND Bus_type IN ({})".format(", ".join(["%s"] * len(bustype_tuple)))
    params = (route, *bustype_tuple, t1, t2, p1, p2, r1, r2)

sql_query = f"""
    SELECT route, Bus_name, Bus_type,
        TIME_FORMAT(Start_time, '%h:%i %p') as departing_time,
        Total_duration,
        TIME_FORMAT(End_time, '%h:%i %p') as reaching_time,
        Ratings, Price, Seats_available, routelink, route, state
    FROM bus_details
    WHERE route LIKE %s
    {bustype_condition}
    AND Start_time BETWEEN %s AND %s
    AND price BETWEEN %s AND %s
    AND Ratings BETWEEN %s AND %s
    ORDER BY {o}
"""

mycursor.execute(sql_query, params)

# displaying bus details    
out = mycursor.fetchall()
df = pd.DataFrame(out, columns=[
    "Route","Bus Name","Bus Type",
    "Departure Time","Duration","Arrival Time",
    "Rating","Price in Rs.","Seats Available",
    "Link", "State", "ID"  
])


if len(df) == 0:
    # if no bus found 
    st.write("No bus found for the given filters and sortings.")
else:
    # displaying bus details
    st.dataframe(df, width=4000, height=500)

    # **Download Button for CSV**



# Add a download button to export the filtered data
if not filtered_data.empty:
    st.download_button(
        label="Download Filtered Data",
        data=filtered_data.to_csv(index=False),
        file_name="filtered_data.csv",
        mime="text/csv"
    )
else:
    st.warning("No data available with the selected filters.")