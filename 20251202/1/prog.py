from asyncio import *


async def producer(output_queue: Queue, interval: int, termination: Event):
    index = 0
    await sleep(interval)
    while not termination.is_set():
        message = f"{index}_{interval}"
        await output_queue.put(message)
        index += 1
        await sleep(interval)


async def data_processor(input_queue: Queue, storage: Queue, termination: Event):
    while True:
        if termination.is_set() and input_queue.empty():
            return
        try:
            data = await wait_for(input_queue.get(), timeout=0.05)
        except TimeoutError:
            continue
        await storage.put(data)
        input_queue.task_done()


async def consumer(input_storage: Queue, quantity: int, interval: int, termination: Event):
    await sleep(interval)
    for i in range(quantity):
        data_item = await input_storage.get()
        print(data_item)
        input_storage.task_done()
        await sleep(interval)
    termination.set()


async def application_entry():
    try:
        interval_a, interval_b, interval_c, message_count = map(int, input().strip().split(","))
    except ValueError as e:
        print(f"Неверный формат ввода: {e}")
        return
    if any(val <= 0 for val in [interval_a, interval_b, interval_c, message_count]):
        print("Все параметры должны быть положительными числами")
        return
    termination_flag = Event()
    message_queue = Queue()
    data_storage = Queue()
    producer_a = create_task(producer(message_queue, interval_a, termination_flag))
    producer_b = create_task(producer(message_queue, interval_b, termination_flag))
    processor = create_task(data_processor(message_queue, data_storage, termination_flag))
    data_consumer = create_task(consumer(data_storage, message_count, interval_c, termination_flag))
    await data_consumer
    for task in (producer_a, producer_b, processor):
        task.cancel()
    await gather(producer_a, producer_b, processor, return_exceptions=True)


run(application_entry())
