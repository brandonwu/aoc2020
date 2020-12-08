#!/usr/bin/env python

def parse(line):
    ins, val_str = line.split()
    val = int(val_str)
    return (ins, val)


def main(arr):
    acc = 0
    pc = 0
    trace = []
    # list of trace indices with jmps or nops
    to_patch = []
    visited = set()
    patching, patches_collected = False, False
    while pc < len(arr):
        if pc in visited:
            patching, patches_collected = True, True

            patch = to_patch.pop()

            # remove pc of instruction we're patching from visited so we can
            # re-run it without triggering this loop detect
            # keep the pcs run after this trace point because they
            # lead to terminal states (there are no conditional jmps)
            old_pc, _, _, _ = trace[patch]
            visited.remove(old_pc)

            pc, acc, old_ins, val = trace[patch]

            if old_ins == 'jmp':
                ins = 'nop'
            elif old_ins == 'nop':
                ins = 'jmp'
            print('>PATCH< pc={0:3} {1} -> {2}'.format(pc, old_ins, ins))

            # truncate execution trace to before last patch point
            trace = trace[:patch:]

        if not patching:
            ins, val = arr[pc]
        trace.append((pc, acc, ins, val))
        print('pc={1:3} {2} {3:+4} acc={0}'.format(acc, pc, ins, val))
        visited.add(pc)

        if ins == 'acc':
            acc += val
            pc += 1
        elif ins == 'jmp':
            if not patches_collected:
                to_patch.append(len(trace) - 1)
            pc += val
        elif ins == 'nop':
            if not patches_collected:
                to_patch.append(len(trace) - 1)
            pc += 1

        patching = False

    return acc


def run(file):
    arr = f.readlines()
    print(main([parse(line.strip()) for line in arr]))


if __name__=='__main__':
    with open('testinput', 'r') as f:
        run(f)
    with open('input', 'r') as f:
        run(f)
