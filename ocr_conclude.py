import ocr_online
from collections import deque

# 常见的OCR错误映射
corrections = {
    '7': '1',  # 错误识别为7的应当是1
    # 可以根据实际情况添加更多的映射关系
}

# 计算两点之间的欧氏距离
def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

# 根据已知数字推断缺失数字的位置
def infer_missing_numbers(numbers):
    detected = {item['words']: item['center'] for item in numbers}
    all_nums = {'1', '2', '3', '4'}
    missing_nums = all_nums - set(detected.keys())
    inferred = {}
    
    for num in missing_nums:
        if num == '1' and '2' in detected and '3' in detected:
            x2, y2 = detected['2']
            x3, y3 = detected['3']
            inferred['1'] = (x3, y2)  # 左上角
        elif num == '2' and '1' in detected and '4' in detected:
            x1, y1 = detected['1']
            x4, y4 = detected['4']
            inferred['2'] = (x4, y1)  # 右上角
        elif num == '3' and '1' in detected and '4' in detected:
            x1, y1 = detected['1']
            x4, y4 = detected['4']
            inferred['3'] = (x1, y4)  # 左下角
        elif num == '4' and '2' in detected and '3' in detected:
            x2, y2 = detected['2']
            x3, y3 = detected['3']
            inferred['4'] = (x2, y3)  # 右下角
    return {**detected, **inferred}

def main():
    # 图片路径
    image_path = r'C:\Users\luojiatao\Desktop\CRAIC_vision\01.jpg'
    result = ocr_online.ocr_image(image_path)
    print(result)
    # 提取文字结果并计算中心位置
    words_results = [
        {'words': corrections.get(item['words'], item['words']),  # 使用映射纠正错误
         'center': (item['location']['left'] + item['location']['width'] / 2,
                    item['location']['top'] + item['location']['height'] / 2)}
        for item in result['words_result']
    ]
    # 分离数字和字母
    numbers = [item for item in words_results if item['words'].isdigit()]
    numbers = infer_missing_numbers(numbers)  # 更新包含推断数字的列表
    letter_queue = deque([(item['words'], item['center']) for item in words_results if item['words'].isalpha()])
    pairs = {}
    matched_numbers = set()
    
    # 从队列中依次处理每个字母
    while letter_queue:
        letter, letter_center = letter_queue.popleft()
        closest_number = None
        min_distance = float('inf')
        for number, center in numbers.items():
            if number not in matched_numbers:
                dist = distance(letter_center, center)
                if dist < min_distance:
                    min_distance = dist
                    closest_number = number
        # 匹配最近的数字
        if closest_number:
            pairs[letter] = pairs.get(letter, []) + [closest_number]
            matched_numbers.add(closest_number)
    # 为未匹配的数字分配NONE标识
    for number in numbers:
        if number not in matched_numbers:
            pairs.setdefault('NONE', []).append(number)
    # 输出结果
    print(pairs)

if __name__ == '__main__':
    main()
