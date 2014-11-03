def counting_rabbit_pairs(months, step=1):
    if months == 0:
        return 0
    elif months == 1:
        return 1
    else:
        return counting_rabbit_pairs(months-1, step) + counting_rabbit_pairs(months-2, step)*3

if __name__ == "__main__":
    print counting_rabbit_pairs(29, 3)
