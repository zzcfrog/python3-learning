#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=' ')

print()

for i in range(10):
    if i == 5:
        break
    print(i, end=' ')