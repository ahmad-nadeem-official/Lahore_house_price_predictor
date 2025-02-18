import tkinter as tk
from tkinter import ttk, font
from main import predict_house_price

# Initialize the main window
window = tk.Tk()
window.title("House Price Predictor")
window.geometry("600x630")
window.resizable(False, False)
window.configure(bg="#f9f9f9")

# Fonts
title_font = font.Font(family="Helvetica", size=20, weight="bold")
label_font = font.Font(family="Helvetica", size=12, weight="normal")
button_font = font.Font(family="Helvetica", size=12, weight="bold")

# Header Label
header_label = tk.Label(
    window,
    text="🏡 House Price Predictor",
    bg="#0078D7",
    fg="white",
    font=title_font,
    pady=10,
    width=40,
    anchor="center"
)
header_label.pack(pady=20)

# Input Frame
input_frame = tk.Frame(window, bg="#f9f9f9", padx=20, pady=20, relief="ridge", bd=2)
input_frame.pack(pady=10, padx=20, fill="x")

# House Type
house_type_label = tk.Label(input_frame, text="House Type:", bg="#f9f9f9", font=label_font)
house_type_label.grid(row=0, column=0, sticky="w", pady=5, padx=10)
house_type_options = ['House' ,'Flat' ,'Penthouse' ,'Room']
house_type_dropdown = ttk.Combobox(input_frame, values=house_type_options, font=label_font, state="readonly", width=30)
house_type_dropdown.grid(row=0, column=1, pady=5)

# Number of Bedrooms

bedrooms_label = tk.Label(input_frame, text="Number of Bedrooms:", bg="#f9f9f9", font=label_font)
bedrooms_label.grid(row=1, column=0, sticky="w", pady=5, padx=10)
bedrooms_options = [5,  3 , 4 , 2 , 6,  1,  7, 11,  8 , 9, 10]
bedrooms_dropdown = ttk.Combobox(input_frame, values=bedrooms_options, font=label_font, state="readonly", width=30)
bedrooms_dropdown.grid(row=1, column=1, pady=5)

# Number of Bathrooms
bathrooms_label = tk.Label(input_frame, text="Number of Bathrooms:", bg="#f9f9f9", font=label_font)
bathrooms_label.grid(row=2, column=0, sticky="w", pady=5, padx=10)
bathrooms_options = [6  ,5 , 3 , 4,  2,  1 , 7 , 8,  9, 10]
bathrooms_dropdown = ttk.Combobox(input_frame, values=bathrooms_options, font=label_font, state="readonly", width=30)
bathrooms_dropdown.grid(row=2, column=1, pady=5)

