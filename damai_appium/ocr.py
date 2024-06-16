"""
__Author__ = "wahh159"
__Version__ = "1.0.0"
__Description__ = "大麦app抢票自动化"
__Created__ = 2023/12/8 9:10
"""

from appium import webdriver
import pytesseract
from PIL import Image
import time
# main_start_time = time.time()  # 记录开始时间
print('OCR流程执行')
def capture_and_ocr(driver, left, top, right, bottom):
    start_time = time.time()  # 记录开始时间
    # 截图并保存为图片文件
    screenshot_path = ("screenshot" + time.strftime("%H-%M-%S",time.localtime()) +".png")
    driver.save_screenshot(screenshot_path)

    # 读取截图文件并截取指定区域
    image = Image.open(screenshot_path)
    cropped_image = image.crop((left, top, right, bottom))
    # pytesseract.pytesseract.tesseract_cmd = 'G:\\tesseractOcr\\\\tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    # 使用 OCR 获取文字
    # custom_config = r'--oem 1 --psm 6'
    # text = pytesseract.image_to_string(cropped_image, lang='chi_sim', config=custom_config)

    ##
    cropped_image = image.crop((left, top, right, bottom))
    # path = "img\\text-img.png"

    testdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'

    text = pytesseract.image_to_string(cropped_image, config=testdata_dir_config, lang='chi_sim') 
    ##
    print('开始抢票OCR',text)
    end_time = time.time()  # 记录结束时间
    elapsed_time = end_time - start_time  # 计算时间差

    print(f"OCR 耗时：{elapsed_time} 秒")
    return text