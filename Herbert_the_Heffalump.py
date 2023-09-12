def num_rushes(slope_height, rush_height_gain, back_sliding):
    """Determines the number of rushes required to reach the height"""
    if rush_height_gain >= slope_height:
        return 1
    else:
        product = slope_height - rush_height_gain + back_sliding
        return 1 + num_rushes(product, rush_height_gain, back_sliding)
    
ans = num_rushes(10, 10, 9)
print(ans)

ans = num_rushes(10, 10, 10)
print(ans)