# Location
locations = [
    'DHA Defence', 'Bahria Orchard', 'Paragon City', 'Askari', 'Khayaban-e-Amin', 'Nishtar Colony', 'Central Park Housing Scheme',
    'New Lahore City', 'Bahria Nasheman', 'Bahria Town', 'Eden', 'State Life Housing Society', 'Bankers Avenue Cooperative Housing Society',
    'Raiwind Road', 'Johar Town', 'Highcourt Society', 'Thokar Niaz Baig', 'Military Accounts Housing Society', 'Defence Road', 'Multan Road', 'Jubilee Town',
    'Punjab University Employees Society', 'Al Noor Park Housing Society', 'Harbanspura', 'Park View City', 'Mughalpura', 'GT Road', 'Rail Town (Canal City)',
    'Green City', 'Lahore Medical Housing Society', 'College Road', 'Ferozepur Road', 'Architects Engineers Housing Society', 'Sunfort Gardens', 'Canal Garden', 'Kahna',
    'Sanda', 'Gulberg', 'DHA 11 Rahbar', 'Izmir Town', 'LDA Avenue', 'Gulshan-e-Ravi', 'Punjab Coop Housing Society', 'Valencia Housing Society', 'Wapda Town',
    'Sue-e-Asal', 'EME Society', 'IEP Engineers Town', 'Sheraz Town', 'PCSIR Housing Scheme', 'Allama Iqbal Town', 'Al Rehman Garden', 'Main Canal Bank Road', 'OPF Housing Scheme',
    'Nasheman-e-Iqbal', 'Gulshan-e-Lahore', 'Revenue Society', 'Peco Road', 'Pine Avenue', 'Gosha-e-Ahbab', 'Garden Town', 'Pak Arab Housing Society', 'Abid Road',
    'Vital Homes Housing Scheme', 'Sabzazar Scheme', 'Tariq Gardens', 'Shadab Garden', 'Venus Housing Scheme', 'Bedian Road', 'Sui Gas Housing Society', 'Ghous Garden',
    'Canal Fort II', 'Nawab Town', 'Tricon Village', 'Icon Valley', 'Mozang', 'Dream Avenue Lahore', 'Chaudhary Colony', 'Formanites Housing Scheme', 'Chungi Amar Sadhu',
    'Faisal Town', 'IBL Housing Scheme', 'NFC 1', 'Model Town', 'Cantt', 'Shoukat Town', 'Chinar Bagh', 'Sukh Chayn Gardens', 'New Garden Town', 'Rehmanpura (Ferozpur Road)',
    'Shalimar Link Road', 'Al-Hamd Park', 'HBFC Housing Society', 'Divine Gardens', 'TIP Housing Scheme', 'Park Avenue Housing Scheme', 'Ashraf Garden', 'Punjab Govt Employees Society',
    'Ichhra', 'Beacon House Society', 'Rehan Garden', 'Audit & Accounts Housing Society', 'Rizwan Garden Scheme', 'Wagha Town', 'PIA Housing Scheme', 'Manawan', 'Al-Hafiz Town',
    'PCSIR Staff Colony', 'Lahore Motorway City', 'Fazaia Housing Scheme', 'Cavalry Extension', 'Punjab Small Industries Colony', 'Iqbal Park', 'Rehman Villas', 'Hamza Town', 'Bagarian',
    'Sami Town', 'Marghzar Officers Colony', 'UET Housing Society', 'Lahore - Kasur Road', 'City Life Homes', 'Noor Jahan Road', 'Public Health Society', 'Grand Avenues Housing Scheme',
    'Alpha Society', 'New Super Town', 'Shanghai Road', 'Tajpura', 'Walton Road', 'Bankers Town', 'Shershah Colony - Raiwind Road', 'New Muslim Town', 'Al-Hamad Colony (AIT)',
    'Taj Bagh Scheme', 'Canal Bank Housing Scheme', 'Shahdara', 'Cantt View Society', 'Ahlu Road', 'Cavalry Ground', 'Zaheer Villas', 'Abdalians Cooperative Housing Society',
    'Habib Homes', 'T & T Aabpara Housing Society', 'Muslim Town', 'Baghbanpura', 'Government Employees Cooperative Housing Society (GECHS)', 'Lalazaar Garden', 'Manhala Road',
    'Defence Fort', 'Rehman Housing Society', 'Gulshan View Residence Society', 'Atari Saroba', 'Jamal Homes', 'Samanabad', 'Raj Garh', 'Islampura', 'Super Town', 'GOR',
    'Sharaqpur Road', 'Al-Qayyum Garden', 'Shah Jamal', 'Chughtai Garden', 'Airline Housing Society', 'Shadman', 'Al Jalil Garden', 'Punjab Government Servant Housing Foundation',
    'Davis Road', 'West Wood Housing Society', 'Ashiana-e-Quaid Housing Scheme', 'Ring Road', 'Alfalah Town', 'Land Breeze Housing Society', 'Awasia Housing Society', 'Samundari Road',
    'Hassan Town', 'Zahoor Manzil', 'Al Zohra Garden'
]


location_label = tk.Label(input_frame, text="Location:", bg="#f9f9f9", font=label_font)
location_label.grid(row=3, column=0, sticky="w", pady=5, padx=10)
location_dropdown=ttk.Combobox(input_frame, values=locations, font=label_font, state="readonly", width=30)
location_dropdown.grid(row=3, column=1, pady=5)

