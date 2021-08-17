ln, wd = map(int, input().split())
pattern = [('.|.'* (2*i + 1)).center(wd, '-') for i in range(ln//2)]
print('\n'.join(pattern + ['WELCOME'.center(wd, '-')] + pattern[: : -1]))