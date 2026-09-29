"""钢厂核心逻辑：炉料、高炉、脱硫和连铸。"""

import json


def new_game():
    return {"batches": {}, "furnace_load": 0, "furnace_capacity": 2, "material": 100, "safety": 100, "batch_id": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["batch_id"] += 1
    return state


def charge(state, batch_id, amount):
    state["batches"][batch_id] = amount
    state["material"] -= amount
    return True


def smelt(state, batch_id):
    state["furnace_load"] += 1
    return True


def check_temp(state, temp):
    if temp < 30:
        return "over"
    return "ok"


def cancel(state, batch_id):
    return True


def desulfur(state, amount):
    return True


def leak(state):
    state["safety"] -= 10
    state["safety"] -= 10
    return state["safety"]


def cast(state, amount):
    return True


def main():
    print("钢厂 - 命令: charge/smelt/temp/cancel/desulfur/leak/cast/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
