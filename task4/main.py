import requests
import asyncio
import aiohttp
import threading
import time
from multiprocessing import Process

# urls = [
#     'https://get.pxhere.com/photo/mountain-snow-winter-mountain-range-weather-alpine-extreme-sport-skiing-season-ridge-summit-sports-equipment-chamonix-mountaineering-winter-sport-sports-resort-mountains-alps-ski-piste-high-mountains-ski-touring-nordic-skiing-ski-mountaineering-ski-equipment-mountainous-landforms-geological-phenomenon-grandes-choir-asses-1160313.jpg',
#     'https://sportishka.com/uploads/posts/2023-12/1702121858_sportishka-com-p-chelovek-idushchii-v-goru-pinterest-7.jpg',
#     'https://pixnio.com/free-images/2017/02/13/2017-02-13-10-28-07.jpg',
#     'https://s1.1zoom.ru/big0/969/Mountains_Mountaineering_Himalayas_Nepal_Crag_Snow_565213_1280x853.jpg',
#     'https://sportishka.com/uploads/posts/2022-11/1667473213_34-sportishka-com-p-ryukzak-dlya-pokhoda-v-gori-oboi-39.jpg'
# ]

MAX_LENGTH = 70
urls = []


def input_url(urls):
    count = int(input("Введите количество url адресов: "))
    while count != 0:
        url = input("Введите url адрес: ")
        urls.append(url)
        count -= 1


def save_image_sync(url):
    response = requests.get(url)
    url_split = url.split('/')
    if len(url_split[len(url_split) - 1]) > MAX_LENGTH:
        filename = url_split[3]
    else:
        filename = url_split[len(url_split) - 1]

    with open(f'images/{filename}.png', 'wb') as dir:
        dir.write(response.content)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds ")


def save_image_thread(urls):
    threads = []

    for url in urls:
        thread = threading.Thread(target=save_image_sync, args=[url])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds ")


def save_image_processes(urls):
    processes = []
    for url in urls:
        process = Process(target=save_image_sync, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds ")


async def save_image_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            url_split = url.split('/')
            if len(url_split[len(url_split) - 1]) > MAX_LENGTH:
                filename = url_split[3]
            else:
                filename = url_split[len(url_split) - 1]
            with open(f'images/{filename}.png', 'wb') as dir:
                image = await response.read()
                dir.write(image)

    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds ")


async def sava_image_async_main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(save_image_async(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == '__main__':
    input_url(urls)

    # for url in urls:
    #     save_image_sync(url)

    # save_image_thread(urls)

    # save_image_processes(urls)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(sava_image_async_main())
