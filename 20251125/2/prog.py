import sys
import math


def parse_number(s):
    try:
        return float(s)
    except ValueError:
        return 0.0


class AssemblerInterpreter:
    def __init__(self, code):
        self.code_lines = code.split('\n')
        self.labels = {}
        self.commands = []
        self.vars = {}
        self.pc = 0

    def parse(self):
        cmd_count = 0
        for line_num, line in enumerate(self.code_lines):
            line = line.lstrip()
            if not line or line.isspace():
                continue
            label = None
            if ':' in line:
                parts = line.split(':', 1)
                if parts[0].strip() and not parts[0].isspace():
                    label = parts[0].strip()
                    line = parts[1].strip()
                else:
                    line = line.replace(':', ' ', 1).strip()
            if not line:
                if label:
                    self.labels[label] = cmd_count
                continue
            tokens = line.split()
            if not tokens:
                continue
            op = tokens[0].lower()
            args = tokens[1:]
            valid_cmd = False
            if op == 'stop' and len(args) == 0:
                valid_cmd = True
            elif op == 'store' and len(args) == 2:
                valid_cmd = True
            elif op in {'add', 'sub', 'div', 'mul'} and len(args) == 3:
                valid_cmd = True
            elif op in {'ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle'} and len(args) == 3:
                valid_cmd = True
            elif op == 'out' and len(args) == 1:
                valid_cmd = True
            if valid_cmd:
                if label:
                    self.labels[label] = len(self.commands)
                self.commands.append((op, args))
                cmd_count += 1

    def get_value(self, arg):
        try:
            return float(arg)
        except ValueError:
            return self.vars.get(arg, 0.0)

    def execute(self):
        for cmd, args in self.commands:
            if cmd.startswith('if') and len(args) == 3:
                label = args[2]
                if label not in self.labels:
                    return
        self.pc = 0
        while self.pc < len(self.commands):
            cmd, args = self.commands[self.pc]
            self.pc += 1
            if cmd == 'stop':
                break
            elif cmd == 'store':
                value_str, var = args
                value = parse_number(value_str)
                self.vars[var] = value
            elif cmd in {'add', 'sub', 'div', 'mul'}:
                src_str, op_str, dst = args
                src = self.get_value(src_str)
                op = self.get_value(op_str)
                if cmd == 'add':
                    result = src + op
                elif cmd == 'sub':
                    result = src - op
                elif cmd == 'div':
                    if op == 0:
                        result = math.inf
                    else:
                        result = src / op
                elif cmd == 'mul':
                    result = src * op
                self.vars[dst] = result
            elif cmd.startswith('if'):
                src_str, op_str, label = args
                src = self.get_value(src_str)
                op = self.get_value(op_str)
                jump = False
                if cmd == 'ifeq':
                    jump = src == op
                elif cmd == 'ifne':
                    jump = src != op
                elif cmd == 'ifgt':
                    jump = src > op
                elif cmd == 'ifge':
                    jump = src >= op
                elif cmd == 'iflt':
                    jump = src < op
                elif cmd == 'ifle':
                    jump = src <= op
                if jump:
                    self.pc = self.labels[label]
            elif cmd == 'out':
                src_str = args[0]
                value = self.get_value(src_str)
                print(value)


interpreter = AssemblerInterpreter(sys.stdin.read())
interpreter.parse()
interpreter.execute()
