def calc_checksum(calc_cs):
    if len(calc_cs) % 2 != 0:
        calc_cs = calc_cs + str(0)

    it = 0
    check_sum = 0
    while it < len(calc_cs):
        part1 = ord(calc_cs[it])*256 + ord(calc_cs[it+1])
        part2 = 65535 - part1
        part3 = check_sum + part2
        check_sum = (part3 % 65536) + (part3 / 65536)
        it = it + 2

    return (65535 - check_sum)

def checksum(recvdCheckSum, seq_num, data):#check checksum
    calc_cs = str(seq_num)+data
    if calc_checksum(calc_cs) == recvdCheckSum:
        return True
    else:
        return False