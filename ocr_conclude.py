import ocr_online

# 常见的OCR错误映射
corrections = {
    '7': '1',  # 错误识别为7的应当是1
    # 添加更多的错误和正确的映射关系
}

# 全局变量
pairs = {}

# 计算两点之间的欧氏距离
def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def main():
    # 图片路径
    image_path = r'C:\Users\luojiatao\Desktop\CRAIC_vision\ocr.png'
    result = ocr_online.ocr_image(image_path)

    # 提取文字结果并计算中心位置
    words_results = [
        {'words': corrections.get(item['words'], item['words']),  # 使用映射纠正错误
         'center': (item['location']['left'] + item['location']['width'] / 2,
                    item['location']['top'] + item['location']['height'] / 2)}
        for item in result['words_result']
    ]

    # 分离数字和字母
    numbers = [item for item in words_results if item['words'].isdigit()]
    letters = [item for item in words_results if item['words'].isalpha()]

    # 定义一个距离阈值
    distance_threshold = 90  # 这个值需要根据实际情况调整

    # 为每个数字找到最近的字母，如果都太远则认为没有匹配
    global pairs
    pairs.clear()
    for number in numbers:
        closest_letter = None
        min_dist = float('inf')
        for letter in letters:
            dist = distance(number['center'], letter['center'])
            if dist < min_dist:
                min_dist = dist
                closest_letter = letter['words']
        if min_dist < distance_threshold and closest_letter:
            pairs[number['words']] = closest_letter
        else:
            pairs[number['words']] = None  # 没有找到接近的字母，或者距离太远

    # 输出结果
    # print(pairs)

if __name__ == '__main__':
    main()
