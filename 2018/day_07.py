"""Advent of Code Day 7 - The Sum of Its Parts"""


def order_steps(steps):
    """Return order steps must be taken given their requirements."""
    num_steps = len(steps)
    order = ''
    while num_steps:
        ready_steps = []
        for step, requirements in steps.items():
            if step in order:
                continue

            ready = True
            for required in requirements:
                if required not in order:
                    ready = False
                    break

            if ready:
                ready_steps.append(step)

        ready_steps.sort()
        order += ready_steps[0]
        num_steps -= 1

    return order


def build_time(steps):
    """Return build time if steps take 60 + letter value secs to complete."""
    step_times = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), range(61, 87)))
    build_time = 0
    build_queue = []
    completed = set()
    num_steps = len(steps)
    while num_steps:
        ready = []
        for step, requirements in steps.items():
            if step in completed or step in [x[0] for x in build_queue]:
                continue

            step_ready = True
            for required in requirements:
                if required not in completed:
                    step_ready = False
                    break

            if step_ready:
                ready.append([step, step_times[step]])

        ready.sort()
        build_queue.extend(ready)

        done = build_queue.pop(0)
        completed.add(done[0])
        build_time += done[1]
        num_steps -= 1
        # Other 4 workers make progress equal to done time on their tasks
        for in_progress in build_queue[:4]:
            in_progress[1] = in_progress[1] - done[1]

    return build_time


if __name__ == '__main__':

    with open('inputs/day_07.txt') as f:
        lines = f.readlines()

    # Make dict associating each step with its requirements
    steps = {}
    for line in lines:
        parse = line.split()
        if parse[7] not in steps:
            steps[parse[7]] = set()
        steps[parse[7]].add(parse[1])

        if parse[1] not in steps:
            steps[parse[1]] = set()

    # Answer One
    print("Order of steps:", order_steps(steps))

    # Answer Two
    print("Time to build:", build_time(steps))
