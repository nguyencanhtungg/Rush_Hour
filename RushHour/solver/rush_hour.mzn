% rush_hour.mzn

int: n;              % Kích thước lưới (ví dụ: 6 cho lưới 6x6)
int: r;              % Số lượng xe
int: exit_pos;       % Vị trí của cổng thoát

% Mảng kích thước của các xe
array[1..r] of int: size;  

% Mảng hướng của các xe (1: ngang, -1: dọc)
array[1..r] of int: direction; 

% Mảng vị trí ban đầu của các xe
array[1..r] of int: init_pos;  

% Mảng biến đại diện cho vị trí của các xe tại mỗi bước
array[1..r, 1..n] of var 1..n: pos;  

% Xe không được ra khỏi lưới
constraint forall(v in 1..r, t in 1..n)(
    pos[v, t] + size[v] - 1 <= n
);

% Các xe không được chồng lên nhau
constraint forall(v1 in 1..r, v2 in 1..r where v1 != v2, t in 1..n)(
    pos[v1, t] + size[v1] - 1 < pos[v2, t] \/
    pos[v2, t] + size[v2] - 1 < pos[v1, t]
);

% Mục tiêu: xe đỏ (xe 1) phải ra khỏi lưới
solve minimize;

