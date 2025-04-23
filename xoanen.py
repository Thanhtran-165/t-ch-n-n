# Nhập các thư viện cần thiết
from rembg import remove
from PIL import Image, ImageEnhance
import os

# Xác định thư mục chứa file mã nguồn (thư mục làm việc hiện tại)
code_directory = os.getcwd()

print("Chào mừng đến với chương trình xóa nền ảnh!")
print("Nhập đường dẫn đến ảnh cần xóa nền (hoặc gõ 'end' để kết thúc):")

while True:
    # Yêu cầu người dùng nhập đường dẫn ảnh
    input_path = input("Nhập đường dẫn: ").strip()

    # Kiểm tra nếu người dùng muốn kết thúc
    if input_path.lower() == 'end':
        print("Kết thúc chương trình. Cảm ơn bạn đã sử dụng!")
        break

    # Loại bỏ dấu ngoặc kép nếu có
    input_path = input_path.strip('"')

    # Kiểm tra xem đường dẫn có tồn tại không
    if not os.path.exists(input_path):
        print("Đường dẫn không tồn tại. Vui lòng kiểm tra lại.")
        continue

    # Đường dẫn để lưu file hình ảnh đầu ra (trong thư mục chứa mã nguồn)
    output_path = os.path.join(code_directory, "output.png")

    # Mở hình ảnh đầu vào
    inp = Image.open(input_path)

    # Tăng cường chất lượng ảnh (điều chỉnh độ tương phản)
    enhancer = ImageEnhance.Contrast(inp)
    inp_enhanced = enhancer.enhance(1.5)  # Tăng độ tương phản lên 1.5 lần

    # Xóa nền của hình ảnh
    output = remove(inp_enhanced)

    # Lưu hình ảnh đã xóa nền
    output.save(output_path)

    # Thông báo quá trình đã hoàn tất
    print("Quá trình xóa nền đã hoàn tất. Ảnh đã được lưu tại:", output_path)

    # Mở ảnh để xem (tùy thuộc vào hệ điều hành)
    if os.name == 'nt':  # Windows
        os.startfile(output_path)
    elif os.name == 'posix':  # macOS hoặc Linux
        os.system(f"open {output_path}")
    else:
        print("Không thể mở ảnh tự động. Vui lòng mở thủ công tại:", output_path)

    print("\nNhập đường dẫn tiếp theo hoặc gõ 'end' để kết thúc.")