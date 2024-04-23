import ocr_online
from collections import deque

# 常见的OCR错误映射
corrections = {
    '7': '1'  # 错误识别为7的应当是1
    # 添加更多的错误和正确的映射关系
}
pairs={}

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
    # 将字母和其中心位置作为元组放入队列
    letter_queue = deque([(item['words'], item['center']) for item in words_results if item['words'].isalpha()])

    # 记录已匹配的数字
    matched_numbers = set()


    # 从队列中依次处理每个字母
    while letter_queue:
        letter, letter_center = letter_queue.popleft()
        closest_number = None
        min_distance = float('inf')

        for number in numbers:
            if number['words'] not in matched_numbers:
                dist = distance(letter_center, number['center'])
                if dist < min_distance:
                    min_distance = dist
                    closest_number = number['words']

        # 匹配最近的数字
        if closest_number:
            pairs[letter] = pairs.get(letter, []) + [closest_number]
            matched_numbers.add(closest_number)

    # 为未匹配的数字分配NONE标识
    for number in numbers:
        if number['words'] not in matched_numbers:
            pairs.setdefault('NONE', []).append(number['words'])

    # 输出结果
    # print(pairs)

if __name__ == '__main__':
    main()
