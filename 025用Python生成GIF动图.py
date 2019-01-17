"""
imageio 库可以轻松实现
"""

import imageio

def create_gif(image_list, gif_name, duration=1):
    """创建GIF图"""
    frames = []

    # 读取并将图片放到frames中
    for image in image_list:
        frames.append(imageio.imread(image))

    # 保存成GIF图
    imageio.mimsave(gif_name, frames, 'GIF', duration = duration)

    return

def main():
    """主函数"""
    image_list = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
    gif_name = 'new.gif'
    duration = 1.5
    create_gif(image_list, gif_name, duration)
    return


if __name__ == "__main__":
    main()
