from minizinc import Instance, Model, Solver

# Tải mô hình MiniZinc từ file rush_hour.mzn
model = Model("/Users/nguyencanhtung/Program/python/Game/RushHour/solver/rush_hour.mzn")


# Chọn solver (ví dụ: Gecode)
solver = Solver.lookup('cbc')

# Tạo một phiên bản của bài toán dựa trên mô hình
instance = Instance(solver, model)

# Cung cấp dữ liệu cho mô hình
instance["n"] = 6  # Lưới 6x6
instance["r"] = 2  # Có 2 xe
instance["exit_pos"] = 6  # Cổng thoát ở ô 6
instance["size"] = [2, 3]  # Kích thước của các xe
instance["direction"] = [1, -1]  # Xe 1 ngang, xe 2 dọc
instance["init_pos"] = [2, 1]  # Vị trí khởi đầu của các xe

# Giải bài toán
result = instance.solve()

# In ra kết quả
print(result)
