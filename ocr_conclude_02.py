import ocr_online

def determine_positions(ocr_results):
    letters = [item for item in ocr_results['words_result'] if item['words'].isalpha()]
    letter_centers = []

    # 计算每个字母的中心坐标并存储
    for item in letters:
        left = item['location']['left']
        top = item['location']['top']
        width = item['location']['width']
        height = item['location']['height']

        center_x = left + width / 2
        center_y = top + height / 2
        letter_centers.append((item['words'], center_x, center_y))

    # 寻找最小和最大的 x, y 值
    min_x = min(letter[1] for letter in letter_centers)
    max_x = max(letter[1] for letter in letter_centers)
    min_y = min(letter[2] for letter in letter_centers)
    max_y = max(letter[2] for letter in letter_centers)

    # 定义2x2矩阵并计算中心点
    matrix = [[None, None], [None, None]]
    matrix_center_x = (min_x + max_x) / 2
    matrix_center_y = (min_y + max_y) / 2

    # 划分剩余的字母
    for letter, x, y in letter_centers:
        if x < matrix_center_x and y < matrix_center_y:
            matrix[0][0] = letter
        elif x >= matrix_center_x and y < matrix_center_y:
            matrix[0][1] = letter
        elif x < matrix_center_x and y >= matrix_center_y:
            matrix[1][0] = letter
        else:
            matrix[1][1] = letter

    return matrix

def main():
    image_path = r'C:\Users\luojiatao\Desktop\CRAIC_vision\ocr.png'
    ocr_results = ocr_online.ocr_image(image_path)
    matrix = determine_positions(ocr_results)
    print("Matrix:", matrix)

if __name__ == '__main__':
    main()
