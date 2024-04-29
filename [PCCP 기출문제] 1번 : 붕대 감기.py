def solution(bandage, health, attacks):
    time = -1
    attack_cursor = 0
    max_health = health
    heal_continuous = 0

    while True:
        if health <= 0: return -1
        if attack_cursor == len(attacks): break
        time += 1
        attack_time, damage = attacks[attack_cursor]

        if attack_time == time:
            health -= damage
            heal_continuous = 0
            attack_cursor += 1
            continue

        health = min(health + bandage[1], max_health)
        heal_continuous += 1

        if heal_continuous == bandage[0]:
            health = min(health + bandage[2], max_health)
            heal_continuous = 0

    return health