# Area
area = [
    '1 Kanal', '8 Marla', '10 Marla', '5 Marla', '2.5 Marla', '2 Kanal', '1.3 Kanal', '3 Marla', '4 Marla', '12 Marla', '1.1 Kanal', '9 Marla',
    '6.1 Marla', '7.6 Marla', '7 Marla', '3.5 Marla', '6 Marla', '1.3 Marla', '2.3 Marla', '2.2 Marla', '2.6 Marla', '2 Marla', '5.5 Marla', '7.3 Marla',
    '11 Marla', '1.8 Marla', '16 Marla', '3.8 Marla', '2.7 Marla', '2.4 Marla', '6.8 Marla', '11.1 Marla', '4.2 Marla', '1.4 Marla', '8.7 Marla', '1.5 Marla',
    '1.6 Kanal', '13 Marla', '5.1 Marla', '1.6 Marla', '1.5 Kanal', '8.2 Marla', '5.3 Marla', '5.2 Marla', '1.7 Kanal', '1.8 Kanal', '1.2 Kanal', '4.6 Marla',
    '14 Marla', '3.3 Marla', '5.4 Marla', '4.9 Marla', '17 Marla', '18 Marla', '4 Kanal', '13.4 Marla', '3.9 Marla', '11.5 Marla', '2.8 Marla', '3 Kanal',
    '6.5 Marla', '2.3 Kanal', '4.1 Kanal', '7.8 Marla', '2.9 Marla', '15 Marla', '3.2 Marla', '4.5 Marla', '12.7 Marla', '6.3 Marla', '1.7 Marla', '3.6 Marla',
    '6 Kanal', '11.2 Marla', '19.2 Marla', '4.4 Kanal', '12.9 Marla', '6.7 Marla', '10.5 Marla', '10.7 Marla', '7.5 Marla', '1.9 Marla', '2.1 Marla', '1.4 Kanal',
    '10.8 Marla', '4.4 Marla', '5 Kanal', '3.2 Kanal', '9.3 Marla', '7.2 Marla', '5.8 Marla', '5.6 Marla', '10.1 Marla', '9.5 Marla', '3.1 Marla', '13.1 Marla',
    '8.1 Marla', '13.3 Marla', '17.8 Marla', '8 Kanal', '14.1 Marla', '14.7 Marla', '13.5 Marla', '18.7 Marla', '14.8 Marla', '9.6 Marla', '3.7 Marla',
    '4.8 Marla', '9.2 Marla', '12.5 Marla', '6.8 Kanal', '9.4 Marla', '14.5 Marla', '17.2 Marla', '13.7 Marla', '4.7 Marla', '1.1 Marla', '8.4 Marla',
    '15.1 Marla', '2.4 Kanal', '2.1 Kanal', '1 Marla', '2.6 Kanal', '2.2 Kanal', '8.5 Marla', '19 Marla', '9.8 Marla', '1.2 Marla', '9.1 Kanal', '13.8 Marla',
    '7.9 Marla', '6.2 Marla', '2.8 Kanal', '9.7 Marla', '12.6 Marla', '7.1 Marla', '6.9 Marla', '7.7 Marla', '5.9 Marla', '4.2 Kanal', '12.2 Marla', '4.1 Marla',
    '7.4 Marla', '2.9 Kanal', '4.5 Kanal', '11.6 Marla', '11.3 Marla', '12.8 Marla', '1.9 Kanal', '3.5 Kanal', '9.1 Marla', '2.5 Kanal', '10.6 Marla',
    '14.2 Marla', '6.6 Marla', '11.8 Marla', '3.1 Kanal', '9.9 Marla', '11.9 Marla', '10.9 Marla', '7 Kanal', '3.4 Marla', '8.8 Marla', '15.6 Marla',
    '17.5 Marla', '5.7 Marla', '18.5 Marla', '12.4 Marla', '3.3 Kanal', '2.7 Kanal'
]
area.extend([
    '3.1 Kanal', '12.6 Marla', '7.1 Marla', '6.9 Marla', '7.7 Marla', '5.9 Marla', '4.2 Kanal', '12.2 Marla', '4.1 Marla',
    '7.4 Marla', '2.9 Kanal', '4.5 Kanal', '11.6 Marla', '11.3 Marla', '12.8 Marla', '1.9 Kanal', '3.5 Kanal', '9.1 Marla',
    '2.5 Kanal', '10.6 Marla', '14.2 Marla', '6.6 Marla', '11.8 Marla', '3.1 Kanal', '9.9 Marla', '11.9 Marla', '10.9 Marla',
    '7 Kanal', '3.4 Marla', '8.8 Marla', '15.6 Marla', '17.5 Marla', '5.7 Marla', '18.5 Marla', '12.4 Marla', '3.3 Kanal'
])

area_label = tk.Label(input_frame, text="Area (sq ft):", bg="#f9f9f9", font=label_font)
area_label.grid(row=4, column=0, sticky="w", pady=5, padx=10)
area_entry = ttk.Combobox(input_frame, values=area, font=label_font, state="readonly", width=30)
area_entry.grid(row=4, column=1, pady=5)

# Result Label
result_frame = tk.Frame(window, bg="#ffffff", pady=20, padx=10, relief="ridge", bd=2)
result_frame.pack(pady=20, padx=20, fill="x")
result_label = tk.Label(
    result_frame,
    text="Predicted Price: N/A",
    bg="#ffffff",
    fg="#0078D7",
    font=label_font,
    height=2,
    anchor="center"
)
result_label.pack()

# Predict Button
def on_predict():
    house_type = house_type_dropdown.get()
    bedrooms = bedrooms_dropdown.get()
    bathrooms = bathrooms_dropdown.get()
    location = location_dropdown.get()
    area = area_entry.get()

    if house_type and bedrooms and bathrooms and location and area:
        try:
            price = predict_house_price(house_type, int(bedrooms), int(bathrooms), location, area)
            result_label.config(text=f"Predicted Price: PKR{price:,.2f}")
        except Exception as e:
            result_label.config(text="Error: Unable to predict. Check inputs.")
    else:
        result_label.config(text="Error: Please fill all fields.")

predict_button = tk.Button(
    window,
    text="Predict Price",
    font=button_font,
    bg="#0078D7",
    fg="white",
    command=on_predict,
    relief="raised",
    width=20,
    height=2
)
predict_button.pack(pady=10)

# Footer
footer_label = tk.Label(
    window,
    text="© 2025 House Price Predictor | Powered by AI",
    bg="#f9f9f9",
    font=("Helvetica", 10),
    fg="gray"
)
footer_label.pack(side="bottom", pady=10)

# Run the Tkinter event loop
window.mainloop()
