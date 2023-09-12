def num_rushes(slope_height, rush_height_gain, back_sliding):
    """Determines the number of rushes required to reach the height"""
    if rush_height_gain >= slope_height:
        return 1
    else:
        product = slope_height - (rush_height_gain) + back_sliding
        return 1 + num_rushes(product, (rush_height_gain * 0.95), (back_sliding * 0.95))
    
ans = num_rushes(100, 15, 7)
print(ans)

ans = num_rushes(10, 10, 9)
print(ans)