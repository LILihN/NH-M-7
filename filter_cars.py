import pandas as pd

# Đọc file CSV từ GitHub
file_path = "sports_car_prices.csv"  # Tên file CSV đã upload
df = pd.read_csv(file_path)

# Chọn 5 cột cần thiết
selected_columns = ["Car Make", "Car Model", "Year", "Engine Size (L)", "Horsepower"]

# Lọc các hãng xe mong muốn
brands = ["Porsche", "Lamborghini", "Ferrari", "Audi", "BMW"]
filtered_df = df[df["Car Make"].isin(brands)][selected_columns]

# Lưu dữ liệu mới ra file CSV
filtered_df.to_csv("filtered_sports_cars.csv", index=False)

print("Dữ liệu đã được lọc và lưu vào 'filtered_sports_cars.csv'!")
