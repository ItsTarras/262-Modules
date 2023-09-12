def transmission_delay(packet_length_bytes, rate_bps):
    """Returns the number of seconds in transmission delay"""
    #The formula is Bits/Rate
    
    #So for starters, we are given packet_length in BYTES.
    #Start by converting to bits.
    return (packet_length_bytes * 8) / rate_bps


def transmission_delaay(packet_length_bytes, rate_mbps):
    """Does the same as the above function, instead using rate_mbps as input"""

    print((packet_length_bytes * 8) / (rate_mbps * 1000000))
    
    return ((packet_length_bytes * 8) / (rate_mbps * 1000000))

def total_time(cable_length_km, packet_length_b):
    """Returns the total time it takes for data to go through a cable of length x"""
    # speed of light data transmission is 200,000 km / s in a cable
    # Time in seconds it takes for data to go through cable
    cable_time = cable_length_km / 200000
    print(f"cable time is {cable_time}")
    
    return cable_time
print(f"{total_time(10000, 8000):.4f}")